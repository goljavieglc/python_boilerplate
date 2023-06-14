'''
    Modulo de decoradores
'''

import functools
from typing import Dict
from numpy.random import random, choice

def anadir_ruido(noise_probability : float, noise_distribution : Dict[str, float]):
    '''
        Funcion que añade ruido

        :param noise_probability: La probabilidad de que se aplique ruido
        :type noise_probability: float

        :param noise_distribution: La distribucion del ruido
        :type noise_distribution: Dict[str, float]

        :returns: Returns a decorator function
        :rtype: Func(func)
    '''
    def inner_decorator(func):
        possible_noise_values = list(noise_distribution.keys())
        noise_value_probabilities = list(noise_distribution.values())
        @functools.wraps(func)
        def wrapper(*args):
            true_value = func(*args)
            if random() <= noise_probability: #ie con prob `noise_probability`
                vals, probs = exclude_true_value(
                    possible_noise_values,
                    noise_value_probabilities,
                    true_value
                )
                return choice(vals, p=probs)

            return true_value
        return wrapper
    return inner_decorator


def exclude_true_value(possible_noise_values, noise_value_probabilities, true_value):
    '''
        Funcion que excluye el valor true

        :param possible_noise_values: La probabilidad de que se aplique ruido
        :type noise_probability: float

        :param noise_distribution: La distribucion del ruido
        :type noise_distribution: Dict[str, float]

        :returns: Returns a decorator function
        :rtype: Func(func)
    '''
    try:
        i = possible_noise_values.index(true_value)
        possible_noise_values = possible_noise_values[:i] + possible_noise_values[i+1:]
        noise_value_probabilities = noise_value_probabilities[:i] + noise_value_probabilities[i+1:]
        noise_val_prob_sum = sum(noise_value_probabilities)
        noise_value_probabilities = [x/noise_val_prob_sum for x in noise_value_probabilities]
    except ValueError:
        pass
    return possible_noise_values, noise_value_probabilities

if __name__ == "__main__":
    @anadir_ruido(0.5, {'ups!':0.7, 'UPS!':0.3})
    def funcion_de_ejemplo(numero_a_multiplicar):
        '''
            multiplica el número * 2
        '''
        return 2*numero_a_multiplicar
    for x in range(10):
        print(funcion_de_ejemplo(x))
    