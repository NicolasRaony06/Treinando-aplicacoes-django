from django.db import models
from random import choices

def generator(char_range):
    alfanum = "abcdefghijklmnopqrstuvxwyz0123456789"

    try:
        value = choices(alfanum, k=int(char_range))
        return value
    except:
        return None

