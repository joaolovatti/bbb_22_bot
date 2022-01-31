# Libraries

from logic.click_point import ClickPoint

import pyautogui as pyauto

import time

from logic.exit_handler import ExitHandler

# Public

class BotManager:
    '''
    Controla a interação do BOT.
    '''

    def __init__(self):

        self._computed_votes = 0

    # Interface

    def executar_voto(self):
        '''
        Executa a seguinte sequência de etapas:

        1. Encontra a localização do botão do participante. E clica nele.

        2. Encontra a localização do botão do Catcha. E clica nele.

        3. Encontra a localização do botão de "Votar novamente". E clica nele.

        No caso de erro, a página sofre um refresh.
        '''

        try:

            self._click_on_participant()

            time.sleep(1)

            self._click_on_catcha()

            time.sleep(1)

            self._click_on_votar_novamente()

            time.sleep(1)

            self._increment_computed_votes()

            print(f'Votos computados = {self._computed_votes}.')

        except Exception as e:

            self.refresh_page()

            time.sleep(4)

    def refresh_page(self):
        '''
        Executa um refresh na página do browser.
        '''

        pyauto.press('f5')

    def start_cycle(self, quit_keyword):
        '''
        Inicia o ciclo de funcionamento do bot.

        Sendo finalizado a partir do pressionar a "quit_keyword".
        '''

        _exit_handler = ExitHandler(exit_keyword = quit_keyword)

        while True:
    
            self.executar_voto()

            if _exit_handler.check():
        
                break

    # Implementation

    def _increment_computed_votes(self):

        self._computed_votes += 1

    def _click_on_participant(self):

        _participante = ClickPoint(path='assets/participante.png', h_offset=100)

        _participante.instant_click(1, duration=3,
                            noise_amplitude=30, is_random=True, duration_offset=0.5)

    def _click_on_catcha(self):

        _catpha = ClickPoint(path='assets/catcha.png', h_offset=50)

        _catpha.instant_click(1, duration=3,
                      noise_amplitude=10, is_random=True, duration_offset=0.5)

    def _click_on_votar_novamente(self):

        _votar_novamente_button = ClickPoint(
            path='assets/votar_novamete.png')

        _votar_novamente_button.instant_click(
            1, duration=3, is_random=True, noise_amplitude=20, duration_offset=0.5)
