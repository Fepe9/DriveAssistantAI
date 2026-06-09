from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/drive"]

flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret_471506589302-pshqq7l4t8dhff5no9map1l8pa06j0g4.apps.googleusercontent.com.json",
    SCOPES
)

creds = flow.run_local_server(port=0)

service = build("drive", "v3", credentials=creds)

results = service.files().list(
    pageSize=10,
    fields="files(id, name)"
).execute()

files = results.get("files", [])

print("\n=== FILE TROVATI ===\n")

for file in files:
    print(f"{file['name']} ({file['id']})")