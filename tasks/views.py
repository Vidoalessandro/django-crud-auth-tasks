from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def helloworld(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm,
    })