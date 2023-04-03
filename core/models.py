from django.db import models
from django.contrib import admin
import datetime


class Question(models.Model):
    questoes = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Data de publicamento:")
    @admin.display(boolean = True,
                    ordering = "pub_date",
                    description = "Recentemente publicado?",
                    )

    def __str__(self):
        return(self.questoes)
    
    def was_published_recently(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        return (now - datetime.timedelta(days=1) <= self.pub_date <= now)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return(self.choice_text)
    