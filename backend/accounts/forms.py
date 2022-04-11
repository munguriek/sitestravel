from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Index
# from django.contrib.auth import get_user_model
# User = get_user_model()
from django.shortcuts import render, redirect


# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'telephone',)


class SignupForm(forms.Form):
    # full_name = forms.CharField(max_length=30, label='Full name')
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telephone'}))

    def signup(self, request, user):
        user.full_name = self.cleaned_data['full_name']
        user.email = self.cleaned_data['email']
        user.telephone = self.cleaned_data['telephone']
        user.save()
        return redirect('profile')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ('email', 'telephone', 'photo', 'full_name', 'permit_class', 'permit',  )
        exclude = ('password',)


class IndexForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IndexForm, self).__init__(*args, **kwargs)
        self.fields['address'].label = "Address (Enter district followed country)"
        self.fields['tel_1'].label = "Primary telephone number"
        self.fields['tel_2'].label = "Secondary telephone number"
        self.fields['email'].label = "Email address"
        self.fields['facebook'].label = "Facebook url"
        self.fields['twitter'].label = "Twitter url"
        self.fields['youtube'].label = "Youtube url"
        self.fields['whatsapp'].label = "Whatsapp url"
        self.fields['instagram'].label = "Instagram url"
        self.fields['tel_2'].required = False
        self.fields['facebook'].required = False
        self.fields['twitter'].required = False
        self.fields['youtube'].required = False
        self.fields['whatsapp'].required = False
        self.fields['instagram'].required = False

    class Meta:
        model = Index
        fields = '__all__'
        exclude = ('id', )   
      