from httpx import post, put
from pyogg import VorbisFile
from mutagen import File

class lol:
    def __init__(gay, token: str) -> None:
        gay.Token = token
        
    def attachment(gay, channel: int, filePath: str) -> dict:
        try:
            z = post(
                f'https://discord.com/api/v9/channels/{channel}/attachments',
                headers={'Authorization': gay.Token},
                json={
                      "files": [
                        {
                          "filename": "voice-message.ogg",
                          "file_size": VorbisFile(filePath).buffer_length,
                          "id": "6"
                        }
                      ]
                    }
            )
            if z.status_code == 200:
                return z.json()['attachments'][0]
            else:
                exit(z.text)
        except Exception as err:
            exit(err)
    
    def uploadToCloud(gay, upload_url: str, filePath: str) -> bool:
        try:
            with open(filePath, 'rb') as fobj:
                x = put(
                    upload_url,
                    data=fobj.read(),
                    headers={'Content-Type': 'audio/ogg'}
                    )
                if x.status_code == 200:
                    return True
                else:
                    exit(x.text)
        except Exception as err:
            exit(err)
    
    def uploadToDiscord(gay, channel: int, filePath: str) -> tuple:
        try:
            z = a.attachment(channel, filePath)
            n = gay.uploadToCloud(z['upload_url'], filePath)
            if n:
                y = post(
                    f'https://discord.com/api/v9/channels/{channel}/messages',
                    headers={
                        'Authorization': gay.Token,
                        'x-super-properties': 'eyJvcyI6IkFuZHJvaWQiLCJicm93c2VyIjoiRGlzY29yZCBBbmRyb2lkIiwiZGV2aWNlIjoiZHJlYW0ybHRla3MiLCJzeXN0ZW1fbG9jYWxlIjoiZnItRlIiLCJjbGllbnRfdmVyc2lvbiI6IjE3My4yMyAtIHJuIiwicmVsZWFzZV9jaGFubmVsIjoiZ29vZ2xlUmVsZWFzZSIsImRldmljZV92ZW5kb3JfaWQiOiI5M2RjMDRiOS04ODhkLTQ1NjMtYmI0OC1iMzA4NTNhYjNjOWMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiIiLCJicm93c2VyX3ZlcnNpb24iOiIiLCJvc192ZXJzaW9uIjoiMjUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNzMwMjMsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',
                        'user-agent': 'Discord-Android/173023;RNA',
                        'content-type': 'application/json'
                        },
                    json={
                          "content": "",
                          "channel_id": f"{channel}",
                          "type": 0,
                          "flags": 8192,
                          "attachments": [
                            {
                              "id": z['id'],
                              "filename": z['upload_filename'].split('/')[1],
                              "uploaded_filename": z['upload_filename'],
                              "duration_secs": File(filePath).info.length,
                              "waveform": "KBkKDRAKGBIWcnZ+o1xub6GUX6CITm0b"
                            }
                          ]
                        }
                )
                if y.status_code == 200:
                    return True, 'Successfully uploaded audio file !'
                else:
                    return False, y.json()
        except Exception as err:
            exit(err)

a = lol(
    input('Token >')
)

b = a.uploadToDiscord(
    int(input('Channel ID >')),
    input('.ogg audio file path > ') # './audio.ogg'
    )
print(b[1])
