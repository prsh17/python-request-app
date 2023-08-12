import requests

def main():
    url = "https://www.google.com"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Content retrieved successfully!")
        # print(response.text)
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
