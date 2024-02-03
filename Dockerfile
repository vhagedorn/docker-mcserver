FROM eclipse-temurin:17

ARG server_jar

COPY server/ /server
COPY $server_jar /server/server.jar
WORKDIR /server
RUN chmod 777 *

CMD ["java", "-jar", "server.jar", "nogui"]
