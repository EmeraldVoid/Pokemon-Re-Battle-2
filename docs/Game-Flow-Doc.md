<p align="center">
  <img src="https://i.imgur.com/nVPMQZU.png" alt="Pokémon Re:Battle 2 Logo">
</p>

<p align="center">
  A challenging, fan-made Pokémon battle simulator built with PSDK and RPG Maker XP. Featuring Nuzlocke rules, advanced AI, and more intense battles than a traditional Pokémon game.
  <br><br>
  <a href="https://github.com/EmeraldVoid/Pokemon-Re-Battle-2/releases"><strong>Download Latest Release »</strong></a>
  <br><br>
  <a href="https://github.com/EmeraldVoid/Pokemon-Re-Battle-2/issues">Report a Bug</a>
  ·
  <a href="#faq">FAQ</a>
  ·
  <a href="https://pokemon-re-battle-2.vercel.app/">Official Website</a>
</p>

<br>

> [!NOTE]
> This is a living Game Flow Document. As the scope of the game and its development evolves, this document is subject to change.

<br>

| **Document Version:** | 1.0           |
|-----------------------|---------------|
| **Contributors:**     | Emerald_Void, |

<br>

<h1 align="center">Intro Cutscene Event</h1>

**After selecting "Play" from the title screen, the player is presented with the following message:**

<br>

> "Do you wish to skip the intro?"

<br>

> "This is not recommended for your first run."

[*SHOW CHOICE*]: **Yes / No**

---

**If Yes:**

* The intro cutscene is skipped.
* Player selects appearance.
* Player chooses a name.
* Player receives **starting gear** (details currently in development).
* Player is given **\[TBD] Pokémon.**
* Gameplay begins.

**If No:**

* The intro cutscene plays.

* The game explains the core rules:

  * **Nuzlocke Rules:**

    * Fainted Pokémon are permanently removed from the party.
    * Only the first encounter per area may be caught.
    * A full party wipe ends the run.
  * **Battle Rounds System:**

    * Battles are organized into **Rounds**, each consisting of **10 consecutive battles.**
    * During a Round, the player cannot use Pokémon Centers. Only healing items from the bag are allowed.
    * After completing the 10th battle, Pokémon Centers, shops, and other services become available until the next Round begins.

* Following the explanation:

  * Player selects appearance.
  * Player chooses a name.
  * Player receives **starting gear** (details currently in development).
  * Player is given **\[TBD] Pokémon.**
  * Gameplay begins.

---

<br><br>

<h1 align="center">Gameplay Flow</h1>

### Upstairs (Player’s Room)

* The player starts here after completing the intro event.
* **Item:** 1x Super Potion is available in the room.
* **Stairs:** Lead downstairs to the main floor.

### Downstairs (Main Floor)

* **Mom** is seated at the table.

  * Talking to her grants the player an item (item currently undecided).
* **Door:** Leads outside to the town.
* **Stairs:** Lead back upstairs to the player’s room.

### Exterior (Town)

**Map Size:** Undecided

**Key Buildings:**

* **Poké Mart**
* **Pokémon Center**
* **Professor’s Lab**
* **Battle Arena / Battle Tower**

---

**Poké Mart:**

* Standard item shop.
* Multiple vendors planned, potentially offering specialized items.

**Pokémon Center:**

* Used to heal Pokémon.
* **Possible Feature:** Players may be required to **pay a fee** to use healing services (pending design confirmation).

**Professor’s Lab:**

* Provides utility services:

  * **Name Rater**
  * **Move Tutor**
  * **PC access**
  * **Pokémon Seller**
  * **Obtain [Starter](https://github.com/EmeraldVoid/Pokemon-Re-Battle-2/blob/main/docs/Starters.md) (optional)**
* Additional features are planned but not yet finalized.

**Battle Arena / Battle Tower:**

* The central hub for gameplay progression.
* Players build teams, take on increasingly difficult opponents, and continue the battle loop.
* PC access available for managing Pokémon and teams.

