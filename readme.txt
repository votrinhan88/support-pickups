Remember InfamousSabre's Pickups mod? !!! NOW COMES WITH UNINSTALLATION OIV !!!

Unfortunately his mod does not support the latest DLC weapons. As far as I know he's busy right now so I tried continuing his work.

FEATURING:
Updating 20 DLC weapons:
+ Arena War DLC: Up-n-Atomizer, Unholy Hellbringer, Widowmaker
+ The Diamond Casino Heist DLC: Ceramic Pistol, Navy Revolver, Hazardous Jerry Can
+ The Cayo Perico Heist DLC: Military Rifle, Combat Shotgun, Perico Pistol
+ The Contract DLC: Heavy Rifle, Stun Gun MP, Fertilizer Can, (*)Compact EMP Launcher
+ Criminal Enterprises DLC: Metal Detector, Service Carbine, Precision Rifle
+ Los Santos Drug Wars DLC: WM 29 Pistol, Candy Cane, Coil Railgun, Acid Package
+ San Andreas Mercenaries DLC: Tactical SMG
+ The Chop Shop DLC: Battle Rifle, Hacking Device, Snowball Launcher
+ Bottom Dollar Bounties DLC: The Shocker
+ Agents of Sabotage DLC: El Strickler

(*): So I dug deeper and discovered the .ydr files of Compact EMP Launcher (w_lr_compactml.ydr & w_lr_compactml_hi.ydr) don't have "Bounds" like other weapons --> I guess it's the reason why its pickup model couldn't be drawn as an individual object. Unless the next dlc_patch is released or someone is generous enough to redo its .ydr, then it is what it is. I don't know how to, but am happy with the current state anyway.

Customized 8 slots (rearranged, based on michelangelo777):
+ 0: Fist
+ 1: Throwable
+ 2: Submachine
+ 3: Assault Rifle/Shotgun
+ 4: Heavy Weapon
+ 5: Sniper Rifle/Light Machine Gun/Miscellaneous
+ 6: Handgun
+ 7: Melee
Or 4 slots (original of InfamousSabre):
+ 0: Fist
+ 1: (Light) Handgun/Melee
+ 2: (Heavy) Submachine/Assault Rifle/Shotgun/Heavy Weapon/Sniper Rifle/Light Machine Gun/Miscellaneous
+ 3: Throwable

Changelog:
1.70.beta (GTA V v1.69 Bottom Dollar Bounties - 1.70 Agents of Sabotage)
+ Add 2 new DLC weapons

0.8.alpha (GTA V v1.67 San Andreas Mercenaries - 1.68 The Chop Shop)
+ Add 4 new DLC weapons

0.7.alpha (GTA V v1.66 Los Santos Drug Wars)
+ Add 4 new DLC weapons
+ Fix the position of Micro SMG, Golf Club, Pool Cue, Baseball Bat

0.6.alpha (GTA V v1.61 Criminal Enterprises)
+ Add 3 new DLC weapons

0.5.stable (GTA V v1.58 The Contract)
+ Add 4 new DLC weapons
+ Installation will automatically delete DamageEngine module
+ Uninstallation that only touches necessary files, nothing more or less, will automatically delete Pickups.asi but keep Pickups.ini

0.4 (GTA V v1.57 Los Santos Tuners)
+ Fix Double-action Revolver and Heavy Revolver Mk II do not have ammo
+ Re-organize OIV package

0.3 
+ Rework the update.rpf/common/data/ai/weapons.meta from update 1.52. Preserving the properties of delayed hit (See video, sorry for my editting skill :P) from InfamousSabre's old version with updated realistic bullet speed (muzzle velocity), while changing the maximum capacity of ammo (see the XLSX workbook for more details). The damage, recoil & other parameters are preserved from vanilla.
+ Update slots.xml so that weapon positions attached on body are correspondent to the weapon wheel.

0.2
+ Optional: pickups.xml and slots.xml with 4 slots such as InfamousSabre. (as a tribute to his work)

0.1.alpha
+ Change the order of slots in slots.xml
+ Rearrange weapons to its group in pickups.xml (was a mess in michelangelo777's file, I'd prefer this way :) thanks anyway pal)
+ Change ammo type of Minigun so that it could have 600 bullets (originally 180 bullets drain out too fast)
+ Change ammo type of Unholy Hellbringer, Widowmaker to have independent ammo (orginally use same ammo of Combat MG and Minigun)

__________________________________________________
0. IMPORTANT
REQUIRED: Pickups 2.2 by InfamousSabre. My work only updates the new DLC weapons by overwriting his mod and WILL NOT WORK WITHOUT HIS MOD (AND BREAK YOUR GAME).

1. INSTALLATION: HAVE CHANGED! PLEASE READ CAREFULLY
+ Backup your two files: ./mods/update/update.rpf/common/data/ai/weapons.meta and ./mods/update/update.rpf/common/data/pickups.meta
+ Download Pickups 2.2 by InfamousSabre but DO NOT INSTALL THROUGH OpenIV
+ Extract Pickups 2.2 as archive
+ Move ONLY the folder Pickups and the files Pickups.asi, Pickups.ini to GTA V folder
+ DO NOT INSTALL ANYTHING ELSE. Now we move on to my update.
+ Extract my Support for InfamousSabre's Pickups
+ Move the folder from ./composed/mod/Pickups to GTA V/Pickups
+ Move ./composed/mod/pickups.meta to ./mods/update/update.rpf/common/data/pickups.meta
+ Move ./composed/mod/weapons.meta to ./mods/update/update.rpf/common/data/ai/weapons.meta
+ Optional 4 slots: move the files pickups.xml and slots.xml from ./composed/optional-4-slots GTA V/Pickups.

2. UNINSTALLATION
+ Delete Pickups/, Pickups.asi, Pickups.ini
+ Recover your previously backed-up: ./mods/update/update.rpf/common/data/ai/weapons.meta and ./mods/update/update.rpf/common/data/pickups.meta

3. CREDITS
InfamousSabre for Pickups https://www.gta5-mods.com/scripts/pickups (I have included his README together)
michelangelo777 for 7 Visible Weapons on Player https://www.gta5-mods.com/weapons/7-visible-weapons-player
sjaak327 for Simple Trainer for GTA V (used in testing) https://www.gta5-mods.com/scripts/simple-trainer-for-gtav
trembacz for diff-checker https://github.com/trembacz/diff-checker
RAGE Multiplayer wiki for the weapons icons and references https://wiki.rage.mp/index.php?title=Weapons
GTA Wiki for references https://gta.fandom.com/wiki/Main_Page

4. DISCLAIMER
Do not upload elsewhere. Do not used for commercial, financial, or personal gain.
You are free to improve upon mine so long as I and former authors are properly credited and original mod pages are linked.
Respect the work of former authors as well, as my work is based on theirs.

5. AUTHOR's FOOTNOTE
This is my first mod (if support update is considered one). But I'm all ears to your feedbacks :D.
I've also included an XLSX workbook in details of my work. I think it'd might anyhow help someone and the community in general.

Known issues/To-dos (if time permits)
- The pickups of Unholy Hellbringer, Widowmaker behaves very strangely: cannot pickup ammo. Changing the ammo type fixes it at the moment, but I'd like an easier solution.
- Some weapons could be more well-positioned at the attaching points.
- The effects for pickups similar to Stryfaar's Immersive Pickups (another great work btw)