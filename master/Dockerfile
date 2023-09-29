FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5001
ENV NAME GameMaster
CMD ["python", "app.py"]
