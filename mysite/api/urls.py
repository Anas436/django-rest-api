from django.urls import path
from . import views

urlpatterns = [

    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogposts-view-create"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestory.as_view(), name="update"),

]