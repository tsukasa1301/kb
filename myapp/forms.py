from django.forms import ModelForm
from myapp.models import Episode
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from myproject import settings

class EpisodeForm(ModelForm):
    class Meta:
        model = Episode
        fields = ('name', 'ken', 'episode')



class ContactForm(forms.Form):
    namae = forms.CharField() # 名前
    address = forms.CharField() #アドレス
    message = forms.CharField(widget=forms.Textarea) #問い合わせ内容
    fields = ('namae', 'address', 'message')

    # メール送信処理
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        namae = self.cleaned_data['namae']
        address = self.cleaned_data['address']
        message = self.cleaned_data['message']
        from_email = settings.EMAIL_HOST_USER
        to = [settings.EMAIL_HOST_USER]

        send_mail(namae, address, message, from_email, to)
