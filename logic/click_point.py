# Libraries

import pyautogui as pyauto

import random

from logic.evaluater import Evaluater

# Public


class ClickPoint:
    '''
    Representa um ponto na tela que será foco de alguma ação do BOT.
    '''

    # Constructor

    def __init__(self, path='', coordenate=(0, 0), h_offset=0, v_offset=0):
        '''
        → path: Path da imagem do elemento que deseja identificar na imagem.
                Esse valor possui preferência na construção do ClickPoint.

        → coordenate: Coordenadas na tela.
        '''

        if (path != ''):

            coordenate = pyauto.locateCenterOnScreen(
                path,
                confidence=0.8
            )

            self._coordenate = [
                coordenate[0] - h_offset,
                coordenate[1] - v_offset
            ]

        elif (coordenate != (0, 0)):

            self._coordenate = coordenate

    # Interface

    def instant_click(self, n, duration=1, noise_amplitude=0, is_random=False, duration_offset=0):
        '''
        Define a quanidade de cliques no point.

        Argumentos:

        → n: Número de cliques.

        → duration: Delay da ação em segundos.

        → noise_amplitude: Valor máximo do ruído sobre a posição e duration da ação sobre point.

        → is_random: Ativa a presença de ruído.

        → duration_offset: Valor de offset para o delay da ação em segundos.
        '''

        pyauto.click(clicks=n,
                     interval= Evaluater.condition(
                         is_random, duration + duration_offset, random.random() * duration + duration_offset),
                     x=self._coordenate[0] + Evaluater.condition(
                         is_random, noise_amplitude, random.random() * noise_amplitude),
                     y=self._coordenate[1] + Evaluater.condition(
                         is_random, noise_amplitude, random.random() * noise_amplitude)
                     )
