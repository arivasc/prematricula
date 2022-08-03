from django.urls import path
from Schools.views import (
    CursoListView,
    CursoDetailView,
    CursoCreateView,
    CursoUpdateView,
)

app_name = 'cursos'
urlpatterns = [
    path('', CursoListView.as_view(), name = 'curso-list'),
    path('<int:pk>/', CursoDetailView.as_view(), name = 'curso-detail'),
    path('crear/', CursoCreateView.as_view(), name = 'curso-create'),
    path('<int:pk>/editar/', CursoUpdateView.as_view(), name = 'curso-update'),

]
