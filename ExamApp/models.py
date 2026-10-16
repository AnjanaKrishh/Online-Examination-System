from django.db import models
"""
"Schema":QuestionsDb
Fields:question,option_a,option_b,option_c,option_d,correct_answer
"""

# Create your models here.
class QuestionsDb(models.Model):
    question = models.CharField(max_length=200)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1)

    