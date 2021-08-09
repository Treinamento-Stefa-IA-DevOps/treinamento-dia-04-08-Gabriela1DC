#FROM python:3.8-slim
FROM centos/python-36-centos7        # imagem base

COPY . /app                          # copia tudo dentro do contexto para o diretorio /app dentro do container

WORKDIR /app                         # seta o /app como diretorio base

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]
# comando rodado ao iniciar o container