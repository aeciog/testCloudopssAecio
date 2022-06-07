# Teste CloudOpss Solution 

<h4 align="center"> 
	🚧  Teste 🚀 incompleto...  🚧
</h4>


### Steps

- [x] Step 1 - Criar um repositório no github para armazenar todos scripts e códigos
- [x] Step 2 - Criar um dockerfile para aplicação python
- [x] Step 3 - Criar um docker-compose para subir o container python para conectar com banco mysql
- [ ] Step 4 - Criar um Dockerfile para aplicação Jenkins com autenticação automatizada
- [ ] Step 5 - Criar um jenkinsfile com stage de build e geração de imagem docker do step 2
- [x] Step 6 - Escrever o read-me detalhando passo-a-passo de como executar os scripts

### Extra
- [ ] 1. Automação para gerar a imagem docker automático
- [ ] 2. Pipeline com steps de build e push


### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
Git, Fask, Python3. 

### 🎲 Rodando o Dockerfile

```bash
#Container Criado para aplicação python3 conectado ao banco de dados Mysql
docker run -d -p 8000:5000 test-cloudopss-dev:1.0

#Executar a imagem mysql
docker exec -ti mysqldb mysql -u root -p

```

### Considerações sobre o teste
Na sua maioria tive uma certa dificuldade, mas com auxilio da documentação conseguir realizar maior parte do teste, no Step 4 e 5 foi minha maior dificuldade até o momento ainda não sabia da exitencia do Jenkins uma ferramenta poderosa de automatização. Fiquei honrado e grato pela porta que aberta, pelas descobertas deste teste.
