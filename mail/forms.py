from django.forms import ModelForm
from .models import User, EmailContent


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = "__all__"


class EmailContentForm(ModelForm):

    class Meta:
        model = EmailContent
        fields = "__all__"
