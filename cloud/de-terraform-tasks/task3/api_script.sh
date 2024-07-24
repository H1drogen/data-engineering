#!/bin/bash

sudo yum install -y git
git config --global user.name =
git clone https://github.com/northcoders/de-sample-server.git
sudo apt install python3

fastapi run  ./src/api/app.py