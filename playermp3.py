import pygame
import random
print("Boa noite, temos 2 músicas para você ouvir hoje!")
print("Qual você deseja ouvir hoje?")
#música de sua escolha, abaixo apenas um exemplo
music = str(input("1 - música1 \n2 - música2\n3 - Aleatório ")).strip()
#playlist com apenas 2 músicas, mas deve-se colocar todas que pretender usar.
playlist = [1,2]
if music == ("1"):
    pygame.init()
    pygame.mixer.music.load(r"C:\Users\Pichau\CODANDO\09\música1.mp3")
    pygame.mixer.music.play()
    input("Seu pedido é uma ordem!")
    pygame.event.wait
if music == ("2"):
    pygame.init()
    pygame.mixer.music.load(r"C:\Users\Pichau\CODANDO\09\música2.mp3")
    pygame.mixer.music.play()
    input("Seu pedido é uma ordem!")
    pygame.event.wait
if music == ("3"):
    a = random.choice(playlist)
    b = a
    print(b)
    if b == (1):
            pygame.init()
            pygame.mixer.music.load(r"C:\Users\Pichau\CODANDO\09\música1.mp3")
            pygame.mixer.music.play()
            input("Seu pedido é uma ordem!")
            pygame.event.wait
    if b == (2):
            pygame.init()
            pygame.mixer.music.load(r"C:\Users\Pichau\CODANDO\09\música2.mp3")
            pygame.mixer.music.play()
            input("Seu pedido é uma ordem")
            pygame.event.wait
