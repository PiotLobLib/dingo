from django.shortcuts import render


def welcome(request):
    return render(request=request, template_name="greetings/welcome.html")


def about(request):
    return render(request=request, template_name="greetings/about.html")


def contact(request):
    return render(request=request, template_name="greetings/contact.html")
