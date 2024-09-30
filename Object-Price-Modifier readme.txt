How It Works:
itemId: This is the ID of the soul gem or other item that you want to modify. You should replace "your_soulgem_id" with the actual ID of the item.
newPrice: The new price you want to assign to the item.
onGameStart: This function checks whether the item exists and then updates its base value (cost) when the game starts.
Steps to Use:
Save the script in a .lua file (e.g., soulgem_price_modifier.lua).
Place the Lua script in the correct directory for Lua scripts in OpenMW or MWSE (usually in Data Files/MWSE/mods/ for Morrowind or the relevant Lua directory for OpenMW).
Start the game, and the cost of the item will be modified at game initialization.