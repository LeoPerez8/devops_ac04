from unittest import TestCase
from com.Perez.Televisao import Televisao


class TestTelevisao(TestCase):
    def setUp(self):
        self.televisao = Televisao("Samsung")

    def teste_cria_desligada(self):
        self.assertEqual(self.televisao.ligada, False)

    def teste_ligar(self):
        self.televisao.ligar()
        self.assertEqual(self.televisao.ligada, True)
