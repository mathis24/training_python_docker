
# Start containers

docker network create --driver=bridge --subnet=192.168.0.0/24 --gateway=192.168.0.1 mynet

## mysql

docker run --name mysql -d \
    -p 3306:3306 \
    -e MYSQL_USER=user \
    -e MYSQL_PASSWORD=__puser__ \
    -e MYSQL_ROOT_PASSWORD=__ro0t__ \
    -e MYSQL_DATABASE=data \
    --restart unless-stopped \
    -v vmysql:/var/lib/mysql \
    --net=mynet \
    mysql:8

## grafana
docker run -d \
-p 3000:3000 \
--name=grafana \
-e "GF_SECURITY_ADMIN_USER=admin" \
-e "GF_SECURITY_ADMIN_PASSWORD=__graf__" \
-v vgraf:/var/lib/grafana \
--net=mynet \
grafana/grafana

# Run script

python main.py
# training_python_docker
