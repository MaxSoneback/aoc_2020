import requests
import sys
import os
from bs4 import BeautifulSoup as bs
from cred import SESSION_ID

base_url = "https://adventofcode.com/2020/day"
script_dir = os.path.dirname(__file__)

cookies = {
        'session': SESSION_ID
        }


def read_from_file(dir_calling: str) -> str:
    with open(f'{os.path.join(script_dir, dir_calling)}\\input.txt',
              'r') as f:
        return f.read()


def read_from_api(day_nr: int) -> str:
    res = requests.get(
                        url=f"{base_url}/{day_nr}/input",
                        cookies=cookies
                    )
    return res.content.decode('UTF-8')


def import_data(day_nr: int, rel_file: str, to_list = False) -> str:
    dir_calling = os.path.dirname(rel_file)
    try:
        data = read_from_file(dir_calling)
        print("Loaded data from local cache")

    except FileNotFoundError:
        print("Local file not found, fetching and caching")
        data = read_from_api(day_nr)
        with open(f"{os.path.join(script_dir, dir_calling)}\\input.txt",
                  "w+") as f:
            f.write(data)

    if to_list:
        data = [x for x in data.split('\n') if x != ""]
    return data


def submit(day_nr: int, part: int, ans: str) -> (str, int):
    data = {
        'level': part,
        'answer': ans
    }
    res = requests.post(
                        url=f"{base_url}/{day_nr}/answer",
                        data=data,
                        cookies=cookies
                        )
    soup = bs(res.content, 'html.parser')
    info = soup.find("main").find("article").find("p")
    return info.text, res.status_code

