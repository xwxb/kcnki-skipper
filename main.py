import requests
import json
import time
import random
from datetime import datetime, timedelta
from config import HEADERS, SESSION_ID, DEFAULT_LECTURE_DURATION, DEBUG_MODE

def load_course_lectures():
    courses = {}
    with open('list.txt', 'r') as f:
        for line in f:
            parts = line.strip().split()
            if parts:  # Skip empty lines
                course_id = parts[0]
                lecture_ids = parts[1:] if len(parts) > 1 else []
                courses[course_id] = lecture_ids
    return courses

def process_lecture(course_id, lecture_id, duration=DEFAULT_LECTURE_DURATION):
    url = 'https://k.cnki.net/kedu/record/recordlearnFoot'
    total_watch_time = 0
    order = 1
    is_complete = False
    start_time = datetime.now()
    interval = 30  # minimum control window

    while not is_complete:
        byte_rate = random.uniform(1000000, 10000000)  # 1-10 MB/s
        total_watch_time += interval
        end_time = start_time + timedelta(seconds=total_watch_time)
        end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')

        data = {
            'courseId': course_id,
            'typeId': 1,
            'duration': interval,
            'endTime': end_time_str,
            'remark': 'Mac && chrome null',
            'source': 'k-wb-edu-courseLearn',
            'watchTime': total_watch_time,
            'lectureId': lecture_id,
            'isComplete': is_complete,
            'browserName': 'chrome',
            'secondTerminalName': 'Mac',
            'terminalName': 'pc',
            'sessionId': SESSION_ID,
            'byteRate': byte_rate,
            'order': order
        }

        if DEBUG_MODE:
            print(f"Request data: {json.dumps(data, indent=2)}")

        response = requests.post(url, headers=HEADERS, data=json.dumps(data))
        resp_data = response.json()

        if DEBUG_MODE:
            print(f"Response: {json.dumps(resp_data, indent=2)}")
        elif resp_data.get('data', 0) != 0:
            print(f"Unexpected response: {json.dumps(resp_data, indent=2)}")

        print(f"Course {course_id} - Lecture {lecture_id}: {total_watch_time}/{duration}s (Round {order})")

        if total_watch_time >= duration:
            is_complete = True
        
        order += 1
        time.sleep(interval)

def main():
    courses = load_course_lectures()
    for course_id, lectures in courses.items():
        print(f"\nProcessing course {course_id}")
        for lecture_id in lectures:
            print(f"\nStarting lecture {lecture_id}")
            process_lecture(course_id, lecture_id)

if __name__ == "__main__":
    main()