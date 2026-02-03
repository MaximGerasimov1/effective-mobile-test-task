FROM python:3.11-slim
WORKDIR /app
RUN groupadd -r backendgroup && useradd -r -g backendgroup backenduser
COPY --chown=backenduser:backendgroup app.py .
EXPOSE 8080
USER backenduser
CMD ["python3","app.py"]
