#!/usr/bin/python3
"""
Script that fetches https://alu-intranet.hbtn.io/status
and displays the response body with formatting.
"""
import requests

def main():
    """
    Fetches the status from alu-intranet.hbtn.io/status
    and prints the response body information.
    """
    url = "https://alu-intranet.hbtn.io/status"
    
    # Send GET request to the URL
    response = requests.get(url)
    
    # Get the response content as text
    content = response.text
    
    # Display the response as required
    print("Body response:")
    print(f"    - type: {type(content)}")
    print(f"    - content: {content}")

if __name__ == "__main__":
    main()
