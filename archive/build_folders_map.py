from googleapiclient.discovery import build
import pickle
import json

# ID cartella 4DS
ROOT_FOLDER_ID = "1PZtO68xtIjF28lmB46m85cemrnE60PBy"

with open("token.pickle", "rb") as token:
    creds = pickle.load(token)

service = build("drive", "v3", credentials=creds)

folders_map = {}

def scan_folder(folder_id, current_path):
    results = service.files().list(
        q=f"'{folder_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false",
        fields="files(id,name)"
    ).execute()

    folders = results.get("files", [])

    for folder in folders:

        name = folder["name"]
        folder_id = folder["id"]

        path = f"{current_path}/{name}"

        folders_map[path] = folder_id

        print(path)

        scan_folder(folder_id, path)

scan_folder(ROOT_FOLDER_ID, "4DS")

with open("folders.json", "w", encoding="utf-8") as f:
    json.dump(folders_map, f, indent=2, ensure_ascii=False)

print("\nCreato folders.json")
print(f"Cartelle trovate: {len(folders_map)}")