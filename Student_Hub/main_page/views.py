from django.shortcuts import render


def home(request):
    return render(request, 'main_page/home.html ')

def how_to_make_website(request):
    return render(request, 'main_page/how_to_make_website.html ')


def signin(request):
    return render(request, 'main_page/signin.html ')


def signin_teacher(request):
    return render(request, 'main_page/signin_teacher.html ')
