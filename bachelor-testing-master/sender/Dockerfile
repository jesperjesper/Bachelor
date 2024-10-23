FROM python:latest
RUN apt-get update && apt-get install -y libpcap-dev
COPY . .
RUN pip install --no-cache-dir -r requirements.txt --default-timeout=200
CMD ["python", "test.py"]
