import re

def encontrar_palavras_por_regex(regex, caminho_arquivo_entrada, caminho_arquivo_saida):
    try:
        # Ler o conteúdo do arquivo de entrada
        with open(caminho_arquivo_entrada, 'r') as arquivo_entrada:
            texto = arquivo_entrada.read()

        # Encontrar todas as palavras que correspondem ao padrão da regex
        palavras_encontradas = re.findall(regex, texto)

        # Escrever as palavras encontradas em um arquivo de saída
        with open(caminho_arquivo_saida, 'w') as arquivo_saida:
            for palavra in palavras_encontradas:
                arquivo_saida.write(palavra + '\n')

        print(f"Palavras encontradas pela regex '{regex}' foram salvas no arquivo '{caminho_arquivo_saida}'.")
    except FileNotFoundError:
        print("Arquivo de entrada não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
regex = r'".*"'  # Padrão que corresponde a todas as palavras em uma string
arquivo_entrada = "exemplo_codigo_para_ser_buscado.cs"  # Substitua pelo caminho correto do arquivo de entrada
arquivo_saida = "lista_palavras_encontradas_saida.txt"  # Substitua pelo caminho desejado para o arquivo de saída

encontrar_palavras_por_regex(regex, arquivo_entrada, arquivo_saida)
