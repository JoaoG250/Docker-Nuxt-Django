FROM python:3.8

ARG WORKDIR=/usr/src/nuxtdjango-api/

# Criando diretório de trabalho
WORKDIR ${WORKDIR}
COPY ./api/ ./

# Instalando dependências do python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
