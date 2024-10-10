from django.urls import path

from .views import ListarExercicios, EditarExercicios
from .views.view_treinos import ListarTreinos, EditarTreinos


urlpatterns = [
    path('treinos/', ListarTreinos.as_view(), name='treinos-list-create'),
    path('treinos/<uuid:pk>/', EditarTreinos.as_view(), name='treino-edit'),
    path('exercicios/', ListarExercicios.as_view(), name='exercicios-list-create'),
    path('exercicios/<uuid:pk/>', EditarExercicios.as_view(), name='exercicios-edit'),
]
