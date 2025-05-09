# Funcoes embutidas em Python (Built-in Functions)

# Saída e entrada de dados
print("Olá, mundo!")  # Exibe mensagens na tela
input("Digite seu nome: ")  # Captura entrada do usuário

# Conversão de tipos
tipo_int = int("10")  # Converte para inteiro
tipo_float = float("10.5")  # Converte para float
tipo_str = str(100)  # Converte para string
tipo_bool = bool(1)  # Converte para booleano: True (1) ou False (0)

# Operações matemáticas
abs(-5)  # Retorna o valor absoluto (5): Transforma valores negativos em positivos
pow(2, 3)  # Potência (2³ = 8) : Calcula a potência de um número.
round(3.14159, 2)  # Arredonda um número (3.14)
max(10, 20, 30)  # Retorna o maior valor (30)
min(10, 20, 30)  # Retorna o menor valor (10)
sum([1, 2, 3])  # Soma os elementos de uma lista (6)

# Manipulação de listas e sequências
len("Python")  # Retorna o tamanho da string (6)
list(range(5))  # Cria uma lista [0, 1, 2, 3, 4] 
sorted([3, 1, 2])  # Retorna uma lista ordenada [1, 2, 3]

# Manipulação de strings
chr(65)  # Converte um código ASCII para caractere ('A')
ord('A')  # Converte um caractere para código ASCII (65)

# Funções lógicas e de comparação
all([True, True, False])  # Retorna False (porque há um False na lista)
any([False, False, True])  # Retorna True (porque há um True na lista)

# Trabalhando com objetos e tipos
type(10)  # Retorna o tipo da variável (<class 'int'>)
isinstance(10, int)  # Verifica se o valor é do tipo especificado (True)

dir([])  # Lista métodos disponíveis para um objeto

# Funções especiais
zip([1, 2], ["a", "b"])  # Agrupa listas [(1, 'a'), (2, 'b')]
map(str.upper, ["python", "java"])  # Aplica função a cada elemento da lista ['PYTHON', 'JAVA']
filter(lambda x: x > 5, [3, 7, 2, 8])  # Filtra elementos [7, 8]

# Funções para arquivos
open("arquivo.txt", "w")  # Abre um arquivo para escrita

# Encerramento do programa
exit()  # Encerra a execução do programa
