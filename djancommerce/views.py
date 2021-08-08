from .forms import *
from django.shortcuts import render
from django import forms
from .slugger import slugger
from .models import Category


def new_category(request):
    if request.method != 'POST':
        # Create blank form
        form = CategoryForm()
    else:
        # Post submitted data and process it
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            new_cat = form.save(commit=False)
            new_cat.slug = slugger(new_cat.name)
            new_cat.save()

    context = {'form': form}
    return render(request, 'new_topic.html', context)