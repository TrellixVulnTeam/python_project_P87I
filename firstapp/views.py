# coding:utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import request
from django.urls import reverse


def index(request):
    return HttpResponse(u"Welcome 姜戈!")
def add(request):
    a = request.GET['x']
    b = request.GET['y']
    return HttpResponse(str(int(a)+int(b)))
def new_add(request, x, y):
    return HttpResponse(str(int(x)+int(y)))
def cal(request):
    return render(request, 'first/cal.html')
# 转发 根据urls中的name来确定转发对象
def add2(request, x, y):
    return HttpResponseRedirect(
        reverse('add2', args=(x, y))
    )
