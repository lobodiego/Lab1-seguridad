import operator
import unicodedata
import sys



def preprocesamiento (archivo):
	f=open(archivo,'r',encoding='utf8')
	HERALDOSNEGROS = f.read()
#PREGUNTAS 1
	cambio_letra = HERALDOSNEGROS.maketrans("jhñkHYuwy", "iinlIZvvz")
	HERALDOSNEGROS_pre = HERALDOSNEGROS.translate(cambio_letra)
	print('\n***PREGUNTA N1***')
	print('Sustituciones: \n''\n'+ HERALDOSNEGROS_pre +'\n')
#PREGUNTAS 2
	sin_tilde = HERALDOSNEGROS_pre.maketrans("áéíóúüñÁÉÍÓÚÜ", "aeiouunAEIOUU")
	HERALDOSNEGROS_pre = HERALDOSNEGROS_pre.translate(sin_tilde)
	print('\n***PREGUNTA N2***')
	print('Eliminacion de tildes: \n''\n'+HERALDOSNEGROS_pre+'\n')
#PREGUNTAS 3
	HERALDOSNEGROS_pre = HERALDOSNEGROS_pre.upper()
	print('\n***PREGUNTA N3***')
	print('Texto a mayusculas: \n''\n'+HERALDOSNEGROS_pre+'\n')
#PREGUNTAS 4
	eliminar = HERALDOSNEGROS_pre.maketrans( '','' ," .¡!,;:\n")
	HERALDOSNEGROS_pre = HERALDOSNEGROS_pre.translate(eliminar)
	
	print('\n***PREGUNTA N4***')
	print('Sin signos de puntuacion: \n''\n'+HERALDOSNEGROS_pre+'\n')
	
	file=open('HERALDOSNEGROS_pre.txt','w')
	file.write(HERALDOSNEGROS_pre)

#PREGUNTA 5 - FRECUENCIAS
def frecuencias(archivo):
	f=open(archivo,'r')
	HERALDOSNEGROS_pre = f.read()
	total_frec ={}
	for i in HERALDOSNEGROS_pre:
		if i in total_frec:
			total_frec[i] +=1
		else:
			total_frec[i]=1
	total_frec = sorted(total_frec.items(), key=operator.itemgetter(1))
	frec_top=total_frec[-5:]
	frec_top.reverse()
	print('\n***PREGUNTA N5***')
	print('Frecuencias totales: \n')
	print(total_frec)
	print(' \n5 Mayores Frecuencias:')
	print(frec_top)

#PREGUNTA 6 - KASISKI
def kasiski(archivo):
	f=open(archivo, 'r',encoding='utf8')
	HERALDOSNEGROS=f.read()

	trigrams ={}
	for index, character in enumerate(HERALDOSNEGROS[0:len(HERALDOSNEGROS)-4]):
		temp = HERALDOSNEGROS[index: index+3]
		cont=0
		if temp not in trigrams:
			trigrams[temp]=[index]
			for i in range(index+1, len(HERALDOSNEGROS)-3):
				if temp==HERALDOSNEGROS[i:i+3]:
					trigrams[temp].append(cont+index+1)
				cont=cont+1
	trigrams={k:v for k, v in trigrams.items() if len(v)>1}
	print('\n''\n***PREGUNTA N6***')
	print('Kasiski: \n')
	print(trigrams)	

#PREGUNTA 7 - UNICODE8
def to_unicode(archivo):
        print('\n''\n***PREGUNTA N7***')
        print('Unicode: \n')
        with open(archivo, encoding='utf-8') as f:
                for line in f:
                        print(repr(line))

#PREGUNTA 9 - INSERCION DE CADENA
def insert_cadena(archivo):
	f=open(archivo,'r')
	HERALDOSNEGROS=f.read()
	HERALDOSNEGROS_nuevo=''
	for index, item in enumerate(HERALDOSNEGROS):
		if index %20 ==0 and index != 0:
			HERALDOSNEGROS_nuevo= HERALDOSNEGROS_nuevo+'AQUI'
		HERALDOSNEGROS_nuevo=HERALDOSNEGROS_nuevo+item
	if(len(HERALDOSNEGROS_nuevo)%4)>0:
		HERALDOSNEGROS_nuevo=HERALDOSNEGROS_nuevo+('X'*(4-(len(HERALDOSNEGROS_nuevo)%4)))
	print('\n''\n***PREGUNTA N9***')
	print('Insertando Cadena X: \n')
	print(HERALDOSNEGROS_nuevo)


#main (1-4)
preprocesamiento('HERALDOSNEGROS.txt')
#main(5)
frecuencias('HERALDOSNEGROS_pre.txt')
#main(6)
kasiski('HERALDOSNEGROS_pre.txt')
#main(7)
to_unicode('HERALDOSNEGROS.txt')
#main(9)
insert_cadena('HERALDOSNEGROS_pre.txt')


