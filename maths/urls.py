from django.urls import path
from maths.views import Calculator

urlpatterns = [
    path('', Calculator.math),
    path('add/<a>/<b>', Calculator.add),
    path('sub/<a>/<b>', Calculator.sub),
    path('mul/<a>/<b>', Calculator.mul),
    path('div/<a>/<b>', Calculator.div),
]
