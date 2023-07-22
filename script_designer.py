import re

def encontrar_palavras_por_regex(regex, caminho_arquivo_entrada, caminho_arquivo_saida):
    try:
        # Ler o conteúdo do arquivo de entrada
        with open(caminho_arquivo_entrada, 'r') as arquivo_entrada:
            texto = arquivo_entrada.read()

        # Encontrar todas as palavras que correspondem ao padrão da regex
        palavras_encontradas = re.findall(regex, texto)
        print(palavras_encontradas[0][1])
        # Escrever as palavras encontradas em um arquivo de saída
        with open(caminho_arquivo_saida, 'w') as arquivo_saida:
            for i in range(0, len(palavras_encontradas)-1):
                arquivo_saida.write(palavras_encontradas[i][0] + '.SetText()' + '\n')

            arquivo_saida.write('\n')
            arquivo_saida.write('\n')
            arquivo_saida.write('\n')

            for i in range(0, len(palavras_encontradas)-1):
                arquivo_saida.write(palavras_encontradas[i][1] + '\n')

        print(f"Palavras encontradas pela regex '{regex}' foram salvas no arquivo '{caminho_arquivo_saida}'.")
    except FileNotFoundError:
        print("Arquivo de entrada não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso

#regex = r'".*"'  # Padrão que corresponde a todas as palavras em uma string
regex = r'this\.(.*)\.Text\s=\s(".*");'  # Padrão que corresponde a todas as palavras em uma string

arquivo_entrada = "designer_exemplo.cs"  # Substitua pelo caminho correto do arquivo de entrada
arquivo_saida = "teste/saida_designer.txt"  # Substitua pelo caminho desejado para o arquivo de saída

encontrar_palavras_por_regex(regex, arquivo_entrada, arquivo_saida)
