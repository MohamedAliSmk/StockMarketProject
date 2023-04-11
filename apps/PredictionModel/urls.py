from django.urls import path, re_path
import views

path('Companys/<str:symbol>',views.prediction , name="prediction"),
path('Companys/<str:symbol>',views.predict_next_day , name="predict_next_day"),
  