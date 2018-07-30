#!/usr/bin/env python

import sys, io
import math
import string
from operator import itemgetter, attrgetter
import collections


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z



#CRIA A LISTA DE OPERACOES QUE VEM DO STDIN	
def cria_operacoes(lista_op):
	for line in sys.stdin: #Ler as entradas do arquivo do stdin, separa cada caracter por espaco.
		linha = line.split() #split dos elementos do arquivo transformando em sub listas
		lista_op.append(linha)

#NODO ESTRUTURA DO NODO
class nodo(object):
	def __init__(self,ident,ativo,sus,tabela):
		self.ident = ident
		self.ativo = ativo
		self.sus = sus
		self.tabela = dict()
	def __repr__(self):
	 	return repr((self.ident, self.ativo, self.sus, self.tabela))




def number_of_bits(n):
    return int(math.log(n, 2)) + 1

#CRIAR A TABELA DE ROTAS PARA CADA NODO ATIVO

def criarotas(lista,tam_dht,objeto):
	dht = int(math.floor(math.log(tam_dht,2)))
	j = objeto.ident
	valid = int(j) 
	for i in range(0,dht):
		idcalc = valid + int(math.pow(2,i))
		acheio_obj = acha_objeto(lista,idcalc)
		valtabela = procura_sucessor(lista,acheio_obj)
		#print valtabela
		objeto.tabela[int(idcalc)] = int(valtabela)


def atualizarota_ativos(lista,tam_dht):
	for x in lista:
		if x.ativo == 1:
			criarotas(lista,tam_dht,x)
		
			

def atualiza_tabela(lista):
	for x in lista:
		if x.ativo == 1:
			ks = list(x.tabela.keys())
			for n in ks:
				a = acha_objeto(lista,n)
				atualiza = procura_sucessor(lista,a)
				x.tabela[n] = atualiza


#PROCURA UM OBJETO
def acha_objeto(lista,i):
	for n in range(0,len(lista)):
		if lista[n].ident == i:
			x = lista[n]
			return x




#EXCLUE UM OBJETO DA LISTA DE NODOS ATIVOS SETANDO ATIVO PARA 0
def exclue_objeto(lista,i):
	for n in range(0,len(lista)):
		if lista[n].ident == i:
			lista[n].ativo = 0

	
#PROCURA O MAIOR NODO PARA CRIAR A LISTA BASEADA NO TAMANHO
def maior_nodo(lista):
	numeros = []
	for val in range(0,len(lista)):
		n = int(lista[val][2])
		numeros.append(n)
	return max(numeros)


lista = []
lista_nodos = []
cria_operacoes(lista)


maiorid = maior_nodo(lista) * 2
bits = number_of_bits(maiorid)

#POPULA A LISTA COM OBJETOS FICTICIOS
for n in range(0,maiorid):
	x = nodo(int(n),0,0,dict())
	lista_nodos.append(x)



def imprime_ativos(lista):
	for n in range(0,len(lista)):
		if int(lista[n].ativo) == 1:
			print n,lista[n]



# ACHA SUCESSOR
def procura_sucessor(lista,x):
	achei = 0
	b = nodo(1,1,0,{})
	i = int(x.ident)
	for n in range(i+1,len(lista)):
		if lista[n].ativo == 1:
			achei = 1
			return int(lista[n].ident)
	if achei == 0:
		return int(b.ident)

# ATRIBUI SUCESSOR NA ESTRUTURA DO NODO
def procura_sucess(lista,x):
	achei = 0
	a = nodo(1,1,0,{})
	i = int(x.ident)
	for n in range(i+1,len(lista)):
		if lista[n].ativo == 1:
			lista[i].sus = int(lista[n].ident)
			achei = 1
			return int(lista[n].ident)
	if achei == 0:
		return  int(a.ident)


def atualiza_suss(lista):
	for n in lista:
		if n.ativo == 1:
			procura_sucess(lista,n)



def lookup(lista,x,val,ope):
	achei = 0
	while achei != 1:
		objetinho = acha_objeto(lista,x)
		ks = list(objetinho.tabela.keys())
		listarota = ks
		print ope, "L" ,val	
		for n in listarota:
			if n == val:
		 	  achei = 1
		 	  print ope, "L" ,val, "{",objetinho.tabela[val],"}" 
		if achei == 0:
			maximo = max(listarota)
			x = objetinho.tabela[maximo]
			print ope,"T",x, objetinho.tabela





conta_operacoes = 1
tamanho_dht = 0
tam_lista = len(lista)

conta_entradas = 0
for n1 in range(0,tam_lista):
	tam_sublista = len(lista[n1])
	if 'E' in lista[n1]:
		if conta_entradas == 0: # Verifica se e o primeiro nodo a entrar se sim nao vai procurar sucessor nem criar tabela
			x = nodo(int(lista[n1][2]),1,0,{})
			lista_nodos[int(lista[n1][2])] = x
			tamanho_dht = tamanho_dht + 1
			conta_operacoes = conta_operacoes + 1
			conta_entradas = conta_entradas + 1
		else:# como e o segundo e terceiro e quarto.... entao ele vai procurar o sucessor do anterior x = ao nodo anterior novo nodo = y
			y = nodo(int(lista[n1][2]),1,0,{})
			lista_nodos[int(lista[n1][2])] = y
			atualiza_suss(lista_nodos)
			tamanho_dht = tamanho_dht + 1
			criarotas(lista_nodos,tamanho_dht,y)
			if conta_entradas == 1:
				procura_sucess(lista_nodos,x)
				atualiza_suss(lista_nodos)
				criarotas(lista_nodos,tamanho_dht,x)
				atualiza_tabela(lista_nodos)
			procura_sucess(lista_nodos,y)
			atualiza_suss(lista_nodos)
			criarotas(lista_nodos,tamanho_dht,y)
			atualiza_suss(lista_nodos)
			atualiza_tabela(lista_nodos)	
			conta_operacoes = conta_operacoes + 1	
	# RETIRA UM NODO ATIVO COPIA A TABELA DE ROTAS E PASSA PARA O SUCESSOR E ATUALIZA A TABELA DE ROTAS 
	if 'S' in lista[n1]:
		atualiza_tabela(lista_nodos)
		atualizarota_ativos(lista_nodos,tamanho_dht)
		conta_operacoes = conta_operacoes + 1
		exclue = int(lista[n1][2])
		obj = acha_objeto(lista_nodos,exclue)
		objsuss = lista_nodos[exclue].sus
		a1 = lista_nodos[exclue].tabela
		a2 = lista_nodos[objsuss].tabela
		lista_nodos[objsuss].tabela = merge_two_dicts(a1, a2)
		lista_nodos[exclue].ativo = 0
		atualizarota_ativos(lista_nodos,tamanho_dht)
		atualiza_tabela(lista_nodos)
		
	#USO DA FUNCAO LOOKUP PROCURA O NODO NA TABELA INFORMADA CASO NAO EXISTA PEGA O MAIOR NODO DA TABELA MAIS PROXIMO E PROCURA ATE ENCONTRAR
	if 'L' in lista[n1]:
		atualiza_suss(lista_nodos)
		atualizarota_ativos(lista_nodos,tamanho_dht)
		atualiza_tabela(lista_nodos)
		ope = int(lista[n1][2])
		look = int(lista[n1][3])
		lookup(lista_nodos,ope,look,conta_operacoes)
		conta_operacoes = conta_operacoes + 1	
	# INSERE UMA ROTA NA TABELA DE ROTAS ATUALIZA A TABELA DE ROTAS PARA ACHAR O SUCESSOR DO MESMO !	
	if 'I' in lista[n1]:
		atualiza_suss(lista_nodos)
		atualiza_tabela(lista_nodos)
		valid = lista[n1][2]
		ainserir = lista[n1][3]
		valorinserir = lista_nodos[int(ainserir)]
		lista_nodos[int(valid)].tabela[int(lista[n1][3])] = int(ainserir)
		atualiza_suss(lista_nodos)
		atualizarota_ativos(lista_nodos,tamanho_dht)
		conta_operacoes = conta_operacoes + 1
	atualiza_tabela(lista_nodos)
