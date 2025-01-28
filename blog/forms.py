from django import forms
from .models import Contact,Blog,BlogCommment


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"

        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your first name'}),
            "last_name":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your last name'}),
            "e_mail":   forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),                                                                                  
            "phone_number":forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your phone number'}),
            "contact_message":forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your message'})
        }


class CreateBlogForm(forms.ModelForm):

    class Meta:
        model= Blog
        exclude=('post_date','slug')
        widgets={
            'author':forms.TextInput(attrs={'value':'','id':'author','type':'hidden'})
        }


class UpdateBlogForm(forms.ModelForm):

    class Meta:
        model= Blog
        exclude=('post_date','slug')
        widgets={
            'author':forms.TextInput(attrs={'value':'','id':'author','type':'hidden'})
        }

class CommmentBlogForm(forms.ModelForm):
    class Meta:
        model=BlogCommment
        fields="__all__"

        widgets={'author':forms.TextInput(attrs={'value':'','id':'author','type':'hidden'}),
                'blog':forms.TextInput(attrs={'value':'','id':'blog','type':'hidden'}),
                'description': forms.Textarea(attrs={'class':'form-control'}),
        }


        