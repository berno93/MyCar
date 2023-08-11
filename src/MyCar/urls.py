from django.urls import path
from MyCar.views import MyCarHome, MyCarCreate, MyCarUpdate, MyCarDetail, MyCarDelete
from django.contrib.auth.decorators import login_required

app_name = "posts"


urlpatterns = [
    path('', MyCarHome.as_view(), name="home"),
    path('create/', login_required(MyCarCreate.as_view()), name="create"),
    path('edit/<str:slug>/', MyCarUpdate.as_view(), name="edit"),
    path('<str:slug>/', MyCarDetail.as_view(), name="post"),
    path('delete/<str:slug>/', MyCarDelete.as_view(), name="delete"),
]
