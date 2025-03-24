from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("wiki/search", views.search, name='search'),
    path("wiki/new-page", views.new_page, name="new_page"),
    path("wiki/random", views.random_page, name="random-page"),
    path('wiki/edit/<str:title>', views.edit, name='edit'),
    path("wiki/<str:TITLE>", views.get_entry_page, name="entry_page")   
]
