
all:
	make build
	make up

build:
	@docker-compose -f ./docker-compose.yml build

up:
	@docker-compose -f ./docker-compose.yml up

down:
	@docker-compose -f ./docker-compose.yml down

clean:
	@docker-compose -f ./docker-compose.yml down --rmi all --volumes --remove-orphans

re: clean all

.PHONY: all re down clean build up



