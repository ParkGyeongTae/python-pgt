FROM python:3.11.2-alpine

RUN pip install --upgrade pip

COPY ./requirements.txt /opt/requirements.txt

RUN pip install -r /opt/requirements.txt && \
    pip freeze > /opt/requirements-result.txt



# RUN apt update && \
#     apt install vim -y && \
#     apt install net-tools -y && \
#     apt install iputils-ping -y

# RUN /usr/local/bin/python -m pip install --upgrade pip

# COPY ./asset/requirements.txt /opt/requirements.txt

# RUN pip install -r /opt/requirements.txt && \
#     pip freeze > /opt/requirements-result.txt
#     # bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)

# RUN mkdir /code && \
#     mkdir /result && \
#     chmod -R 777 /code && \
#     chmod -R 777 /result

# COPY ./code /code
# COPY ./result /result

# WORKDIR /code

ENTRYPOINT bash