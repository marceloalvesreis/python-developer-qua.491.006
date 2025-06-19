import time
from datetime import datetime

try:
    while True:
        agora = datetime.now()
        hora_formatada = agora.strftime("%H:%M:%S")
        print(f"\rHora atual: {hora_formatada}", end="")
        time.sleep(1)
except Exception as e:
    print("\nPrograma interrompido pelo usuário.")