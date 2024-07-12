from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime

def token_is_valid(token):
    conceived_token_data = token.date_conceived
    plus_15_min = conceived_token_data + timedelta(minutes=15)
    now_date = datetime.now()

    return (plus_15_min >= now_date)


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email_token_code = models.IntegerField()
    url_token_code = models.IntegerField()
    date_conceived = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Email Token: {self.email_token_code} | Url Token: {self.url_token_code} | Used: {self.used}"
