from django.shortcuts import  redirect,render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import SignupForm,LoginUserForm,PasswordChangingForm,EditUserProfileForm,UserPublicDetailsForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordChangeView
from blog.models import Blog,BlogCommment
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import  SuccessMessageMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import UserProfile



def signUp(request):
    if request.method =='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
         form.save()
         messages.success(request,"Your account is  created succesfully")
         new_user = authenticate(
             username=form.cleaned_data['username'],
             password=form.cleaned_data['password1']
        )
         login(request,new_user)
         return redirect ('blog_home')
        else:
            messages.error(request,"Error")
    else:
        form=SignupForm()
    return render (request,"authors/register.html",{"form":form})



def logIn(request):
    if request.method =='POST':
        form=LoginUserForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,"You are logged in  succesfully")
                return redirect ('blog_home')
            else:
                messages.error(request,"Error")
        else:
             messages.error(request,"Username or password  incorrect") 
    form=LoginUserForm()                  
    return render (request,"authors/login.html",{"login_form":form})



def logOut(request):
    logout(request)
    messages.success(request,"Yoy have suceesfully logged out")
    return redirect ('blog_home')






def profile(request,user_name):
    user_related_data=Blog.objects.filter(author__username = user_name)
    user_profile_data= UserProfile.objects.get(user=request.user.id)

    context={
        "user_related_data": user_related_data,
       "user_profile_data": user_profile_data

    }
    return render(request,"authors/profile.html",context)





class PasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    form_class=PasswordChangingForm
    login_url='login'
    success_url= reverse_lazy('password_success')

def password_success(request):
      return render(request,"authors/password_change_success.html")

class UpdateUserView(SuccessMessageMixin,generic.UpdateView ):
    form_class=EditUserProfileForm
    template_name="authors/edit_user_profile.html"
    success_url=reverse_lazy('blog_home')
    success_message="user  updated"
    

    def get_object(self,querset=None):
        return self.request.user
    

class DeleteUser(LoginRequiredMixin,SuccessMessageMixin,generic.DeleteView):
    model=User
    login_url='login'
    template_name="authors/delete_user_confirm.html"
    success_message="User has been deleted"
    success_url=reverse_lazy('blog_home')


class UpdatePublicDetails(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView):
    login_url='login'
    form_class=UserPublicDetailsForm
    template_name="authors/edit_public_details.html"
    success_url=reverse_lazy('blog_home')
    success_message="user  updated"
    

    def get_object(self,querset=None):
     return self.request.user.userprofile
    
class Dashboard(LoginRequiredMixin,generic.View):
    login_url="login"
    
    def get (self,request):
        user_related_data=Blog.objects.filter(author__username=request.user.username)
        user_comments=BlogCommment.objects.filter(author__username=request.user.username)


        paginator=Paginator(user_related_data,10)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)

        context={
            'user_related_data':user_related_data,
            'page_obj':page_obj,
            'user_comments':user_comments
        }
        return render(request,"authors/dashboard.html",context)
        
    