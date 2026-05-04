def validar_senha(senha):
    # Lista para guardar os requisitos que faltam
    requisitos_ausentes = []
    
    # Validação de comprimento (Decisão)
    if len(senha) < 8:
        requisitos_ausentes.append("Comprimento mínimo de 8 caracteres")
        
    # Validação de caracteres usando iteração implícita (Repetição e Decisão)
    if not any(char.isupper() for char in senha):
        requisitos_ausentes.append("Um caractere maiúsculo")
        
    if not any(char.islower() for char in senha):
        requisitos_ausentes.append("Um caractere minúsculo")
        
    if not any(char.isdigit() for char in senha):
        requisitos_ausentes.append("Um número")
        
    # isalnum() retorna True se for letra ou número. Negando isso, achamos os especiais.
    if not any(not char.isalnum() for char in senha):
        requisitos_ausentes.append("Um caractere especial")
        
    # Resultado final (Decisão)
    if not requisitos_ausentes:
        return "✅ Senha forte"
    else:
        resultado = "❌ Requisitos ausentes:\n"
        for requisito in requisitos_ausentes: # (Repetição)
            resultado += f" - {requisito}\n"
        return resultado

# --- Testando o código ---
print(validar_senha("senha123")) 
print("------------------------")
print(validar_senha("Senha@123"))