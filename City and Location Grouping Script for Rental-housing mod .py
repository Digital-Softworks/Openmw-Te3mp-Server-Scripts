import json


def txt_to_json_grouped(txt_file_path, json_file_path):
    """
    Convert a text file with city and location data into a grouped JSON format based on tiers.

    Args:
    - txt_file_path (str): The path to the input text file.
    - json_file_path (str): The path to the output JSON file.
    """
    grouped_data = {}

    try:
        # Open the text file and read its contents
        with open(txt_file_path, 'r') as txt_file:
            for line in txt_file:
                # Strip leading/trailing whitespaces
                line = line.strip()
                if line:
                    # Split the line by the first comma
                    parts = line.split(",", 1)
                    if len(parts) == 2:
                        # Full city and location name (e.g., "Necrom, All Saints' Crematorium")
                        city_and_location = parts[0].strip() + "," + parts[1].split('(')[0].strip()

                        # Extract the tier from the value (e.g., "Tier 1" from "Metropolises (Tier 1)")
                        tier_info = parts[1].split('(')[-1].strip(" ()")  # Extract tier info from parentheses
                        if "Tier" in tier_info:
                            tier = tier_info.split("Tier")[-1].strip()  # Extract the tier number (e.g., "1")
                            tier_key = f"Tier {tier}"  # Format the tier as "Tier X"
                        else:
                            tier_key = "Unknown Tier"

                        # Initialize the list for this tier if it doesn't exist
                        if tier_key not in grouped_data:
                            grouped_data[tier_key] = []

                        # Append the full city and location to the appropriate tier
                        grouped_data[tier_key].append(city_and_location)

        # Write the grouped data to a JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(grouped_data, json_file, indent=4)

        print(f"Conversion successful! Grouped JSON saved to {json_file_path}")

    except Exception as e:
        print(f"Error during conversion: {e}")


# Use raw strings to avoid escape sequence issues
txt_file_path = r"filtered_cities.txt"  # Corrected file path
json_file_path = r"grouped_output.json"  # Corrected file path

# Call the function
txt_to_json_grouped(txt_file_path, json_file_path)
