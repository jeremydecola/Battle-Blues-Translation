# Battle Blues (3DO) English Translation 

Battle Blues (배틀 블루스) is a CyberPunk SRPG made by Shin's Entertainment in 1996 and published by LG electronics who produced their very own 3DO systems in South Korea at the time. 
The game was never localized for a western audience as the 3DO did not sell well in the West, let alone in Korea. 

<p align="center">
  <img src="graphics/bb_pinup.jpg" width=25%>  
</p>

## Balance Changes
It seems as though the developers behind this game didn't invest many ressources in quality assurance... The game is brutally difficult and in an unfair way. There is a lot of random number generation and your party member's stats are insulting low. Even after using Cheat Engine to give myself 999 999 starting credit and buying all the best weapons and items, I found it impossible to complete even the first Chapter. I have located where the stats are stored and was able to re-balance the game. I will be making balance changes while I continue translating. My goal is not to make this game easier, simply playable/enjoyable. I will ultimately create 3 profiles, Easy, Normal, Hard. The original difficulty could be considered a notch up from hard, let's call it Impossible mode.

## Progress
v0.1.3
* BBPBT v0.2 -> Added radiobutton logic. Various aesthetic fixes. Added zlib1.dll which is required to run OperaFS.
* New Pin-Up Original Artwork! 

v0.1.2
* Created a patching tool "Battle Blues Patch and Balance Tool" with a user-friendly GUI which uses PyAutoGUI and performs simple move commands to automate the patching process.
* Translated text for Scene 2 and Scene 3 of Chapter 1 but did edit the .cel files yet.

v0.1.1 
* Item Pickup Translated
* Restructuring of folders

v0.1.0
* Intro Translated
* Chapter 1 Part 1 Translated
* 2x all ATK and DEF stats for party members 
* 2x starting credit (from 15 000 to 30 000)

## Translation Procedure

Unlike other games where text is usually encoded and stored seperately from the game's graphics, the text in this game is embedded in proprietary 3DO image/sprite .cel format files. Modifying the game means modifying these .cel files.
In order to extract the .cel files, modify them and rebuild the game to run on an unmodified 3DO bios, we can make use of the tools found in the TOOLS section of this repository: 

1. OperaFS: De-Compile (Select "ISO, BIN, NRG" and browse for the Battle Blues .iso or .img file)
2. Once uncompiled, run 3DOResExplorer8(Neuro).exe and browse to (...)\PARCE_Battle Blues\pic where the 3DO image files (in proprietary .cel format) are contained.
3. Select an image in the 3DOResExplorer explorer to view it, then select Command and save to export it as a .bmp image
4. Edit the image with your favorite image editor (GIMP, Photoshop, ...) and make sure to export as 24-bit 
5. Use BmpTo3DOCel.exe to conver the edited .bmp back to .cel
6. OperaFS: Compile (Browse the uncompiled game ) -> export as .iso
7. Sign your game and regenerate rom_tags : 3DOEncrypt.exe genromtags ISOFILE.iso

