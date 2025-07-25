from django.db import models

class User(models.Model):
    user_nickname = models.CharField(max_length=100, primary_key=True)
    user_name = models.CharField(max_length=150)
    user_email = models.EmailField()
    user_age = models.IntegerField()

    def __str__(self):
        return f'Nickname: {self.user_nickname} | Email: {self.user_email}'