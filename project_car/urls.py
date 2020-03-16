"""project_car URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from orders import views

urlpatterns = [

    path('', views.index_page, name='index'),
    # path('dashboard/', views.dashboard_services_page, name='dashboard'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),

    path('mine/', views.ManageServiceListView.as_view(), name='manage_service_list'),
    path('create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('<pk>/edit/', views.ServiceUpdateView.as_view(), name='service_edit'),
    path('<pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),

]
