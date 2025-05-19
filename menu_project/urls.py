from django.contrib import admin
from django.urls import path
from menu.views import test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>/', test_view, name='page'),
    path('', test_view, name='home'),
]
