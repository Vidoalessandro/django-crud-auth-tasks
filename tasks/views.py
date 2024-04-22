from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User

# Create your views here.
@csrf_protect
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('User created succesfully')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists',
                })
        return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Passwords do not match',
            })