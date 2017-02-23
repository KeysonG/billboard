from django.conf.urls import url

from . import views
from django.contrib.auth import views as authviews

urlpatterns = [
	url(R'^$', views.post_list, name='post_list'),
	url(R'^new-post$', views.new_post, name='new_post'),
	url(R'^login/$', authviews.login, name='login'),
	url(R'^logout/$', authviews.logout, {'next_page': '/'}, name='logout'),
	url(R'^new/comment$', views.new_comment, name='new_comment'),


]