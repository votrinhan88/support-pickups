# support-pickups
**Support for InfamousSabre's Pickups GTA V Mod - v1.70.2**. [See mod at gta5-mods.com](https://www.gta5-mods.com/misc/support-for-infamoussabre-s-pickups)

### Features
Remember InfamousSabre's **[Pickups](https://www.gta5-mods.com/scripts/pickups)** mod? Unfortunately his mod does not support the latest DLC weapons so I tried continuing his work.
+ **Updating 26 DLC weapons** and their bullet speeds up to **GTA V 1.70**.
    <details><summary>Full list of updated weapons</summary>

    + Arena War DLC: Up-n-Atomizer, Unholy Hellbringer, Widowmaker
    + The Diamond Casino Heist DLC: Ceramic Pistol, Navy Revolver, Hazardous Jerry Can
    + The Cayo Perico Heist DLC: Military Rifle, Combat Shotgun, Perico Pistol
    + The Contract DLC: Heavy Rifle, Stun Gun MP, Fertilizer Can, Compact EMP Launcher(*)
    + Criminal Enterprises DLC: Metal Detector, Service Carbine, Precision Rifle
    + Los Santos Drug Wars DLC: WM 29 Pistol, Candy Cane, Coil Railgun, Acid Package
    + San Andreas Mercenaries DLC: Tactical SMG
    + The Chop Shop DLC: Battle Rifle, Hacking Device, Snowball Launcher
    + Bottom Dollar Bounties DLC: The Shocker
    + Agents of Sabotage DLC: El Strickler
    + (*): So I dug deeper and discovered the .ydr texture files of Compact EMP Launcher (w_lr_compactml.ydr & w_lr_compactml_hi.ydr) don't have "Bounds" like other weapons --> I guess it's why its pickup model couldn't be drawn properly. But this is out of my scope.
    </details>
+ **Customized number of slots:** 8 slots and 4 slots
    <details><summary>List of weapon slots</summary>

    + 8 slots (rearranged, based on michelangelo777):
        + 0: Fist
        + 1: Throwable
        + 2: Submachine
        + 3: Rifle/Shotgun
        + 4: Heavy Weapon
        + 5: Sniper Rifle/Machine Gun/Miscellaneous
        + 6: Handgun
        + 7: Melee
    + 4 slots (original of InfamousSabre):
        + 0: Fist
        + 1: (Light) Handgun/Melee
        + 2: (Heavy) Submachine/Assault Rifle/Shotgun/Heavy Weapon/Sniper Rifle/Light Machine Gun/Miscellaneous
        + 3: Throwable
    </details>
+ **Simplified installation and uninstallation.**
+ **Supplementary resources** for custom scripting


### Installation
1. **REQUIRED: [Pickups 2.2](https://www.gta5-mods.com/scripts/pickups)** by InfamousSabre. I only update the new weapons, which WILL NOT WORK WITHOUT HIS MOD (AND BREAK YOUR GAME).
2. Backup your two files: `GTA V/mods/update/update.rpf/common/data/ai/weapons.meta` and `GTA V/mods/update/update.rpf/common/data/pickups.meta`
3. Download Pickups 2.2 by InfamousSabre. **DO NOT INSTALL THROUGH OPENIV BUT EXTRACT AS ARCHIVE.**
4. Move the folder `Pickups` and the files `Pickups.asi`, `Pickups.ini` to GTA V folder
5. **DO NOT INSTALL ANYTHING ELSE FROM PICKUPS.** Now we move on to my update.
6. Extract my **Support for InfamousSabre's Pickups** mod
7. Move the folder `./composed/mod/Pickups` to `GTA V/Pickups`
8. Move everything inside `./weapon-merger/composed/merged/update/update.rpf/dlc_patch` to `GTA V/mods/update/update.rpf/dlc_patch`
9. Move everything inside `./composed/mod/update/update.rpf` to `GTA V/mods/update/update.rpf`
10. Optional 4 slots: move the files `pickups.xml` and `slots.xml` from `./composed/optional-4-slots` to `GTA V/Pickups`.

### Uninstallation
1. Delete `Pickups/`, `Pickups.asi`, `Pickups.ini`
2. Extract `./weapon-merger/weapons-pickups-meta-uninstall-1.70.7z` to current folder (same level as this file).
3. Open the `./weapon-merger/composed/uninstall-content-dlcpatch.yaml` - This is the instruction to handle `content.xml` in each `dlc_patch`
4. Copy everything in `./uninstall/update/update.rpf` to  `GTA V/mods/update/update.rpf`
    + These should have reverted the DLCs under `to-patch` in `./composed/uninstall-content-dlcpatch.yaml`
5. For the remaining DLCs, i.e. under `to-delete` in `./weapon-merger/composed/uninstall-content-dlcpatch.yaml`, you can safely delete the `content.xml` file manually.
    + Originally these files do not exist in the vanilla version


### Changelog
+ 1.70.2 (GTA V v1.69 Bottom Dollar Bounties - 1.70 Agents of Sabotage)
    + Add 2 new DLC weapons
    + Add Python script to merge all weapon-.meta and pickups.meta
    + Add supplementary resources and documents.
    <details><summary>Previous versions</summary>

    + 0.8.alpha (GTA V v1.67 San Andreas Mercenaries - 1.68 The Chop Shop)
        + Add 4 new DLC weapons
    + 0.7.alpha (GTA V v1.66 Los Santos Drug Wars)
        + Add 4 new DLC weapons
        + Fix the position of Micro SMG, Golf Club, Pool Cue, Baseball Bat
    + 0.6.alpha (GTA V v1.61 Criminal Enterprises)
        + Add 3 new DLC weapons
    + 0.5.stable (GTA V v1.58 The Contract)
        + Add 4 new DLC weapons
        + Installation will automatically delete DamageEngine module
        + Uninstallation that only touches necessary files, nothing more or less, will automatically delete Pickups.asi but keep Pickups.ini
    + 0.4 (GTA V v1.57 Los Santos Tuners)
        + Fix Double-action Revolver and Heavy Revolver Mk II do not have ammo
        + Re-organize OIV package
    + 0.3
        + Rework the update.rpf/common/data/ai/weapons.meta from update 1.52. Preserving the properties of delayed hit (See video, sorry for my editting skill :P) from InfamousSabre's old version with updated realistic bullet speed (muzzle velocity), while changing the maximum capacity of ammo (see the XLSX workbook for more details). The damage, recoil & other parameters are preserved from vanilla.
        + Update slots.xml so that weapon positions attached on body are correspondent to the weapon wheel.
    + 0.2
        + Optional: pickups.xml and slots.xml with 4 slots such as InfamousSabre. (as a tribute to his work)
    + 0.1.alpha
        + Change the order of slots in slots.xml
        + Rearrange weapons to its group in pickups.xml (was a mess in michelangelo777's file, I'd prefer this way :) thanks anyway pal)
        + Change ammo type of Minigun so that it could have 600 bullets (originally 180 bullets drain out too fast)
        + Change ammo type of Unholy Hellbringer, Widowmaker to have independent ammo (orginally use same ammo of Combat MG and Minigun)
    </details>

### Credits
+ InfamousSabre for the mod [Pickups 2.2](https://www.gta5-mods.com/scripts/pickups)
+ michelangelo777 for [7 Visible Weapons on Player](https://www.gta5-mods.com/weapons/7-visible-weapons-player)
+ sjaak327 for [Simple Trainer](https://www.gta5-mods.com/scripts/simple-trainer-for-gtav) (used in testing) 
+ [RAGE Multiplayer Wiki](https://wiki.rage.mp/index.php?title=Weapons) and [GTA Wiki](https://gta.fandom.com/wiki/Main_Page) for the weapons icons and references 

### Disclaimer
+ Do not upload elsewhere. Do not used for commercial, financial, or personal gain.
+ Respect the work of former authors as well, as my work is based on theirs.
+ You are free to improve upon mine so long as I and former authors are properly credited and original mod pages are linked.
+ I've also included an XLSX workbook in details of my work. I think it'd might anyhow help someone and the community in general.