import json
import os
import glob

def merge_json_files():
    all_data = []
    files = glob.glob("*.json")
    files_to_ignore = ["AllSpain.json"]
    
    for file in files:
        if file in files_to_ignore:
            continue
        
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    all_data.extend(data)
                elif isinstance(data, dict):
                    all_data.append(data)
        except Exception as e:
            print(f"Error reading {file}: {e}")

    seen = set()
    unique_data = []
    for entry in all_data:
        name = entry.get("name")
        province = entry.get("province")
        identifier = (name, province)
        
        if identifier not in seen:
            seen.add(identifier)
            unique_data.append(entry)

    unique_data.sort(key=lambda x: (x.get("region", ""), x.get("province", ""), x.get("name", "")))

    with open("AllSpain.json", "w", encoding="utf-8") as f:
        json.dump(unique_data, f, indent=2, ensure_ascii=False)
    
    print(f"Merged {len(unique_data)} unique campsites into AllSpain.json")

if __name__ == "__main__":
    merge_json_files()
