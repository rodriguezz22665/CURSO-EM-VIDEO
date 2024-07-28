# Faça um programa que abra e reproduza o áudio de um arquivo mp3.

import pygame

pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

# !!!!!! CONTÉM UM ERRO: pygame.error: No file 'ex21.mp3' found in working directory 'C:\Users\rodri\OneDrive\Documentos\GitHub\CURSO-EM-VIDEO'. !!!!!!!


