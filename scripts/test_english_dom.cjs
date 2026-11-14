// Real English banks; audio is mocked to verify control flow, not actual sound quality.
const {JSDOM,VirtualConsole}=require('jsdom');
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const entries=JSON.parse(fs.readFileSync(path.join(root,'content/system/INDEX.json'))).lessons.filter(e=>e.subject==='ta'&&e.path);
const ids=entries.map(e=>e.id);
const banks=entries.map(e=>JSON.parse(fs.readFileSync(path.join(root,e.path))));
const html=fs.readFileSync(path.join(root,'index.html'),'utf8').replace('<script src="content/system/lesson-content.js"></script>',()=>'<script>'+fs.readFileSync(path.join(root,'content/system/lesson-content.js'),'utf8')+'</script>');
(async()=>{
 let spoken=[];
 const dom=new JSDOM(html,{url:'http://localhost/',runScripts:'dangerously',virtualConsole:new VirtualConsole(),beforeParse(w){
  w.scrollTo=()=>{};w.SpeechSynthesisUtterance=function(text){this.text=text};
  w.speechSynthesis={cancel(){},getVoices:()=>[{lang:'vi-VN',name:'Vietnamese'},{lang:'en-GB',name:'English'}],speak:s=>spoken.push(s)};
  w.fetch=async url=>({ok:true,json:async()=>String(url).includes('CHUONG_TRINH_LOP_3_FULL.json')?JSON.parse(fs.readFileSync(path.join(root,'data/CHUONG_TRINH_LOP_3_FULL.json'))):String(url).endsWith('INDEX.json')?{lessons:ids.map(id=>({id,path:id+'.json',question_count:12}))}:banks[ids.findIndex(id=>String(url).includes(id))]});
 }});
 await new Promise(r=>dom.window.addEventListener('load',r));const w=dom.window;await w.lessonContentReady;w.load('EnglishDOM');
 for(const c of banks){
  w.go({p:'lesson',id:c.id});
  for(const v of c.vocabulary)assert(w.A.textContent.includes(v.meaning_vi)&&w.A.textContent.includes(v.example));
  for(const p of c.pronunciation)assert(w.A.textContent.includes(p));
  for(const group of Object.values(c.skills))for(const item of group)assert(w.A.textContent.includes(item));
  assert(w.A.textContent.includes('Giọng máy'));assert(!w.A.textContent.includes('3 nhận biết'));
  w.A.querySelector('[data-english-audio]').click();let s=spoken.at(-1);assert.equal(s.lang,'en-GB');assert.equal(s.voice.lang,'en-GB');assert(s.text.includes(c.vocabulary[0].word));
  s.onerror();assert(w.A.textContent.includes('Chưa phát được'));s.onend();assert(w.A.textContent.includes('Đã đọc xong'));
  w.startQ(c.id,'all');assert.equal(w.v.qs.length,10);assert.equal(new Set(w.v.qs.map(q=>q.question_id)).size,10);
  const q=w.v.qs[0];w.ans(w.v.opts.indexOf(q.answer));assert.equal(w.v.done,1);assert(w.A.textContent.includes(q.explanation));
  w.startLessonGame(c.id);assert.equal(w.G.lessonContentId,c.id);
 }
 w.go({p:'lesson',id:ids[0]});w.speechSynthesis=undefined;w.A.querySelector('[data-english-audio]').click();assert(w.A.textContent.includes('chưa hỗ trợ'));
 banks[0].vocabulary[0].example='<img src=x onerror=alert(1)>';
 w.go({p:'lesson',id:ids[0]});assert(!w.A.querySelector('img[src=x]'));assert(w.A.textContent.includes('<img src=x'));
 dom.window.close();console.log('PASS English DOM: all ready English banks, skill sections, 10-question sessions, games, machine audio label/English voice/error/unsupported, escaping. Actual sound not verified.');
})().catch(e=>{console.error(e);process.exit(1)});
