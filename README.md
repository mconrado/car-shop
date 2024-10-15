# CAR-SHOP API

Sistema de API de gerenciamento de carro de um distrito.

*Docker, Flask, Pytest, Flask-Migrate


## INSTALAÇÃO
1. Clone o repositório.
2. Copie o arquivo .env-sample, salve como .env e defina as variáveis de ambiente.
3. Execute o comando docker compose.

```console
git clone git@github.com:mconrado/car-shop.git
docker compose up --build -d
```

4. Rode os testes.
```console
docker exec -it -e FLASK_ENV=testing car-shop-web-1 pytest ../tests
```

5. Faça a carga de dados
```console
docker exec -it -e FLASK_ENV=development car-shop-web-1 flask db upgrade
```


### URLs de acesso API:
owner GET http://localhost:5000/owner/id-registrado

owner POST http://localhost:5000/owner

car GET http://localhost:5000/car/id-registrado

car POST http://localhost:5000/car

##### **Ou importe o arquivo postman.json no Postman.*



### TO-DO:
- Cobertura de testes incompleta, falta: ~get owner~, todas as rotas de car, validar a regra de negócio.
- Implementação de regra 3 carros no máximo por proprietário.
- Automatizar quem não tem carro setar sales_o = True.
- Talvez um mock para os testes e simulação de dados.


### ABORDAGEM:
Por se tratar de uma modelagem pequena resolvi não tratar como N x N em alguns casos:
- relação do proprietário com os carros.
- relação dos carros com as propriedades cor e modelo, neste caso tratando como imutaveis.
É válido repensar numa questão de dados maior e sua escalabilidade.
