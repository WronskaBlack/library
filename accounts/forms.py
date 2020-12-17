from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    def save(self, commit=True):
        self.instance.is_active = False
        return super().save(commit)
