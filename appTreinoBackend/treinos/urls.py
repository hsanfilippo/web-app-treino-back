from django.urls import path

from views import ListarTreinos, EditarTreinos


urlpatterns = [
    path('treinos/', ListarTreinos.as_view(), name='treinos-list-create'),
    path('treinos/<uuid:pk>/', EditarTreinos.as_view(), name='treino-edit'),
]
