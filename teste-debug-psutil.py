import psutil
import time

print("Monitorando uso de memória RAM\n")

nome_digitado = input("Digite seu nome: ")

while True:
    mem = psutil.virtual_memory()
    
    print(f"Uso: {mem.percent}%")
    print(f"Maquina do {nome_digitado}")

    time.sleep(2)