
FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5000
ENV NAME Player
CMD ["python", "app.py"]
