from googleapiclient.discovery import build
import pickle

# Login
with open("token.pickle", "rb") as token:
    creds = pickle.load(token)

service = build("drive", "v3", credentials=creds)

# File nella root
results = service.files().list(
    q="'root' in parents and trashed=false",
    pageSize=1000,
    fields="files(id,name,mimeType)"
).execute()

files = results.get("files", [])

# Salva report
with open("drive_report.txt", "w", encoding="utf-8") as f:

    f.write("=== FILE NELLA ROOT ===\n\n")

    for file in files:
        f.write(f"Nome: {file['name']}\n")
        f.write(f"ID: {file['id']}\n")
        f.write(f"Tipo: {file['mimeType']}\n")
        f.write("\n")

print(f"\nCreato drive_report.txt con {len(files)} elementi")