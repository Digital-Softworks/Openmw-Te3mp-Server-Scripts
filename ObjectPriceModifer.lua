local itemId = "Object_ID"  -- Replace with the actual item ID
local newPrice = 500  -- Set the new price you want for the item

-- Event triggered when the game starts
local function onGameStart()
    -- Check if the item exists in the game world
    local item = tes3.getObject(itemId)
    if item then
        -- Change the base value (cost) of the item
        item.value = newPrice
        mwse.log("[Object Price Modifier] Updated price of %s to %d", itemId, newPrice)
    else
        mwse.log("[Object Price Modifier] Item with ID '%s' not found.", itemId)
    end
end

-- Register the function to run when the game starts
event.register("initialized", onGameStart)
