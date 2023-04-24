# Python-web-automation
Framework de automação de testes web com **Python**.

## Tecnologias e padrões utilizados:

- Python
- Biblioteca Venv
- Pytest
- Selenium-webdriver
- Page Objects

#

- **Python**

  Python é uma linguagem de programação interpretada, de alto nível, dinâmica e de uso geral. Ela suporta múltiplos paradigmas de programação, incluindo orientação a objetos, programação funcional e procedural. Python tem uma sintaxe simples e clara, com tipagem dinâmica e gerenciamento automático de memória. É uma linguagem portável e possui uma grande biblioteca padrão, além de uma ampla comunidade de desenvolvedores. Python é amplamente utilizado em áreas como ciência de dados, desenvolvimento web, automação de tarefas e aprendizado de máquina.
  
- **Biblioteca Venv**

  A biblioteca venv é uma ferramenta do Python para criar ambientes virtuais isolados. Ela permite que você crie um ambiente de desenvolvimento com uma versão específica do Python e instale as bibliotecas necessárias sem interferir no ambiente de desenvolvimento principal. Isso ajuda a evitar conflitos de dependências entre projetos e garante que cada projeto tenha seu próprio ambiente de execução independente.
  
- **Pytest**

  O Pytest é um framework de teste de software para a linguagem Python. Ele oferece uma abordagem simples e fácil de usar para escrever, organizar e executar testes automatizados em projetos Python. O Pytest possui uma sintaxe simples e legível que permite escrever testes em formato de funções Python. Além disso, ele oferece uma ampla gama de recursos e plugins para estender a funcionalidade e suportar testes mais complexos, como testes parametrizados e fixtures. O Pytest também possui recursos para executar testes em paralelo, relatórios detalhados de resultados de testes e integração com outras ferramentas de teste e CI/CD. O Pytest é amplamente utilizado na comunidade Python e é considerado uma das melhores opções para testes de software em projetos Python, por sua simplicidade, eficiência e recursos avançados.
  
- **Selenium webdriver**

  O Selenium WebDriver é uma ferramenta de automação de testes para aplicações web que permite a escrita de testes automatizados em diferentes linguagens de programação. Ele simula a interação do usuário com o navegador web, permitindo a validação do conteúdo e a execução de ações em elementos da página. É compatível com vários navegadores e amplamente utilizado em testes de integração e de aceitação automatizados para melhorar a qualidade do software.

- **Page Objects**

  Page Objects é um padrão de projeto utilizado em testes de software para melhorar a manutenibilidade e legibilidade dos testes automatizados. Ele consiste em mapear cada página da aplicação testada como um objeto, onde seus elementos são encapsulados em métodos e atributos. Assim, os testes passam a ser escritos em um nível de abstração mais alto, tornando-os mais compreensíveis e fáceis de serem mantidos.
  
### Links para acesso as documentações das ferramentas:

- Python

> https://docs.python.org/3/

- Biblioteca Venv

> https://docs.python.org/3/library/venv.html

- Pytest

> https://docs.pytest.org/en/7.2.x/

- Selenium webdriver

> https://www.selenium.dev/

## Criando ambiente virtual com biblioteca venv

Para criar o ambiente virtual basta utilizar o seguinte comando:

```python -m venv <nome do ambiente>```

Aguarde alguns instantes até que o ambiente virtual seja criado. Isso deve criar uma pasta chamada com o nome do ambeinte no diretório atual. Para ativar o ambiente virtual, digite o seguinte comando no terminal:

**No Windows:**

```<nome do ambiente>\Scripts\Activate.ps1```

**No mac e Linux**

```source <nome do ambiente>/bin/activate```

ATENÇÃO:

> Ao executar o ambiente virtual no windows pode aparecer um erro de permissão de acesso. Este erro acontece devido algumas politicas de segurança da Microsoft,
para solucionar o erro basta seguir este link: 

> https://pt.stackoverflow.com/questions/220078/o-que-significa-o-erro-execu%C3%A7%C3%A3o-de-scripts-foi-desabilitada-neste-sistema

## Instalando dependencias do projeto

Antes de executar o projeto, devemos instalar as dependências no nosso ambiente virtual criado. Atenção, uma vez criado o ambiente virtual e instalado as dependências
necessarias do projeto, estas dependências ficarão disponiveis apenas no ambiente virtual criado. Caso esse ambiente virutal seja deletado, será necessario instalar
novamente as dependências do projeto.

### Instalando Pytest

Para instalar o Pytest, basta executar este comando no terminal:

> pip install -U pytest

### Instalando Selenium webdriver

Para instalar o Selenium webdriver, basta executar este comando no terminal:

> pip install selenium

Após as instalações das dependencias com sucesso, podemos executar os testes do projeto.

## Execucao dos teste com pytest

O Pytest identifica os arquivos e classes de teste, atraves da palavra reservada **test**, neste caso, ao utilizar o pytest é necessario utilizar este palavra nos metodos de teste e arquivos de teste que forem criados.

- Para executar apenas 1 teste simples:

> pytest <nome_do_arquivo_de_teste>

- Para executar 1 teste com um report mais amigavel (Verboso) no terminal, executar o seguinte comando:

> pytest -v <nome_do_arquivo_de_teste>

Ao importar o **Pytest** no arquivo de teste, conseguimos utilizar **marks** para executar e identificar testes especificos. Você pode consultar mais detalhes sobre os marks na seguinte documentação: https://docs.pytest.org/en/7.1.x/example/markers.html

- Para executar testes com marks especificos (tags), podemos utilizar o seguinte comando

> pytest -v -m <nome_da_tag_do_cenario>

> Ex: pytest -v -m buy_two_product

Caso queira executar todos os testes contidos no projeto, basta executar o comando no terminal:

> pytest

## Atenção

Ao executr o projeto em sistemas operacionais linux, pode surgir um erro como este:

> selenium.common.exceptions.WebDriverException: Message: unknown error: Chrome failed to start: crashed.

ou pode aparecer um erro como este:

> RROR tests/test_CT01_add_products_cart.py::TestCT01::test_CT01_Add_products_cart - selenium.common.exceptions.WebDriverException: Message: unknown > > error: cannot find Chrome binary

para resolver este problema, siga os passos a seguir:

- Verificar se o chromedriver baixado é compativel com a versão do aplicativo google-chrome instalado na maquina.

- Verificar se os binarios do google-chrome são encontrados dentro da pasta **/usr/bin**, se não for encontrado, é recomendavel instalar o google chrome novamente e adiciionar na pasta. Se for instalado pelo repositorio da distribuição, os binarios devem aparecer automaticamente na pasta.
Você pode verificar se o google-chrome esta dentro desta pasta com o seguinte comando no terminal:

    - which google-chrome

- Apos realizar a verificação do google-chrome, deve-se adicionar o chromedriver dentro do diretorio **usr/bin**, no mesmo local que o google-chrome também estará. Para mover o binario do chromedriver ao diretorio, basta usar o comando:

    - sudo mv chromedriver /usr/bin/chromedriver

  Lembrando que o comando deve ser executado no mesmo diretorio que o binario se encontra naquele momento.

- Após adicionar o chromedriver dentro do repositorio **usr/bin**, é necessario alterar as permissões do chromedriver para execução com root. Para fazer estas operações basta seguir estes comandos:
    
    - sudo chown root:root /usr/bin/chromedriver
    - sudo chmod +x /usr/bin/chromedriver

- Após executar estes comandos para verificar se tudo ocorreu de forma correta, você pode executar este comando no terminal:

    - ls -l /usr/local/bin/chromedriver
  
  Este comando apresentará no terminal as permissões que o binario do chromedriver possuir, de acordo como foi feito nos passos anteriores.

Feito estes passos, o erro que estava sendo apresentado possivelmente foi solucionados e os testes podem ser executados com sucesso.

## Considerações

- Este projeto foi realizado com intuito de estudo sober a linguagem Python, e as tecnologias de automação de testes.
- O projeto pode receber atualizações de acordo com novos módulos que podem ser lançados no curso referente a este projeto.
