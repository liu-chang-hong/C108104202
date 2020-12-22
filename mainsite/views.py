from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainsite.models import PlayList, Video, Post , PlayList1, PlayList2, PlayList3
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

def chart(request, year=0, month=0):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    branches = Branch.objects.all()
    if year == 0:
        data = StoreIncome.objects.all()
    else:
        data = StoreIncome.objects.filter(income_year=year)
        if month>0:
            data = data.filter(income_month=month)
    if year>0 and month>0:
        title ="{}年{}月各分店營收情形".format(year, month)
    elif year>0:
        title ="{}年".format(year)
    else:
        title = "各分店營收情形"
    return render(request, "mychart.html", locals())
def taipei(request):
    return render(request,"taipei.html", locals())
def newtaipei(request):
    return render(request,"newtaipei.html", locals())
def kao(request):
    return render(request,"kao.html", locals())
def tyu(request):
    return render(request,"tyu.html", locals())
def taipeicar(request):
    return render(request,"taipeicar.html", locals())
def newtaipeicar(request):
    return render(request,"newtaipeicar.html", locals())
def kaocar(request):
    return render(request,"kaocar.html", locals())
def tyucar(request):
    return render(request,"tyucar.html", locals())
def playlist(request):
    now = datetime.now()
    items = PlayList.objects.all()
    return render(request, "playlist.html", locals())
def playlist1(request):
    now = datetime.now()
    items = PlayList1.objects.all()
    return render(request, "playlist1.html", locals())
def playlist2(request):
    now = datetime.now()
    items = PlayList2.objects.all()
    return render(request, "playlist2.html", locals())
def playlist3(request):
    now = datetime.now()
    items = PlayList3.objects.all()
    return render(request, "playlist3.html", locals())
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