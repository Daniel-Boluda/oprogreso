docker build -t oprogreso -f Dockerfile .
docker tag oprogreso bolferdocker/oprogreso:0.0.8
docker push bolferdocker/oprogreso:0.0.8
