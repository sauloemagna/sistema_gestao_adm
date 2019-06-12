from django.urls import path
from .views import  (FuncionariosList,
                     FuncionarioEdit,
                     FuncionarioDelete,
                     FuncionarioCreate,
                     report_funcionario,
                     Pdf)

urlpatterns = [

    path('', FuncionariosList.as_view(), name ='list_funcionarios'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name ='update_funcionario'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name ='delete_funcionario'),
    path('novo/', FuncionarioCreate.as_view(), name ='create_funcionario'),
    path('report_funcionario/', report_funcionario, name ='report_funcionario'),
    path('report_funcionario_html/', Pdf.as_view(), name ='report_funcionario_html'),

]
