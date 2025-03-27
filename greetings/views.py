from django.shortcuts import render


def welcome(request):
    return render(request=request, template_name="greetings/welcome.html")


# instead TemplateView is used in urls
def about(request):
    return render(request=request, template_name="greetings/about.html")


# instead TemplateView is used in urls
def contact(request):
    return render(request=request, template_name="greetings/contact.html")
