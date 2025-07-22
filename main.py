# Saudação inicial
print("Olá turma do Python!")
print("Tudo bem com vocês?")

# Solicita o nome do utilizador
nome: str = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Prazer em te conhecer.")

# Pergunta a idade do utilizador
idade: int = int(input("Quantos anos você tem? "))

# Resposta personalizada com base na idade
if idade < 12:
    print("Uau! Você é bem jovem para estar aprendendo Python, que incrível!")
elif 12 <= idade <= 18:
    print("Legal! Aprender Python na sua idade é uma ótima escolha!")
elif 19 <= idade <= 40:
    print("Muito bem! Python é excelente para qualquer área profissional.")
else:
    print("Nunca é tarde para aprender algo novo, parabéns!")
    
    # Pergunta sobre o interesse na programação
interesse: str = input("O que mais te interessa em aprender com Python? ")