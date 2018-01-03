from django.shortcuts import render, HttpResponse, redirect
from cmdb_app import models

# Create your views here.

def login(request):
    error_msg = ""
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        user = request.POST.get("user", None)
        pwd = request.POST.get("pwd", None)
        user_obj = models.AdminInfo.objects.filter(username=user, password=pwd).first()
        if user_obj:
            res = redirect('/index/')
            res.set_cookie('user', user, max_age=86400)
            return res
        else:
            error_msg = "用户名或密码错误"
        return render(request, 'login.html', {'error_msg': error_msg})


def auth(func):
    def inner(reqeust, *args, **kwargs):
        v = reqeust.COOKIES.get('user')
        if not v:
            return redirect('/login/')
        return func(reqeust, *args, **kwargs)
    return inner

@auth
def group(request):
    v = request.COOKIES.get('user')
    obj_Group = models.UserGroup.objects.all()
    return render(request, 'group.html',
                  {'current_user': v, 'obj_Group': obj_Group})

@auth
def users(request):
    v = request.COOKIES.get('user')
    obj_UserProfile = models.UserProfile.objects.all()
    obj_AdminInfo = models.AdminInfo.objects.all()
    return render(request, 'users.html',
                  {'current_user': v,
                   'obj_UserProfile': obj_UserProfile,
                   'obj_AdminInfo': obj_AdminInfo,
                   })

@auth
def test(request):
    v = request.COOKIES.get('user')
    obj_execl = models.execl.objects.all()
    return render(request, 'test.html', {'current_user': v,'obj_execl':obj_execl })
