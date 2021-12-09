import csv
import models 

path = 'udemy_courses.csv'

models.Course.objects.all().delete()

with open(path) as f:
    reader = csv.reader(f, encoding='utf-8')
    i = 0
    for row in reader:
        i += 1
        if i == 1:
            continue
        course = models.Course.objects.create(
            course_id = row[0],
            course_title = row[1],
            url = row[2],
            is_paid = row[3],
            price = row[4],
            num_subscribers = row[5],
            num_reviews = row[6],
            num_lectures = row[7],
            level = row[8],
            content_duration = row[9],
            published_timestamp = row[10],
            subject = row[11],
        )
        course.save()