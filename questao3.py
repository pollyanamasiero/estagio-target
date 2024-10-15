# Questão 3

# Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
#
# Ao final do processamento, qual será o valor da variável SOMA?

# Trecho original:
# int INDICE = 12, SOMA = 0, K = 1;
# enquanto K < INDICE faça {
#     K = K + 1;
#     SOMA = SOMA + K;
# }
# imprimir(SOMA);

# Explicação:
# Começa com K = 1, soma K a cada iteração até K ser igual a 12.
# Soma será a soma de 2 a 12.

SOMA = 0
K = 1
INDICE = 12

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)


# Ao final do processamento, o valor de SOMA será 77.