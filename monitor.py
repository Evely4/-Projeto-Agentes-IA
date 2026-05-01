import time
import random
import logging
from datetime import datetime

# Configuração de Logs conforme diretrizes do @Backend e @DevOps
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MonitorSistema:
    """
    Classe para monitoramento de métricas computacionais.
    Foco: Predição de falhas em consumo de energia e CPU.
    """
    
    def __init__(self):
        self.limite_alerta_cpu = 85.0
        self.limite_alerta_energia = 90.0
        self.executando = True

    def ler_sensores_simulados(self):
        """Simula a coleta de dados com tratamento de erro."""
        try:
            return {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "cpu_usage": round(random.uniform(10.0, 100.0), 2),
                "power_consumption": round(random.uniform(20.0, 110.0), 2)
            }
        except Exception as e:
            logging.error(f"Erro crítico na leitura dos sensores: {e}")
            return None

    def analisar_dados(self, leitura):
        """Lógica de detecção de anomalias conforme manual do @QA."""
        if leitura["cpu_usage"] > self.limite_alerta_cpu:
            logging.warning(f"🚨 ALERTA: CPU em {leitura['cpu_usage']}% - Risco de falha!")
            
        if leitura["power_consumption"] > self.limite_alerta_energia:
            logging.warning(f"⚡ ANOMALIA: Consumo elevado de {leitura['power_consumption']}W!")
        else:
            logging.info(f"✅ Estável: CPU {leitura['cpu_usage']}% | Energia {leitura['power_consumption']}W")

    def iniciar(self, ciclos=10):
        """Inicia o monitoramento com limite de ciclos para evitar loop infinito."""
        logging.info(f"Iniciando Monitoramento de Engenharia por {ciclos} ciclos...")
        
        try:
            contador = 0
            while contador < ciclos:
                dados = self.ler_sensores_simulados()
                if dados:
                    self.analisar_dados(dados)
                
                time.sleep(2)  # Intervalo de 2 segundos entre coletas
                contador += 1
                
            logging.info("Monitoramento concluído com sucesso. Sistema encerrado de forma segura.")
            
        except KeyboardInterrupt:
            logging.info("Encerrando monitoramento manualmente via teclado (Ctrl+C).")
            self.executando = False

if __name__ == "__main__":
    monitor = MonitorSistema()
    # Você pode alterar o número de ciclos aqui (ex: monitor.iniciar(5))
    monitor.iniciar(10)