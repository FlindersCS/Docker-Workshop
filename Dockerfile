FROM ubuntu:latest

WORKDIR /app

# Update the package lists
RUN apt-get update

# Install Python and pip
RUN apt-get install -y python3 python3-pip

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV ENV_1="test"
ENV ENV_2="test2"
ENV ENV_3="test3"
ENV ENV_4="test4"

COPY app/* /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask"]
CMD ["run"]
