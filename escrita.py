import psutil
import csv
import datetime
import time 
import os

# Criação do arquivo
verificarArquivo = os.path.exists('arquivo-teste.csv')

# Formatação do array de dados
dataAtual = datetime.datetime.now()
dadosCPU = psutil.cpu_percent(interval=1)
dadosRAM = psutil.virtual_memory().percent
dadosDISCO = psutil.disk_usage('/').percent
header = ['Data e Hora', 'CPU', 'RAM', 'DISCO']
dadosCapturados = [dataAtual, dadosCPU, dadosRAM, dadosDISCO]

print("Escrito por: Diego Menegaldo")
with open('arquivo-teste.csv', 'a', newline='') as arquivo:
        escrever = csv.writer(arquivo)
        if not verificarArquivo:
            escrever.writerow(header)
            print("Header escrito com sucesso as: ", dataAtual)
        while True:
            escrever.writerow(dadosCapturados)
            print("Dados escritos com sucesso as:", dataAtual)
            time.sleep(10)
