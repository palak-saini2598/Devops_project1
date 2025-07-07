FROM redhat/ubi8

RUN yum install python3 -y

RUN pip3 install flask

COPY devops.py /devops.py

CMD ["python3", "/devops.py"]
