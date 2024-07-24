FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install openssh-server git openjdk-17-jdk maven redis curl iputils-ping htop -y

WORKDIR /root

COPY . /root/acmeair-mainservice-springboot

WORKDIR /root/acmeair-mainservice-springboot
RUN mvn clean package

EXPOSE 80
CMD ["java", "-jar", "/root/acmeair-mainservice-springboot/target/acmeair-mainservice-springboot-2.1.1-SNAPSHOT.jar"]
