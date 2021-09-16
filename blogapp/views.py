from django.shortcuts import render,redirect
from .models import blog
from.forms import ModeForm
from django.contrib.auth.models import User,auth


# Create your views here.

def home(request):
    product = blog.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        img=request.FILES['img']
        desc=request.POST.get('desc')
        date=request.POST.get('date')
        obj = blog(name=name,img=img,desc=desc,date=date)
        obj.save()
        print("blog added")

    return render(request,"index.html",{'product':product})

def delete(request,blogid):
    del_task = blog.objects.get(id=blogid)
    if request.method=="POST":
        del_task.delete()
        return redirect('/')
    return render(request,'delete.html',{'del':del_task})


def update(request,id):
    obj=blog.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'form':form,'obj':obj})

