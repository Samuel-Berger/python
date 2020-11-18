# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
# https://www.vultr.com/docs/how-to-install-and-use-podman-on-ubuntu-20-04#1__Install_Podman
# https://podman.io/getting-started/

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Fedora Magazine!"}
