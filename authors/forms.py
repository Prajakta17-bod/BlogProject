from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserPublicDetailsForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['user'].widget.attrs.update({
            'hidden':"hidden"
        })

        self.fields['bio'].widget.attrs.update({
            'rows':"3"
        })
        
        self.fields['website'].widget.attrs.update({
            'rows':"3"
        })

        
    class Meta:
        model= UserProfile
        fields= "__all__"




class LoginUserForm(AuthenticationForm):
  def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter your username' })
        
        self.fields['password'].widget.attrs.update ({'class':'form-control','placeholder':'Enter your password' })

class Meta:
        fields=['username','password']




class SignupForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter your username' })
        
        self.fields['first_name'].widget.attrs.update ({'class':'form-control','placeholder':'Enter your firstname' })

        self.fields['last_name'].widget.attrs.update ({'class':'form-control','placeholder':'Enter your lastame' })

        self.fields['email'].widget.attrs.update ({'class':'form-control','placeholder':'Enter your email id' })

        self.fields['password1'].widget.attrs.update ({'class':'form-control','placeholder':'Enter your password' })

        self.fields['password2'].widget.attrs.update ({'class':'form-control','placeholder':'confirm your password' })

        

    username=forms.CharField(max_length=150)
    first_name=forms.CharField(max_length=150)
    last_name=forms.CharField(max_length=150)
    email=forms.EmailField(max_length=150)
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class PasswordChangingForm(PasswordChangeForm):
     old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Old password'}))
     new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New password'}))
     new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm  newpassword'}))



     class Meta:
        model=User
        fields=['old_password','new_password1','new_password2']




class EditUserProfileForm(UserChangeForm):
     email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter you username'}))
     first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter you first name'}))
     last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter you last name'}))
     username= forms.CharField( max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter you last name'}))
                                                             

     
     class Meta:
        model=User
        fields=['username','first_name','last_name','email']


