from googleapiclient.discovery import build
import pickle

FILE_ID = "1QtS6MYV77ZiiIIeLR7ts8TFtm_oSWa7hoc2gkCfxZRA"

CURRENT_PARENT = "0ADScYzYkPI8bUk9PVA"

NEW_PARENT = "1MtyD_nWAx4Btt82HGy6k_L4jCltDNuGC"

with open("token.pickle", "rb") as token:
    creds = pickle.load(token)

service = build("drive", "v3", credentials=creds)

updated_file = service.files().update(
    fileId=FILE_ID,
    addParents=NEW_PARENT,
    removeParents=CURRENT_PARENT,
    fields="id,name,parents",
    supportsAllDrives=True
).execute()

print("\n=== FILE SPOSTATO ===\n")
print(updated_file)