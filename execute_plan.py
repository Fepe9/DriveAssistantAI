import json
import pickle

from googleapiclient.discovery import build


def normalize_path(path):

    path = path.replace(
        "4DS - Anno scolastico 2025-26",
        "4DS"
    )

    path = path.replace(
        "3DS - Anno scolastico 2024-25",
        "3DS"
    )

    path = path.replace(
        "2DS - Anno scolastico 2023-24",
        "2DS"
    )

    path = path.replace(
        "1DS - Anno scolastico 2022-23",
        "1DS"
    )

    path = path.replace(" / ", "/")

    return path.strip()


def create_folder(service, name, parent_id):

    metadata = {
        "name": name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_id]
    }

    folder = service.files().create(
        body=metadata,
        fields="id,name"
    ).execute()

    return folder["id"]


# LOGIN

with open("token.pickle", "rb") as token:
    creds = pickle.load(token)

service = build("drive", "v3", credentials=creds)

# CARICA FILE

with open("plan.json", "r", encoding="utf-8") as f:
    plan = json.load(f)

with open("folders.json", "r", encoding="utf-8") as f:
    folders = json.load(f)

ROOTS = {
    "1DS": "1J1-qbvPC_kwQ1qN9YNo5RgT2toP0k4Xm",
    "2DS": "1h8WWTFmXxadzKi3y0cLAZIX511VkOX2z",
    "3DS": "1L81y8VvivclmKR0FHl3Mx7HvCFEI80oi",
    "4DS": "1PZtO68xtIjF28lmB46m85cemrnE60PBy",
    "Tirocinio & Bootcamp": "1oEsM03jNhLCX85DG3IgK7iW29N-cQBem"
}

files = plan["file"]

print("\n=== FILE PROPOSTI ===\n")

for i, file in enumerate(files, start=1):

    dest = normalize_path(file["destinazione"])

    print(f"{i}. {file['nome']}")
    print(f"   → {dest}")
    print(f"   Confidenza: {file['confidenza']}%")
    print()

print("Inserisci i numeri da spostare.")
print("Esempio: 1 2 5")
print()

selection = input("> ")

selected = []

for x in selection.split():

    try:
        selected.append(int(x))
    except:
        pass

print("\n=== ESECUZIONE ===\n")

for idx in selected:

    try:

        file = files[idx - 1]

        file_id = file["id"]

        destination = normalize_path(
            file["destinazione"]
        )

        # CREA CARTELLE MANCANTI

        if destination not in folders:

            print()
            print("Cartella non trovata:")
            print(destination)
            print()

            create = input("Crearla? (s/n) ").lower()

            if create != "s":

                print("Saltato.")
                continue

            parts = destination.split("/")

            current_path = parts[0]

            if current_path not in ROOTS:

                print("Root sconosciuta.")
                continue

            current_id = ROOTS[current_path]

            for part in parts[1:]:

                next_path = current_path + "/" + part

                if next_path not in folders:

                    new_id = create_folder(
                        service,
                        part,
                        current_id
                    )

                    folders[next_path] = new_id

                    print(
                        f"Creata cartella: {next_path}"
                    )

                current_id = folders[next_path]
                current_path = next_path

            with open(
                "folders.json",
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    folders,
                    f,
                    indent=2,
                    ensure_ascii=False
                )

        folder_id = folders[destination]

        metadata = service.files().get(
            fileId=file_id,
            fields="parents,name"
        ).execute()

        previous_parents = ",".join(
            metadata["parents"]
        )

        service.files().update(
            fileId=file_id,
            addParents=folder_id,
            removeParents=previous_parents,
            fields="id,parents"
        ).execute()

        print(f"✓ Spostato: {file['nome']}")

    except Exception as e:

        print(f"✗ Errore su {idx}")
        print(e)

print("\nFine.")