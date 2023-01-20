#!/bin/bash

while true; do
  /usr/bin/python3 /home/jibon/option_crawler.py 2>&1 >> /dev/null &
  sleep 5;
done
