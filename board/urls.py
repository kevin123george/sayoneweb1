from django.urls import path
from . import views

urlpatterns = [
    path("", views.board_index, name="board_index"),
    path('boardform/',views.board_Form,name="board_form"),
    path("<int:pk>/", views.board_detail, name="board_detail"),
    path('like/',views.like_post,name="like_post"),
    path("<int:pk>/edit", views.post_update.as_view(), name="board_edit"),
    path("<int:pk>/delete", views.post_delete.as_view(), name="post_delete"),

]
