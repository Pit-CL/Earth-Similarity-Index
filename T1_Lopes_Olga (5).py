# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:44:13 2020

@author: Olga Margarida
"""

import os  # importar la librario OS

path = os.getcwd()  # obtener el camino de la carpeta donde estamos a trabajar
datos = path + '\p4ds_esi_messy_data.txt'  #archivo datos contiene los datos que vamos a leer
# El archivo debe estar ubicado en la misma carpeta donde se ejecute el codigo

fo = open(datos, 'r')  #abrir el archivo datos que contiene la informacion

# iniciar las listas que van a contener los datos del archivo
c, c1, c2 = [], [], []
n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12 = [],[],[],[],[],[],[],[],[],[],[],[]

# leer el archivo. Una linea por variables.
c = fo.readline()  # c, c1 y c2 - datos del encabezado
c1 = fo.readline()
c2 = fo.readline()
n1 = fo.readline()  # n1 a n12 - datos de los planetas
n2 = fo.readline()
n3 = fo.readline()
n4 = fo.readline()
n5 = fo.readline()
n6 = fo.readline()
n7 = fo.readline()
n8 = fo.readline()
n9 = fo.readline()
n10 = fo.readline()
n11 = fo.readline()
n12 = fo.readline()

fo.close()  # cerrar el archivo datos

# limpiar los dados. Substituir ** y '' y tratar "Moon"

nn1 = n1.replace('**', ',').replace(' ', '')
nn2 = n2.replace('**', ',').replace(' ', '')
nn3 = n3.replace('**', ',').replace(' ', '')
nn4 = n4.replace('0.27      0.6', '0.27,0.6').replace('**',
                                                      ',').replace(' ', '')
nn5 = n5.replace('**', ',').replace(' ', '')
nn6 = n6.replace('**', ',').replace(' ', '')
nn7 = n7.replace('**', ',').replace(' ', '')
nn8 = n8.replace('**', ',').replace(' ', '')
nn9 = n9.replace('**', ',').replace(' ', '')
nn10 = n10.replace('**', ',').replace(' ', '')
nn11 = n11.replace('**', ',').replace(' ', '')
nn12 = n12.replace('**', ',').replace(' ', '')

# dividir los datos en varias strings a traves del separador ','

n_n1 = nn1.split(sep=',')
n_n2 = nn2.split(sep=',')
n_n3 = nn3.split(sep=',')
n_n4 = nn4.split(sep=',')
n_n5 = nn5.split(sep=',')
n_n6 = nn6.split(sep=',')
n_n7 = nn7.split(sep=',')
n_n8 = nn8.split(sep=',')
n_n9 = nn9.split(sep=',')
n_n10 = nn10.split(sep=',')
n_n11 = nn11.split(sep=',')
n_n12 = nn12.split(sep=',')

#Calcular el ESI interno, superficial y global de cada objeto-para todos los planetas

peso = ['0.57', '1.07', '0.7', '5.58']  #definicion del values de peso

# Definicion de la funcion Planeta
# Planeta es una funcion que va a leer los datos asociados a cada uno de los planetas

# inicializacion de las variables global
Radio_P = 0  # radius planeta
Density_P = 0  # densidad planeta
V_Esc_P = 0  # Velocidad escape planeta
Tsurf_P = 0  # temperatura planeta
N_Planeta = [] #inicializar la lista que va a contener los nombre de los planetas


def Planeta(x):
    global Radio_P
    global Density_P
    global V_Esc_P
    global Tsurf_P

    if x == 1:
        Radio_P = n_n1[2]
        Density_P = n_n1[3]
        V_Esc_P = n_n1[5]
        Tsurf_P = n_n1[7]
        N_Planeta.append(n_n1[0])
    if x == 2:
        Radio_P = n_n2[2]
        Density_P = n_n2[3]
        V_Esc_P = n_n2[5]
        Tsurf_P = n_n2[7]
        N_Planeta.append(n_n2[0])
    elif x == 3:
        Radio_P = n_n3[2]
        Density_P = n_n3[3]
        V_Esc_P = n_n3[5]
        Tsurf_P = n_n3[7]
        N_Planeta.append(n_n3[0])
    elif x == 4:
        Radio_P = n_n4[2]
        Density_P = n_n4[3]
        V_Esc_P = n_n4[5]
        Tsurf_P = n_n4[7]
        N_Planeta.append(n_n4[0])
    elif x == 5:
        Radio_P = n_n5[2]
        Density_P = n_n5[3]
        V_Esc_P = n_n5[5]
        Tsurf_P = n_n5[7]
        N_Planeta.append(n_n5[0])
    elif x == 6:
        Radio_P = n_n6[2]
        Density_P = n_n6[3]
        V_Esc_P = n_n6[5]
        Tsurf_P = n_n6[7]
        N_Planeta.append(n_n6[0])
    elif x == 7:
        Radio_P = n_n7[2]
        Density_P = n_n7[3]
        V_Esc_P = n_n7[5]
        Tsurf_P = n_n7[7]
        N_Planeta.append(n_n7[0])
    elif x == 8:
        Radio_P = n_n8[2]
        Density_P = n_n8[3]
        V_Esc_P = n_n8[5]
        Tsurf_P = n_n8[7]
        N_Planeta.append(n_n8[0])
    elif x == 9:
        Radio_P = n_n9[2]
        Density_P = n_n9[3]
        V_Esc_P = n_n9[5]
        Tsurf_P = n_n9[7]
        N_Planeta.append(n_n9[0])
        N_Planeta[8]   = 'GJ 581 g'
    elif x == 10:
        Radio_P = n_n10[2]
        Density_P = n_n10[3]
        V_Esc_P = n_n10[5]
        Tsurf_P = n_n10[7]
        N_Planeta.append(n_n10[0])
        N_Planeta[9] = 'GJ 581 b'
    elif x == 11:
        Radio_P = n_n11[2]
        Density_P = n_n11[3]
        V_Esc_P = n_n11[5]
        Tsurf_P = n_n11[7]
        N_Planeta.append(n_n11[0])
        N_Planeta[10]  = 'HD 96167 b'
    elif x == 12:
        Radio_P = n_n12[2]
        Density_P = n_n12[3]
        V_Esc_P = n_n12[5]
        Tsurf_P = n_n12[7]
        N_Planeta.append(n_n12[0])
        N_Planeta[11] = 'WASP-26 b'
    else:
        pass
    return (Radio_P, Density_P, V_Esc_P, Tsurf_P, N_Planeta
            )  # esta funcion retorna los parametros asociados al planeta

#inicializar listas q van a contener los calculos de los ESI(ESI_int,ESI_sup,ESI_glb)
ESI_int, ESI_sup, ESI_glb = [], [], []  

#calculo de los ESI interno, ESI superficial, ESI global de todos los planetas
for i in range(1, 13):  
    Radio_T = n_n1[2]
    Density_T = n_n1[3]
    V_Esc_T = n_n1[5]
    Tsurf_T = n_n1[7]
    Planeta(i)

    # calculo ESIint
    A1 = (float(Radio_P) - float(Radio_T)) / (float(Radio_P) + float(Radio_T))
    A2 = 1 - abs(A1)
    A3 = float(peso[0]) / 2
    A4 = A2**A3

    A01 = (float(Density_P) - float(Density_T)) / (float(Density_P) +
                                                   float(Density_T))
    A02 = 1 - abs(A01)
    A03 = float(peso[1]) / 2
    A04 = A02**A03

    Calculo_ESI_int = A4 * A04

    # calculo ESIsuperficial
    AA1 = (float(V_Esc_P) - float(V_Esc_T)) / (float(V_Esc_P) + float(V_Esc_T))
    AA2 = 1 - abs(AA1)
    AA3 = float(peso[2]) / 2
    AA4 = AA2**AA3

    AA01 = (float(Tsurf_P) - float(Tsurf_T)) / (float(Tsurf_P) +
                                                float(Tsurf_T))
    AA02 = 1 - abs(AA01)
    AA03 = float(peso[3]) / 2
    AA04 = AA02**AA03

    Calculo_ESI_sup = AA4 * AA04

    # calculo ESIglobal
    A3 = float(peso[0]) / 4
    A4 = A2**A3

    A03 = float(peso[1]) / 4
    A04 = A02**A03

    A003 = float(peso[2]) / 4
    A004 = AA2**A003

    A0003 = float(peso[3]) / 4
    A0004 = AA02**A0003

    Calculo_ESI_glb = A4 * A04 * A004 * A0004
    
    # addicionar los calculos de ESIs de todos los planetas en la lista ESIs
    ESI_int.append(float(Calculo_ESI_int)) 
    ESI_sup.append(float(Calculo_ESI_sup))  
    ESI_glb.append(float(Calculo_ESI_glb))

# Definicion de la funcion que va a determinar si cada objeto de la lista 
# es similar a la Tierra (SI o NO)


def Teste(x, resultado='SI'):
    '''La funcion "Teste" verifica se el planeta x es similar a la Tierra (SI/NO). 
    
    Parametro
             argument 1(float) : valor del ESI global del planeta a comparar
             argument 2(String): es opcional. Por defect es "SI". 
             
    Retorna
             retorna el resultado del teste de similitude.  
             Devuelve "SI" se ESI Global del planeta >= 0.8 y "NO" lo contrario
    '''

    if x < 0.8:
        resultado = 'NO'
    return (resultado)


#print(Teste.__doc__)

Resultado_Teste = []  # inicializar la lista que va a contener los resultados 
                      # de lo teste/prueba de similitud

for i in range(0, 12):
    ESI_glb_Planeta_i = ESI_glb[
        i]  # atribuir a la variable ESI_glb_Planeta_i el valor de ESI global
    # del planeta i
    Teste(ESI_glb_Planeta_i)  # Envocar la funcion "Teste"
    Resultado_Teste.append(
        Teste(ESI_glb_Planeta_i
              ))  # anadir el resultado de lo teste a lista Resultado_Teste

# Criar la carpera "TAREA1_2020" en la misma carpeta donde se ejecute el codigo

path_carpeta = path + '\\TAREA1_2020'  # crear una carpeta/pasta nueva
if not os.path.exists(path_carpeta): #verificar se la carpeta "TAREA1_2020" existe. 
    os.makedirs(path_carpeta)        #Si no existe se va a crearla

# generar un archivo con el formato "P4DS_T1_YYMMDD_Apellido_Nombre.txt"

from datetime import date  # llamar la funcion

data_atual = date.today()
DD = data_atual.strftime(
    '%d')  # obtener la informacion asociada con el dia de hoy  DD
MM = data_atual.strftime(
    '%m')  # obtener la informacion asociada con el mes de hoy  MM
YY = data_atual.strftime(
    '%y')  # obtener la informacion asociada con el año de hoy  YY
DATA = YY + MM + DD  # DATA va a contener la informacion  "YYMMDD"

Nombre = 'Olga'
Apellido = 'Lopes'

# n_archivo va a contener el nombre del archivo.
#La informacion asociada a "YYMMDD" va a cambiar de acuerdo 
#com la fecha de ejecucion del codigo

n_archivo = path_carpeta+'\P4DS_T1_'+DATA +'_'+Apellido+'_'+ Nombre+'.txt'

# escribir el cuadro con los calculos en el archivo

with open(n_archivo, 'w') as Arc:
    Arc.write('{:<16}{:^16}{:^16}{:^16}{:^16}'.\
              format('Nombre','ESI_int','ESI_sup','ESI_glb','Similar'))
    Arc.write('\n')
    Arc.write('-' * 76)
    for i in range(0, 12):
        Arc.write(('\n {:<16}{:^16.3f}{:^16.3f}{:^16.3f}{:^14}'.\
                   format(N_Planeta[i],ESI_int[i],ESI_sup[i],ESI_glb[i],\
                          Resultado_Teste[i])))