CONTAINER_ID=$(docker ps --filter name=haeahn_drf_be -q)
docker stop $CONTAINER_ID
docker rm $CONTAINER_ID
docker rmi haeahn_drf_be-web
docker-compose up -d --build
