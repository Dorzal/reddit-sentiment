FROM python:3

ARG FOLDER

ENV FOLDER "$FOLDER"

WORKDIR /usr/src/app

COPY ${FOLDER}/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "./main.py" ]