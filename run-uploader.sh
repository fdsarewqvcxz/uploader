#!/bin/bash

function docker_compose_build() {
  docker-compose build --pull --no-cache
}

function docker_compose_down() {
  docker-compose down --remove-orphans
}

function docker_compose_up() {
  docker-compose -f docker-compose.yaml up -d
}

function docker_compose_restart() {
  docker-compose -f docker-compose.yaml up -d --build --remove-orphans --force-recreate
}

docker_compose_build
docker_compose_down
docker_compose_up
#docker_compose_restart
docker system prune -f
