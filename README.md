# trabalho_final_htap

# Instruções para execução

#Preparando ambiente

Para preparar o ambiente tenha o python3 instalado em seu sistema.

Digite o comando abaixo dentro da pasta raiz do projeto:

```
python3 -m venv env
```

Em seguida digite:

```
source env/bin/activate
```

Feito isso agora é possível fazer a instalação de todas as dependências executando o comando:

```
pip install -r requirements.txt

# Preparando o banco de dados

Para subir o banco de dados crie o container com o comando abaixo:

```
docker-compose up
```

# Ingestão de dados:

Este projeto utiliza o cliente mongoDB Studio 3T for MongoDB: https://studio3t.com

Instale o cliente e crie uma conexão padrão para ele, não são necessários dados de senha e usuário.

Feito isso, crie um banco de dados com o nome: crimes_data, em seguida dentro desse banco de dados crie uma collection chamada: crimes.

Para realizar a ingestão dos dados clique com o botão direito encima da collection, escolha a opção import, e em seguida selecione csv.

Isso abrirá uma aba no lado direito. Nessa aba vá na opção 'Import from CSV File'. Em seguida clique em Execute. Pronto, a ingestão de dados será realizada.

# Executando o projeto

Para executar o projeto digite no terminal o seguinte comando:

```

python3 main.py
