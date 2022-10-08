Assignment4 
Yonghwan Kim A11746276

This docker image creates Ubuntu-based system environment that uses Python Django and Nginx to host a web server.

This would be helpful to develop a python based backend program that can be hosted by Nginx with easy implementation.

User can expect to see an example index.html page is already hosted by nginx that can interact with Python Django
to deal with data flow when the backend program is implemented.

----------------------------------------------------------------------------------------------------------------------

Link to the Docker Image
https://hub.docker.com/r/kyongh/web-env-docker

Reporsitory Name with Docker Image
kyongh/web-env-docker

Docker Pull command
docker pull kyongh/web-env-docker

----------------------------------------------------------------------------------------------------------------------

Commands used:

Change the local directory into where DockerFile and index.html file is at.
Make sure to have index.html file in the directory.
Example: cd assignment4/docker

Create image file
docker build --tag webenvdocker -f DockerFile.txt .

Create a container and host index.html on local
docker run -it -d -p 8000:80 --name webcontainer webenvdocker

Create a tag Target image the refers to source image
docker tag webenvdocker kyongh/web-env-docker

Push the image to the dockerhub repository
docker push kyongh/web-env-docker