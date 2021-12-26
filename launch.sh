#!/bin/sh
echo "======= Initilazing ======="
export PYTHONPATH="${PYTHONPATH}:${PWD}/app"

echo "======= Requirements ======="
pip install -r requirements.txt

echo "======= Docker ======="
cd docker/mongodb

OUTPUT=$(docker-compose ps | awk 'NR==3 {print $4}')

if [ "$OUTPUT" != "Up" ]; then
	docker-compose up -d
fi
echo "---------------------------------------------------------------------------------------------"
docker-compose ps
echo "---------------------------------------------------------------------------------------------"
cd ../../
echo "======= Launching ======="
python ./app/__init__.py


echo "exit 0"
