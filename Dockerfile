FROM tiagopeixoto/graph-tool

RUN pacman -S --noconfirm python-pip

RUN pacman -S --noconfirm gcc

RUN pip install networkx

RUN pip install wisardpkg

CMD [ "sh" ]