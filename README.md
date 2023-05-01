# Music app
Trata-se de uma API que lida com dados de musicas, artistas e albuns de musica.
Este projeto usa o framework `Flask` do `python` que se comunica com um banco de dados `PostgreSQL` usando o ORM `SQLalchemy`.


## Rodando 
Antes de qualquer coisa certifique-se de que seu ambiente tem os [requisitos necessários](#requisitos). Para executar a aplicação basta rodar o comando a seguir:
```bash
flask --app music_app run
```


## Requisitos
Antes de rodar o projeto, primeiramente faça o seguinte:
1. Certifique-se de que possui o `Python 3.11.2` ou superior instalado na sua máquina.
2. Instale os requisitos rodando o comando:
    ```bash
    pip install -r requirements.txt
    ```
3. Crie o seu banco de dados postgres e faça o restore do dump presente no arquivo `db.out` que está na raiz do projeto.
4. Crie e configure um arquivo .env com as seguintes informações:
    ```env
         DRIVERNAME= //Nome do sgbd escolhido + nome do driver
         USERNAME_DB= // Nome de usuario do banco
         PASSWORD_DB= // Senha do banco
         HOST= // Servidor no qual o banco está hospedado
         PORT= // Porta que o banco está roando
         DATABASE= // Nome do banco de dados 
    ```
## Autores
- [Jhonata Caio](https://github.com/jhonatacaiob)
- [Marcos Beraldo](https://github.com/MarcosBB)
