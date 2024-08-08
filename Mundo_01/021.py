"""
021
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

import pygame

pygame.init() # inicia o módulo
pygame.mixer.music.load('021_song.mp3') # carrega o arquivo
pygame.mixer.music.play() # reproduz a música
input()
pygame.event.wait() # espera por um evento para manter o programa em execução enquanto a música toca