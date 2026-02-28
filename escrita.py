import psutil
import csv
import datetime
import time 
import os

# Criação do arquivo
verificarArquivo = os.path.exists('arquivo-teste.csv')

# Formatação do array de dados
header = ['Data e Hora', 'CPU', 'RAM', 'DISCO']

print("Escrito por: Diego Menegaldo")
with open('arquivo-teste.csv', 'a', newline='') as arquivo:
        escrever = csv.writer(arquivo)
        if not verificarArquivo:
            escrever.writerow(header)
            print("Header escrito com sucesso as: ", datetime.datetime.now())
        while True:
            dataAtual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            dadosCPU = psutil.cpu_percent(interval=1)
            dadosRAM = psutil.virtual_memory().percent
            dadosDISCO = psutil.disk_usage('/').percent
            dadosCapturados = [dataAtual, dadosCPU, dadosRAM, dadosDISCO]
            escrever.writerow(dadosCapturados)
            print("Dados escritos com sucesso as:", datetime.datetime.now())
            time.sleep(0.1)
