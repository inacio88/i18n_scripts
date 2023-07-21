import xml.etree.ElementTree as ET
from googletrans import Translator

def translate_to_english(array_of_strings):
    translator = Translator()

    translated_array = []
    for string in array_of_strings:
        # Detecting the language of the input string
        lang = translator.detect(string).lang

        # If the input string is already in English, no need to translate
        if lang == 'en':
            translated_array.append(string)
        else:
            # Translating the string to English
            translated_string = translator.translate(string, src=lang, dest='en').text
            translated_array.append(translated_string)

    return translated_array



def adicionar_valor_resx(caminho_arquivo, chave, valor):
    try:
        # Carregar o arquivo .resx existente
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()

        # Verificar se a chave já existe no arquivo .resx
        for data in root.findall("./data"):
            if data.attrib.get("name") == chave:
                print(f"A chave '{chave}' já existe no arquivo.")
                return

        # Criar um novo elemento 'data' para a nova chave-valor
        novo_elemento = ET.Element("data")
        novo_elemento.set("name", chave)
        novo_elemento.set("xml:space", "preserve")

        valor_elemento = ET.SubElement(novo_elemento, "value")
        valor_elemento.text = valor + "\n"

        # Adicionar o novo elemento ao root
        root.append(novo_elemento)

        # Salvar as alterações de volta ao arquivo
        tree.write(caminho_arquivo, encoding="utf-8", xml_declaration=True)

        print(f"Chave '{chave}' adicionada com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar a chave '{chave}': {e}")

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

if __name__ == "__main__":

    entrada_lista_strings = "teste/lista_strings_encontradas.txt"  # Substitua pelo caminho do arquivo desejado
    linhas = read_file_to_array_sem_linha_vazia(entrada_lista_strings)

    # Exemplo de uso
    caminho_arquivo_resx = "exemplo_recurso_ingles.resx"

    portuguese_strings = linhas
    english_strings = translate_to_english(portuguese_strings)
    #print(english_strings)
    
    for i in range(0, len(linhas)-1):
        chave = portuguese_strings[i].replace('"','')
        valor = english_strings[i].replace('"','')
        adicionar_valor_resx(caminho_arquivo_resx, chave, valor)
