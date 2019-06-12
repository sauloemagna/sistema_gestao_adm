from django.urls import path
from .views import (HoraExtraCreate,
                    HoraExtraDelete,
                    HoraExtraList,
                    HoraExtraUpdate,
                    HoraExtraUpdateBase,
                    UtilizouHE,
                    NaoUtilizouHE,
                    ExportCSV,
                    ExportExcel)

urlpatterns = [

    path('', HoraExtraList.as_view(), name ='list_hora_extra'),
    path('edita-funcionario/<int:pk>/', HoraExtraUpdate.as_view(), name ='update_hora_extra'),
    path('editar/<int:pk>/', HoraExtraUpdateBase.as_view(), name ='update_hora_extra_base'),
    path('utilizou-he/<int:pk>/', UtilizouHE.as_view(), name ='utilizou_he'),
    path('naoutilizou-he/<int:pk>/', NaoUtilizouHE.as_view(), name ='nao_utilizou_he'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name ='delete_hora_extra'),
    path('novo/', HoraExtraCreate.as_view(), name ='create_hora_extra'),
    path('exportar-csv/', ExportCSV.as_view(), name ='export_csv'),
    path('exportar-excel/', ExportExcel.as_view(), name ='export_excel'),

]
