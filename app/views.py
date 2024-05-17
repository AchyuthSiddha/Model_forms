from django.shortcuts import render

# Create your views here.
from app.forms import StudentForm

def Std(request):
    submitted=False
    name=''
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print("form is valid sucessfully:")
            print('Rollno:',form.cleaned_data['Rollno'])
            print("name:",form.cleaned_data['Name'])
            print('Marks:',form.cleaned_data['Smarks'])
            submitted=True
            name=form.cleaned_data['Name']
    form=StudentForm()
    return render(request,'index.html',{'form':form,'submitted':submitted,'name':name})

