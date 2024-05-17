from django import forms

class StudentForm(forms.Form):
    Rollno=forms.IntegerField()
    Name=forms.CharField()
    Smarks=forms.IntegerField()




# echo "# Model_forms" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/AchyuthSiddha/Model_forms.git
# git push -u origin main