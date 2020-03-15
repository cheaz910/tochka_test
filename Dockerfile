FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRET_KEY b#8!er59a3wkz-gc)8a6)^2zgs0j(l2zpsr#$!+bg0)9@7caii
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/