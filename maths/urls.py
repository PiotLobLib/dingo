from django.urls import path
from maths.views import Calculator, maths_list, math_details, results_list

app_name = "maths"
urlpatterns = [
    path('', Calculator.math),
    path('add/<a>/<b>', Calculator.add),
    path('sub/<a>/<b>', Calculator.sub),
    path('mul/<a>/<b>', Calculator.mul),
    path('div/<a>/<b>', Calculator.div),
    path('histories/', maths_list, name="list"),
    path('histories/<int:id>', math_details, name="details"),
    path('results/', results_list, name="results"),
]
