from django.shortcuts import render,redirect
from .models import Project, Skills
from .forms import AddProjectForm
from django.contrib import messages

from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalLoginView
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login


from django.views.decorators.csrf import csrf_exempt
# Create your views here.






# HOME PAGE VIEW

def homePage(request):
    template = 'base/home.html'
    projects = Project.objects.all()
    skills = Skills.objects.all()
    
#   Modal Options to LOGIN
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            user = authenticate(request, username=username,password=password)                  
            if user is not None:
                login(request, user)
            else:
                print("error")
# END OF MODAL OPTION TO LOGIN 

    # success_message = 'Success: You were successfully logged in.'
    # extra_context = dict(success_url=reverse_lazy('index'))

    context = { 'projects' : projects, 'skills' : skills }
    return render (request, template, context)



# GO TO PROJECT VIEW

def project (request, pk):
    template = 'base/project.html'
    project = Project.objects.get(id=pk)
    context = {'project':project}

    return render(request, template, context)



# ADD A PROJECT

def addProject (request):
    #Definition du template
    template = 'base/projectform.html'
    form = AddProjectForm()
    # Validation du Formulaire
    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # Récuperation du nom project
            projectname = form.cleaned_data.get("title")
            # Envoie du message 
            messages.success(request, f"Le project {projectname} a été ajouté !")

            form.save()
            return redirect("home")
    
    #Definition du Context 
    context = {'form':form}

    return render(request, template,context)

# EDIT PROJECT 

def editProject (request,pk):
    #On recupere l'ID du project et on pointe sur le bon project
    project = Project.objects.get(id=pk)
    
    print(project.id)
    #Definition du template
    template = 'base/projectform.html'
    #On pointe sur le formulaire du project ID en question
    form = AddProjectForm(instance=project)
    # Validation du Formulaire
    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES, instance=project)
        print(form)
        if form.is_valid():
            # Récuperation du nom project
            projectname = form.cleaned_data.get("title")
            # Envoie du message 
            messages.success(request, f"Le project {projectname} a été modifié !")

            form.save()
            return redirect('project',project.id )
    
    #Definition du Context 
    context = {'form':form}

    return render(request, template,context)


def deleteProject (request,pk):
    #On recupere l'ID du project et on pointe sur le bon project
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect("home")
  



