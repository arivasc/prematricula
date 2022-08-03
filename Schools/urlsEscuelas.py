from django.urls import path
from Schools.views import (
    EscuelaListView,
    EscuelaDetailView,
    EscuelaCreateView,
    EscuelaUpdateView,
)

app_name = 'escuelas'
urlpatterns = [
    path('', EscuelaListView.as_view(), name = 'escuela-list'),
    path('<int:pk>/', EscuelaDetailView.as_view(), name = 'escuela-detail'),
    path('crear/', EscuelaCreateView.as_view(), name= 'escuela-create'),
    path('<int:pk>/editar/', EscuelaUpdateView.as_view(), name = 'escuela-update'),

]
