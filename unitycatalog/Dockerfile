FROM alpine:3.20.0

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV TZ=Etc/UTC

RUN apk update && apk upgrade && \
    apk add --no-cache git curl bash tar && \
    git clone https://github.com/unitycatalog/unitycatalog.git

RUN wget --quiet https://cdn.azul.com/public_keys/alpine-signing@azul.com-5d5dc44c.rsa.pub -P /etc/apk/keys/ && \
    apk --repository https://repos.azul.com/zulu/alpine --no-cache add zulu17-jdk~=17.0.11 tzdata

ENV JAVA_HOME=/usr/lib/jvm/zulu17

ENV UNITYCATALOG_HOME="/unitycatalog"
ENV PATH="$PATH:$JAVA_HOME/bin:$UNITYCATALOG_HOME/bin"

WORKDIR /unitycatalog

RUN ./build/sbt -info clean package

EXPOSE 8080

ENTRYPOINT ["start-uc-server"]
CMD ["8080"]
