import pandas as pd
from sklearn import preprocessing


def esi_interno(planeta):

    radio_peso = 0.57
    densidad_peso = 1.07
    if planeta == Earth:
        i = 0
    elif planeta == Mars:
        i = 1
    elif planeta == Mercury:
        i = 2
    elif planeta == Moon:
        i = 3
    elif planeta == Venus:
        i = 4
    elif planeta == Io:
        i = 5
    elif planeta == Jupyter:
        i = 6
    elif planeta == Titan:
        i = 7
    elif planeta == GJ581g:
        i = 8
    elif planeta == GJ581b:
        i = 9
    elif planeta == HD96167b:
        i = 10
    elif planeta == WASP26b:
        i = 11
