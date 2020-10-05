FROM python:3.8.5-alpine3.12
RUN mkdir /opt/countrycode
ADD code/requirment.txt /opt/countrycode
ADD code/lookup.py /opt/countrycode
ADD code/get_data.py /opt/countrycode
RUN chmod -R 777 /opt/countrycode/
RUN pip3.8 install -r  /opt/countrycode/requirment.txt
cmd python3.8 /opt/countrycode/lookup.py
