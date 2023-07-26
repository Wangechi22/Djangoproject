from django.shortcuts import render, redirect
from .models import People


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = People.objects.create(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")


# these functions are for displaying the pages
def aboutpage(request):
    return render(request, "about.html")


def servicespage(request):
    return render(request, "services.html")


def loginpage(request):
    return render(request, "login.html")


def projectspage(request):
    return render(request, "projects.html")


def indexpage(request):
    data = People.objects.all()
    context = {"data" : data}
    return render(request, "index.html", context)


def signuppage(request):
    return render(request, "signup.html")
