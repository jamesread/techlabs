FROM centos:latest
USER root
MAINTAINER Development Team
ADD src/ /var/www/html/
RUN yum install httpd -y
EXPOSE 80
CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["/usr/sbin/httpd"]

