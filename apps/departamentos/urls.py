from django.urls import path
from .views import (DepartamentoList,
                    DepartamentoCreate,
                    DepartamentoUpdate,
                    DepartamentoDelete
                    )

urlpatterns = [
    path('list/', DepartamentoList.as_view(), name='list_departamentos'),
    path('new/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('update/<int:pk>/', DepartamentoUpdate.as_view(), name='update_departamento'),
    path('delete/<int:pk>/', DepartamentoDelete.as_view(), name='delete_departamento'),

]
