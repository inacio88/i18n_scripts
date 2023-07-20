### Script i18n
#### Descrição
 lorem3

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