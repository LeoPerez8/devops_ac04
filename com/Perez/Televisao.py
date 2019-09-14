class Televisao:
    '''
    Classe Televisão implementa a abstração de uma televisão recebe como
    argumento de criação a marca da televisão.
    '''
    def __init__(self, marca):
        self.marca = marca
        self.ligada = False
        self.canal = None

    def ligar(self):
        # função que liga TV
        self.ligada = True
        self.canal = 5
        return self.ligada
