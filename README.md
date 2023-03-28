# python-web-automation
Framework de automação de testes web com python

**Criar ambiente virtul**
python -m venv venv

**Inicializar ambiente virtual**
venv\Scripts\Activate.ps1

**Erro de permissao do powershell solução**
https://pt.stackoverflow.com/questions/220078/o-que-significa-o-erro-execu%C3%A7%C3%A3o-de-scripts-foi-desabilitada-neste-sistema

**Erro resolvido com a doc do selenium**
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

session not created: This version of ChromeDriver only supports Chrome version 83

**Documentação do xpath**
https://www.w3schools.com/xml/xpath_intro.asp

**Execucao de teste com pytest**

O pytest identifica os arquivos e classes de teste, atraves da palavra reservada **test**, neste caso, ao utilizar o pytest é necessario utilizar este palavra nos metodos de teste e arquivos de teste que forem criados.

- Para executar apenas 1 teste simples
> pytest <nome do arquivo de teste>

- Para executar 1 teste com um report mais amigavel (Verboso)
> pytest -v <nome do arquivo de teste>

Ao importar o **Pytest** no arquivo de teste, conseguimos utilizar marks para executar e identificar testes especificos. Você pode consultar mais detalhes sobre os marks na seguinte documentação: https://docs.pytest.org/en/7.1.x/example/markers.html

- Para executar testes com marks especificos (tags), podemos utilizar o seguinte comando
> pytest -v -m <nome_da_tag_do_cenario>
> pytest -v -m buy_two_product