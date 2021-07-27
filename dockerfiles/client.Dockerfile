FROM node:14

# Atualizando npm
RUN npm install -g npm@latest

ARG WORKDIR=/usr/src/nuxtdjango-client/

# Criando diretório de trabalho
WORKDIR ${WORKDIR}
COPY ./client/ ./

# Intalando dependências do node
RUN npm install

# Compilando código
RUN npm run build
