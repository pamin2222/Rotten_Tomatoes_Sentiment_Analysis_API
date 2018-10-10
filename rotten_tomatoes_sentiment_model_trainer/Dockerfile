
FROM tensorflow/tensorflow:1.10.0-gpu-py3

ENV LANG C.UTF-8

WORKDIR /usr/src/pkgs
ADD . /usr/src/pkgs

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y wget
RUN apt-get install -y libgtk2.0-0
RUN apt-get install -y libicu-dev
RUN apt-get install -y git

#python 3.6
RUN apt install -y build-essential checkinstall libreadline-gplv2-dev \
	libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev \
	libbz2-dev openssl

RUN mkdir -p $HOME/opt
RUN cd $HOME/opt
RUN curl -O https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
RUN tar -xzf Python-3.6.5.tgz
RUN cd Python-3.6.5/ && ./configure && make && make install


#py3 as default
RUN echo "alias python=python3 \n" > ~/.bashrc
RUN echo "alias pip=pip3" >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"
RUN rm /usr/bin/python
RUN ln -s /usr/bin/python3.6 /usr/bin/python

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apt install -y libsm6 libxext6
RUN pip3 install -U spacy
RUN python3.6 -m spacy download en


RUN cd /.

CMD /bin/bash
