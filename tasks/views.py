from django.shortcuts import render
from .models import Task
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    try:
        description = request.POST.get('description')
        newTask = Task.objects.create(descriptor=description)
    except Exception as e: print(str(e))
    tasks = Task.objects.order_by('updatedOn')
    return render(request,'tasks/home.html', { 'tasks': tasks })
    
def toggle(request, task_id):
    task = get_object_or_404(Task,pk=task_id)
    task.toggle_active_state()
    task.save()
    tasks = Task.objects.order_by('updatedOn')
    return render(request,'tasks/home.html', { 'tasks': tasks })
    
def done(request, task_id):
    task = get_object_or_404(Task,pk=task_id)
    task.set_as_done()
    task.save()
    tasks = Task.objects.order_by('updatedOn')
    return render(request,'tasks/home.html', { 'tasks': tasks })
    
    