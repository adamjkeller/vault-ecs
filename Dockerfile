from alpine:latest

ENV CODE_DIR "/opt/vault-unsealer"

RUN mkdir -p ${CODE_DIR}
# Will add all python files, requirements.txt to install pippies, and the keys.yml file to load the keys
ADD ./*.py ./requirements.txt ./keys.yml ${CODE_DIR}/
RUN apk --update add python py-pip &&\
    pip install -r ${CODE_DIR}/requirements.txt
