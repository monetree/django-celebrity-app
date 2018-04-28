from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from . models import country,state,city,publication


def test(request):
    # pubs = state.objects.select_related('country')
    pubs = publication.objects.select_related('country','state','city')
    print(pubs)
    return render(request,'test/index.html',{'data':pubs})

def one(request):
    return redirect('/test',{ 'pk':'result' })

