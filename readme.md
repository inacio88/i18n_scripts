### Script i18n
#### Descrição
- 4 processos serão feitos aqui, os 3 primeiros estão desenhados abaixo.
- 1° Geração da lista de strings.
- 2° A partir da lista gerada, fazer a substuição de cada string sem i18n com o métodos adicionado.
- 3° A partir da lista gerada, adcioná-las no .resx em inglês e português.
- 4° Pegar o nome dos elementos de um formulário e jogar num arquivo de saída nome + .SetText, e mais abaixo ainda no mesmo arquivo de saída as respctivas strings para serem utilizadas no processo n°3.

 #### Passo a passo do diagrama

![alt text](https://github.com/inacio88/i18n_scripts/blob/main/diagrama/fluxugrama.jpg?raw=true)


~~~sh
~~~

~~~python
~~~

##### Passo 1 - Gerar a lista a partir do arquivo que lá no final terá substituições
~~~sh
python script_regex.py
~~~

###### Repare que aqui foi definido três coisas importantes dentro do script
~~~python
regex = r'"(.*?)"(?!.i18n)'
arquivo_entrada = "exemplo_codigo_para_ser_buscado.cs"
arquivo_saida = "teste/lista_strings_encontradas.txt"
~~~

##### Passo 2 Começar a sanitizar a lista gerada no passo anterior
- O primeiro argumento é a regex
- O segundo é o que entrará no lugar da regex, no caso, uma string vazia como estamos eliminando.
- Esse comando abaixo remove string do tipo:
    - "dd/MM/yyyy HH:mm"
    - "MM/yyyy"
    - "dd/MM/yyyy"
~~~sh
python script_substituicao.py '".?.?/?../....*"' '' teste/lista_strings_encontradas.txt
~~~

- Esse comando abaixo remove string do tipo:
    - "{0:n3}"
~~~sh
python script_substituicao.py '"[\{.*\}].*"' '' teste/lista_strings_encontradas.txt
~~~

- Conforme Wittgenstein, "Os limites da minha linguagem são os limites do meu mundo", então esse passo pode ser repetido enquanto você for capaz de escrever boas regex para facilitar mais o trabalho de sanitizar.

##### Passo 3 (para os limitados)
- Caso o limite do seu mundo seja a esquina da sua casa, ou seja, incapaz de escrever regex para todos os casos, aqui você pode olhar manualmente o arquivo e deletar linha por linha.

##### Passo 4 Substituição no arquivo original com a lista final
~~~sh
python script_lista_substituir.py
~~~
###### Repare que aqui foi definido duas coisas importantes dentro do script
~~~python
entrada_lista_strings = "teste/lista_strings_encontradas.txt"  
saida_arquivo_onde_tera_substituicao = "exemplo_final.cs"
~~~

###### !ATENCÃO!
- Perceba que no exemplo_final.cs temos o seguinte
~~~python
var oie = "Não foi possível realizar 7a liberação de alguns registros:\n".i18n();
var oie2 = "Não foi possível realizar 7a liberação de alguns registros:\n".i18n().i18n();
~~~
- Isso acontece por termos inicialmente duas strings iguais e uma com .i18n() desde o início e a outra porque foi acrescida pelo script.
- A dica é (.i18n\(\))\1, você já tem o script em mãos para resolver isso.
- Confira no seu arquivo onde ocorrem as substituições para vê se deu tudo certo.



 #### Nessa parte vamos executar os scripts para add chave e valor no xml resx
~~~sh
python script_xml_ingles_add.py
python script_xml_portugues_add.py
~~~

###### Repare que aqui foi definido duas coisas importantes dentro do script
~~~python
entrada_lista_strings = "teste/lista_strings_encontradas.txt"
caminho_arquivo_resx = "exemplo_recurso_ingles.resx"
~~~


###### !ATENCÃO!
- Perceba que quebra de linhas geradas pelo script ainda não é a ideal, por tanto, é necessário conferir manualmente. Apenas de todas as tags abrirem e fecharem corretamente.
~~~xml
</value></data><data name="Primeiro texto" xml:space="preserve"><value>Primeiro texto
</value></data><data name="Segundo texto" xml:space="preserve"><value>Segundo texto
</value></data></root>
~~~

##### Script do designer
~~~sh
python script_designer.py
~~~
###### Repare que aqui foi definido três coisas importantes dentro do script
- Como aqui estamos interessados em dois elementos da linha, tem dois grupos delineados.
- No arquivo de saída terá o nome do elemento + metodo, e mais embaixo as strings.
~~~python
regex = r'this\.(.*)\.Text\s=\s(".*");' 
arquivo_entrada = "designer_exemplo.cs"
arquivo_saida = "teste/saida_designer.txt"
~~~
- Formatação
~~~sh
python script_substituicao.py '("preserve">)(<value>.*)' '\1\n\t\2' exemplo_recurso.resx;
python script_substituicao.py '(</value>)(</data>)' '\1\n\2' exemplo_recurso.resx;
python script_substituicao.py '(<value>)(.*)\n(</value>)' '\1\2\3' exemplo_recurso.resx;
python script_substituicao.py '(</data>)(<data.*)' '\1\n\2' exemplo_recurso.resx
~~~
## Para executar todos esses scripts

- Aqui será num ambiente python virtual

# Criando o ambiente
~~~sh
virtualenv ambiente_script
~~~

# Ativando o ambiente NO LINUX
~~~sh
source ambiente_script/bin/activate
~~~
# Dependências dos scripts
~~~sh
pip install elementpath
pip install argparse
pip install googletrans==4.0.0-rc1
~~~

# Ativando o ambiente NO WINDOWS acho que é assim no powershell confirmar depois
~~~sh
ambiente_script\bin\activate
~~~

# Dependência
~~~sh
pip install elementpath
~~~

# Execução
~~~sh
python script_i18n.py
~~~

--------------------------------------------------------------------------------------

### Script regex

# Execução
~~~sh
python script_regex.py
~~~



--------------------------------------------------------------------------------------

### Script substituição
###### !Atenção! se não quiser usar o escape na aspas duplas da regex, passe ela dentro de aspas simples

# Dependência
~~~sh
pip install argparse
~~~

# Execução
~~~sh
python script_substituicao.py "\".*\"" "\"TT\"" exemplo_codigo_para_ser_buscado.cs
~~~


# Execução
~~~sh
 python script_substituicao.py "(\".*\")" "\1.i18n()" exemplo_codigo_para_ser_buscado.cs
~~~

### Execução eliminando alguns formatos de data
~~~sh
 python script_substituicao.py '".?.?/?../....*"' '' teste/lista_strings_encontradas.txt
~~~

### Execução eliminando alguns formatos tipo "{0:n4}"
~~~sh
python script_substituicao.py '"[\{.*\}].*"' '' teste/lista_strings_encontradas.txt
~~~

--------------------------------------------------------------------------------------

### Script add xml
###### !Atenção! se não quiser usar o escape na aspas duplas da regex, passe ela dentro de aspas simples

# Dependência
~~~sh
pip install googletrans==4.0.0-rc1
~~~

# Execução
~~~sh
python script_xml_portugues_add.py
~~~



------------------------------------------------------------------------
###### Exemplos de regex úteis
- Negação de algo do tipo "{0:n4}"
~~~sh
"[^\{.*\}].*"
~~~

- Formato data
~~~sh
".?.?/?../....*"
~~~

- Pegar mais de uma string numa mesma linha
~~~sh
".*?"
~~~