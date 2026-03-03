import csv

somaCpu = somaRam = somaDisco = 0
cpuMax = ramMax = discoMax = 0
contador = 0

with open('arquivo-teste.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        cpu = float(linha['CPU'])
        ram = float(linha['RAM'])
        disco = float(linha['DISCO'])

        somaCpu += cpu
        somaRam += ram
        somaDisco += disco

        if cpu > cpuMax:
            cpuMax = cpu
        if ram > ramMax:
            ramMax = ram
        if disco > discoMax:
            discoMax = disco

        contador += 1

if contador > 0:
    media_cpu = somaCpu / contador
    media_ram = somaRam / contador
    media_disco = somaDisco / contador

    with open('relatorio-tratado.csv', 'w', newline='') as arquivoTratado:
        escrever = csv.writer(arquivoTratado)

        escrever.writerow([
            'Media CPU (%)',
            'Pico CPU (%)',
            'Media RAM (%)',
            'Pico RAM (%)',
            'Media DISCO (%)',
            'Pico DISCO (%)'
        ])

        escrever.writerow([
            f"{media_cpu:.2f}",
            f"{cpuMax:.2f}",
            f"{media_ram:.2f}",
            f"{ramMax:.2f}",
            f"{media_disco:.2f}",
            f"{discoMax:.2f}"
        ])

    print("Arquivo relatorio-tratado.csv criado com sucesso!")
else:
    print("Nenhum dado encontrado no arquivo original.")