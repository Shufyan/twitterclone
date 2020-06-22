# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from twitteruser.models import TwitterUser 

class UserCreateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = TwitterUser
        fields = UserCreationForm.Meta.fields
        # fields = UserCreationForm.Meta.fields + ('location',)
        # fields = ('username', 'email', 'password1', 'password2')
        # model = get_user_model()
        # model = TwitterUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = 'Display Name'
        # self.fields['email'].label = 'Email Address'