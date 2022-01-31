# Libraries

import keyboard

# Public


class ExitHandler:
    '''
    Gerencia a inativação do funcionamento do programa.
    '''

    #Constructor

    def __init__(self, exit_keyword):
        '''
        → exit_keyword: Tecla que quando pressionada finaliza o funcionamento
            do programa.
        '''

        self._exit_keyword = exit_keyword

    # Implementation

    def check(self):
        '''
        Avalia se deve inativar o programa.
        '''

        return keyboard.is_pressed(self._exit_keyword)
        
