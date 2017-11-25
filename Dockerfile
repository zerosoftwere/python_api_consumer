FROM python:3

WORKDIR /usr/src/app
COPY requriements.txt ./
RUN pip install -r requriements.txt

COPY app.py staitc templates ./
CMD ["gunicorn", "-c", "gunicorn.conf.py"]
