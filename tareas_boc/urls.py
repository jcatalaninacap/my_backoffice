from django.urls import path
from . import views

urlpatterns = [
    #path('tareas_boc/', views.tareas_boc, name='tareas_boc'),
    path('json-to-grid/', views.json_to_grid, name='json_to_grid'),
]