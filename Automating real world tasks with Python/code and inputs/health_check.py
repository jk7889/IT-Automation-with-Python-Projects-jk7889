#!/usr/bin/env python3
import psutil
import shutil
import socket
import emails


def check_cpu_usage():
    """Function to check if the cpu usage is more than 80%"""
    usage = psutil.cpu_percent(1)
    if usage > 80:
        return True
    else:
        return False


def check_disk_usage():
    """Function to check if disk usage is less than 20%"""
    du = shutil.disk_usage("/")
    free = du.free / du.total * 100
    if free < 20:
        return True
    else:
        return False


def check_memory_usage():
    """Function to check if only 500MB left"""
    mem = psutil.virtual_memory()
    threshold = 500 * 1024 * 1024  # 500MB
    if mem.available < threshold:
        return True
    else:
        return False


def check_host_ip():
    """Function to check if localhost resolves to 127.0.0.1"""
    name = socket.gethostbyname("localhost")
    if str(name) == "127.0.0.1":
        return True
    else:
        return False


def main():
    """Deciding subject of the email (alert) depending on the error and sending the alert"""
    if check_cpu_usage():
        subj = "Error - CPU usage is over 80%"
    if check_disk_usage():
        subj = "Error - Available disk space is less than 20%"
    if check_memory_usage():
        subj = "Error - Available memory is less than 500MB"
    if not check_host_ip():
        subj = "Error - localhost cannot be resolved to 127.0.0.1"

    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_error_report("automation@example.com", "student-jk-8b0ed7c6f@example.com", subj, body)
    emails.send_email(message)


if __name__ == "__main__":
    main()
