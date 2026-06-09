from googleapiclient.discovery import build
import pickle

with open("token.pickle", "rb") as token:
    creds = pickle.load(token)

service = build("drive", "v3", credentials=creds)

results = service.files().list(
    q="'root' in parents and trashed=false",
    pageSize=100,
    fields="files(id,name,mimeType)"
).execute()

files = results.get("files", [])

print("\n=== FILE NELLA ROOT ===\n")

for f in files:
    print(f"{f['name']} | {f['id']}")