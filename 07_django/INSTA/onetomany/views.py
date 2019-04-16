from django.shortcuts import render, redirect
from .forms import *
from .models import Writer, Book, Chapter
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = WriterModelForm(request.POST)

        if form.is_valid(): # request.POST에 있는 data가 저장가능??
            form.save()
            return redirect('detail')
        else: # 실패하면?
            pass # 밑의 return render로 들어감
    elif request.method == 'GET':
        form = WriterModelForm()
    return render(request, 'new.html', {
        'form': form
    })


def update(request, id):
    writer = Writer.objects.get(id=id)
    if request.method == 'POST':
        form = WriterModelForm(request.POST, instance=writer)

        if form.is_valid():
            form.save()
            return redirect('성공')
        else:
            return redirect('실패!')
    elif request.method == 'GET':
        form = WriterModelForm(instance=writer)
        return render(request, 'edit.html', {
            'form': form
        })