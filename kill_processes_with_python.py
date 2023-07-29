import psutil
import time

# definir as portas para encerrar processos
portas = [80, 443, 3306, 21, 14147]

# obter uma lista de todos os processos em execução
processos = psutil.process_iter()

# percorrer a lista de processos
for processo in processos:
    try:
        # obter informações sobre o processo
        info = processo.as_dict(attrs=['pid', 'name', 'connections'])

        # percorrer as conexões do processo
        for conn in info['connections']:
            # verificar se a conexão está em uma das portas especificadas
            if conn.laddr.port in portas:
                # encerrar o processo
                processo.kill()
                print(f"Processo {info['name']} encerrado na porta {conn.laddr.port}")
                break
    except:
        # se não for possível obter informações sobre o processo, continuar
        continue

time.sleep(10)
