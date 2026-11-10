import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=R/'content/system/drafts'
def read(n):return json.loads((D/n).read_text())
k=read('BATCH27_KNOWLEDGE.json')['lessons']
r=[read('BATCH27_B21_READING.json'),read('BATCH27_B22_READING.json')]+read('BATCH27_B23_B24_READING.json')['lessons']
l=read('BATCH27_B21_B22_LANGUAGE.json')['lessons']+read('BATCH27_B23_B24_LANGUAGE.json')['lessons']
wrong=[
[['Nắng đã bị bà giấu đi.','Na quên lấy áo từ ngoài vườn.','Áo có thể giữ nắng nhưng Na mở sai lúc.'],['Trời luôn mưa và không có vườn.','Bà không thích nhìn nắng.','Na không muốn đến thăm bà.'],['Na hiểu ngay toàn bộ lời bà.','Na giận vì bà không nhận quà.','Na quyết định không gặp bà nữa.'],['Na chỉ tới thăm bà một lần.','Na nhờ người khác thay mình mãi.','Na đem áo cất rồi không chơi ngoài vườn.']],
[['Ông chạy nhanh vượt cả đoàn.','Ông không muốn nhìn công trình.','Ông bảo mình khoẻ hơn xưa.'],['Ông đã ngủ quên trên xe.','Ông cố tình trốn gia đình.','Ông bỏ đi mua đồ chơi.'],['Không cho ông nói chuyện nữa.','Để ông tự chạy theo đoàn.','Để mọi người nghĩ mình mạnh nhất.'],['Ông chưa từng giúp mình.','Người lớn luôn khoẻ mãi.','Mình không cần quan tâm ai.']]]
meta=[('Tia nắng bé nhỏ',97,99,['Na','Bà nội']),('Để cháu nắm tay ông',100,103,['Dương','Ông ngoại']),('Tôi yêu em tôi',104,106,['Người kể','Em gái']),('Bạn nhỏ trong nhà',107,110,['Người kể','Cúp'])]
for j,(a,b,z,m) in enumerate(zip(k,r,l,meta)):
 title,start,end,chars=m;ident=a['id'];c=read_template=json.loads((R/'content/tieng-viet/tap-1/TV3_T1_B20.json').read_text())
 c.update(id=ident,lesson_no=21+j,title=title,topic='Mái nhà yêu thương',objectives=a['objectives'],status='AI_CHECKED_AWAITING_TEACHER')
 c['source'].update(printed_pages=[start,end],pdf_pages=[start+1,end+1],review='Nguồn đã đọc trực quan trong các lượt trước; đối chiếu các ghi chú BATCH27 đã lưu. B24 kết thúc110;111 chuyển chủ điểm. Không chép toàn văn.')
 c['reading']=dict(summary=a['introduction'],characters_or_images=chars,message=a['rules'][0])
 c['knowledge']=dict(introduction=a['introduction'],rules=a['rules'],common_errors=a['common_errors'],steps=['Đọc bài ở trang nguồn.','Tìm chi tiết làm căn cứ trước khi trả lời.','Luyện nói, viết và tự sửa theo tiêu chí.'])
 c['examples']=a['examples'];c['practice']=[]
 for n,q in enumerate(b['questions']+z['questions']):
  skill='reading' if n<4 else q['skill'];opts=q.get('wrong')
  if opts is None:opts=wrong[j][n]
  x=dict(question_id=f'{ident}_Q{n+1:02}',type='mcq',skill=skill,question=q['question'],correct_answer=q['answer'],options=[q['answer']]+opts,explanation=q['explanation'])
  if skill=='reading':x['evidence']=q['evidence']
  c['practice'].append(x)
 c['language_practice']={s:[q['question']+' Đáp án: '+q['correct_answer']+' '+q['explanation'] for q in c['practice'] if q['skill']==s] for s in ['vocabulary','sentences','spelling','expression']}
 c['activities']=[dict(title='Thực hành theo bài',materials=['Vở','Bút'],steps=[a['writing_task']['prompt'],'Đọc cho người thân nghe rồi sửa một ý chưa rõ.'],check=a['writing_task']['check'])]
 c['games'][0].update(id=ident+'_GAME',title='Kho báu: '+title,question_ids=[q['question_id'] for q in c['practice']]);c['verification']['teacher_approved']=False
 p=R/f'content/tieng-viet/tap-1/{ident}.json';p.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 lines=['# '+title,'AI_CHECKED_AWAITING_TEACHER',str(c['source']),*c['objectives'],a['introduction'],*a['rules'],*c['knowledge']['steps'],*a['common_errors']]
 for e in c['examples']:lines +=[e['question'],*e['steps']]
 lines +=c['activities'][0]['steps']+c['activities'][0]['check']
 for q in c['practice']:lines +=[q['question'],*q['options'],'Đáp án: '+q['correct_answer'],q['explanation'],q.get('evidence','')]
 lines +=[c['games'][0]['title'],*c['games'][0]['rules'],*map(str,c['assessment'].values()),*map(str,c['feedback'].values())]
 p.with_suffix('.md').write_text('\n\n'.join(lines)+'\n')
print('TV21–24:48 câu,4 trò chơi')
