from django import forms
from .models import Subject, Lesson

class Subject_Form(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'

class Lesson_Form(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = '__all__'

