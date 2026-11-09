"""Yêu cầu theo môn; không áp số lượng/phân mức Toán cho môn ngôn ngữ."""
def validate_subject(obj):
    subject=obj['subject']
    assert subject in ('toan','tv','ta'), ('Môn không hỗ trợ',subject)
    qs=obj['practice']
    if subject=='toan':
        assert len(qs)>=40
        counts={}
        for q in qs:counts[q['difficulty']]=counts.get(q['difficulty'],0)+1
        assert counts==dict(nhan_biet=10,thong_hieu=10,van_dung=20)
        assert obj['assessment']['session_size']==10
        assert obj['assessment']['distribution']==dict(nhan_biet=3,thong_hieu=3,van_dung=4)
    elif subject=='tv':
        # Đọc hiểu phải gắn với văn bản; không lưu toàn văn sách trong trường này.
        reading=obj['reading']
        assert reading['summary'] and reading['characters_or_images'] and reading['message']
        assert obj['source']['printed_pages'] and obj['source']['review']
        assert obj['language_practice']['vocabulary']
        assert obj['language_practice']['sentences']
        assert obj['language_practice']['spelling']
        assert obj['language_practice']['expression']
        assert qs and all(q.get('skill') for q in qs)
        assert any(q['skill']=='reading' and q.get('evidence') for q in qs)
        assert obj['assessment']['session_size']<=len(qs)
    else:
        assert obj['vocabulary'] and obj['patterns'] and obj['pronunciation']
        for v in obj['vocabulary']:assert v['word'] and v['meaning_vi'] and v['example']
        assert obj['skills']['reading'] and obj['skills']['writing'] and obj['skills']['speaking']
        assert qs
