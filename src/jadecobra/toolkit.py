import datetime
import json
import pathlib
import shutil
import time
import os

def logger(message, level="INFO"):
    print(f"[{level}] {message}")

def error(message):
    logger(message, level="ERROR")

def delete(filepath):
    try:
        os.remove(filepath)
    except FileNotFoundError:
        f"Could not find {filepath}"

def file_exists(filepath):
    return pathlib.Path(filepath).exists()

def make_parent_directory(filepath):
    return os.makedirs(pathlib.Path(filepath).parent, exist_ok=True)

def write_config(filepath=None, parser=None):
    "Write Config Parameters to filepath"
    make_parent_directory(filepath)
    with open(filepath, "w") as configfile:
        parser.write(configfile)

def write_file(filepath=None, data=None):
    "Write Credentials to filepath"
    filepath = filepath.replace('\\', '/')
    make_parent_directory(filepath)
    logger(f"Writing data to {filepath}")
    with open(filepath, "w") as writer:
        writer.write(str(data))

def delimiter():
    print("="*80)

def header(environment):
    delimiter()
    print(f"\t[WARNING] You are making changes to the {environment} Environment [WARNING]")
    delimiter()

def log_performance(message):
    performance = f"{datetime.datetime.now()}:{message}\n"
    logs_path = 'tests/logs'
    os.makedirs(logs_path, exist_ok=True)
    with open(f'{logs_path}/performance.log', 'a') as writer:
        writer.write(performance)
    print(performance)

def time_it(*args, function=None, description='run process', **kwargs):
    start_time = time.time()
    result = function(*args, **kwargs)
    log_performance(f'{description}:{time.time() - start_time:.1f}')
    return result

def to_camel_case(text):
    return ''.join(text.title().split('-'))

def get_commit_message():
    return input("Enter commit message: ")

def read_json(filepath):
    '''Return a dictionary from a json file'''
    with open(f'{filepath}.template.json') as template:
        return json.load(template)

def remove_dist():
    '''Remove Dist folder for new distribution'''
    try:
        shutil.rmtree('dist')
    except FileNotFoundError:
        'already removed'

def git_push():
    for command in (
        f'commit -am "{get_commit_message()}"',
        'pull',
        'push',
    ):
        os.system(f'git {command}')