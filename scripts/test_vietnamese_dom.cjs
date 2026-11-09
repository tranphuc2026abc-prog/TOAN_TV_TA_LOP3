// Fixture kiểm tra kỹ thuật; không phải học liệu đã đối chiếu sách.
const {JSDOM,VirtualConsole}=require('jsdom');
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const catalog=JSON.parse(fs.readFileSync(path.join(root,'data/CHUONG_TRINH_LOP_3_FULL.json')));
const id=catalog.lessons.find(x=>x.subject==='tv').id;
const fixture={id,subject:'tv',volume:1,title:'Fixture kiểm thử Tiếng Việt',source:{printed_pages:[1,2]},objectives:['Mục tiêu thử'],knowledge:{introduction:'Giải thích thử',rules:['Quy tắc thử'],steps:['Bước thử'],common_errors:['Lỗi thử']},examples:[{question:'Ví dụ thử',steps:['Lời giải thử']}],reading:{summary:'Tóm tắt fixture <img src=x>',characters_or_images:['Nhân vật fixture'],message:'Thông điệp fixture'},language_practice:{vocabulary:['Từ fixture'],sentences:['Câu fixture'],spelling:['Chính tả fixture'],expression:['Diễn đạt fixture']},practice:Array.from({length:12},(_,i)=>({question_id:id+'_TEST'+i,type:'mcq',question:'Câu fixture '+i,correct_answer:'Đáp án '+i,options:['Đáp án '+i,'Sai A','Sai B','Sai C'],explanation:'Giải thích '+i,skill:'reading',evidence:'Chi tiết fixture'})),verification:{teacher_approved:false},games:[{id:'TESTGAME',title:'Game thử',objective:'Mục đích thử',mode:'treasure',rules:['Quy tắc thử']}],assessment:{session_size:6,scoring:'Điểm thử',review_advice:'Ôn thử'}};
(async()=>{
 const html=fs.readFileSync(path.join(root,'index.html'),'utf8').replace('<script src="content/system/lesson-content.js"></script>',()=>'<script>'+fs.readFileSync(path.join(root,'content/system/lesson-content.js'),'utf8')+'</script>');
 const vc=new VirtualConsole();
 const dom=new JSDOM(html,{url:'http://localhost/',runScripts:'dangerously',virtualConsole:vc,beforeParse(w){w.scrollTo=()=>{};w.fetch=async url=>({ok:true,json:async()=>String(url).endsWith('INDEX.json')?{lessons:[{id,path:'fixture.json',question_count:12}]}:fixture});}});
 await new Promise(r=>dom.window.addEventListener('load',r));const w=dom.window;await w.lessonContentReady;w.load('FixtureTV');w.go({p:'lesson',id});
 for(const text of ['Nhân vật fixture','Thông điệp fixture','Từ fixture','Câu fixture','Chính tả fixture','Diễn đạt fixture','Luyện tập 6 câu'])assert(w.A.textContent.includes(text),text);
 assert(!w.A.textContent.includes('3 nhận biết'));assert(!w.A.querySelector('img[src="x"]'));
 w.startQ(id,'all');assert.equal(w.v.qs.length,6);assert.equal(new Set(w.v.qs.map(q=>q.question_id)).size,6);
 const q=w.v.qs[0];w.ans(w.v.opts.indexOf(q.answer));assert.equal(w.v.done,1);assert(w.A.textContent.includes(q.explanation));dom.window.close();
 console.log('PASS TV DOM: 6/12 câu không phân mức Toán; đủ nhóm ngôn ngữ, escape HTML và phản hồi.');
})().catch(e=>{console.error(e);process.exit(1)});
