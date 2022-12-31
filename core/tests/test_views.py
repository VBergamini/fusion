from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@mail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha mensagem'
        }
        # A clase Cliente permite criar um objeto e enviar uma requisição http sem acessar o navegador
        self.cliente = Client()

    def test_form_valid(self):
        # Como o reverse_lazy cria um redirecionamento para a view index, se os dados passados em data forem
        # corretos vai ser gerado um http request com status_code 302 (o status 302 significa temporariamente
        # redirecinado)
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        # Se o request for igual ao code 302 o assert Equals retorna True
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        # Aqui os dados do formuários estão incompletos o que faz que o formulário não seja enviado
        dados = {
            'nome': 'Felicity Jones',
            'assunto': 'Meu assunto'
        }
        # Como o formulário não é válido o request terá o status_code 200, ou seja, o direcionamento foi realizado
        # com sucesso mas os dados não foram enviados pois eram inválidos.
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        # Se o request tiver um status_code igual a 200 o assertEquals retorna True.
        self.assertEquals(request.status_code, 200)

