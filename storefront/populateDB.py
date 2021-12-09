import csv
import json
import requests
import datetime
csvfile = open('udemy_courses.csv', 'r', encoding='utf-8')
jsonfile = open('file.json', 'w')
url = 'http://127.0.0.1:8000/playground/create-course/'
fieldnames = ("course_id", "course_title", "url", "is_paid",
                "price", "num_subscribers", "num_reviews", "num_lectures",
                "level", "content_duration", "published_timestamp", "subject")
reader = csv.DictReader( csvfile, fieldnames)
print(reader)
data = []
ii=int(0)
for row in reader:
    ii += 1
    if ii == 1:
        continue
    data.append(row)
    if ii == 10:
        break

x = requests.post(url, data = data)
print(x.status_code)
    

