from django.test import TestCase
from django.test import Client #solicitações HTTP
from django.urls import reverse_lazy
from django.urls import reverse
from usuario.models import Usuario
from datetime import date  # Importe o módulo date
from django.contrib.auth import get_user_model
from model_mommy import mommy
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from portfolio.models import Portfolio
from carteira.models import Carteira
from carteira_acao.models import Carteira_Acao

# VIEWS - ERRO
class ErroViewsTestCase(TestCase):
    def test_pagina_erro_500(self):
        url = reverse('pagina_erro_500')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, 'erro_500.html')

#--------------------------------------------------------------------------------------------------------------

class HomeViewTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
            first_name='first',
            last_name='last',
            is_staff=False,
            is_active=True,
            date_joined='2023-01-01',
            endereco='Test Endereco',
            data_nascimento=date(2000, 1, 1)
        )
        self.usuario_logado = mommy.make('usuario.Usuario')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_log_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

        # Adicione mais asserções conforme necessário para verificar o comportamento da view

    def test_charts_view(self):
        response = self.client.get(reverse('charts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grafico_bar.html')

        # Adicione mais asserções conforme necessário para verificar o comportamento da view

#--------------------------------------------------------------------------------------------------------------

# VIEWS - USUARIO

class Meu_PerfilViewTestCase(TestCase):
    def setUp(self):
        # Criando um usuário usando get_user_model
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
            first_name='first',
            last_name='last',
            is_staff=False,
            is_active=True,
            date_joined='2023-01-01',
            endereco='Test Endereco',
            data_nascimento=date(2000, 1, 1)
        )

        # Criando um usuário usando model_mommy
        self.usuario_logado = mommy.make('usuario.Usuario')

    def test_meu_perfil_view(self):
        # Acessando a view sem estar logado
        response = self.client.get(reverse('meu_perfil'))

        # Verificando se o usuário é redirecionado para a página de login
        self.assertRedirects(response, '/usuario/tela_login/?next=/usuario/meu_perfil/')

        # Logando o usuário
        self.client.login(username='testuser', password='testpassword')

        # Acessando a view após estar logado
        response = self.client.get(reverse('meu_perfil'))

        # Verificando se a resposta é um redirecionamento bem-sucedido (código 302)
        self.assertRedirects(response, '/usuario/tela_login/?next=/usuario/meu_perfil/')
