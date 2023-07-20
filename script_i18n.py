import xml.etree.ElementTree as ET

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
        valor_elemento.text = valor

        # Adicionar o novo elemento ao root
        root.append(novo_elemento)

        # Salvar as alterações de volta ao arquivo
        tree.write(caminho_arquivo, encoding="utf-8", xml_declaration=True)

        print(f"Chave '{chave}' adicionada com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar a chave '{chave}': {e}")

# Exemplo de uso
caminho_arquivo_resx = "exemplo_recurso.resx"
chave = "laranfja"
valor = "orangef"

adicionar_valor_resx(caminho_arquivo_resx, chave, valor)
