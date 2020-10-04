This repository is for EC 601 Project #2.

phase1a.py
This is a python program which uses the Twitter API in a basic way. It requests tweets with a specific hashtag (in this case, "#Celtics"). Note that if this program is re-run, the date may need to be adjusted. The matching tweets are printed to the terminal and also written to a csv file.

phase1b.py
This is a python program which interacts with the Google Natural Language Processing API in a basic way. It sends two sentences to Google's NLP and prints out the sentiment of each of the sentences individually, as well as the average for the two sentences.

phase2.py
This is a python program which combines usage of the Twitter API and the Google NLP API. It prompts the user for a search string (the hashtag that the user is interested in evaluating). The hashtag is then used with the Twitter API to grab a specified number (default = 100) of tweets that match the specified hashtag. These tweets are saved to a CSV file for later analysis. Then, the Twitter data stored in the CSV file is extracted to build a list of tweets which is passed to the Google NLP API. For each tweet, the sentiment (score and magnitude) is fetched and stored. The average of the sentiment score and magnitude is then printed for the user to consume. Note that a verbose option (-v) is provided if the user would like to have additional information printed as the program is interacting with the APIs.

Usage:

python phase1a.py
python phase1b.py
python phase2.py
python phase2.py -v