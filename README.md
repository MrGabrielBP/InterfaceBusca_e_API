# API e Interface WEB para busca
Este projeto consiste em um sistema de busca. Ele é composto por dois componentes: um servidor Python que fornece uma API para realizar a busca textual em um arquivo CSV de operadoras de saúde e uma interface web em Vue.js que permite aos usuários pesquisar operadoras e exibir os resultados.

A busca é realiza pelo nome (razão social) da empresa a partir dos dados contidos no CSV. Os resultados encontrados são exibidos na interface WEB da seguinte maneira: `código ANS | CNPJ | Razão Social`.

## Funcionalidades

O projeto possui as seguintes funcionalidades:

- Interface web intuitiva com uma barra de pesquisa.
- Comunicação com o servidor Python para realizar a busca textual.
- Exibição dos resultados da busca em tempo real.

## Bibliotecas Utilizadas

### Servidor Python:

- Flask: Um framework web leve para criar aplicativos web em Python.
- Flask-Cors: Uma extensão para o Flask que lida com o erro de CORS (Cross-Origin Resource Sharing) do navegador.
- csv: Módulo nativo do Python para ler arquivos CSV.

### Interface web Vue.js:

- Vue.js: Um framework JavaScript progressivo para a construção de interfaces de usuário.
- HTML e CSS: Linguagens padrão para a estrutura e estilização da interface web.

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

### Interface web Vue.js:

1. Certifique-se de ter o Node.js instalado em sua máquina (versão 14 ou superior).
2. Navegue até o diretório do projeto `frontend`.
3. Instale as dependências: `npm install`
4. Inicie o servidor de desenvolvimento: `npm run serve`

## Utilização

Após a instalação, você pode acessar a interface web em seu navegador no endereço `http://localhost:8080` (ou outra porta indicada pelo servidor de desenvolvimento do Vue.js). Na página, você encontrará uma barra de pesquisa. Digite o termo de busca desejado e pressione o botão "Pesquisar". Os resultados serão exibidos na parte inferior da página.

O servidor Python estará em execução em segundo plano e lidará com as requisições de busca realizadas pela interface web. Certifique-se de que o servidor esteja em execução antes de usar a interface web.

## Screenshots

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
