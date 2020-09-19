# Google-IT-Automation-with-Python

## Final Project Problem Statement

Okay, here's the scenario:

You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:

* Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints.
* Send a report back to the supplier, letting them know what you imported.

Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:

* Run a script on your web server to monitor system health.
* Send an email with an alert if the server is ever unhealthy.

## Scipts

`upload.py`
* Converts images to .jpeg
* Resizes the images
* Uploads the images to designated URL

`reports.py`
* Generates a PDF report for the email

`report_email.py`
* Generates email message with an optional attachment
* Sends the message to the configured SMTP server

`run.py`
* Preprocesses the supplier data
* Uploads the supplier data to designated URL
* Uses reports.py to generate a PDF report for the email
* Uses report_email.py to send the email

`health_check.py`
* Checks cpu_usage, disk_usage, memory_usage and localhost
* Sends an email to the admin if any of the conditions have been violated




