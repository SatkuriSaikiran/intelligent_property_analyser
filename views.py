from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm, PropertyUpdateForm

def property_list(request):
    properties = Property.objects.all()
    context = {'properties': properties}
    return render(request, 'property_list.html', context)

def property_add(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    context = {'form': form}
    return render(request, 'property_add.html', context)

def property_update(request, pk):
    property = Property.objects.get(pk=pk)
    if request.method == 'POST':
        form = PropertyUpdateForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyUpdateForm(instance=property)
    context = {'form': form}
    return render(request, 'property_update.html', context)