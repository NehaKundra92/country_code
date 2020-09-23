FROM python:3.8.5-alpine3.12
RUN mkdir /opt/countrycode
ADD code /opt/countrycode
RUN chmod -R 777 /opt/countrycode
RUN pip3.8 install -r  /opt/countrycode/requirment.txt
RUN python3.8 /opt/countrycode/get_data.py
cmd python3.8 /opt/countrycode/lookup.py
