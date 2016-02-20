#!/usr/bin/env python3
import requests
import os
import argparse
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'My User Agent 1.0',
}

def check_website(link, interval, id_to_check, file_name, verbose):

    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, file_name)


    while True:
        #create file if doesn't exist
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                if verbose:
                    print("Memory file created")

        try:
            if verbose:
                print("Making request...")
            r = requests.get(link, headers=headers)
        except:
            if verbose:
                print("No internet connection...")

        if r.status_code == 200:
            new_data = BeautifulSoup(r.text, 'html.parser')
            if id_to_check:
                new_data = new_data.find(id=id_to_check)
            new_data = str(new_data)
            with open(filepath, 'r+') as file:
                file_data = file.read()
                #if something changed since the last check
                if new_data != file_data:
                    file.seek(0)
                    file.truncate()
                    file.write(new_data)
                    os.system("zenity --info --text='Something has changed at {}'".format(link))
        else:
            if verbose:
                print("hmm response status is" + str(r.status_code))
        
        time.sleep(interval)
        


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Checks if the page has changed since the last check')
    parser.add_argument('-l', '--link', help="URL to your web page", required=True)
    parser.add_argument('-t', '--time', type=int, help="Time interval between checks (seconds)", default=60)
    parser.add_argument('-d', '--id', help="id of interesing web part. Entire website by default")
    parser.add_argument('-v', '--verbose', type=bool, help="output stuff", choices=[False,True], default=False)
    parser.add_argument('-f', '--file', help="name of file. Default: last_visit.txt")
    args = parser.parse_args()

    if args.time < 0:
        raise argparse.ArgumentTypeError("Interval cannot be negative...")
    

    check_website(args.link, args.time, args.id, args.file or "last_visit.txt", args.verbose)
    

    
