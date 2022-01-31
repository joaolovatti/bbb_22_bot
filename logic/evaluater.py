# Public

class Evaluater():

    @staticmethod
    def condition(condition, false_value, true_value):
        '''
        Avalia uma "condition".

        Caso true, retorna o "true_value".

        Caso false, retorna o "false_value".
        '''

        if condition:

            return true_value

        else:

            return false_value