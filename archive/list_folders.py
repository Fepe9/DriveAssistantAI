from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import pickle

SCOPES = ["https://www.googleapis.com/auth/drive"]

creds = None

if os.path.exists("token.pickle"):
    with open("token.pickle", "rb") as token:
        creds = pickle.load(token)

if not creds:
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret_471506589302-pshqq7l4t8dhff5no9map1l8pa06j0g4.apps.googleusercontent.com.json",
        SCOPES
    )
    creds = flow.run_local_server(port=0)

    with open("token.pickle", "wb") as token:
        pickle.dump(creds, token)

service = build("drive", "v3", credentials=creds)

results = service.files().list(
    q="mimeType='application/vnd.google-apps.folder'",
    pageSize=100,
    fields="files(id,name)"
).execute()

folders = results.get("files", [])

print("\n=== CARTELLE TROVATE ===\n")

for folder in folders:
    print(f"{folder['name']} ({folder['id']})")