FROM python:3.11

COPY requirements.txt .

COPY app.py .

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENTRYPOINT ["solara", "run", "app.py", "--host=0.0.0.0", "--port", "80"]
