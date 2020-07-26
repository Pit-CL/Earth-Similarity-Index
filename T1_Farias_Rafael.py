# -*- coding: utf-8 -*-.
"""
Tarea 1 P4DS.

Alumno: Rafael Farías Poblete.
"""
import os
from datetime import date

path = os.getcwd()
data = path + '\\p4ds_esi_messy_data.txt'

df = open(data, 'r')
# Abre el archivo a trabajar en modo lectura.
name, medida, linea = [], [], []
wasp26, hd96167, gj581b, gk581g, titan, jupyter, io, venus,\
    moon, mercury, mars, earth = [
    ], [], [], [], [], [], [], [], [], [], [], []
# Creo las listas que van a contener los datos.
name = df.readline()
medida = df.readline()
linea = df.readline()
earth = df.readline()
mars = df.readline()
mercury = df.readline()
moon = df.readline()
venus = df.readline()
io = df.readline()
jupyter = df.readline()
titan = df.readline()
gj581g = df.readline()
gj581b = df.readline()
hd96167 = df.readline()
wasp26 = df.readline()
# Una línea por variable.
df.close()

clean_earth = earth.replace('**', ',').replace(' ', '')
clean_mars = mars.replace('**', ',').replace(' ', '')
clean_mercury = mercury.replace('**', ',').replace(' ', '')
clean_moon = moon.replace('0.27      0.6',
                          '0.27,0.6').replace('**', ',').replace(' ', '')
clean_venus = venus.replace('**', ',').replace(' ', '')
clean_io = io.replace('**', ',').replace(' ', '')
clean_jupyter = jupyter.replace('**', ',').replace(' ', '')
clean_titan = titan.replace('**', ',').replace(' ', '')
clean_gj581g = gj581g.replace('**', ',').replace(' ', '').replace('GJ581g',
                                                                  'GJ 581 g')
clean_gj581b = gj581b.replace('**', ',').replace(' ', '').replace('GJ581b',
                                                                  'GJ 581 b')
clean_hd96167 = hd96167.replace('**', ',').replace(' ',
                                                   '').replace('HD96167b',
                                                               'HD 96167 b')
clean_wasp26 = wasp26.replace('**', ',').replace(' ', '').replace('WASP-26b',
                                                                  'WASP-26 b')
# Listas a las cuales hay que aplicarles split con separador de ',' obteniendo
# de esta manera las listas finales a trabajar f_nombreDelAstro.

f_earth = clean_earth.split(sep=',')
f_mars = clean_mars.split(sep=',')
f_mercury = clean_mercury.split(sep=',')
f_moon = clean_moon.split(sep=',')
f_venus = clean_venus.split(sep=',')
f_io = clean_io.split(sep=',')
f_jupyter = clean_jupyter.split(sep=',')
f_titan = clean_titan.split(sep=',')
f_gj581g = clean_gj581g.split(sep=',')
f_gj581b = clean_gj581b.split(sep=',')
f_hd96167 = clean_hd96167.split(sep=',')
f_wasp26 = clean_wasp26.split(sep=',')
# Listas finales para poder trabajar.

end = [
    f_earth, f_mars, f_mercury, f_moon, f_venus, f_io, f_jupyter, f_titan,
    f_gj581g, f_gj581b, f_hd96167, f_wasp26
]
# Lista general para poder aumentar el contador en +1 y recorrer
# todas las listas.


def esi_s(planeta, velocidad_peso=0.70, temperatura_peso=5.58):
    """Esta función permite calcular el Esi  Superficial de los planetas.

    Args:
        planeta ([str]): [se debe ingresar el nombre del planeta].
        velocidad_peso ([float]): [valor por defecto 0.7].
        temperatura_peso ([float]): [valor por defecto 5.58].

    Returns
    -------
        [float]: [Resultado del cálculo del Esi Superior].
    """
    global i
    if planeta == 'Earth':
        i = 0
    elif planeta == 'Mars':
        i = 1
    elif planeta == 'Mercury':
        i = 2
    elif planeta == 'Moon':
        i = 3
    elif planeta == 'Venus':
        i = 4
    elif planeta == 'Io':
        i = 5
    elif planeta == 'Jupiter':
        i = 6
    elif planeta == 'Titan':
        i = 7
    elif planeta == 'GJ 581 g':
        i = 8
    elif planeta == 'GJ 581 b':
        i = 9
    elif planeta == 'HD 96167 b':
        i = 10
    elif planeta == 'WASP-26 b':
        i = 11
    else:
        print('Planeta no se encuentra en el archivo')

    esi_sup = ((1 - (abs(
        (float(end[0 + i][5]) - float(end[0][5])) /
        (float(end[0 + i][5]) + float(end[0][5])))))**(velocidad_peso / 2)) * (
            (1 - (abs((float(end[0 + i][7]) - float(end[0][7])) /
                      (float(end[0 + i][7]) + float(end[0][7])))))
            ** (temperatura_peso / 2))
    return esi_sup


def esi_i(planeta, radio_peso=0.57, densidad_peso=1.07):
    """Esta función permite calcular el Esi  Interno de los planetas.

    Args:
        planeta ([str]): [se debe ingresar el nombre del planeta].
        radio_peso ([float]): [valor por defecto 0.57].
        densidad_peso ([float]): [valor por defecto 1.07].

    Returns
    -------
        [float]: [Resultado del cálculo del Esi Interno].
    """
    global i
    if planeta == 'Earth':
        i = 0
    elif planeta == 'Mars':
        i = 1
    elif planeta == 'Mercury':
        i = 2
    elif planeta == 'Moon':
        i = 3
    elif planeta == 'Venus':
        i = 4
    elif planeta == 'Io':
        i = 5
    elif planeta == 'Jupiter':
        i = 6
    elif planeta == 'Titan':
        i = 7
    elif planeta == 'GJ 581 g':
        i = 8
    elif planeta == 'GJ 581 b':
        i = 9
    elif planeta == 'HD 96167 b':
        i = 10
    elif planeta == 'WASP-26 b':
        i = 11
    else:
        print('Planeta no se encuentra en el archivo')

    esi_int = ((1 - (abs(
        (float(end[0 + i][2]) - float(end[0][2])) /
        (float(end[0 + i][2]) + float(end[0][2])))))**(radio_peso / 2)) * (
            (1 - (abs((float(end[0 + i][3]) - float(end[0][3])) /
                      (float(end[0 + i][3]) + float(end[0][3])))))
            ** (densidad_peso / 2))
    return esi_int


def esi_g(planeta):
    """Esta función permite calcular el Esi  global de los planetas.

    Args:
        planeta ([str]): [se debe ingresar el nombre del planeta].

    Returns
    -------
        [float]: [Resultado del cálculo del Esi global].
    """
    global i
    velocidad_peso = 0.70
    temperatura_peso = 5.58
    radio_peso = 0.57
    densidad_peso = 1.07

    if planeta == 'Earth':
        i = 0
    elif planeta == 'Mars':
        i = 1
    elif planeta == 'Mercury':
        i = 2
    elif planeta == 'Moon':
        i = 3
    elif planeta == 'Venus':
        i = 4
    elif planeta == 'Io':
        i = 5
    elif planeta == 'Jupiter':
        i = 6
    elif planeta == 'Titan':
        i = 7
    elif planeta == 'GJ 581 g':
        i = 8
    elif planeta == 'GJ 581 b':
        i = 9
    elif planeta == 'HD 96167 b':
        i = 10
    elif planeta == 'WASP-26 b':
        i = 11
    else:
        print('Planeta no se encuentra en el archivo')

    esi_glob = ((
        ((1 - (abs(
            (float(end[0 + i][2]) - float(end[0][2])) /
            (float(end[0 + i][2]) + float(end[0][2])))))**(radio_peso / 2)) *
        ((1 - (abs(
            (float(end[0 + i][3]) - float(end[0][3])) /
            (float(end[0 + i][3]) + float(end[0][3])))))**(densidad_peso / 2))
    )**(1 / 2)) * ((((1 - (abs(
        (float(end[0 + i][5]) - float(end[0][5])) /
        (float(end[0 + i][5]) + float(end[0][5])))))**(velocidad_peso / 2)) *
        ((1 - (abs((float(end[0 + i][7]) - float(end[0][7])) /
                   (float(end[0 + i][7]) + float(end[0][7]))))) **
         (temperatura_peso / 2)))**(1 / 2))
    return esi_glob


def testsino(x):
    """Función que permite realizar el test lógico SI, NO.

    Args:
        x ([funcion]): [Se debe ingresar la función que calcula el Esi.
        General de los planetas, por ejemplo: testsino(esi_g('Mars'))].

    Returns
    -------
        [str]: [Resultado del test puede ser SI o NO].
    """
    if x > 0.8:
        resultado = 'SI'
    else:
        resultado = 'NO'
    return (resultado)


path_tarea = path + '\\TAREA1_2020'
if not os.path.exists(path_tarea):
    os.makedirs(path_tarea)
# Nos permite conocer si el directorio existe y en caso de no existir crearlo.

fecha_hoy = date.today()
DD = fecha_hoy.strftime('%d')
MM = fecha_hoy.strftime('%m')
YY = fecha_hoy.strftime('%y')
fecha = YY + MM + DD

Nombre, Apellido = 'Rafael', 'Farias'

archivo_final = path_tarea + '\\P4DS_T1_' + \
    fecha + '_' + Apellido + '_' + Nombre + '.txt'
# Formato solicitado de guardado del archivo.

np = [f_earth[0], f_mars[0], f_mercury[0], f_moon[0], f_venus[0], f_io[0],
      f_jupyter[0], f_titan[0], f_gj581g[0], f_gj581b[0], f_hd96167[0],
      f_wasp26[0]]
# Lista que guarda el nombre de los planetas

f = open(archivo_final, 'w')
f.write('{:<19} {:^} {:>13} {:^} {:>13} {:^} {:>11} {}'.format(
    'Nombre', 'ESI_int', ' ', 'Esi_sup', ' ', 'Esi_glb', ' ', 'Similar\n'))
f.write('-'*91, )
f.write('\n')
for i in range(0, 12):
    f.write('{:<20} {:^.3f} {:>15} {:^.3f} {:>15} {:^.3f} {:>15} {}\n'.format(
        np[i], (esi_i(np[i])), ' ', (esi_s(np[i])), ' ', (esi_g(np[i])), ' ',
        testsino(esi_g(np[i]))))
f.close()
# Escritura y cierre del archivo.
