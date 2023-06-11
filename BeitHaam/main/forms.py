from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AddNewCategory(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    image = forms.CharField(label="Image", max_length=500)

class AddNewDish(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    price = forms.IntegerField(label="Price")
    image = forms.CharField(label="Image", max_length=500)
    description = forms.CharField(label="Description",max_length=500)
    is_gluten_free = forms.BooleanField(required=False)
    is_vegan = forms.BooleanField(required=False)

class AddNewTopping(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    price = forms.IntegerField(label="Price")
    image = forms.CharField(label="Image", max_length=500)

class SubmitDelivery(forms.Form):
    street = forms.CharField(label="Street",max_length=200)
    house_number = forms.IntegerField()
    city = forms.CharField(label="City",max_length=200)
    comment = forms.CharField(label="Comment",max_length=200)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))

    class Meta:
        model=User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'