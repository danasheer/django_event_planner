from django.shortcuts import render,get_object_or_404 , redirect
from .models import Event
from .forms import CreateEventForm
# Create your views here.

def event_list(request):
    events = Event.objects.all()
    print(
        'list'
    )
    return render(request, 'event_list.html',{'events':events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})

def info(request):
    return render(request, 'info.html')

def create_event(request):
    form = CreateEventForm()
    context = {

        "form":form,
     }
    return render(request, 'create_event.html',context)