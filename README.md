# Re4J Mod Loader

Hi, this is a beta-phase mod loader made by this 11 year old, J- I mean EthanBipin436-Star (Wow, what a dumb name!).

The mods can be made by using Python. The Re4J Guide will be noted below. An example mod made for testing is included. It will probably fail, because this mod was meant for testing when I was not allowed to game.

The Modding Guide is below:

---

## Quickstart Guide

1. Place your `.py` mod files into the `./mods/` folder.
2. Double-click **`Re4J Prep.bat`** to verify your scripts and set up the build environment.
3. Check the console window for any script errors or status messages.

---

## Folder Layout

```text
Re4J-LCE-Framework/
│
├── mods/                  # Place your custom .py mod scripts here
│   └── sample_portal_gun.py
├── build/                 # Generated source files for engine injection
└── assets/                # Custom textures, icons, and audio files
```
---

##Re4J Modding API Reference
All mod scripts placed in the ./mods/ folder automatically have access to the re4j module.

---

## 1. Registering Custom Items
Registers a new item in the game's registry with a numerical ID and internal name.

Syntax: re4j.register_item(item_id, internal_name)

Parameters:

item_id (int): Unique item ID (e.g., 500+ to avoid vanilla ID collisions).

internal_name (string): Identifier for the item.

Example:

Python Code:
import re4j
# Registering the item

re4j.register_item(500, "portal_gun")

---

## 2. Placing / Modifying Blocks
Places or replaces a block at specified 3D world coordinates.
Syntax: re4j.set_block(x, y, z, block_id)
Parameters:
x (int): World X-coordinate.
y (int): World Y-coordinate (Height, 0–256).
z (int): World Z-coordinate.
block_id (int): Vanilla or custom block ID.

Example:
Python Code:

import re4j

# Place a Diamond Block (ID: 57) at world origin (0, 64, 0)
re4j.set_block(0, 64, 0, 57)

# Place a Stone Block (ID: 1) under player spawn
re4j.set_block(0, 63, 0, 1)

---

### Complete LCE Vanilla Block ID Registry

| Block Name | Block ID |
| :--- | :--- |
| **Air** | `0` |
| **Stone** | `1` |
| **Grass Block** | `2` |
| **Dirt** | `3` |
| **Cobblestone** | `4` |
| **Oak Planks** | `5` |
| **Sapling** | `6` |
| **Bedrock** | `7` |
| **Flowing Water** | `8` |
| **Still Water** | `9` |
| **Flowing Lava** | `10` |
| **Still Lava** | `11` |
| **Sand** | `12` |
| **Gravel** | `13` |
| **Gold Ore** | `14` |
| **Iron Ore** | `15` |
| **Coal Ore** | `16` |
| **Wood / Log** | `17` |
| **Leaves** | `18` |
| **Sponge** | `19` |
| **Glass** | `20` |
| **Lapis Lazuli Ore** | `21` |
| **Lapis Lazuli Block** | `22` |
| **Dispenser** | `23` |
| **Sandstone** | `24` |
| **Note Block** | `25` |
| **Bed Block** | `26` |
| **Powered Rail** | `27` |
| **Detector Rail** | `28` |
| **Sticky Piston** | `29` |
| **Cobweb** | `30` |
| **Tall Grass** | `31` |
| **Dead Bush** | `32` |
| **Piston** | `33` |
| **Piston Head** | `34` |
| **Wool** | `35` |
| **Piston Extension / Moving Block** | `36` |
| **Dandelion / Yellow Flower** | `37` |
| **Poppy / Red Flower** | `38` |
| **Brown Mushroom** | `39` |
| **Red Mushroom** | `40` |
| **Gold Block** | `41` |
| **Iron Block** | `42` |
| **Double Stone Slab** | `43` |
| **Single Stone Slab** | `44` |
| **Bricks** | `45` |
| **TNT** | `46` |
| **Bookshelf** | `47` |
| **Mossy Cobblestone** | `48` |
| **Obsidian** | `49` |
| **Torch** | `50` |
| **Fire** | `51` |
| **Mob Spawner** | `52` |
| **Oak Wood Stairs** | `53` |
| **Chest** | `54` |
| **Redstone Wire** | `55` |
| **Diamond Ore** | `56` |
| **Diamond Block** | `57` |
| **Crafting Table** | `58` |
| **Wheat Crop** | `59` |
| **Farmland** | `60` |
| **Furnace** | `61` |
| **Lit Furnace** | `62` |
| **Standing Sign** | `63` |
| **Oak Door Block** | `64` |
| **Ladder** | `65` |
| **Rail** | `66` |
| **Cobblestone Stairs** | `67` |
| **Wall Sign** | `68` |
| **Lever** | `69` |
| **Stone Pressure Plate** | `70` |
| **Iron Door Block** | `71` |
| **Wooden Pressure Plate** | `72` |
| **Redstone Ore** | `73` |
| **Glowing Redstone Ore** | `74` |
| **Redstone Torch (Unlit)** | `75` |
| **Redstone Torch (Lit)** | `76` |
| **Stone Button** | `77` |
| **Snow Layer** | `78` |
| **Ice** | `79` |
| **Snow Block** | `80` |
| **Cactus** | `81` |
| **Clay Block** | `82` |
| **Sugar Cane Block** | `83` |
| **Jukebox** | `84` |
| **Fence** | `85` |
| **Pumpkin** | `86` |
| **Netherrack** | `87` |
| **Soul Sand** | `88` |
| **Glowstone** | `89` |
| **Nether Portal** | `90` |
| **Jack-o'-Lantern** | `91` |
| **Cake Block** | `92` |
| **Redstone Repeater (Unlit)** | `93` |
| **Redstone Repeater (Lit)** | `94` |
| **Stained Glass (LCE)** | `95` |
| **Trapdoor** | `96` |
| **Monster Egg (Infested Stone)** | `97` |
| **Stone Bricks** | `98` |
| **Huge Brown Mushroom** | `99` |
| **Huge Red Mushroom** | `100` |
| **Iron Bars** | `101` |
| **Glass Pane** | `102` |
| **Melon Block** | `103` |
| **Pumpkin Stem** | `104` |
| **Melon Stem** | `105` |
| **Vines** | `106` |
| **Oak Fence Gate** | `107` |
| **Brick Stairs** | `108` |
| **Stone Brick Stairs** | `109` |
| **Mycelium** | `110` |
| **Lily Pad** | `111` |
| **Nether Brick** | `112` |
| **Nether Brick Fence** | `113` |
| **Nether Brick Stairs** | `114` |
| **Nether Wart** | `115` |
| **Enchanting Table** | `116` |
| **Brewing Stand** | `117` |
| **Cauldron** | `118` |
| **End Portal** | `119` |
| **End Portal Frame** | `120` |
| **End Stone** | `121` |
| **Dragon Egg** | `122` |
| **Redstone Lamp (Unlit)** | `123` |
| **Redstone Lamp (Lit)** | `124` |
| **Double Wooden Slab** | `125` |
| **Single Wooden Slab** | `126` |
| **Cocoa** | `127` |
| **Sandstone Stairs** | `128` |
| **Emerald Ore** | `129` |
| **Ender Chest** | `130` |
| **Tripwire Hook** | `131` |
| **Tripwire Line** | `132` |
| **Emerald Block** | `133` |
| **Spruce Wood Stairs** | `134` |
| **Birch Wood Stairs** | `135` |
| **Jungle Wood Stairs** | `136` |
| **Command Block** | `137` |
| **Beacon** | `138` |
| **Cobblestone Wall** | `139` |
| **Flower Pot** | `140` |
| **Carrot Crop** | `141` |
| **Potato Crop** | `142` |
| **Wooden Button** | `143` |
| **Mob Head / Skull** | `144` |
| **Anvil** | `145` |
| **Trapped Chest** | `146` |
| **Light Weighted Pressure Plate** | `147` |
| **Heavy Weighted Pressure Plate** | `148` |
| **Redstone Comparator (Unlit)** | `149` |
| **Redstone Comparator (Lit)** | `150` |
| **Daylight Detector** | `151` |
| **Redstone Block** | `152` |
| **Nether Quartz Ore** | `153` |
| **Hopper** | `154` |
| **Quartz Block** | `155` |
| **Quartz Stairs** | `156` |
| **Activator Rail** | `157` |
| **Dropper** | `158` |
| **Stained Clay / Terracotta** | `159` |
| **Stained Glass Pane** | `160` |
| **Leaves 2 (Acacia / Dark Oak)** | `161` |
| **Wood 2 (Acacia / Dark Oak Log)**| `162` |
| **Acacia Wood Stairs** | `163` |
| **Dark Oak Wood Stairs** | `164` |
| **Hay Bale** | `170` |
| **Carpet** | `171` |
| **Hardened Clay** | `172` |
| **Coal Block** | `173` |
| **Packed Ice** | `174` |
| **Large Flower (Double Plant)** | `175` |



Complete Example Mod Script (./mods/sample_portal_gun.py)
Python Code:

import re4j

print("[Portal Mod] Registering items and spawning structures...")

# Register custom items
re4j.register_item(500, "portal_gun_blue")
re4j.register_item(501, "portal_gun_orange")

# Spawn a 3x3 platform of diamond blocks at spawn
for x in range(-1, 2):
    for z in range(-1, 2):
        re4j.set_block(x, 63, z, 57)

print("[Portal Mod] Ready!")


---

Do not ask me questions, I have 0 idea of what is going on, because I forgot the research. ( 0 AI used! )

