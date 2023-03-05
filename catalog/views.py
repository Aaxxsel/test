from django.shortcuts import render, redirect

from catalog.forms import TitleText
from catalog.models import Notes


# Create your views here.

def index(request):
    return render(request, "catalog/home_page.html")


def tasks_list(request):
    notes_list = Notes.objects.filter()
    return render(request, "catalog/tasks_list.html", {'notes_list': notes_list})


def new_task(request):
    if request.method == "POST":
        form = TitleText(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            note = Notes.objects.create(headings=title, text=text)
            return redirect('tasks_list')
    elif request.method == 'GET':
        return render(request, "catalog/task_form.html")


def task(request, task_id):
    text_task = Notes.objects.filter(id=task_id).first()
    return render(request, "catalog/task.html", {"text_task": text_task})


def del_task(request, del_task_id):
    Notes.objects.filter(id=del_task_id).delete()
    return redirect('tasks_list')
