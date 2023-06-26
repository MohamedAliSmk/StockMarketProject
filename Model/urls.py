from django.urls import path, re_path
from . import views

urlpatterns = [
path('predict/<str:Ticker>/<int:next_days>', views.Prediction_Comp, name='Prediction_Comp'),
]
