from django import forms
from .models import Comment, Post, User, Account
from django.contrib.auth.forms import AuthenticationForm


class TicketForm(forms.Form):
    # زمانی از این فیلد استفاده میشه که ما از form.as_p استفاده کنیم👇🏻
    # SUBJECT_CHOICES = (
    #     ('پیشنهاد', 'پیشنهادات'),
    #     ('انتقاد', 'انتقادات'),
    #     ('گزارش', 'گزارشات')
    # )
    name = forms.CharField(max_length=250, required=True, label="نام",
                           widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوداگی'}))
    phone = forms.CharField(max_length=11, required=True, label="شماره تلفن")
    email = forms.EmailField(required=True, label="ایمیل")
    # زمانی از این فیلد استفاده میشه که ما از form.as_p استفاده کنیم👇🏻
    # subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    # زمانی از این فیلد استفاده میشه که ما از فرم را به صورت دستی پر کنیم👇🏻
    subject = forms.CharField(label="موضوع")
    message = forms.CharField(widget=forms.Textarea, required=True, label="پیام")

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError("شماره تلفن باید عددی باشد")
            if len(phone) < 11:
                raise forms.ValidationError("شماره تلفن باید 11 رقم باشد")
            else:
                return phone


class CommentForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if name:
            if len(name) < 3:
                raise forms.ValidationError("نام وارد شده کوتاه است")
            else:
                return name

    class Meta:
        model = Comment
        # exclude = ['created', 'updated', 'active', 'post']
        fields = ['name', 'body']
        # widgets = {
        #     'body': forms.TextInput(attrs={
        #         'placeholder': 'متن کامنت',
        #         'style': 'border-radius: 5px;'
        #     }),
        #     'name': forms.TextInput(attrs={
        #         'placeholder': 'مثلا : امیررضا جمشیدی',
        #         'style': 'border-radius: 5px;'
        #     })
        # }


class SearchForm(forms.Form):
    query = forms.CharField()


class CreatePostForm(forms.ModelForm):
    img1 = forms.ImageField()
    img2 = forms.ImageField()

    class Meta:
        model = Post
        fields = ['title', 'description', 'reading_time', 'category']


# login form👇🏻
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=250, required=True)
#     password = forms.CharField(max_length=250, required=True, widget=forms.PasswordInput)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput, label="repeat password")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("پسورد وارد شده با تاییده پسورد یکی نمی باشد")
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class AccountEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['date_of_birth', 'job', 'bio', 'photo']
