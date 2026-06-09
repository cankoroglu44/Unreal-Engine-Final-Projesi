# Unreal Engine Final Projesi

A first-person survival/collection game built with **Unreal Engine 5** as a final project. The player must collect items scattered across the level while avoiding an AI-controlled enemy — all within a fully custom Blueprint architecture.

---

## Gameplay Overview

- Navigate a first-person environment and collect all required items
- An AI enemy patrols and chases the player — getting caught triggers a Game Over
- Collect all items to unlock the exit gate and reach the ending
- Full UI flow: HUD → Game Over screen → Restart support

---

## Features

### First-Person Character System
| Blueprint | Description |
|---|---|
| `BP_FirstPersonCharacter` | Core player pawn — movement, camera, input handling |
| `BP_FirstPersonPlayerController` | Input bindings and player controller logic |
| `BP_FirstPersonCameraManager` | Camera FOV and view management |
| `BP_FirstPersonGameMode` | Game rules, win/lose conditions |

Animations are driven by a full **Animation Blueprint** (`ABP_FP_Copy`) with a Control Rig warp (`CtrlRig_FPWarp`) for procedural first-person weapon alignment.

---

### AI Enemy
| Blueprint | Description |
|---|---|
| `BP_Enemy` | AI pawn with patrol and chase behavior |
| `WBP_GameOver` | Game Over widget triggered on player death |

The enemy uses Unreal's built-in AI perception and navigation systems. On detecting the player, it transitions from patrol to active chase. A dedicated **chase sound** (`ChaseSound`) cues the player when the enemy is alerted.

---

### Collectibles & Win Condition
| Blueprint | Description |
|---|---|
| `BP_Item` | Collectible pickup — tracked by game mode |
| `BP_Gate` | Exit gate that unlocks when all items are collected |

Collecting an item plays a feedback sound (`CollectItem`) and updates the HUD counter. Once the item count reaches zero, `BP_Gate` opens and the player can proceed to the ending level.

---

### UI / HUD
| Widget | Description |
|---|---|
| `PlayerHUD` | In-game HUD — displays remaining item count and player state |
| `WBP_GameOver` | Shown on death — includes restart functionality |
| `ENDING` (Widget + Level) | End screen displayed upon successful level completion |

---

## Project Structure

```
Content/
├── Blueprints/
│   ├── AI/             # Enemy BP and Game Over widget
│   ├── Collectibles/   # Item pickup and gate logic
│   └── hud/            # Player HUD and ending screen
├── Characters/
│   └── Mannequins/     # Skeletal meshes, animations, materials
├── FirstPerson/
│   ├── Blueprints/     # Player character, controller, game mode
│   └── Anims/          # Animation blueprint and control rig
├── Input/              # Enhanced Input actions and mappings
├── Levels/
│   ├── DEMO_MAP.umap   # Main gameplay level
│   └── ENDING.umap     # Ending cinematic/screen level
├── Meshes/             # Door and key static meshes
└── Sounds/             # Chase and collect audio cues
```

---

## Technical Details

- **Engine:** Unreal Engine 5
- **Scripting:** 100% Blueprint (no C++)
- **Input System:** Enhanced Input (IMC_Default)
- **Animation:** Animation Blueprint + Control Rig
- **AI:** NavMesh-based movement with Behavior-driven chase logic

---

## How to Run

1. Clone or download the repository
2. Open `Proje.uproject` with Unreal Engine 5
3. Open `Content/Levels/DEMO_MAP.umap`
4. Press **Play** in the editor

> **Note:** `DerivedDataCache/`, `Intermediate/`, and `Saved/` directories are excluded from source control and will be regenerated automatically by the engine on first launch.
