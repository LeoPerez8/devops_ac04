class Televisão:
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


    def desligar(self):
        # função que desliga TV
        self.ligada = False


    def aumenta_canal(self):
        # função que aumenta o canal
        if self.ligada:
            self.canal += 1


    def diminui_canal(self):
        ''' 
        função que diminui canal
        '''
        if self.ligada:
            self.canal -= 1


    def pula_canal(self, n_canal):
        # função que pula o canal
        self.canal = n_canal


# tv = Televisão()
# tv.ligada
# stop = True
# while stop:
#     click = input()
#     if click == '' and tv.ligada:
#         tv.ligada = not(tv.ligada)
#         print(" _________")
#         print("|         |")
#         print("| -_-_-_- |")
#         print("| Ligada  |")
#         print("|_________|")
#     elif click == "" and tv.ligada:
#         tv.ligada = not(tv.ligada)
#         print(" _________")
#         print("|         |")
#         print("|         |")
#         print("|Desligada|")
#         print("|_________|")
#     elif click == "  ":
#         parou = False
#     else:
#         stop = True
