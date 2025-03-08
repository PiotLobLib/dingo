from django.http import HttpResponse


class Calculator:
    @staticmethod
    def math(request):
        return HttpResponse("Tu będzie matma")

    @staticmethod
    def add(request, a, b):
        a, b = int(a), int(b)
        return HttpResponse(a + b)

    @staticmethod
    def sub(request, a, b):
        a, b = int(a), int(b)
        return HttpResponse(a - b)

    @staticmethod
    def mul(request, a, b):
        a, b = int(a), int(b)
        return HttpResponse(a * b)

    @staticmethod
    def div(request, a, b):
        a, b = int(a), int(b)
        if b == 0:
            return HttpResponse("Nie dziel przez 0")
        return HttpResponse(a / b)
