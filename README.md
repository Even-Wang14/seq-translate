# seq-translate
This is a DNA/RNA seq translate web tool.
# Software
With docker, flask, Vue, Nginx
# Usage
## Build front-end image 
```
cd ./vue
docker build -t nginx-docker .
```
## Build backend-image
```
cd ./flask
docker build -t flask_trans .
```
## Build docker network
`docker network create –subnet 172.18.0.0/16 –gateway 172.18.0.1 transnetwork`
## Build continers and run server
```
docker run --name flask-trans -p 5000:5000 -d --restart=always --network=transnetwork --ip 172.18.0.3 flask_trans
docker run --name nginx-vue -p 8030:80 -d --restart=always --network=transnetwork --ip 172.18.0.2 nginx-docker
```
> If change flask-trans IP please modify ./vue/nginx.conf  -> proxy_pass   http://your.new.ip.0:5000;

