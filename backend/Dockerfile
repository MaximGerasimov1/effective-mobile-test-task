FROM python:3.11-slim
WORKDIR /app
RUN groupadd -r backendgroup && useradd -r -g backendgroup backenduser
COPY app.py .
RUN chown -R backenduser:backendgroup /app
EXPOSE 8080
CMD ["python3","app.py"]
