#!/usr/bin/env sh
cd ../valu3s-its
docker-compose down
git reset --hard
docker-compose up -d