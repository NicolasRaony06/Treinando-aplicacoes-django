from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("logout/", views.logout, name="logout"),
    path("reset_password/", views.reset_password, name="reset_password"),
    path("receive_token/<str:user_email>", views.receive_token, name="receive_token"),
    path("change_password/<str:user_email>/", views.change_password, name="change_password"),
]
