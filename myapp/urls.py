from django.conf.urls import include, url

from myapp import views
from myapp.views import ContactView


app_name = 'myapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^myapp/about/$', views.about, name='about'),
    url(r'^myapp/contact/$', views.contact, name='contact'),
    url(r'^myapp/contact/send/$', ContactView.as_view(), name='sendmail'),    
    url(r'^myapp/Contribution/$', views.Contribution, name='Contribution'),
    url(r'^myapp/Contribution/toukou/$', views.toukou, name='toukou'),
    url(r'^myapp/episode/$', views.episode, name='episode'),
    url(r'^myapp/policy/$', views.policy, name='policy'),
    url(r'^myapp/kiyaku/$', views.kiyaku, name='kiyaku'),
]
