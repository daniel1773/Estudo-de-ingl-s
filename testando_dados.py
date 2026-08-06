from conexao_bd import conectar_db
import random


#a funcao de 'conectar' retorna a variavel 'conexao'
cursor = conectar_db().cursor()
cursor.execute("""
SELECT *
FROM Vocabulario
""")

dados = cursor.fetchall()

#busca linha aleatoria do banco
linha_puxada = random.choice(dados)

#separar cada variavel com seus dados
palavra_certa = linha_puxada[1]
traducoes_certas = linha_puxada[2]
sinonimos = linha_puxada[3]
antonimos = linha_puxada[4]
exemplo_frase = linha_puxada[5]


# Alternativa certa (TRADUCOES)
traducao_certa = random.choice(traducoes_certas.split("; "))


# Alternativas erradas (TRADUCOES)
lista_filtrada = [] #lista de 7 sem a alternativa certa de 'linha puxada'
while len(lista_filtrada) < 7:
    a = random.choice(dados)
    if a != linha_puxada and a not in lista_filtrada:
        lista_filtrada.append(a)

traducoes_erradas = [] #lista de 3 com as alternativas erradas de traduções
while len(traducoes_erradas) < 3:
    b1 = random.choice(lista_filtrada)
    b2 = b1[2]
    b3 = random.choice(b2.split("; ")) #transforma a string em lista pelo separador '; '
    if b3 not in traducoes_erradas and b3 not in traducoes_certas:
        traducoes_erradas.append(b3)


# Total de Alternativas (TRADUCOES)
alternativas_t = [i for i in traducoes_erradas]
alternativas_t.append(traducao_certa)


##caso queira usar depois##
#palavras_erradas = []
#for _ in range(3):
#    i = random.choice(lista_filtrada)
#    p = i[1]
#    palavras_erradas.append(p)


###total de alternativas (PALAVRAS)###
#alternativas_p = [i for i in palavras_erradas]
#alternativas_p.append(palavra_certa)

#print(alternativas_p)


#INCIANDO PROGRAMA
def lines(n):
    linha1 = '=-' * n
    linha2 = linha1 + '=' 
    return linha2

print(lines(4))
print("Bom dia")
print(lines(4))

print('\nPalavra: ', palavra_certa)

random.shuffle(alternativas_t) #embaralhando as alternativas
for i, elemento in enumerate(alternativas_t, start=1):
    print(f"{i}º) {elemento}")

resposta_usuario = input('Número da escolha: ')
try:
    resposta_usuario_int = int(resposta_usuario)
except ValueError:
    print("ERRO: é aceito somente números inteiros!")

texto_apos_resposta = f"""\nOutras traduções: {traducoes_certas}\n\nSinonimos: {sinonimos}\nAntonimos: {antonimos}
\nExemplo: {exemplo_frase}\n"""

if alternativas_t[resposta_usuario_int - 1] == traducao_certa:
    print("\nAcertouuuu!")
    print(texto_apos_resposta)
else:
    print("\nErrou!")
    print(f"\nOpção correta: {traducao_certa}\n{texto_apos_resposta}")