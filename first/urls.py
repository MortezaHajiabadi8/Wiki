from django.urls import path, include
from . import views

app_name = 'first'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('signout/', views.SignOutView.as_view(), name='signout'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('upload/thesis/', views.SubmitThesisView.as_view(), name='upload_thesis'),
   
]