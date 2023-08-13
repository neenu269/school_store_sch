from.import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('',views.main,name='main')

]