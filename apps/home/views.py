 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


def setting(request):
    return render(request, "setting.html")

def profile(request):
    return render(request, "profile.html")

def Companys(request):
    return render(request, "Companys.html")

def LastNews(request):
    return render(request, "LastNews.html")

def Trending(request):
    return render(request, "Trending.html")

def chart(request):
    return render(request, "chart.html")

def Community(request):
    return render(request, "Community.html")
