from django.test import TestCase
from model_mommy import mommy
from django.utils import timezone
from datetime import date, datetime
from carteira.models import Carteira
from acao.models import Acao
from carteira_acao.models import Carteira_Acao
from portfolio.models import Portfolio
from usuario.models import Usuario


#--------------------------------------------------------------------------------------------------------------
#MODEL - PORTFOLIO 
class PortfolioTestCase(TestCase):
    def setUp(self):
        self.portfolio = mommy.make('Portfolio')

    def test_str(self):
        self.assertEquals(str(self.portfolio), "({}) {}".format(self.portfolio.id_portfolio, self.portfolio.nome_portfolio))


#--------------------------------------------------------------------------------------------------------------

#MODEL - USUARIO
class UsuarioTestCase(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            username='john_doe',
            email='john.doe@example.com',
            endereco='123 Main St, City',
            data_nascimento=timezone.now().date()
        )

    def test_str(self):
        self.assertEqual(str(self.usuario), self.usuario.email)

#--------------------------------------------------------------------------------------------------------------

#MODEL - CARTEIRA_ACAO
class CarteiraAcaoTestCase(TestCase):
    def setUp(self):
        # Criando uma instância de Acao
        acao = Acao.objects.create(
            nome_acao='Exemplo Ação',
            preco_mais_baixo=50.0,
            preco_mais_alto=100.0,
            simbolo_acao='EXMP',
            nome_empresa='Empresa',
        )

        # Criando uma instância de Usuario
        usuario = Usuario.objects.create_user(
            password='testpassword',
            last_login=timezone.now(),
            is_superuser=True,
            username='testuser',
            first_name='first',
            last_name='last',
            is_staff=True,
            is_active=True,
            date_joined=timezone.now(),
            email='testuser@example.com',
            endereco='Test Street, 123',
            data_nascimento='1990-01-01'
        )

        # Criando uma instância de Portfolio
        portfolio = Portfolio.objects.create(
            nome_portfolio="Meu Portfolio",
            descricao_portfolio="Descricao Meu Portfolio",
            id_usuario=usuario
        )

        # Criando uma instância de Carteira
        carteira = Carteira.objects.create(
            nome_carteira='Minha Carteira',
            valor_total_carteira=1000.0,
            id_portfolio=portfolio
        )

        # Criando uma instância de Carteira_Acao com data_insercao manual
        data_insercao = datetime(2023, 11, 25, 20, 59, 25, 2052, tzinfo=timezone.utc)
        self.carteira_acao = Carteira_Acao.objects.create(
            lote_acao=10,
            data_insercao=data_insercao,
            cotacao=50.0,
            data_compra=date(2023, 1, 1),
            id_acao=acao,
            id_carteira=carteira
        )

    def test_str(self):
        # Verificando se a representação em string está correta
        expected_str = "({}) {}".format(
            self.carteira_acao.id_carteira_acao,
            self.carteira_acao.lote_acao,
            self.carteira_acao.data_insercao,
            self.carteira_acao.cotacao,
            self.carteira_acao.data_compra,
            self.carteira_acao.id_acao,
            self.carteira_acao.id_carteira,
        )
        self.assertEqual(str(self.carteira_acao), expected_str)

#--------------------------------------------------------------------------------------------------------------

#MODEL - CARTEIRA
class CarteiraTestCase(TestCase):
    def setUp(self):
        # Criando uma instância de Carteira usando o mommy
        self.carteira = mommy.make('Carteira')

    def test_str(self):
        # Verificando se a representação em string está correta
        expected_str = "({}) {}".format(
            self.carteira.id_carteira,
            self.carteira.nome_carteira,
            self.carteira.valor_total_carteira,
            self.carteira.descricao_carteira,
            self.carteira.id_portfolio
        )
        self.assertEqual(str(self.carteira), expected_str)

#--------------------------------------------------------------------------------------------------------------

#MODEL - ACAO
class AcaoTestCase(TestCase):
    def setUp(self):
        # Criando uma instância de Acao usando o mommy
        self.acao = mommy.make(Acao)

    def test_str(self):
        # Verificando se a representação em string está correta
        expected_str = "({}) {}".format(
            self.acao.id_acao,
            self.acao.nome_acao,
            self.acao.preco_mais_baixo,
            self.acao.preco_mais_alto,
            self.acao.simbolo_acao,
            self.acao.nome_empresa
        )
        self.assertEqual(str(self.acao), expected_str)