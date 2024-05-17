from typing import Any
from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField(widget=forms.Textarea)


    def clean_name(self):
        print("validating name field")
        inputname=self.cleaned_data['name']
        if len(inputname) < 4:
            raise forms.ValidationError("Atleast four character should be valid otherwise its throw an error")
        return inputname



# echo "# Model_forms" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/AchyuthSiddha/Model_forms.git
# git push -u origin main