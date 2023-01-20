#!/bin/bash

while true; do
  python3 option_crawler.py 2>&1 >> /dev/null &
  sleep 5;
done
