#this is a Dockerfile for the Docker AWS project. 
FROM nginx
COPY index.html /usr/share/nginx/html
EXPOSE 8081
RUN apt update -y
CMD ["nginx", "-g", "daemon off;"]
