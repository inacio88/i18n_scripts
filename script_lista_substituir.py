import re
import argparse

def read_file_to_array_sem_linha_vazia(filepath):
    lines_array = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()  # Remover espaços em branco e quebras de linha no início e no final
                if line:
                    lines_array.append(line)
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")

    return lines_array

#Essa função esta limitada a apenas onde não tenha duas strings tipo "texto_identico".i18n() e "texto_identico" sem o metodo
def simples_replace(velha_string, replacement, filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()

        modified_content = content.replace(velha_string, replacement)

        with open(filepath, 'w') as file:
            file.write(modified_content)

        print(f"Substitution successful in {filepath}!")
        file.close()
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")

# Exemplo de uso
if __name__ == "__main__":
    entrada_lista_strings = "teste/lista_strings_encontradas.txt"  # Substitua pelo caminho do arquivo desejado
    linhas = read_file_to_array_sem_linha_vazia(entrada_lista_strings)


    saida_arquivo_onde_tera_substituicao = "teste/lista_saida.txt"  # Substitua pelo caminho do arquivo desejado


    for sentenca in linhas:
        simples_replace(sentenca, sentenca + ".i18n()", saida_arquivo_onde_tera_substituicao)




# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Regex Replace Script")
#     parser.add_argument("regex", help="Regular expression pattern to search for")
#     parser.add_argument("replacement", help="Replacement text for matches")
#     parser.add_argument("filepath", help="Path to the file where to perform the substitution")

#     args = parser.parse_args()

#     regex_replace(args.regex, args.replacement, args.filepath)
