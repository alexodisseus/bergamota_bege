#!/usr/bin/python
# -*- coding: latin-1 -*-
from donaclotilde import *

from datetime import date
import sqlite3


class Model(Donaclotilde):
	"""docstring for Model"""
	def __init__(self):
		#super(Model, self).__init__()
		#self.arg = argi

		self.usuario="defalt"
		self.entrada_select=[]
		self.entrada_from_table=[]
		self.entrada_insert=[]
		self.entrada_count=[]
		self.entrada_where=[]
		self.query=[]


	def connect_db(self):
		self.conn = sqlite3.connect('database.db')
		self.cursor = self.conn.cursor()
	

	def salvar(self,kwargs):
		
		data_hoje = date.today()
		kwargs["criado_em_multa"] = str(data_hoje)
		kwargs["valor_multa"] = "Pendente"
		kwargs["status_multa"] = "Pendente"

		valores=[]
		for x in kwargs.values():
			valores.append(x)

		colunas=[]
		for x in kwargs.keys():
			colunas.append(x)

		sql = self.set("cadastro_multa",valores,colunas)
		#print(sql)
		verifica = self.buscar_multa_repetida(kwargs)
		
		if verifica != []:
			return verifica
		else:
			self.insert(sql)
			return True


	def listall(self):

		self.select('codigo_infracao')
		#self.select('data_termo')
		self.select('peso_infracao')
		self.select('descricao_infracao')
		self.select('codigo_infracao')
		#self.select('data_termo')
		self.select('peso_infracao')
		self.select('descricao_infracao')
		self.select('descricao_infracao')
		
		self.from_table("infracao")
		sql = self.get()
		data = self.result_list(sql)

		return data

	def listar_infracao_filtro(self,busca):

		self.select('codigo_infracao')
		self.select('descricao_infracao')
		
		self.from_table("infracao")
		if busca:
			self.where(busca,"descricao_infracao")
		

		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass
