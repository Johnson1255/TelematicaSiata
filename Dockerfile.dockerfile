FROM ubuntu
RUN apt update
RUN apt install python3.10 -y
RUN apt install python3-pip -y
WORKDIR /SIATA
COPY pagina.py .
COPY requirementsPagina.txt .
RUN pip3 install -r requirementsPagina.txt
#CMD ["python3.10","pagina.py"]