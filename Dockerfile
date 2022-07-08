FROM python:3.9.6

WORKDIR /stdlogo
COPY . /stdlogo
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "stdlogo"]
