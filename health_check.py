#!/usr/bin/env python3

import shutil
import psutil
import socket
import os
from report_email import generate_email
from report_email import send_email


def check_cpu_usage(cpu):
    """This function checks if CPU usage is under 80%"""
    return psutil.cpu_percent(cpu) < 80


def check_disk_usage(disk):
    """This function checks if available disk space is more than 20%"""
    du = shutil.disk_usage(disk)
    return du.free / du.total * 100


def check_memory_usage():
    """This function checks if available memory is more than 500MB"""
    memory = dict(psutil.virtual_memory()._asdict())['available']
    available_memory = (memory / 1024) / 1024
    return available_memory > 500


def resolve_hostname():
    """This function will check if localhost cannot be resolved to 127.0.0.1"""
    hostname = socket.gethostbyname('localhost')
    return hostname == '127.0.0.1'


def check_warnings():
    warnings = []
    """This function will return subject according to the conditions set above"""
    if not check_disk_usage('/'):
        warning = 'Error - Available disk space is less than 20%'
        warnings.append(warning)
    if not check_cpu_usage(1):
        warning = 'Error - CPU usage is over 80%'
        warnings.append(warning)
    if not check_memory_usage():
        warning = 'Error - Available memory is less than 500MB'
        warnings.append(warning)
    if not resolve_hostname():
        warning = 'Error - localhost cannot be resolved to 127.0.0.1'
        warnings.append(warning)

    return subjects


if __name__ == "__main__":
    # Get the username from environment variable
    USER = os.getenv('USER')
    # Run the check error function to fetch warnings
    warnings = check_warnings()
    # If we found None as return value do nothing, otherwise send email
    if warnings is not []:
        for warning in warnings:
            # body line give in assignment for email
            new_body = 'Please check your system and resolve the issue as soon as possible.'
            # structuring email and attaching the file. Then sending the email, using the custom module.
            msg = generate_email("automation@example.com", "{}@example.com".format(USER),
                                 warning, new_body, "")
            send_email(msg)
