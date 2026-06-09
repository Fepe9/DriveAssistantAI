import json

with open("plan.json", "r", encoding="utf-8") as f:
    data = json.load(f)

files = data["file"]

print("\n=== PIANO DI ORGANIZZAZIONE ===\n")

for i, file in enumerate(files, start=1):
    print(f"{i}. {file['nome']}")
    print(f"   Destinazione: {file['destinazione']}")
    print(f"   Confidenza: {file['confidenza']}%")
    print(f"   Motivo: {file['motivazione']}")
    print()