from django import forms

from todolist.models import Task
 
class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user', 'date', 'is_finished']