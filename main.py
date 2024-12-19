import requests
import json
import time
from datetime import datetime, timedelta

# 请求的 URL
url = 'https://k.cnki.net/kedu/record/recordlearnFoot'
# 请求头信息，需替换为你自己的凭证
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    填入你的cookie
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://k.cnki.net',
    'Pragma': 'no-cache',
    'Referer': 'https://k.cnki.net/courseLearn/53388',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'X-Auth': 'true',
    填入几个token
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sign': 'ab3d599d250717a0d96e82357a037105',
    'timestamp': '1734604896'
}

# 初始化参数
course_id = '53388'
lecture_id = '57259'
duration = 60  # 每次发送的间隔秒数
total_watch_time = 0
order = 1
is_complete = False
byte_rate = 32083.24
session_id = '897h90ij'  # 示例 sessionId，需替换
start_time = datetime.now()

while not is_complete:
    # 更新 watchTime 和 endTime
    total_watch_time += duration
    end_time = start_time + timedelta(seconds=total_watch_time)
    end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')

    # 构建请求数据
    data = {
        'courseId': course_id,
        'typeId': 1,
        'duration': duration,
        'endTime': end_time_str,
        'remark': 'Mac && chrome null',
        'source': 'k-wb-edu-courseLearn',
        'watchTime': total_watch_time,
        'lectureId': lecture_id,
        'isComplete': is_complete,
        'browserName': 'chrome',
        'secondTerminalName': 'Mac',
        'terminalName': 'pc',
        'sessionId': session_id,
        'byteRate': byte_rate,
        'order': order
    }
    print(data)

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f'Order {order}: Status Code {response.status_code}')
    print(response.json())

    # 检查是否完成（根据业务逻辑调整判断条件）
    if total_watch_time >= 36000:  # 假设总时长为 3600 秒
        is_complete = True

    # 更新顺序号
    order += 1

    # 等待下一个周期（测试时可以调小间隔）
    time.sleep(30)  # 这是目前最小风控窗口