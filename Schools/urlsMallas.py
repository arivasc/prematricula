from django.urls import path
from Schools.views import (
    MallaListView,
    MallaDetailView,
    MallaCreateView,
    MallaUpdateView,
)

app_name = 'mallas'
urlpatterns = [
    path('', MallaListView.as_view(), name = 'malla-list'),
    path('<int:pk>/', MallaDetailView.as_view(), name = 'malla-detail'),
    path('crear/', MallaCreateView.as_view(), name= 'malla-create'),
    path('<int:pk>/editar/', MallaUpdateView.as_view(), name = 'malla-update'),
    
]
