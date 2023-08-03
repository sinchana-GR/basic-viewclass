from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.
# fbv returning string as response

def fbv_string(request):
    return HttpResponse('this is fbv')
#html response
def fbv(request):
    return render(request,'fbv.html')

# class baseview returning string as response

class cbv(View):
    def get(self,request):
        return HttpResponse('this is cbv')
    
# class baseview returning html as response by using view class

class cbv_first(View):
    def get(self,request):
        return render(request,'cbv_first.html')
    
# class baseview returning html as response by using template view

class cbv_sec(TemplateView):
    template_name='cbv_sec.html'

# class base view data insertion 


class insert_cbv(View):
    def get(self,request):
        sfo=Studentform()
        d={'sfo':sfo}
        return render(request,'insert_cbv.html',d)
    def post(self,request):
        sfd=Studentform(request.POST)
        if sfd.is_valid():
            sfd.save()
            return HttpResponse('data is inserted')












