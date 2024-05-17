from django.shortcuts import render

# Create your views here.
from app.forms import StudentForm

def Std(request):
    form=StudentForm()
    submitted=False
    name=''
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print("form is valid sucessfully:")
            print('*'*50)
            # print('Rollno:',form.cleaned_data['Rollno'])
            print("name:",form.cleaned_data['name'])
            print('Email:',form.cleaned_data['email'])
            print('address:',form.cleaned_data['address'])

            submitted=True
            name=form.cleaned_data['name']
        else:
            print("some input data validation is fails")
    # form=StudentForm()
    return render(request,'index.html',{'form':form,'submitted':submitted,'name':name})

