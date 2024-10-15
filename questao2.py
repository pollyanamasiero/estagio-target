# Questão 2

# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def count_a_in_string(s):
    # Converter string para minúsculas e contar a letra 'a'
    count = s.lower().count('a')
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

# String a ser verificada
string = input("Informe uma string: ")
print(count_a_in_string(string))
