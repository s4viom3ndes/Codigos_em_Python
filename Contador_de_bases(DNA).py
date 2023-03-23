seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'# Variável que receberá a sequencia

tam = len(seq)# função que retorna como valor inteiro o tamanho da string (seq)

print(f'tamanho: {tam}')
#------------------------------------------------------------------

citosina = 'C'
guanina = 'G'
timina = 'T'
adenina = 'A'
#------------------------------------------------------------------
"""
inicializando os contadores com o valor '0'
"""
contC = 0# Contador da base 'C'
contG = 0# Contador da base 'G'
contA = 0# Contador da base 'A'
contT = 0# Contador da base 'T'

"""
loop que recebe o tamanho da string (Código genético) como parâmetro e o percorre contando as bases
"""

for i in range(tam):
    if citosina in seq[i]:# Verifica se 'C' está na posição 'i', caso sim, contC++ (Soma 1)
        contC = contC + 1

    if guanina in seq[i]:# Verifica se 'G' está na posição 'i', caso sim, contG++ (Soma 1)
        contG = contG + 1

    if adenina in seq[i]:# Verifica se 'A' está na posição 'i', caso sim, contA++ (Soma 1)
        contA = contA + 1

    if timina in seq[i]:# Verifica se 'T' está na posição 'i', caso sim, contT++ (Soma 1)
        contT = contT + 1

soma = contC + contG + contA + contT
        
print(f'C: {contC}\nG: {contG}\nA: {contA}\nT: {contT} \nTotal: {soma}')# Printando os resultados



