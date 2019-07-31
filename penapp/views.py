from django.shortcuts import render, get_object_or_404, redirect
from .models import Pen


def home(request):
    pens = Pen.objects
    return render(request, 'home.html', {'pens':pens})

def detail(request, pen_id):
    details = get_object_or_404(Pen, pk=pen_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
		return render(request, 'new.html')

def create(request):
	pen = Pen()
	pen.title = reqest.GET['title']
	pen.body = request.GET['body']
	pen.pub_date = timezone.datetime.now()
	pen.save()
	return redirect('/pen/'+str(pen.id))

