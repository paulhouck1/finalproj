from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Entry
from .forms import EntryForm
import datetime

# Create your views here.
def index(request):
    entries = Entry.objects.all().order_by('date')
    return render(request, "calapp/index.html",{'entries':entries})

def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            ###
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
			
            Entry.objects.create(
                name=name,
                date=date,
                time=time,
            ).save()

            return HttpResponseRedirect('/')
    else:
        form = EntryForm()
    return render(request, "calapp/form.html", {'form': form})
    
def delete(request, pk):
	
    if request.method == "DELETE":
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()
		
    return HttpResponseRedirect('/')
		