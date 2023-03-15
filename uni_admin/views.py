
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def delete_concour(request, concour_id):
    concour = get_object_or_404(concours, id=concour_id)
    concour.delete()
    return redirect('concour')



def concour_admin(request):
    list_concours = concours.objects.all()
    search_term = request.GET.get('q')
    if search_term:
        list_concours = list_concours.filter(name__icontains=search_term)
    return render(request,'uni_admin/concour.html',{"list_concours" : list_concours})



def add_con(request):
    if request.method == 'POST':
        form = add_Concour(request.POST)
        if form.is_valid():
        
            new_name = form.cleaned_data["name"]
            new_university_name = form.cleaned_data["university"]
            new_description = form.cleaned_data["description" ]
            #new_filiere = form.cleaned_data["filiere"]
            new_strat_date = form.cleaned_data["start_date" ]
            new_end_date= form.cleaned_data["end_date"]
            new_documets= form.cleaned_data["doc_necessaire"]
            new_location = form.cleaned_data["location"]
            
            new_university = university.objects.get(name=new_university_name,location=new_location)

            
            new_concour = concours(
                name = new_name,
                university = new_university,
                #filliere= new_filiere,
                description = new_documets,
                start_date = new_strat_date,
                end_date = new_end_date,
                doc_necessaire = new_documets
            )
            
            new_concour.save()
            
            messages.success(request, 'Votre concours a été créé avec succès.')
            return redirect('concour')
    else:
        form = add_Concour()
    return render(request, 'uni_admin/add_concour.html',{
        'form': form
    })