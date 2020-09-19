#!/usr/bin/env python3

import os
import json
import locale
import requests
import datetime
from reports import generate_report
from report_email import generate_email
from report_email import send_email



def catalog_data():
    """This function will return a list of dictionaries with all the details like name, weight, description, image filename.
    It will change the weight to integer format and remove any units of weight.
    """
    catalog = []
    # Going through each filename in the directory
    for file in files:
        # Accepting files that has txt extension and ignoring hidden files
        if not file.startswith('.') and 'txt' in file:
            # Creating absolute path for each image
            _path = path + file
            # creating image name from text files and changing the extension to jpeg
            image_path = file.strip('.txt') + '.jpeg'
            # Opening each file
            with open(_path) as content:
                # parsing content and storing it in a list
                data = content.readlines()
                # extracting the first line and removing the newline
                name = data[0].strip('\n')
                # extracting the second line and removing the newline and lbs. Also changing it to integer
                weight = int(data[1].strip('\n').strip(' lbs'))
                # extracting the third line and removing the newline
                description = data[2].strip('\n')
                # creating a dictionary object with required format
                catalog_object = {"name": "{}".format(name), "weight": weight,
                                  "description": "{}".format(description.replace(u'\xa0', u'')),
                                  "image_name": "{}".format(image_path)}
                # Converting dictionary to json
                dict_to_json = json.dumps(catalog_object)
                # Creating headers to push the data to URL
                header = {'Content-Type': 'application/json'}
                # Pushing data to URL
                r = requests.post(url, headers=header, data=dict_to_json)
                # If the status code is not 2xx raise exception
                print(r.reason)
                # Creating a list
                catalog.append(catalog_object)
                # Removing all the none values
                catalog = list(filter(None, catalog))
    return catalog


def summary(catalog_data):
    """Generating a summary with two lists, which gives the output name and weight"""
    # List the names of fruits in catalog list
    res = ['name: ' + sub['name'] for sub in catalog_data]
    # List the weight of fruits in catalog list
    we = ['weight: ' + str(sub['weight']) + ' lbs' for sub in catalog_data]
    # Initializing the object
    new_obj = ""
    # Calling values from two lists one by one
    for name, weight in zip(res, we):
        if name and input_for == 'pdf':
            new_obj += name + '<br />' + weight + '<br />' + '<br />'

    return new_obj


if __name__ == "__main__":
    # Get the username from environment variable
    USER = os.getenv('USER')
    # Set encoding to avoid ascii errors
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    # File path to the data
    path = '/home/{}/supplier-data/descriptions/'.format(USER)
    # Listing all the files in the path
    files = os.listdir(path)
    # Images file path
    image_directory = '/home/{}/supplier-data/images/'.format(USER)
    # Target URL
    url = "http://localhost/fruits/"
    # Creating date
    current_date = datetime.date.today().strftime("%B %d, %Y")
    # PDF main title
    title = 'Processed Update on ' + str(current_date)
    # Subject line
    new_subject = 'Upload Completed - Online Fruit Store'
    # Body data
    new_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    # Creating the pdf report
    generate_report('/tmp/processed.pdf', title, summary(catalog_data()))
    # Creating and sending the email
    msg = generate_email("automation@example.com", "{}@example.com".format(USER),
                         new_subject, new_body, "/tmp/processed.pdf")
    send_email(msg)
