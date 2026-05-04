def monitorar_servidor():
    print("🖥️ Monitoramento do servidor iniciado. (Digite 'desligar' para sair)")
    
    # Loop de escuta contínua (Repetição)
    while True:
        entrada = input("Informe a temperatura atual do sensor (ºC): ")
        
        # Condição de parada do sistema (Decisão)
        if entrada.lower().strip() == 'desligar':
            print("Desligando o monitoramento. Sistema encerrado.")
            break # Quebra o loop de repetição
            
        try:
            temperatura = float(entrada)
            
            # Validação do limite de temperatura (Decisão)
            if temperatura > 80:
                print("🚨 ALERTA: Limite ultrapassado! Resfriamento ativado.")
            else:
                print("✅ Temperatura dentro da normalidade.")
                
        except ValueError:
            print("⚠️ Erro: Por favor, digite um valor numérico válido ou 'desligar'.")

# --- Testando o código ---
# Para testar, basta chamar a função abaixo (remova o '#' na sua IDE)
# monitorar_servidor()