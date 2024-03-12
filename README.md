## Como funciona?

#### O objetivo deste projeto de Engenharia de Dados é extrair dados da API pública do Pokemon e, após isso, realizar tratamentos e transformações para que o dado fique pronto para consumo. Desta forma, temos um processo de ETL descrito da seguinte forma:

1. Extração: Os dados são retirados da API pública do Pokémon, onde 20 registros por página são obtidos a cada solicitação. Esses registros são armazenados temporariamente em arquivos JSON na camada "transient". O processo de extração continua até que todos os registros disponíveis na API sejam obtidos.

2. Transformação: Nesta etapa, os arquivos JSON contendo os dados extraídos são combinados em um único arquivo e armazenados na camada "raw". Em seguida, os arquivos na camada "transient" são removidos, já que não são mais necessários.

3. Carregamento: O arquivo JSON consolidado é convertido em um formato de arquivo CSV e salvo na camada "trusted". Agora os dados estão em formato tabular, pronto para análise e geração de insights.

4. Próximos passos: Criar a camada "refined", onde serão conduzidas análises detalhadas e previsões utilizando técnicas de Machine Learning. Isso permitirá descobrir insights mais profundos e fazer previsões com base nos dados..

## Pré-requisitos

### - VS Code: É o editor de código que vamos utilizar para desenvolver o nosso projeto de dados. Faça download do VS Code aqui: https://code.visualstudio.com/download

### - Git e GitHub:

Você deve ter o Git instalado em sua máquina.
Você também deve ter uma conta no GitHub. [Instruções de criação de conta no GitHub aqui] (https://docs.github.com/pt/get-started/onboarding/getting-started-with-your-github-account).

### - Pyenv: É usado para gerenciar versões do Python. Instruções de instalação do Pyenv aqui. Vamos usar nesse projeto o Python 3.11.3.

### - Poetry: Este projeto utiliza Poetry para gerenciamento de dependências. Instruções de instalação do Poetry aqui.

## Instalação e configuração

  1. ## Clone o repositório:
     https://github.com/davypedro/poke-api-etl.git

  2. ## Configure a versão do Python com pyenv:
     - pyenv local 3.11.3
    
  3. ## Configurar poetry para Python version 3.11.5 e ative o ambiente virtual:
     - poetry env use 3.11.3
     - poetry shell

  4. ## Instale as dependencias do projeto:
     - poetry install

  Qualquer dúvida, sinta-se à vontade para me procurar:

  E-mail: davypedro7@gmail.com \
  Linkedin: https://www.linkedin.com/in/dpedromoura/
      
      
  
