from django.db import models

# Create your models here.
class Menti(models.Model):
    room = models.CharField(max_length=500)
    users_joined = models.IntegerField(default=0)
    status = models.CharField(choices = (("start","start"),("end","end")) ,default="end", max_length=100)

    def __str__(self):
        return self.room

class Player(models.Model):
    username = models.CharField(max_length=500)
    room = models.ForeignKey(Menti,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Question(models.Model):
    question = models.CharField(max_length=3000)
    room = models.ForeignKey(Menti,on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=500)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

