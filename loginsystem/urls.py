from django.urls import path
# from . views import loginsystem
from . import views
from django.urls import path

# app_name = 'myapp'
urlpatterns = [
    path('', views.loginsystems, name='loginsystem_list'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('pasien/', views.pasien_view, name='pasien'),
    path('dokter/', views.dokter_view, name='dokter'),
    path('obat/', views.obat_view, name='obat'),
    path('laporan/', views.laporan_view, name='laporan'),
    path('settings/', views.settings_view, name='settings')
]
