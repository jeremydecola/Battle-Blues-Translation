# Battle Blues (3DO) English Translation 

Battle Blues (배틀 블루스) is a CyberPunk SRPG made by Shin's Entertainment in 1996 and published by LG electronics who produced their very own 3DO systems in South Korea at the time. 
The game was never localized for a western audience as the 3DO did not sell well in the West, let alone in Korea. 

<p align="center">
  <img src="graphics/bb_pinup.jpg" width=60%>  
</p>

## Balance Changes
It seems as though the developers behind this game didn't invest many ressources in quality assurance... The game is brutally difficult and in an unfair way. There is a lot of random number generation and your party member's stats are insulting low. Even after using Cheat Engine to give myself 999 999 starting credit and buying all the best weapons and items, I found it impossible to complete even the first Chapter. I have located where the stats are stored and was able to re-balance the game. I will be making balance changes while I continue translating. My goal is not to make this game easier, simply playable/enjoyable. I will ultimately create 3 profiles, Easy, Normal, Hard. The original difficulty could be considered a notch up from hard, let's call it Impossible mode.

### Allied Units

Tentative balance changes on Allied Units:

Impossible : Stats unchanged. 

Hard : TBD

Medium : 
* Applied 1.50x Multiplier on all AT and DEF stats. 
* Increased SP for BB to avoid him getting outclassed by Eric. 
* Increased SP for Yuang since he was just a weaker version of Bill. 
* Increased SP and MOV for June in an attempt to make her usefull as she is originally weaker than all other party members.

Easy : 
* Applied 2.00x Multiplier on all AT and DEF stats. 
* Increased SP for BB to avoid him getting outclassed by Eric as well as MOV to give him more mobility. 
* Increased SP for Yuang since he was just a weaker version of Bill. 
* Increased SP and MOV for June in an attempt to make her usefull as she is originally weaker than all other party members.

```diff
@@ 04/07/2021@@
- nerfing DF from 1.50x to 1.25x for Police [Normal].
- nerfing DF and AT of all characters from 2.00x to 1.50x [Easy]
! John is an enemy.
! Psycho (Phyco) is an enemy. 
! Removing buffs on Sasha and Jack.
```

| Name    | AT       | DF       | SP       | MOV   | X  |
|---------|----------|----------|----------|-------|----|
| Jin     | 8/12/12  | 5/7/7    | 10/10/10 | 4/4/5 | 70 |
| Rodrigo | 9/14/14  | 4/6/6    | 16/16/16 | 4/4/4 | 50 |
| BB      | 6/9/9    | 6/9/9    | 3/6/9    | 3/3/4 | 30 |
| Yuang   | 7/10/10  | 4/6/6    | 15/20/20 | 4/4/4 | 80 |
| Bill    | 8/12/12  | 4/6/6    | 16/16/16 | 4/4/4 | 90 |
| June    | 6/9/9    | 4/6/6    | 10/18/18 | 4/5/5 | 80 |
| Police  | 10/15/15 | 15/20/20 | 5/5/5    | 4/4/4 | 5  |
| Eric    | 12/18/18 | 10/15/15 | 6/6/6    | 4/4/4 | 60 |
| Hans    | 5/10/10  | 3/6/6    | 10/10/10 | 4/4/4 | 40 |
| Bump A  | 5/5/5    | 1/5/5    | 0/0/0    | 4/4/4 | 5  |
| Bump B  | 5/5/5    | 1/5/5    | 0/0/0    | 4/4/4 | 5  |
| Bump C  | 5/5/5    | 2/7/7    | 2/2/2    | 4/4/4 | 5  |
| Ray     | 15/22/22 | 20/30/30 | 16/16/16 | 6/6/6 | 60 |
| Shinobu | 20/30/30 | 10/15/15 | 35/35/35 | 5/5/5 | 50 |
| Herman  | 5/5/5    | 20/20/20 | 5/5/5    | 4/4/4 | 5  |
| Jack    | 5/5/5    | 5/5/5    | 5/5/5    | 4/4/4 | 5  |
| Sasha   | 5/5/5    | 5/5/5    | 5/5/5    | 4/4/4 | 5  |
| Simon   | 20/30/30 | 15/22/22 | 28/28/28 | 5/5/5 | 50 |

### Enemy Units

Tentative balance changes on Enemy Units:

Impossible : Stats unchanged. 

Hard : TBD

Medium : 
* Applied 0.75x Multiplier on all DEF stats. 

Easy : 
* Applied 0.75x Multiplier on all AT and DEF stats. 

```diff
@@ 04/07/2021@@
+ buffing DF from 0.75 back to 1.00x [Normal]
```

| Name      | AT       | DF       | SP       | MOV   | X |
|-----------|----------|----------|----------|-------|---|
| FM Com    | 30/30/20 | 25/25/20 | 5/5/5    | 5/5/5 | 5 |
| FM Mid    | 5/5/4    | 5/5/4    | 5/5/5    | 4/4/4 | 5 |
| FM Ninja  | 40/40/30 | 15/15/10 | 5/5/5    | 4/4/4 | 5 |
| FM Ninja2 | 45/45/35 | 15/15/10 | 5/5/5    | 4/4/4 | 5 |
| ANA Heavy | 5/5/4    | 10/10/7  | 5/5/5    | 4/4/4 | 5 |
| ANA Mid   | 5/5/4    | 5/5/4    | 5/5/5    | 4/4/4 | 5 |
| ANA Snipe | 5/5/4    | 5/5/4    | 5/5/5    | 4/4/4 | 5 |
| Def Heavy | 5/5/4    | 5/5/4    | 5/5/5    | 4/4/4 | 5 |
| Def Mid   | 25/25/18 | 13/13/9  | 5/5/5    | 4/4/4 | 5 |
| Robot     | 75/75/60 | 50/50/40 | 5/5/5    | 4/4/4 | 5 |
| Haberac   | 25/25/18 | 22/22/18 | 10/10/10 | 4/4/4 | 5 |
| Geil      | 25/25/18 | 37/37/30 | 5/5/5    | 4/4/4 | 5 |
| Injil     | 15/15/15 | 5/5/4    | 5/5/5    | 4/4/4 | 5 |
| Akba      | 2/2/2    | 5/5/4    | 5/5/5    | 4/4/4 | 5 |
| Bull      | 5/5/4    | 10/10/7  | 5/5/5    | 4/4/4 | 5 |
| Dog       | 25/25/18 | 15/15/10 | 5/5/5    | 4/4/4 | 5 |
| Psycho    | 25/25/18 | 30/30/23 | 10/10/10 | 4/4/4 | 5 |
| John      | 5/5/4    | 5/5/4    | 5/5/5    | 4/4/4 | 5 |
| Ivan      | 25/25/25 | 40/40/30 | 5/5/5    | 4/4/4 | 5 |

## Progress
v0.8.0 
* Chapter 8 Briefing Translated.
* Chapter 8 Part 1, 2 and 3 - Text ready for .cel creation.
* Mission 8 Credit Easy : 40 000 starting Credit / Normal : 30 000 starting Credit / Hard & Impossible : 20 000 starting 

v0.7.0 - CHAPTER 7 COMPLETE!
* Chapter 7 Briefing Translated.
* Chapter 7 Translated.
* Fixed m1e.moov (180 KBps > 100 KBps).

v0.6.1 - CHAPTER 6 COMPLETE!
* Chapter 6 Translated.
* Saved m1b.moov (Chapter 1 Opening Cutscene) with a data rate of 100 KBps instead of 180 KBps. This results in a 38% reduction in filesize and more closely resembles the size of the original video files. The previous picture quality on 180 KBps was slightly sharper but was not enough to justify the outrageous filesizes which ultimately may have made fitting my translation on CD-ROM impossible.
* Set the audio slightly ahead on m1b.moov to better sync audio/video. 

v0.6.0 
* Chapter 6 Briefing Translated. 

v0.5.4 - CHAPTER 5 COMPLETE!
* Chapter 5 Part 1 Translated.
* Chapter 5 Part 2 Translated.

v0.5.3
* Memorial Chapter (Yuang's Chapter) Translated. 
* Chapter 5 Part 1 and 2 - Text ready for .cel creation.

v0.5.2 
* Chapter 1 Ending Cutscene Subtitles Inserted.
* Finished initial playthrough with 1.50x multiplier on all AT and DEF stats of allies, 0.75x multiplier on enemy DEF and double money (first 5 missions only). Despite a few levels which were quite challenging, the game felt overwhelmingly easy and braindead. These multipliers which were previously coined as "Normal" mode would work better as "Easy" mode. 

v0.5.1
* Balance tables added.
* Normal Difficulty balance values applied to wid_tables. 

v0.5.0 
* Chapter 5 Briefing Translated. 
* Mission 5 Credit Easy : 36 000 starting Credit / Normal : 24 000 starting Credit / Hard & Impossible : 12 000 starting Credit

v0.4.2 - CHAPTER 4 COMPLETE! 
* Chapter 4 Part 1 Translated
* Chapter 4 Part 2 Translated.

v0.4.1
* Edited the Starting Credit for Mission 2, 3 and 4 in launchme. 
* Chapter 4 Part 1 and 2 - Text ready for .cel creation.
* Chapter 1 Intro Cutscene Subtitles Inserted.

v0.4.0
* Chapter 4 Briefing Translated.
* Translated the title screen for Chapter 3.
* Translated the title screen for Chapter 4.
* Mission 4 Credit Easy : 42 000 starting Credit / Normal : 26 000 starting Credit / Hard & Impossible : 18 000 starting Credit
* Fixed getitem bombsol.cel ("Dismantling Bomb" -> "Bomb Defused") 

v0.3.1 - CHAPTER 3 COMPLETE!
* Chapter 3 Part 2 Translated.
* Chapter 3 Part 3 Translated.

v0.3.0
* Chapter 3 Briefing Translated.
* Chapter 3 Part 1 Translated.
* Mission 3 Credit Easy : 30 000 starting Credit / Normal : 20 000 starting Credit / Hard & Impossible : 10 000 starting Credit

v0.2.1 - CHAPTER 2 COMPLETE!
* Chapter 2 Translated.

v0.2.0
* Chapter 2 Briefing Translated.
* Translated the title screen for Chapter 2.
* Mission 2 Credit Easy : 30 000 starting Credit / Normal : 20 000 starting Credit / Hard & Impossible : 10 000 starting Credit

v0.1.6
* Chapter 2 Briefing Text Translated but .cel's not yet created

v0.1.5 
* BBPBT v0.3 -> Fully implemented difficulty select. Difficulties are not yet balanced. 
* Played through Chapter 1 and improved the dialogue (modified some non-sensical/cheesy lines). 
* Translated the title screen for Chapter 1.
* Mission 1 Credit : Easy : 45 000 starting Credit / Normal : 30 000 starting Credit / Hard & Impossible : 15 000 starting Credit

v0.1.4 - CHAPTER 1 COMPLETE! 
* Chapter 1 Part 2 Translated.
* Chapter 1 Part 3 Translated.

v0.1.3
* BBPBT v0.2 -> Added radiobutton logic. Various aesthetic fixes. Added zlib1.dll which is required to run OperaFS.
* New Pin-Up Original Artwork! 

v0.1.2
* Created a patching tool "Battle Blues Patch and Balance Tool" with a user-friendly GUI which uses PyAutoGUI and performs simple move commands to automate the patching process.
* Translated text for Scene 2 and Scene 3 of Chapter 1 but did edit the .cel files yet.

v0.1.1 
* Item Pickup Translated.
* Restructuring of folders.

v0.1.0
* Intro Translated.
* Chapter 1 Briefing Translated.
* Chapter 1 Part 1 Translated.
* 2x all ATK and DEF stats for party members.
* 2x starting credit (from 15 000 to 30 000).

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

