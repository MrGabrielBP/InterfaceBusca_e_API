<template>
  <div class="app">
    <div class="header">
      <img class="logo" src="https://i.imgur.com/jMgmH4I.png" alt="Logo" /> <!-- Logotipo da empresa -->
      <div class="search-bar">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="Digite sua pesquisa"
        />
        <button @click="search">Pesquisar</button> <!-- Botão de pesquisa -->
      </div>
    </div>
    <div class="results">
      <div v-for="result in searchResults" :key="result.id" class="result-item">
        {{ result['Registro ANS'] }} | {{ result['cnpj'] }} |
        {{ result['Razão Social'] }} <!-- Exibe os resultados da busca -->
      </div>
    </div>
  </div>
</template>

<script>
const url = 'http://127.0.0.1:5000/buscar'; // URL do servidor de busca

export default {
  data() {
    return {
      searchQuery: '', // Termo de busca inserido pelo usuário
      searchResults: [], // Resultados da busca
    };
  },
  methods: {
    search() {
      const dados = new URLSearchParams();
      dados.append('termo_busca', this.searchQuery);

      const requestOptions = {
        method: 'POST',
        body: dados,
      };

      //vai fazer uma requisição para o servidor
      fetch(url, requestOptions)
        .then((response) => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error('Erro ao realizar a busca.');
          }
        })
        .then((resultados) => {
          this.searchResults = resultados; // Atualiza os resultados da busca
        })
        .catch((error) => {
          console.log('Erro na requisição:', error.message);
        });
    },
  },
};
</script>

<style>
/* Estilos CSS para a interface web */

.app {
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.logo {
  height: 7em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.search-bar {
  display: flex;
  align-items: center;
}

.search-bar input {
  flex-grow: 1;
  padding: 10px;
  font-size: 16px;
  border-radius: 20px;
  border: 1px solid #9a4df3;
}

.search-bar button {
  margin-left: 10px;
  padding: 10px 20px;
  font-size: 16px;
  background-color: #9a4df3;
  color: #fff;
  border: none;
  border-radius: 20px;
  cursor: pointer;
}
.search-bar button:hover {
  border-color: #9a4df3;
  background-color: #242424;
  color: #9a4df3;
}

.results {
  margin-top: 20px;
}

.result-item {
  padding: 10px;
  font-size: 16px;
  background-color: #fff;
  transition: background-color 0.3s ease;
}

.result-item:hover {
  background-color: #f5f5f5;
}
</style>