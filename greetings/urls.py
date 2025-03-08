from django.urls import path
from django.http import HttpResponse


urlpatterns = [
    path('', lambda request: HttpResponse("Hello World!")),
    path('<name>', lambda request, name: HttpResponse(
        f"Hello {name.capitalize()}!"))
]
