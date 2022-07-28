from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from users.views import login_user

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login_user, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register-place/', views.register_place_visit, name='register_places'),
    path('delete-place/<int:id>/', views.delete_place_visit, name='delete_place'),
    path('edit-place/<int:id>/', views.TurismUpdateView.as_view(), name='edit_place'),
    path('place-visit/<int:id>/', views.place_visit_, name='place_visit'),
    path('add-image/', views.add_image_slider, name='add-image'),
    path('delte-image/<int:id>/', views.delete_image, name='delete_image')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)