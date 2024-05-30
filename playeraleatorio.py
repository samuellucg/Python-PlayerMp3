import pygame
import random
print("Boa noite, temos 2 músicas para você ouvir hoje!")
print("Qual você deseja ouvir hoje?")
music = str(input("1 - Heart_Freestyle \n2 - Pink and White\n3 - Aleatório ")).strip()
playlist = [1,2]
if music == ("1"):
    pygame.init()
    pygame.mixer.music.load(r"C:\Users\Pichau\CODANDO\09\Heart_Freestyle_.mp3")
    pygame.mixer.music.play()
    input("Seu pedido é uma ordem!")
    pygame.event.wait
if music == ("2"):
    pygame.init()
    pygame.mixer.music.load(r"C:\Users\Pichau\CODANDO\09\musicaboa.mp3")
    pygame.mixer.music.play()
    input("Seu pedido é uma ordem!")
    pygame.event.wait
if music == ("3"):
    a = random.choice(playlist)
    b = a
    print(b)
    if b == (1):
            pygame.init()
            pygame.mixer.music.load(r"C:\Users\Pichau\CODANDO\09\Heart_Freestyle_.mp3")
            pygame.mixer.music.play()
            input("Seu pedido é uma ordem!")
            pygame.event.wait
    if b == (2):
            pygame.init()
            pygame.mixer.music.load(r"C:\Users\Pichau\CODANDO\09\musicaboa.mp3")
            pygame.mixer.music.play()
            input("Seu pedido é uma ordem")
            pygame.event.wait