# Usa uma imagem oficial do Python
FROM python:3.10-slim

# Define a pasta de trabalho dentro do servidor
WORKDIR /app

# Copia o arquivo de bibliotecas primeiro para ganhar velocidade
COPY requirements.txt .

# Instala as dependências (Python, FastAPI, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do seu código do backend para o servidor
COPY . .

# Comando para iniciar o seu backend (ajuste se seu arquivo principal for outro)
CMD ["python", "main.py"]