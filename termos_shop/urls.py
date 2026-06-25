from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from shop import views
from shop.urls import router
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('api/me/', views.MeAPIView.as_view()),
    path('profile/', views.profile, name='profile'),
    path('about-site/', views.about_site, name='about_site'),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)