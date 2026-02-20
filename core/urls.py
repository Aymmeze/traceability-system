from django.contrib import admin
from django.urls import path
# Importujemy naszą nową funkcję z inventory
from inventory.views import traceability_search 

urlpatterns = [
    path('admin/', admin.site.urls),
    # To jest nasz nowy adres:
    path('', traceability_search, name='search'), 
]