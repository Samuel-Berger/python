FROM fedora:64
RUN dnf install -y python-pip \
    && dnf clean all \
    && pip install fastapi uvicorn aiofiles
WORKDIR /srv
CMD ["uvicorn", "main:app", "--reload"]
