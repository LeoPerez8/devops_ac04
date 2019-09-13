from aula06 import Televisão


def teste_cria_desligada():
    tv = Televisão("Samsung")
    assert not tv.ligada
    assert tv.canal is None


def teste_ligar():
    tv = Televisão("Samsung")
    tv.ligar()
    assert tv.ligada
    assert tv.canal is not None


def test_aumenta_canal_ligada():
    tv = Televisão("Samsung")
    tv.ligar()
    tv.aumenta_canal()
    assert tv.canal == 6


def test_diminui_canal_ligada():
    tv = Televisão("Samsung")
    tv.ligar()
    tv.diminui_canal()
    assert tv.canal == 4


def test_aumenta_canal_desligada():
    tv = Televisão("Samsung")
    tv.desligar()
    tv.aumenta_canal()
    assert tv.canal is None


def test_diminui_canal_desligada():
    tv = Televisão("Samsung")
    tv.desligar()
    tv.diminui_canal()
    assert tv.canal is None


def test_pula_canal():
    tv = Televisão("Samsung")
    tv.ligar()
    tv.pula_canal(10)
    assert tv.canal == 10


def test_desliga_tv():
    tv = Televisão("Samsung")
    tv.ligar()
    tv.desligar()
    assert not tv.ligada
