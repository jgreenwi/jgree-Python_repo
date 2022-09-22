#this is a template for my docker container project 
FROM nginx
COPY index.html /usr/share/nginx/html
EXPOSE 8080