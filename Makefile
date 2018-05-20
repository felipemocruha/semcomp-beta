SHELL:= /bin/bash

env:
	virtualenv -p python3 env

neural_net:
	python neural_net.py

web_app:
	python web_app.py

mongo:
	python mongodb.py

coins:
	python crypto_coins.py
