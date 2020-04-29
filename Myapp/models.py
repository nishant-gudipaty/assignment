from django.db import models


class UserModel(models.Model):
    USER_ROLES = (
        ("NU", "Normal"),
        ("SU", "Admin")
    )
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)
    user_type = models.CharField(max_length=2, choices=USER_ROLES, default="NU")

    def __str__(self):
        return self.full_name


class BookModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amazon_url = models.URLField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.title + " by " + self.author
