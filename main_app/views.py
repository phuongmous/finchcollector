from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Finch, Toy
from .forms import FeedingForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html',
    {
        'finches': finches
    }
)

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    toy_ids = finch.toys.all().values_list('id')
    available_toys = Toy.objects.exclude(id__in=toy_ids)
    #instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', { 
        'finch': finch, 
        'feeding_form': feeding_form,
        'available_toys': available_toys
    })

def add_toy(request, finch_id, toy_id):
   Finch.objects.get(id=finch_id).toys.add(toy_id)
   return redirect('detail', finch_id=finch_id)

def remove_toy(request, finch_id, toy_id):
   Finch.objects.get(id=finch_id).toys.remove(toy_id)
   return redirect('detail', finch_id=finch_id)

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = ['species', 'description', 'lifespan', 'habitat']

class FinchUpdate(UpdateView):
    model =  Finch
    fields = ['description', 'lifespan', 'habitat']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'