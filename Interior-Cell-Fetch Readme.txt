Explanation of the Script:
outputFilePath: This variable specifies the path where the .txt file will be saved. You can modify the path to save the file in a different directory.

cityCellMap: This table stores the names of exterior locations (e.g., cities or regions) and their corresponding interior cells.

getExteriorLocation: This function identifies the exterior location associated with an interior cell. It uses the cell’s grid coordinates (gridX and gridY) to find the corresponding exterior cell. If no exterior cell is found, the location is labeled as "Unknown".

collectInteriorCells: This function iterates through all the cells in the game. For each interior cell, it finds the corresponding exterior location and adds the cell name to the list of interior cells for that location.

exportResultsToFile: This function writes the collected interior cells and their associated exterior locations to a .txt file. The format groups interior cells under their respective exterior locations for easy viewing.

onInitialized: This function is triggered when the game initializes. It runs the logic to collect interior cells and export the results to a .txt file.

How to Use:
Save the Script:

Save the script as interior_cells_exporter.lua.
Place the Script:

Place the .lua script in the appropriate directory for OpenMW Lua scripts, such as Data Files/scripts or Data Files/MWSE/mods/yourmod/.
Launch OpenMW:

Start OpenMW or MWSE-enabled Morrowind, and the script will automatically run at game initialization.
Find the Output:

After launching the game, check the Data Files/Mods/ folder for the generated interior_cells_log.txt file. This file will contain a list of all interior cells, grouped by their exterior city/location.
Customization:
You can modify the outputFilePath to change the location where the log file is saved.
The list of cells is currently organized by their exterior location. If you want different sorting or grouping, you can adjust how cells are categorized in the script.