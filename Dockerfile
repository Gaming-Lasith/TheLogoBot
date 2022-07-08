FROM python:3.9.6

WORKDIR /lasith
COPY . /lasith
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "lasith"]
