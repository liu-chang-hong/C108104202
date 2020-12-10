from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainsite.models import PlayList, Video, Post
from mainsite.models import AccessInfo, Branch, StoreIncome
import random
from datetime import datetime

def homepage(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,"index.html", locals())

def mychart(request, bid=0):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    branches = Branch.objects.all()
    if bid == 0:
        data = StoreIncome.objects.all()
    else:
        data = StoreIncome.objects.filter(branch=bid)
    return render(request, "mychart.html", locals())

def lotto(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    lucky_no = random.randint(1, 42)
    numbers = list()
    for i in range(6):
        numbers.append(random.randint(1, 42))

    return render(request,"lotto.html", locals())

def playlist(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    items = PlayList.objects.all()
    return render(request, "playlist.html", locals())

def showlist(request, id):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    titles = Video.objects.filter(plist=id)
    return render(request, "showlist.html", locals())
    
def showpost(request, slug):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, "post.html", locals())
    except:
        return redirect("/")