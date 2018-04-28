from django.shortcuts import render,get_object_or_404, get_list_or_404
from .models import Todo
from django.http import HttpResponseRedirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from django.utils import timezone


def index(request):
    data=Todo.objects.all()
    return render(request, 'index.html',{'data':data})

def form(request):
    if request.method == 'POST' and request.FILES['file']:
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        obj = Todo(title=title,text=desc,photo=uploaded_file_url)
        obj.save()
    return HttpResponseRedirect('/index')

def delete_rec(request,pid=0):
    id = get_object_or_404(Todo,pk=pid)
    obj = id.delete()
    return HttpResponseRedirect('/index')

def update(request,pid=0):
    id = get_object_or_404(Todo,pk=pid)
    return render(request, 'update.html',{'id':id})

def update_data(request,pid=0):
    title = request.POST.get('title')
    desc = request.POST.get('desc')
    time = timezone.now()
    obj=Todo.objects.filter(pk=pid).update(title=title,text=desc,created_at=time)
    return HttpResponseRedirect('/index')

def session(request):
    sess = request.session['member_id'] = 'data'
    if sess:
        return HttpResponse("You're logged in.")

def get_session(request):
    data = request.session['member_id']
    if data:
        return HttpResponse(data)

def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        obj = Todo(photo=uploaded_file_url)
        obj.save()
        return render(request, 'file_upload.html', {
            'url': uploaded_file_url
        })
    return render(request, 'file_upload.html')
