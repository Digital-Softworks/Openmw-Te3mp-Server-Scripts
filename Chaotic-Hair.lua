local hairList = {
    "b_n_dark_elf_m_hair_01",  -- Replace these with actual hair mesh IDs from Morrowind
    "b_n_dark_elf_m_hair_02",
    "b_n_dark_elf_m_hair_03",
    "b_n_nord_m_hair_01",
    "b_n_redguard_m_hair_01",
    "b_n_breton_f_hair_01"
}

local currentHairIndex = 1
local hairChangeInterval = 5 * 60  -- 5 minutes in seconds

-- Function to change the player's hair
local function changePlayerHair()
    local player = tes3.player
    local newHairMesh = hairList[currentHairIndex]

    -- Get player's current race and gender
    local race = player.object.race
    local gender = player.object.female and "f" or "m"
    
    -- Find the new hair object by ID
    local hair = tes3.getObject(newHairMesh)

    -- Ensure the hair object exists
    if hair then
        -- Change player's hair
        tes3.setPlayerAppearance{hair = hair}
        mwse.log("[Hair Changer] Changed hair to: %s", newHairMesh)
        
        -- Increment hair index, looping back if necessary
        currentHairIndex = currentHairIndex + 1
        if currentHairIndex > #hairList then
            currentHairIndex = 1
        end
    else
        mwse.log("[Hair Changer] Hair with ID '%s' not found.", newHairMesh)
    end
end

-- Function to initialize and start the periodic hair change
local function onInitialized()
    mwse.log("[Hair Changer] Initialized script.")
    
    -- Set up a timer to change hair every 5 minutes
    timer.start{
        duration = hairChangeInterval,
        type = timer.real,
        iterations = -1,  -- Run indefinitely
        callback = changePlayerHair
    }
    
    -- Change hair immediately on startup
    changePlayerHair()
end

-- Register the initialization event
event.register("initialized", onInitialized)

