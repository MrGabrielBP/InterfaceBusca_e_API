# API e Interface WEB para busca
Este projeto consiste em um sistema de busca. Ele é composto por dois componentes: um servidor Python que fornece uma API para realizar a busca textual em um arquivo CSV de operadoras de saúde e uma interface web em Vue.js que permite aos usuários pesquisar operadoras e exibir os resultados.

A busca é realiza pelo nome (razão social) da empresa a partir dos dados contidos no CSV. Os resultados encontrados são exibidos na interface WEB da seguinte maneira: `Código ANS | CNPJ | Razão Social`.

## Funcionalidades

O projeto possui as seguintes funcionalidades:

- Interface web intuitiva com uma barra de pesquisa.
- Comunicação com o servidor Python para realizar a busca textual.
- Exibição dos resultados da busca.

## Bibliotecas Utilizadas

### Servidor Python:

- Flask: Um framework web leve para criar aplicativos web em Python.
- Flask-Cors: Uma extensão para o Flask que lida com o erro de CORS (Cross-Origin Resource Sharing) do navegador.
- csv: Módulo nativo do Python para ler arquivos CSV.

### Interface web Vue.js:

- Vue.js: Um framework JavaScript progressivo para a construção de interfaces de usuário.
- HTML e CSS: Linguagens padrão para a estrutura e estilização da interface web.

## Vue.js - Options API

A interface web em Vue.js foi implementada utilizando a Options API. A Options API é uma forma de escrever componentes Vue.js que permite definir as propriedades, métodos, dados reativos e hooks de ciclo de vida do componente em um objeto options dentro do componente.

No código Vue.js deste projeto, o componente utiliza a Options API para definir o estado de dados e os métodos necessários para realizar a busca e exibir os resultados.

### Dados

- `searchQuery`: Armazena o termo de busca inserido pelo usuário.
- `searchResults`: Armazena os resultados da busca.

### Métodos

- `search()`: Realiza a requisição HTTP para o servidor Python com o termo de busca inserido pelo usuário. Os resultados da busca são atribuídos à propriedade `searchResults`.

A Options API oferece uma abordagem simples e direta para definir a estrutura e o comportamento dos componentes Vue.js. No entanto, tenha em mente que o Vue.js também oferece a Composition API, que é uma abordagem mais flexível e poderosa para a criação de componentes. A escolha entre a Options API e a Composition API depende das necessidades e preferências do projeto.

Para obter mais informações sobre a Options API, consulte a [documentação oficial do Vue.js](https://vuejs.org/v2/guide/components.html#Options-API).

## Instalação

Primeiramente clone o repositório:
```bash
git clone https://github.com/MrGabrielBP/InterfaceBusca_e_API.git
```
Siga as instruções abaixo para configurar o ambiente de desenvolvimento:

### Servidor Python:

1. Certifique-se de ter o Python instalado em sua máquina (versão 3.6 ou superior).
2. Instale as dependências:
```bash
pip install flask flask-cors
```
3. Navegue até o diretório do projeto `servidor`.
4. Execute o servidor:
```bash
python server.py
```

O servidor é por padrão executado na porta 5000.

### Interface web Vue.js:

1. Certifique-se de ter o Node.js instalado em sua máquina (versão 14 ou superior).
2. Navegue até o diretório do projeto `frontend\interface-web`.
3. Instale as dependências:
```bash
npm install
```
4. Inicie o servidor:
```bash
npm run dev
```

## Utilização

Após a instalação, você pode acessar a interface web em seu navegador no endereço padrão `http://localhost:5173` (ou outra porta indicada pelo servidor de desenvolvimento do Vue.js). Na página, você encontrará uma barra de pesquisa. Digite o termo de busca desejado e pressione o botão "Pesquisar". Os resultados serão exibidos na parte inferior da página.

O servidor Python estará em execução em segundo plano e lidará com as requisições de busca realizadas pela interface web. Certifique-se de que o servidor esteja em execução antes de usar a interface web.

## Coleção do Postman

Uma coleção do Postman foi incluída neste projeto. A coleção contém uma solicitação pré-configurada para a rota de busca, permitindo que você teste rapidamente a funcionalidade do servidor Flask.

### Importando a coleção no Postman

Para importar a coleção no Postman, siga estas etapas:

1. Abra o aplicativo Postman.
2. Clique no botão "Importar" na barra de navegação superior.
3. Procure pelo arquivo `API Busca.postman_collection.json` que está no repositório.
5. Clique em Abrir.

### Utilizando a coleção

Após importar a coleção no Postman, você verá uma solicitação chamada "Busca" na coleção. Essa solicitação está pré-configurada para fazer uma busca com o termo "caixa". Você pode modificar o valor do parâmetro "termo_busca" para realizar buscas diferentes.

Certifique-se de que o servidor Flask esteja sendo executado localmente na porta padrão (5000) antes de enviar a solicitação.

### Observação

A coleção do Postman é uma ferramenta útil para testar e validar sua API. Ela permite enviar solicitações HTTP e receber as respostas correspondentes. Você pode usar a coleção para verificar se a rota de busca está funcionando corretamente e testar diferentes termos de busca.

## Screenshots

### Interface WEB

![Interface WEB](https://github.com/MrGabrielBP/InterfaceBusca_e_API/blob/main/interface%20web.png)

### Resposta do Servidor

![Código de respota do servidor](https://github.com/MrGabrielBP/InterfaceBusca_e_API/blob/main/servidor.png)

### Network do DevTools

![Aba Network do DevTools](https://github.com/MrGabrielBP/InterfaceBusca_e_API/blob/main/requisi%C3%A7%C3%A3o.png)

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
