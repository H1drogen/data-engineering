#!/bin/bash

cd /home/ec2-user || exit
echo 'fldfnsjknfd' > example.txt
sudo yum update
sudo yum install -y httpd
sudo su
echo '<html><h1>hello world</h1></html>' > /var/www/html/index.html
service httpd start
