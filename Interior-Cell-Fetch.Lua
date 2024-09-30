-- File path to save the output log (relative to the OpenMW directory)
local outputFilePath = "Data Files/Mods/interior_cells_log.txt"

-- Table to store cities/locations and their interior cells
local cityCellMap = {}

-- Function to get the name of the city or exterior location for an interior cell
local function getExteriorLocation(cell)
    -- If the cell is an interior, check if it has an exterior counterpart
    local closestExterior = cell.gridX and cell.gridY and tes3.getExterior(cell.gridX, cell.gridY)
    if closestExterior then
        return closestExterior.id -- Return the name of the exterior cell (e.g., Balmora, Vivec)
    end
    return "Unknown" -- If no matching exterior is found
end

-- Function to process all interior cells and organize them by exterior location
local function collectInteriorCells()
    for cell in tes3.iterate(tes3.dataHandler.nonDynamicData.cells) do
        -- Only process interior cells (those without a gridX and gridY)
        if cell.isInterior and cell.id ~= "" then
            local exteriorLocation = getExteriorLocation(cell)
            -- If the exterior location doesn't exist in the table, create an entry for it
            if not cityCellMap[exteriorLocation] then
                cityCellMap[exteriorLocation] = {}
            end
            -- Add the interior cell to the list for the exterior location
            table.insert(cityCellMap[exteriorLocation], cell.id)
        end
    end
end

-- Function to export the results to a .txt file
local function exportResultsToFile()
    local file = io.open(outputFilePath, "w")
    if not file then
        mwse.log("[Interior Cell Exporter] Failed to open file for writing: %s", outputFilePath)
        return
    end
    
    file:write("Interior Cells Organized by Exterior Locations:\n\n")

    -- Write each city and its associated interior cells to the file
    for location, interiors in pairs(cityCellMap) do
        file:write("Location: " .. location .. "\n")
        for _, cellName in ipairs(interiors) do
            file:write("  - " .. cellName .. "\n")
        end
        file:write("\n")
    end

    file:close()
    mwse.log("[Interior Cell Exporter] Successfully exported interior cells to: %s", outputFilePath)
end

-- Function to initialize the script
local function onInitialized()
    mwse.log("[Interior Cell Exporter] Script initialized.")
    
    -- Collect all interior cells organized by their exterior locations
    collectInteriorCells()
    
    -- Export the collected data to a .txt file
    exportResultsToFile()
end

-- Register the initialization event
event.register("initialized", onInitialized)
