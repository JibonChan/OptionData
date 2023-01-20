# Option Data Scraper
Crawler to scrape data from NSE for NIFTY (can be changed to any SYMBOL by changing the headers/params)

# How to run
Run the python script option_crawler.py
It will collect and store the results as a json file
Or, Schedule it as per your requirement as shown in the next step

# How to Schedule it to run every 5 seconds
Open crontab and add these two lines
    1. 12 9 * * 1-5 bash option_crawler.sh
    2. 30 15 * * 1-5 ps aux | grep option_crawler.sh | grep -v grep | awk '{print $2}' | xargs kill
First line will run a bash script that runs the python script after every 5 seconds in BG mode every Monday to Friday from 9:12am
Second Line will kill the bash script "option_crawler.sh" on 3.30pm 
