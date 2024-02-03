# docker-mcserver
A very simple container for the minecraft server. Base image is temurin 17.

# Building
Clone and build via:
```sh
docker build . -t mcserver:version
```
Optionally, place multiple server jars in the directory `jars/` then run `build.py` to build all of them 
(it expects paper-style naming, e.g. `jars/paper-1.19.4-550.jar`).

# Usage
There are 2 intended ways of using this image:
1) via `docker-compose up -d` and then `docker attach testserver_compose`
2) via an IntelliJ run configuration:
![screenshot](https://imgur.com/a/0Bd2CUk)
