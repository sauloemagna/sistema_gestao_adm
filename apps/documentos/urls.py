from django.urls import path
from .views import DocumentoCreate, DocumentDelete

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
#   path('deletar/<int:pk>/', DocumentDelete.as_view(), name='delete_documento'),

]
