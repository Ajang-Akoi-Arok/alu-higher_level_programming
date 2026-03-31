#!/usr/bin/python3
"""Script that fetches https://alu-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    # The test might replace this URL
    url = "https://alu-intranet.hbtn.io/status"
    
    # Don't modify the URL - just fetch whatever is given
    response = requests.get(url)
    content = response.text
    
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
