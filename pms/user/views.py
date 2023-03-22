from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,FormView
from .models import User
from .forms import ManagerRegisterForm,DeveloperRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django import forms
from django.views.generic import ListView
from project.models import Project


# Create your views here.
class ManagerRegisterView(CreateView):
    #model = User
    form_class = ManagerRegisterForm
    template_name = 'user/manager_register.html'
    success_url = '/user/dashboard'
    
    
    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'manager'
    #     return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        #response = super().form_valid(form)
        user = form.save()
        if user is not None: 
            subject = "Welcome"
            message = "welcome User!"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
            login(self.request,user)
        return super(ManagerRegisterView,self).form_valid(form)
        #return response
    
    # def form_valid(self,form):
    #     #email = form.cleaned_data.get('email')
        
    #     user = form.save()
    #     login(self.request,user)
    #     return super().form_valid(form)
        

class DeveloperRegisterView(CreateView):
    #model = User
    form_class = DeveloperRegistrationForm
    template_name = 'user/developer_register.html'
    success_url = '/user/dashboard' 
    
    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'developer'
    #     return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        #response = super().form_valid(form)
        user = form.save()
        if user is not None: 
            subject = "Welcome"
            message = "welcome User!"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
            login(self.request,user)
        return super(DeveloperRegisterView,self).form_valid(form)
    


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = "/"
    
    def get_redirect_url(self):
        if self.redirect_authenticated_user:
            if self.request.user.is_manager1:
                return '/user/dashboard/'
            else:
                return '/developer/'
        
    # def form_valid(self, form):
    #     response = super().form_valid(form)
        
    #     subject = "You have logged in"
    #     message = "Thank you for login"
    #     from_email = settings.EMAIL_HOST_USER
    #     recipient_list = [self.request.user.email]
    #     send_mail(subject, message, from_email, recipient_list)
        
    #     return response
        
        
        
class UserLogoutView(LogoutView):
    template_name = "user/logout.html"
    
    
class SignUpForm(forms.Form):
    CHOICES = (
        ('manager', 'Manager'),
        ('developer', 'Developer'),
    )
    account_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    

class SignUpView(FormView):
    template_name = 'user/signup.html'
    form_class = SignUpForm
    

    def form_valid(self, form):
        account_type = form.cleaned_data['account_type']
        if account_type == 'manager':
            # Redirect to manager registration form
            return redirect('managerregister')
        elif account_type == 'developer':
            # Redirect to developer registration form
        
            return redirect('developerregister')
        else:
            return redirect('signup')
    
    
    
#--------------------------------------------------------------------------------------------------------------
@login_required
def dashboard(request):
    return render(request,'user/dashboard.html')

def password(request):
    return render(request,'user/password.html')


class ManagerDashboardView(ListView):            
    
    def get(self, request, *args, **kwargs):
        project = Project.objects.all().values()
        
        return render(request, 'user/manager_dashboard.html',{
            'projects':project,
        })

    template_name = 'user/manager_dashboard.html'
    
class DeveloperDashBoardView(ListView):
    
    model = User
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
    def get_queryset(self):
        
        return super().get_queryset()
    
    template_name = 'user/developer_dashboard.html'