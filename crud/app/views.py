from django.shortcuts import render , redirect
from .forms import studentreg
from .models import user
# Create your views here.


def add(request):
    if request.method == 'POST':
        fm = studentreg(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = user(name = name , email = email , password = password)
            reg.save()
            fm=studentreg()
    else:
        
        fm = studentreg()
    stud = user.objects.all()
    return render (request,'app/addandshow.html',{'form':fm,'stud':stud})



def delete(request , id):
    if(request.method == 'POST'):
        pi = user.objects.get(pk=id)
        pi.delete()
        return redirect (add)


def update(request, id):

    
    if(request.method == 'POST'):
        pi = user.objects.get(pk=id)
        fm = studentreg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = user.objects.get(pk=id)
        fm = studentreg(instance=pi)

    return render (request,'app/createstudent.html',{'form':fm})