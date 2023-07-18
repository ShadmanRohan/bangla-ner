import os
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'w') as f:
        f.write(response.text)

def main():
    os.makedirs('data', exist_ok=True)
    download_file('https://raw.githubusercontent.com/Rifat1493/Bengali-NER/master/Input/all_data.txt', 'data/all_data.txt')
    download_file('https://raw.githubusercontent.com/banglakit/bengali-ner-data/master/main.jsonl', 'data/main.jsonl')

if __name__ == '__main__':
    main()
