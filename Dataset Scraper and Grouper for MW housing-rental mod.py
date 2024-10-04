import os
import json

# Define city tiers
city_tiers = {
    "Metropolises (Tier 1)": ["Vivec", "Old Ebonheart", "Necrom"],
    "Cities (Tier 2)": ["Port Telvannis", "Andothren", "Firewatch", "Balmora", "Dragonstar", "Karthwasten", "Stirk"],
    "Small Cities (Tier 3)": ["Akamora", "Almas Thirr", "Sadrith Mora", "Ald'ruhn"],
    "Towns (Tier 4)": ["Caldera", "Khuul", "Gnisis", "Maar Gan", "Molag Mar", "Pelagiad", "Suran", "Helnim",
                       "Llothanis", "Ranyon-ruhn", "Roa Dyr", "Vhul", "Alt Bosara", "Arvud", "Ald Velothi", "Karthgad"],
    "Villages (Tier 5)": ["Dagon Fel", "Vos", "Gnaar Mok", "Hla Oad", "Seyda Neen", "Darvonis", "Dondril", "Sailen",
                          "Aimrah", "Andar Mok", "Bahrammu", "Merduibh", "Bailcnoss", "Haimtir", "Mairager",
                          "Criaglorc"],
    "Outposts (Tier 6)": ["Ahemmusa Camp", "Erabenimsun Camp", "Urshilaku Camp", "Zainab Camp", "Bal Oyra"]
}


def pair_cells_by_city(data):
    paired_cells = {tier: [] for tier in city_tiers.keys()}  # Initialize dict for each city tier

    for entry in data:
        # Ensure the entry is a dictionary
        if isinstance(entry, dict):
            # Check for both 'name' and 'isExterior'
            name = entry.get("name")
            is_exterior = entry.get("isExterior")

            if name is not None and is_exterior is not None:  # Both keys should exist
                cell_name = name.strip()  # Clean up the name
                is_interior = not is_exterior  # Determine if the cell is interior
                matched = False

                # Check for matching city names
                for tier, cities in city_tiers.items():
                    for city in cities:
                        if city.lower() in cell_name.lower():  # Case insensitive check
                            if is_interior:  # Only consider interior cells
                                paired_cells[tier].append(f"{cell_name} ({tier})")
                                matched = True
                                break
                    if matched:
                        break

                # If no match found, classify as Outposts (Tier 6)
                if not matched and is_interior:
                    paired_cells["Outposts (Tier 6)"].append(f"{cell_name} (Outpost)")
            else:
                print(f"Missing 'name' or 'isExterior' in entry: {entry}")  # Log missing fields
        else:
            print(f"Entry is not a dictionary: {type(entry)} - {entry}")  # Log non-dictionary entry

    return paired_cells


def process_json_files(input_folder, output_file):
    all_cells = []

    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(input_folder, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                    # Check if the loaded data is a dictionary or a list
                    if isinstance(data, dict):
                        all_cells.append(data)  # If it's a single dictionary, add it directly
                    elif isinstance(data, list):
                        all_cells.extend(data)  # If it's a list, extend the current list
                    else:
                        print(f"Unexpected data structure in {filename}: {type(data)} - {data}")

            except json.JSONDecodeError as e:
                print(f"Could not decode JSON from {filename}: {e}")
            except Exception as e:
                print(f"Could not read {filename}: {e}")

    filtered_data = pair_cells_by_city(all_cells)

    # Write the output to the text file
    with open(output_file, 'w', encoding='utf-8') as f:
        for tier, entries in filtered_data.items():
            if entries:  # Only write if there are entries for that tier
                f.write(f"{tier}:\n")
                for entry in entries:
                    f.write(f"{entry}\n")
                f.write("\n")  # Blank line between different tiers


# Define input folder and output file
input_folder = r"CellDataBase"  # Update this path
output_file = r"filtered_cities.txt"  # Update this path

# Process the JSON files
process_json_files(input_folder, output_file)
