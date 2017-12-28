from django.shortcuts import render
from cmdb_app import models

# Create your views here.

def info(request):
    obj_UserProfile = models.UserProfile.objects.all()
    obj_AdminInfo = models.AdminInfo.objects.all()
    return render(request, 'info.html',{'obj_UserProfile':obj_UserProfile,'obj_AdminInfo':obj_AdminInfo})