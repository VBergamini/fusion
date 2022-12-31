import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_path


# Foi criado uma classe para testar a função get_filepath herdando a classe TestCase
class GetFilePathTestCase(TestCase):

    # No setup do teste, é usado o modulo uuid para gerar o nome do arquivo que por padrão ele gera um arquivo de
    # de 40 caracteres e estamos colocando a extensão png manualmente (na função em models isso é feito pelo split
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    # Como nomeamos o valor do arquivo é teste.png, para saber se a função está funcionando corretamnete, este valor
    # deve ser trocado de teste.png para um nome com 40 caracteres.png, o teste consiste em comparar o comprimento
    # do valor do arquivo que é teste.png com o comprimento do valor do filename que é gerado pelo uuid, se forem
    # iguais significa que a função está funcionando corretamente e o retorno do teste será True
    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        # aqui está comparando se len(arquivo) é igual a len(filename) se sim assertTrue será True
        self.assertTrue(len(arquivo), len(self.filename))


# Teste do método __str__ da classe Servico
# Lenbrando que o método __str__ retorna uma string no atributo serviço
class ServicoTestCase(TestCase):

    # usamos os mommy para criar uma instância da classe Serviço e nomeamos de servico
    def setUp(self):
        self.servico = mommy.make('Servico')

# O teste consiste em comparar a instancia criada em self.servico é igual ao retorno do método __str__ que returona
    # servico
    def test_str(self):
        # se o servico criado pelo mommy for igual ao retorno do método __str__ da classe Servico
        # asserEquals retorna True
        self.assertEquals(str(self.servico), self.servico.servico)


# NOS TESTES DAS CLASSSES ABAIXO SEGUE A MESMA LÓGICA DO TESTE ACIMA
class CargoTestCase(TestCase):

    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):

    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)


class FeaturesTestCase(TestCase):

    def setUp(self):
        self.feature = mommy.make('Feature')

    def test_str(self):
        self.assertEquals(str(self.feature), self.feature.nome)


class PlanosTestCase(TestCase):

    def setUp(self):
        self.plano = mommy.make('Planos')

    def test_str(self):
        self.assertEquals(str(self.plano), self.plano.nome)
