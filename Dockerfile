FROM python:3.9-slim
RUN apt-get update
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 80
CMD [ "python3","employees.py" ]
