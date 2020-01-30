from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta():
        fields = ['first_name','username','email','password']
        model = User
        help_texts = {
        'username':None
        }
        widgets ={
            'first_name':forms.TextInput(attrs={
            'class':'form-control'
            }),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'confirm_password':forms.PasswordInput(attrs={'class':'form-control'})

        }

    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        first_name = cleaned_data.get('first_name')
        user_name = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get("confirm_password")


        # exists_username = User.objects.filter(username=user_name).exists();
        # if exists_username == True:
        #     raise forms.ValidationError("Username is taken")

        if len(first_name) < 4:
            raise forms.ValidationError("First name is too short")
        if len(password) < 6:
            raise forms.ValidationError("Password should be more than 6 characters")

        print("password {} {}".format(password,confirm_password))
        if password != confirm_password:
            raise  forms.ValidationError("Password mismatch")



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
