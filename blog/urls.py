"""
This file handles the url patterns for displaying the blog as opposed to displaying the
admin side of the web_site.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]
