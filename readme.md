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
