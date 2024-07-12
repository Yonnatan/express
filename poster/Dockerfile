FROM python:3.12.4-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY post_generator.py import_and_manage_posts.py ./

RUN python post_generator.py

CMD ["python", "import_and_manage_posts.py"]