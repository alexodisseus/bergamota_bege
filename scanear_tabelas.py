from openpyxl import load_workbook
import os
print('olá')

#file tem que escanear a pasta do diretorio para encontrar os arquivos

#tem que fazer a relação de qual arquivo é mais recente
#devolver a comparação dos mesmos






cwd = 'doc/'

dire = os.listdir(cwd)
#paega os arquivos da pasta doc/
print(dire)


#for y in dire: - continuar para escanear os dois arquivos
    
    


workbook = load_workbook(filename=cwd)


sheet = workbook.active

p = 2
for x in dados:


	sheet["A1"] = x[0]
	sheet["b1"] = x[1]
	sheet["c1"] = x[2]
	sheet["d1"] = x[3]
	sheet["e1"] = x[4]
	sheet["f1"] = x[5]
	sheet["g1"] = x[6]
	sheet["H1"] = x[7]
	sheet["I"+str(p)] = x[8]

#a b c d e f g


workbook.save(filename='relatorios/relatorio.xlsx')