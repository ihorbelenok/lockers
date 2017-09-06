from django.conf.urls import url
from lock import views

urlpatterns = [
    url(r'^list/$', views.lockers_list),
    url(r'^add/$', views.lockers_add, name="lockers_add"),
    url(r'^edit/$', views.lockers_edit, name="lockers_edit"),
    url(r'^remove/$', views.lockers_remove, name="lockers_remove"),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]