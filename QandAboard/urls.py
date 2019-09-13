from django.urls import path
from . import views

urlpatterns = [
    path("", views.QandA_index, name="QandA_index"),
    path("<int:pk>/", views.QandA_detail, name="QandA_detail"),
    path("Ask/",views.Ask_Form,name="ask"),
    path("<int:pk>/edit", views.post_update.as_view(), name="QandA_edit"),
    path("<int:pk>/delete", views.post_delete.as_view(), name="QandA_delete"),
    
]
