import csv

while True:
        escolha = int(input("""Digite o que deseja visualizar:
1 - Visualizar todos os dados do CSV sem tratamento
2 - Visualizar relatório de monitoramento
0 - Sair
Escolha: """))

        if escolha == 0:
            print("Encerrando programa...")
            break

        if escolha not in (1, 2):
            print("Opção inválida.\n")
            continue

        with open('arquivo-teste.csv', 'r') as arquivo:
            leitor = csv.DictReader(arquivo)

            if escolha == 1:
                print("\nDados sem tratamento:\n")
                for linha in leitor:
                    print(linha)
            elif escolha == 2:
                somaCpu = 0 
                somaRam = 0
                somaDisco = 0
                cpuMax = 0
                ramMax = 0
                discoMax = 0
                contador = 0

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
                    print("\n Relatório com dados tratados \n")
                    print(f"Média CPU: {media_cpu:.2f}%")
                    print(f"Pico CPU: {cpuMax:.2f}%\n")
                    print(f"Média RAM: {media_ram:.2f}%")
                    print(f"Pico RAM: {ramMax:.2f}%\n")
                    print(f"Média DISCO: {media_disco:.2f}%")
                    print(f"Pico DISCO: {discoMax:.2f}%")
                else:
                    print("Nenhum dado encontrado no arquivo.")