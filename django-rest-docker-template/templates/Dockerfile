FROM python:3.8.5

# Expose ports
EXPOSE 80 8000

# Disable debian warnings!
ENV DEBIAN_FRONTEND noninteractive

# Set the default directory where CMD will execute
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Requirements.txt alone for caching
ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

ADD . /usr/src/app/

ENTRYPOINT ["/usr/src/app/manage.py"]