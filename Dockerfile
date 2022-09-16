FROM python:3.9
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip insatll --no--chace--dir -r requirements.txt
COPY . .
CMD["uvicorn","app.file1:app",":--host","0.0.0.0","--port","8000"]