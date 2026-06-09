from googleapiclient.discovery import build
import pickle

with open("token.pickle", "rb") as token:
    creds = pickle.load(token)

service = build("drive", "v3", credentials=creds)

PARENT_ID = "1WPPMPI4nwSg50urSZZepwLTvRYAGINRJ"

results = service.files().list(
    q=f"'{PARENT_ID}' in parents and mimeType='application/vnd.google-apps.folder'",
    fields="files(id,name)"
).execute()

folders = results.get("files", [])

print("\n=== CONTENUTO 4DS ===\n")

for folder in folders:
    print(folder["name"], "-", folder["id"])