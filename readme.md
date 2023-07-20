### Script i18n
#### Descrição
 lorem3

 #### Passo a passo do diagrama
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
###### Repare que aqui foi definido três coisas importantes dentro do script
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



## Para executar

- Aqui será num ambiente python virtual

# Criando o ambiente
~~~sh
virtualenv ambiente_script
~~~

# Ativando o ambiente NO LINUX
~~~sh
source ambiente_script/bin/activate
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