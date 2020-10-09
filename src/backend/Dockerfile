FROM python:3

RUN python -m pip install --upgrade pip
RUN mkdir /app
WORKDIR /app
EXPOSE 8080
COPY * /app/
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm


CMD ["python", "api.py"]