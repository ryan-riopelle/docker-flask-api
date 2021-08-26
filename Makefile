REPO_NAME=$(notdir $(shell pwd))
IMAGE_NAME=$(REPO_NAME)
CONTAINER_NAME=$(REPO_NAME)

stopdevenv:
	docker-compose -f docker-compose.yml down --remove-orphans

startdevenv: stopdevenv
	docker-compose -f docker-compose.yml up -d --build

docker-build: docker-clean
	docker build --force-rm -t "${IMAGE_NAME}:latest" .

docker-clean:
	docker rmi --force "${IMAGE_NAME}:latest"

run-bash:
	docker exec -it ${CONTAINER_NAME} bash