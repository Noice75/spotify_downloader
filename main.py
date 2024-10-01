import requests
import json
import re
import threading
import time

animation = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]

notcomplete = True

def show_animation():
    global notcomplete
    i = 0
    while notcomplete:
        print(animation[i % len(animation)], end='\r')
        time.sleep(.1)
        i += 1

def download_mp3(mp3_url, data):
    global notcomplete
    try:
        notcomplete = True
        threading.Thread(target=show_animation).start()
        response = requests.get(mp3_url, stream=True)
        if response.status_code == 200:
            with open(f"{data['metadata']['title']+data['metadata'] ['artists']}.mp3", 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            notcomplete = False
            print(f"{data['metadata']['title']} by {data['metadata']['artists']} downloaded successfully.")
        else:
            print(f'Failed to download MP3: {response.status_code}')
    except Exception as e:
        print(f'Error downloading MP3: {e}')

def extract_track_id(spotify_url):
    if('https://open.spotify.com/track/' not in spotify_url):
        print("Invalid url\nInput a url which has track in the url")
        return None
    match = re.search(r'open\.spotify\.com/track/([a-zA-Z0-9]+)', spotify_url)
    if match:
        return match.group(1)
    else:
        return None

def fetch_and_save_content(spotify_url):
    global notcomplete
    print("Starting")
    track_id = extract_track_id(spotify_url)
    if(track_id == None):
        return
    notcomplete = True
    threading.Thread(target=show_animation).start()
    url = f'https://api.spotifydown.com/download/{track_id}'

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'en-US,en;q=0.6',
        'Origin': 'https://spotifydown.com',
        'Priority': 'u=1, i',
        'Referer': 'https://spotifydown.com/',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Gpc': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    }

    try:
        response = requests.get(url, headers=headers)
        notcomplete = False
        print(f'Status Code: {response.status_code}')
        content_type = response.headers.get('Content-Type', '')
        print(f'Content Type: {content_type}')

        if response.status_code == 200:
            if 'application/json' in content_type:
                try:
                    decoded_content = response.content.decode('utf-8')
                    data = json.loads(decoded_content)
                    print(f'Response JSON Data: {data}')
                    
                    download_mp3(data["link"], data)
                except Exception as e:
                    print(f'Error decoding JSON: {e}')
                    print(f'Raw response content (bytes): {response.content}')
            else:
                print(f'Unexpected content type: {content_type}')
                print(f'Raw response content (bytes): {response.content}')
        else:
            print(f'Request failed with status code {response.status_code}')
            print(f'Response content (bytes): {response.content}')
    
    except Exception as e:
        print(f'Request failed: {e}')

while True:
    spotify_url = input("Enter track url = ")
    fetch_and_save_content(spotify_url)
    kill = input("\nDo you want to download more songs (yes/no) = ")
    if(kill.lower() == "no"):
        break
    else:
        continue