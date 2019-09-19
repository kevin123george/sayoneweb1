
from django.contrib import admin
from django.urls import path,include
from authentication import views 
from django.contrib.auth.models import User

urlpatterns = [
    path('admin/', admin.site.urls),
    path("board/", include("board.urls"),name='home'),
    path("QandA/", include("QandAboard.urls")),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit',views.edit,name='edit'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.home),
   
   
]
