from django.conf.urls import url
from .views import profile, user_edit
from django.contrib.auth.views import login, logout_then_login
from .views import signup
from django.contrib.auth.decorators import user_passes_test

urlpatterns = [
  url(r'^profile/', profile, name='profile'),
  url(r'^edit/$', user_edit, name='user_edit'),
  url(r'^logout/', logout_then_login, name='logout'),
  url(r'^login/', user_passes_test(lambda u: u.is_anonymous, login_url='/accounts/profile')(login), {'template_name':'account/login.html'}, name='login'),
  url(r'^signup/', signup, name='signup'),
]