from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='starting-page'),
    path('quiz',views.quiz,name='quiz-page'),
    path('result', views.quiz_system, name='quiz_system'),

]