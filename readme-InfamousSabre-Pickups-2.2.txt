================================================================================================
Pickups
For: Grand Theft Auto: V
By: InfamousSabre

Version 2.2


Read the License, please.

================================================================================================


Description-------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------

Pickups takes a different approach to GTA V's weapon wheel and weapon pickups.
		

Weapon Wheel -

Before: You have 8 slots where each slot can hold multiple weapons, essentially enabling you to carry an entire armory in your pocket.

After: You have any number of slots you want (Default 4), and each slot only holds 1 weapon at a time.
		

Weapon Pickups - 

Before: All weapon pickups are automatically picked up and each pickup always has full ammo, even if the NPC who dropped it already used some. All weapon pickups have no attachments, even if the previous owner had them equipped.

After: You have the choice of automatically picking up weapons or not. If the slot the weapon belongs to is already full, you will have the choice to swap weapons. If any weapon you are currently holding uses the same ammunition, you have the choice between automatically or manually taking ammo. Weapon pickups only contain whatever ammunition was left in them by their previous owner. Weapon pickups will be equipped with any attachments the previous owner was using. A popup will show over nearby weapon pickups to let you know of their ammo count and type.
		
Some ammunition amounts are adjusted to be more realistic. All weapons acquired by entering certain vehicles are disabled. 
This mod changes many game files. Due to this it is incompatible with a large amount of weapon/realism mods including RDE. If you want to use this mod with any incompatible mod, all you must do is merge the conflicting files. Any reward data MUST reflect Pickups game file data, otherwise Pickups will not work properly. Ammo types can be changed, but beware that all stock ammo types have been removed.
If you merge files to make Pickups compatible with other mods, please be generous enough to release them on GTA5-mods.com so others can benefit from your hard work.
		
To change the number of slots, you simply need to edit the data in pickups.xml so that weapons use new slots. If the highest 'group' attribute in pickups.xml is 7, you will then have 8 slots.  If it's 3, you'll have 4 slots. 
You will also need the right textures (in Pickups/Wheel/) for the number of slots you wish to use. I've included a template and textures for 4 and 8 slots. Use the template to make your own textures for the number of slots you desire, then follow the naming scheme I used. The script uses this naming scheme to load the appropriate textures. If it cannot find them, the script WILL NOT WORK.

All the data in pickups.xml is editable, so you can change the display names of the weapons if you desire. Be aware that these name changes only affect the Pickups script. It won't affect the stock weapon wheel or Ammunation.


Visible Loadout - 

When enabled, Visible Loadout will display weapons you're carrying, but not currently using, on various attachment points on your player. There is one attachment point for each slot. If you require more than 4 slots, simply duplicate some of the existing slots in slots.xml. You may also edit their physical attachment points. As all weapons are not made equal, some weapons have their own attachment offsets in order to better fit on the player. These per-weapon offsets are now found in pickups.xml.


Damage Engine - 

Handles the way peds take damage, equalizes max health of all peds to match that of the player (200), and allows disarming of peds. For example, headshots do more damage than body shots which do more damage than hand shots. armor and helmets reduce damage to covered body parts. This is somewhat configurable in DamageEngine.ini.

Damage Multiplier: In percent. Adjusts the difference between the least and most damage a ped can take from a weapon.
Ragdoll Health Threshold: In health units. When a ped's health is above this level, they cannot be ragdolled by being shot. Set to 200 for stock function. Set to 0 for no ragdoll.
Disable Ped Writhe: Boolean, 1 = true, 0 = false. Disables peds from writhing on the ground in pain and subsequently dying before they have lost all their health.
Disarm Peds: Boolean, 1 = true, 0 = false. Allows the player to shoot weapons out of ped's hands.
Disarm Player: Boolean, 1 = true, 0 = false. Allows peds to shoot weapons out of the player's hands.

		


Installation------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------

--Script Install--
Use OpenIV's Package Installer to install Pickups.oiv. If you want to install manually, rename the package to Pickups.zip. All the files are laid out in a very easy to understand structure.


--(PREREQUISITES)--
You will need Alexander Blade's C++ Scripthook 
(http://gtaforums.com/topic/788343-vrel-script-hook-v/)



Known Issues-------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------

-Attachments are not shown on pickup or Visible Loadout models.

-Custom weapon wheel, icons, and text have blurry edges due to DX hook.

-THERE IS NO UNINSTALL PACKAGE!


Changelog---------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------

v1.0:
-Original Release

v2.0:
-Added Visible Loadout option
-Fixed issue that caused certain pickups to forget their attachments
-Fixed loadout detection issues when changing characters
-Fixed issues with Ammunation gun ranges.

v2.1:
-Compatibility with mpbiker dlc

v2.2:
-Compatibility with After Hours dlc
-Added Damage Engine


Contact-----------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
Facebook - https://www.facebook.com/InfamousSabre
Twitter - https://twitter.com/SabreGameDev
Instagram - https://www.instagram.com/vi_gamedev/
Youtube - https://www.youtube.com/user/ignorancesupreme
GTA Forums - http://gtaforums.com/user/759205-infamoussabre/


License-----------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
This software is provided 'as-is', without any express or implied warranty.  In no event will 
the author be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software freely, subject to the following 
restrictions:

The origin of this software must not be misrepresented; you must not claim that you wrote the 
original software. If you use this software in a product, an acknowledgment in the product 
documentation is required.  This software is not to be included with any other software or 
package. If your software or package relies on this software, you must include this software's 
original link in your description, readme, and installation instructions. 
You may not redistribute this software.
