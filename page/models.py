from django.db import models

from accounts.models import CustomUser


# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(CustomUser, related_name="liked_news", blank=True)



    def __str__(self):
        return f"{self.title}    id si {self.id} time {self.created_at}"


# # create table news (
#     title varchar(300),
#     content varchar(300),
# News
# id
# title
#
#
# CustomUser
#
#
#
# like
# id
# news_id
# customuser_id



