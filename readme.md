# flask-devops-project
  docker build . -t flaskapp
  docker network create twotier
  
 docker run -d -p 5000:5000 --network=twotier -e MYSQL_HOST=mysql -e MYSQL_USER=admin -e MYSQL_PASSWORD=admin -e MYSQL_DB=myDb --name=flaskapp flaskapp:latest

docker run -d -p 3306:3306 --network=twotier -e MYSQL_DATABASE=myDb -e MYSQL_USER=admin -e MYSQL_PASSWORD=admin -e MYSQL_ROOT_PASSWORD=admin --name=mysql mysql:5.7

 docker network inspect twotier 