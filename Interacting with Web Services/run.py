#! /usr/bin/env python3

import os
import requests

# List all file
file_list = os.listdir('/data/feedback')

for file in file_list:
        file_path = os.path.join('/data/feedback', file)
        with open(file_path) as feed:
                read_feed = feed.read()
                read_feed = read_feed.splitlines()
                feedback = {'title': read_feed[0], 'name': read_feed[1],
                            'date': read_feed[2], 'feedback': read_feed[3]}
        send_feedback = requests.post('http://104.154.72.121/feedback/', json = feedback)
        print(send_feedback.status_code)