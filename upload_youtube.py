import os
import json
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

def upload():
    credentials = Credentials.from_authorized_user_info(json.loads(os.environ['GOOGLE_CREDENTIALS_JSON']))
    youtube = build("youtube", "v3", credentials=credentials)

    request_body = {
        "snippet": {
            "title": "فيديو تم إنشاؤه تلقائيًا",
            "description": "تم إنشاؤه ونشره تلقائيًا باستخدام GitHub Actions",
            "tags": ["ذكاء اصطناعي", "يوتيوب", "تلقائي"]
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media = MediaFileUpload("video_content/output.mp4")
    response = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    ).execute()

    print(f"تم رفع الفيديو: https://youtu.be/{response['id']}")

if __name__ == "__main__":
    upload()