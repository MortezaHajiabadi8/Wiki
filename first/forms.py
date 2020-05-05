from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Teacher, User, Student, Thesis

class StudentSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name','username', 'email')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        # if commit:
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name','username', 'email')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        return user
    
class ThesisSubmitForm(forms.ModelForm):
    class Meta():
        model = Thesis
        fields = ('subject', 'teacher', 'file')
    
    # def clean_file(self):
    #     file= self.cleaned_data['file']

    #     try:
    #         #validate content type
    #         main, sub = file.content_type.split('/')
    #         if not (sub in ['pdf']):
    #             raise forms.ValidationError(u'Please use PDF file.')

    #         #validate file size
            

    #     except AttributeError:
    #         """
    #         Handles case when we are updating the user profile
    #         and do not supply a new avatar
    #         """
    #         pass

    #     return file
        