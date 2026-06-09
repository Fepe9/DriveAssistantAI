from googleapiclient.discovery import build
import pickle

FILE_ID = "1QtS6MYV77ZiiIIeLR7ts8TFtm_oSWa7hoc2gkCfxZRA"

with open("token.pickle", "rb") as token:
    creds = pickle.load(token)

service = build("drive", "v3", credentials=creds)

file = service.files().get(
    fileId=FILE_ID,
    fields="id,name,parents"
).execute()

print("\n=== FILE ===\n")
print("Nome:", file["name"])
print("Parents:", file.get("parents"))