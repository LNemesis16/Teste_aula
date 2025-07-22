def programa_python():
    print("=" * 40)
    print("Olá turma do Python!")
    print("Tudo bem com vocês?")
    print("=" * 40)
    
    nome: str = input("Qual é o seu nome? ")
    print(f"Olá, {nome}! Prazer em te conhecer.")
    
    # Validação da idade
    while True:
        try:
            idade: int = int(input("Quantos anos você tem? "))
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido para a idade.")
    
    if idade < 12:
        print("Uau! Você é bem jovem para estar aprendendo Python, que incrível!")
    elif 12 <= idade <= 18:
        print("Legal! Aprender Python na sua idade é uma ótima escolha!")
    elif 19 <= idade <= 40:
        print("Muito bem! Python é excelente para qualquer área profissional.")
    else:
        print("Nunca é tarde para aprender algo novo, parabéns!")
    
    interesse: str = input("O que mais te interessa em aprender com Python? ")
    print(f"Interessante, {nome}! Aprender mais sobre '{interesse}' é uma excelente ideia. Boa sorte nos estudos!")
    print("=" * 40)