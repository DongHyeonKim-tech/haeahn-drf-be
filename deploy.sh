git pull
CONTAINER_ID=$(docker ps --filter name=haeahn-drf-be -q)
docker stop $CONTAINER_ID
docker rm $CONTAINER_ID
docker rmi haeahn-drf-be_web
docker-compose up -d --build
