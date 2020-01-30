from django.shortcuts import render
from django.views.generic import View,TemplateView
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.

class HomePageView(TemplateView):
    template_name = "scrapper/home.html"

class RegistrationView(TemplateView):
    form_class = RegisterForm
    template_name = "scrapper/register.html"
    success_url = reverse_lazy("scrapper:account")

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            #hold the cleaned data before saving to databse
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # mimimise annoying the user to travel south to login again
            login(request, user)
            redirect("scrapper:profile")

            #send a notification to the user or system
        return render(request,self.template_name,{'form':form})


class ProfileView(TemplateView):
    template_name = "scrapper/profile.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileView, self).dispatch(request, *args, **kwargs)


class LoginView(TemplateView):
    form_class = LoginForm
    template_name = "scrapper/login.html"

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            # Never trust user input
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

        #Lets see if user exists with the details provided
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('scrapper:profile')
        return render(request,self.template_name,{'form':form})


class LogoutUser(TemplateView):
    template_name = "scrapper/home.html"
    success_url ="/"
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(self.success_url)
