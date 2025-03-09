from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context


class Calculator:
    @staticmethod
    def math(request):
        return HttpResponse("Tu będzie matma")

    @staticmethod
    def add(request, a, b):
        a, b = int(a), int(b)
        wynik = a + b
        c = {"a": a, "b": b, "operacja": "+",
             "wynik": wynik, "title": "dodawanie"}
        return render(
            request=request,
            template_name="maths/operation.html",
            context=c
        )

    @staticmethod
    def sub(request, a, b):
        a, b = int(a), int(b)
        wynik = a - b
        c = {"a": a, "b": b, "operacja": "-",
             "wynik": wynik, "title": "odejmowanie"}
        return render(
            request=request,
            template_name="maths/operation.html",
            context=c
        )

    @staticmethod
    def mul(request, a, b):
        a, b = int(a), int(b)
        wynik = a * b
        c = {"a": a, "b": b, "operacja": "*",
             "wynik": wynik, "title": "mnożenie"}
        return render(
            request=request,
            template_name="maths/operation.html",
            context=c
        )

    @staticmethod
    def div(request, a, b):
        a, b = int(a), int(b)
        if b == 0:
            return HttpResponse("Nie dziel przez 0")
        wynik = a / b
        c = {"a": a, "b": b, "operacja": "/",
             "wynik": wynik, "title": "dzielenie"}
        return render(
            request=request,
            template_name="maths/operation.html",
            context=c
        )
