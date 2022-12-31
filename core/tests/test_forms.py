from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Felicity Jones'
        self.email = 'felicity@mail.com'
        self.assunto = 'Um assunto qualquer'
        self.mensagem = 'Uma mensagem qualquer'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        # Na linha abaixo é a mesma coisa que ContatoForm(request.POST), ou seja,
        # ao preencer o formuário e enviar, estaremos recebendo via POST os dados
        # no formato dos dados acima parecido com um json e o atributo data contém
        # esses dados
        self.form = ContatoForm(data=self.dados)

    def test_send_mail(self):
        # o form1 recebe os dados vindos do form.py
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        # O form2 recebe os dados de self.form criado no setup do teste
        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        # se o res1 for igual a res2 o asssertEquals retorna True
        self.assertEquals(res1, res2)
