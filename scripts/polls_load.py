import csv
from datetime import date

from polls.models import Question, Choice

def run():
    print("Deleting old data...")
    Choice.objects.all().delete()
    Question.objects.all().delete()
    print("Data deleted")

    fhand = open("scripts/dj4e_batch.csv")
    reader = csv.reader(fhand)

    for row in reader:
        print(row)
        q = Question(question_text=row[0], pub_date=date.today())
        q.save()
        for i in range(1, len(row)):
            c = Choice(question=q, choice_text=row[i])
            c.save()
    print("Data loaded")

