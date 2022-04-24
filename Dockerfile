# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 

RUN pip install SpeechRecognition pydub \ pip install fastapi \ pip install "uvicorn[standard]" \ pip install python-multipart

# 
COPY . /code

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
