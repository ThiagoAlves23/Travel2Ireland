from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


# HERE IS THE ENTIRE DJANGO URL COMMAND

urlpatterns = [
    path('register/', views.Sign_Up_View, name='register'),
    path('accounts/profile/', views.profileView.as_view(), name='profile'),
    path('accounts/update/', views.ProfileUpdateView.as_view(), name='profile_update'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),

   
]

# HERE MAKE APP users USE STATIC FILES
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
