import reportlab
import io

from django.contrib.auth.models import User
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.views import View

from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):

        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)


#bloco de relatórios utilizando reportlab
def report_funcionario(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= 'attachemnt; filename="mybpdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, "Relatorio de Funcionario")

    funcionarios = Funcionario.objects.filter(empresa = request.user.funcionario.empresa)

    str_ = 'Nome: %s | Hora Extra: %.2f'
    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, str_ %(
            funcionario.nome, funcionario.total_horas_extras))
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

#bloco de relatório utilizando xhtml2pdf
class Render:

    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):
        params = {
            'today' : 'Variavel today',
            'sales' : 'Variavel sales',
            'request' : request
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')


