from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import pickle

SCOPES = ["https://www.googleapis.com/auth/drive"]

creds = None

if os.path.exists("token.pickle"):
    with open("token.pickle", "rb") as token:
        creds = pickle.load(token)

service = build("drive", "v3", credentials=creds)

results = service.files().list(
    q="'root' in parents and mimeType='application/vnd.google-apps.folder'",
    pageSize=100,
    fields="files(id,name)"
).execute()

folders = results.get("files", [])

print("\n=== CARTELLE NELLA ROOT ===\n")

for folder in folders:
    print(f"{folder['name']} ({folder['id']})")