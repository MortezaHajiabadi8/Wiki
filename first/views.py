from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View
from .forms import TeacherSignUpForm, StudentSignUpForm, ThesisSubmitForm
from .models import User, Teacher, Student
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
class HomeView(TemplateView):
    template_name = 'first/home.html'
    
class SignUpView(TemplateView):
    template_name = 'first/signup.html'
    
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'first/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('first:home')
    
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'first/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('first:home')


class SignOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('first:home'))
    
class SignInView(TemplateView):
    template_name = 'first/login.html'
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse('first:home'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed")
            print("They used username: {} and passoword: {}".format(username, password))
            return HttpResponseRedirect(reverse('first:signin'))

        return render(request, 'first/login.html', {})    
    
class SubmitThesisView(TemplateView):
    success_url = reverse_lazy('first:home')
    template_name = 'first/upload_thesis.html'
    
    def post(self, request, *args, **kwargs):
        thesis_form = ThesisSubmitForm(request.POST, request.FILES)
        data = request.POST.copy()
        if thesis_form.is_valid():
            thesis = thesis_form.save(commit=False)
            student = request.user
            owner = Student.objects.get(user=student)
            thesis.owner = owner
            teacher = data['teacher']
            teacher = Teacher.objects.get(pk=teacher)
            teacher.vote += 1
            teacher.save()
            thesis_form.save()
            return redirect(self.success_url)
        else:
            thesis_form = ThesisSubmitForm()
        return render(request, self.template_name, {'thesis_form': thesis_form})
