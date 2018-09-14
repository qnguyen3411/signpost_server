from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(f'^treasurehunt$', views.find_Thunt),
    url(f'^treasurehunt/add$', views.create_Thunt),
    url(f'^cluenode/delete$', views.delete_node),
    url(f'^cluenode/add', views.create_node),

]
