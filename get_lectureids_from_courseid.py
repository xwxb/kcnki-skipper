import requests

def get_lecture_ids(course_id):
    url = f'https://k.cnki.net/kedu/courseInfo/catalog?courseId={course_id}&progressRequired=true'
    headers = {
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data', [])
        if data:
            lecture_ids = [str(item['id']) for item in data[0].get('list', [])]
            return ' '.join(lecture_ids)
    return ''

# 读文件，每行一个courseid，输出需要的 lecture id
with open('1.txt', 'r') as file:
    for line in file:
        course_id = line.strip()
        lecture_ids = get_lecture_ids(course_id)
        if lecture_ids:
            print(f"{course_id}: {lecture_ids}")