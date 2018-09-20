from django.http import request
from django.shortcuts import render
from secondapp.models import User


def index(request):
    content = u'来自Django的一串字符串'
    contentList = ['PHP', 'Python', 'Java', 'C#', 'ASP']
    contentDir = {'魏' : '曹操', '蜀' : '刘备', '吴' : '孙权'}
    users = User.objects.all()
    return render(request, 'second/index.html', {'cont' : content, 'lists' : contentList, 'map' : contentDir, 'users' : users})