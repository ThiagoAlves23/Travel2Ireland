# LOAD DJANGO MODULES
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views
from django.contrib import auth
from django.urls import reverse_lazy
# Class Based View
from django.views.generic import TemplateView, CreateView

# message alerts
from django.contrib import messages
from django.contrib.messages import constants

# SEARCH THE DJANGO FORM
from .forms import UserForm, ProfileForm, SignUpForm



#PROFILE VIEW
class profileView(TemplateView):
    template_name = 'profile.html' 

    def get(self, request):
        user = request.user
        profile = user.profile
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
        #WHAT IS INSIDE THE CONTEXT CAN BE USED IN THE TEMPLATE
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)

# UPDATE PROFILE
class ProfileUpdateView(TemplateView):
    template_name = 'profile-edit.html'

    # UPLOAD PROFILE INFO
    def get(self, request):
        user = request.user
        profile = user.profile
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)

    #SAVE PROFILE 
    def post(self, request):
        user = request.user
        profile = user.profile
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid(): 
            user_form.save()
            profile_form.save()
            messages.add_message(request, constants.SUCCESS, 'Profile successfully edited!')
            return redirect(reverse_lazy('profile')) 
        context = {
            'user_form':user_form,
            'profile_form':profile_form
        }
        return self.render_to_response(context)

# LOGIN USER
def login_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            messages.add_message(request, constants.ERROR, f'User {request.user.username} is authenticated!')
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.add_message(request, constants.ERROR, 'User or password incorret!')
            return redirect(reverse_lazy('login'))
        else:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, f'Welcome {username}!')
            return redirect(reverse_lazy('index'))

def Sign_Up_View(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'New user Sucess Register!')
            return redirect(reverse_lazy('login'))
        else:
            messages.add_message(request, constants.ERROR, 'Error New user Register!')
            return redirect(reverse_lazy('register'))
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

# CHANGE PASSWORD
class PasswordChangeView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('redirect')
    template_name = 'password/password-change.html'

#RESET PASSWORD
class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'password/password-reset-form.html'
    subject_template_name = 'password/password-reset-subject.txt'
    email_template_name = 'password/password-reset-email.html'

#COMPLETION PAGE ON CHANGING THE PASSWORD
class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'password/password-reset-done.html'

# PASSWORD CHANGE CONFIRMATION
class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'password/password-reset-confirm.html'

#PASSWORD RESET COMPLETE
class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'password/password-reset-complete.html'