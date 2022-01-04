from django import forms

from .models import Userdetails

Select_User= [
    ('admin', 'Admin'),
    ('super_admin', 'Super_Admin'),
    ('manager', 'Manager'),
    ('staff', 'Staff'),
    ]

class UserdetailsForm(forms.ModelForm):
	Select_User = forms.CharField(label='Select_User', widget=forms.Select(choices=Select_User))
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = Userdetails
		fields = ['username', 'mobile_no', 'email', 'password', 'Select_User']