from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms

from .models import Subject,Student,User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)



    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True, request=None):
        user = super(UserCreationForm, self).save(commit=False)

        # set the password
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
            self.save_m2m()

        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
                                         help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password, but you can change the password "
                                                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if not (self.cleaned_data.get('is_teacher') ^ self.cleaned_data.get('is_student')):
            raise forms.ValidationError('Exactly one of is_teacher and is_student should be True.')

        return super(UserChangeForm, self).clean()

    def clean_password(self):
        return self.initial["password"]

    def save(self, commit=True, request=None):
        user = super(UserChangeForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class MyUserAdmin(UserAdmin):


    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('username',  'email')

    fieldsets = (
        (None, {'fields': ('username', 'password', 'is_superuser', 'is_staff','is_teacher','is_student')},),
        ('User Group', {'fields': ('groups',)},),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number',)},),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'email', 'password1', 'password2',  'groups')},),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number',)},),
    )

    search_fields = ('username','email',)
    ordering = ('username',)
    filter_horizontal = ()



    def save_form(self, request, form, change):
        """
        Method overwritten to pass request to save method.
        :param request: The request object
        :param form: The form used (Add / Change)
        :param change: if True, change is done, or add otherwise
        :return:
        """
        return form.save(commit=False, request=request)


admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(User,MyUserAdmin)


