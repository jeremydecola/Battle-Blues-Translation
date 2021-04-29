# Battle Blues (3DO) English Translation 

Battle Blues (배틀 블루스) is a Strategy Role-Playing Game developped by Shin's Entertainment (A.K.A. SHIN'S DECO) in collaboration with LG Electronics in 1996 who also helped publish the game. 

Similar to Panasonic in the West, LG sold its own 3DO consoles in the Korean market. They went on to produce 3 consoles: the Goldstar 3DO Alive which was also sold in Europe without the "Alive" branding, the Goldstar 3DO Alive II which was exclusive to Korea as well as the extremely rare LG 3DO Alive II (essentially just a variant on the Alive II with the LG logo after the company was renamed from "Lucky-Goldstar" to "LG"). 

Battle Blues was never localized for a western audience as the 3DO did not sell well in the West, let alone in Korea. 

## Instructions 
As a pre-requisite, you will need a backup of the original game. For legal and moral reasons, I will not be hosting a download for my backup of the game. 

1. Download the latest release of the Battle Blues Patch & Balance Tool (BBPT) from the Releases section of this repository.
2. Unzip the BBPT.zip file with your favorite file archiver. (I recommend 7zip as it is free and open-source.)
3. Run BBPT.exe
4. Follow the in-app instructions.

Note: The tool is currently very rudimentary and gets the job done but it is very sensitive to environmental conditions (CPU and RAM availability, Clock Speed, etc.)  To ensure that the tool completes the patching process smoothly, ensure that there are no ressource intensive processes running on your system at the time of execution. The application currently makes use of Python AutoGui and emulates keypresses during the patching process, so please avoid using your keyboard after starting the patching operation. If you experience any bugs or errors, please report them to jeremydecola@gmail.com.

Thank you! 

If you like my work, please show your support at: https://ko-fi.com/jeremydecola

All donations will help fund further translation projects.

Future potential projects include:

* Zaphie (PC Survival Horror)
* Zaphie 2 (PC Survival Horror)
* Manic Game Girl (PS1 Action Adventure / Beat-em-up)

<p align="center">
  <img src="graphics/bb_poster_eng.jpg" width=100%>  
</p>

Illustration by Joe N. Brown Art 

## Balance Changes
It seems as though the developers didn't invest many ressources in quality assurance... The game is brutally difficult and in an unfair way. The random number generation is almost never in your favor and your party member's stats are insulting low. I located where the stats are stored in the game's binaries and was able to re-balance the characters slightly as well as up the amount of money given at the start of each level to allow the player to buy more weapons and ammunition. I will create 3 difficulties: Easy, Normal, Hard. The original difficulty will be dubbed "Impossible" mode.

### Allied Units

<details><summary>Tentative balance changes on Allied Units: [SPOILER WARNING]</summary>
  
Impossible : Stats unchanged. 

Hard : Same as Normal but the player will not be given additional Credit for each mission. In other words, the player will have the same amount of Credit to spend as they would in the original game.

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
@@ 04/28/2021@@
- nerfing AT from 1.50x to 1.25x all allies [Normal].

@@ 04/07/2021@@
- nerfing DF from 1.50x to 1.25x for Police [Normal].
- nerfing DF and AT of all characters from 2.00x to 1.50x [Easy]
! John is an enemy.
! Psycho (Phyco) is an enemy. 
! Removing buffs on Sasha and Jack.
```

| Name    | AT       | DF       | SP       | MOV   | X  |
|---------|----------|----------|----------|-------|----|
| Jin     | 8/10/12  | 5/7/7    | 10/10/10 | 4/4/5 | 70 |
| Rodrigo | 9/12/14  | 4/6/6    | 16/16/16 | 4/4/4 | 50 |
| BB      | 6/8/9    | 6/9/9    | 3/6/6    | 3/3/4 | 30 |
| Yuang   | 7/9/10   | 4/6/6    | 15/20/20 | 4/4/4 | 80 |
| Bill    | 8/10/12  | 4/6/6    | 16/16/16 | 4/4/4 | 90 |
| June    | 6/8/9    | 4/6/6    | 10/18/18 | 4/5/5 | 80 |
| Police  | 10/15/15 | 15/20/20 | 5/5/5    | 4/4/4 | 5  |
| Eric    | 12/15/18 | 10/15/15 | 6/6/6    | 4/4/4 | 60 |
| Hans    | 5/7/10   | 3/6/6    | 10/10/10 | 4/4/4 | 40 |
| Bump A  | 5/5/5    | 1/5/5    | 0/0/0    | 4/4/4 | 5  |
| Bump B  | 5/5/5    | 1/5/5    | 0/0/0    | 4/4/4 | 5  |
| Bump C  | 5/5/5    | 2/7/7    | 2/2/2    | 4/4/4 | 5  |
| Ray     | 15/18/22 | 20/30/30 | 16/16/16 | 6/6/6 | 60 |
| Shinobu | 20/25/30 | 10/15/15 | 35/35/35 | 5/5/5 | 50 |
| Herman  | 5/5/5    | 20/20/20 | 5/5/5    | 4/4/4 | 5  |
| Jack    | 5/5/5    | 5/5/5    | 5/5/5    | 4/4/4 | 5  |
| Shasha  | 5/5/5    | 5/5/5    | 5/5/5    | 4/4/4 | 5  |
| Simon   | 20/25/30 | 15/22/22 | 28/28/28 | 5/5/5 | 50 |
</details>

### Enemy Units
<details><summary>Tentative balance changes on Enemy Units:: [SPOILER WARNING]</summary>

Impossible : Stats unchanged. 

Hard : TBD

Medium : 
* Applied 0.75x Multiplier on all DEF stats. 

Easy : 
* Applied 0.75x Multiplier on all AT and DEF stats. 

```diff
@@ 04/28/2021@@
- nerfing DF from 1.00 to 0.80x for Robot [Normal]
+ buffing DF from 0.75 back to 1.00x for Ivan [Easy]

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
| Robot     | 75/75/60 | 50/40/40 | 5/5/5    | 4/4/4 | 5 |
| Haberac   | 25/25/18 | 22/22/18 | 10/10/10 | 4/4/4 | 5 |
| Gail      | 25/25/18 | 37/37/30 | 5/5/5    | 4/4/4 | 5 |
| Injil     | 15/15/15 | 5/5/5    | 5/5/5    | 4/4/4 | 5 |
| Akba      | 2/2/2    | 5/5/4    | 5/5/5    | 4/4/4 | 5 |
| Bull      | 5/5/4    | 10/10/7  | 5/5/5    | 4/4/4 | 5 |
| Dog       | 25/25/18 | 15/15/10 | 5/5/5    | 4/4/4 | 5 |
| Psycho    | 25/25/18 | 30/30/23 | 10/10/10 | 4/4/4 | 5 |
| John      | 5/5/4    | 5/5/4    | 5/5/5    | 4/4/4 | 5 |
| Ivan      | 25/25/25 | 40/40/40 | 5/5/5    | 4/4/4 | 5 |
</details>

### Credit Advance Balancing

| Mission \| | Original Credit | Normal Credit | Easy Credit |
|------------|-----------------|---------------|-------------|
| 1          | 15 000          | 20 000        | 30 000      |
| 2          | 10 000          | 15 000        | 20 000      |
| 3          | 10 000          | 15 000        | 20 000      |
| 4          | 18 000          | 22 000        | 26 000      |
| 5          | 12 000          | 18 000        | 24 000      |
| 6          | -               | -             | -           |
| 7          | 15 000          | 20 000        | 30 000      |
| 8          | 20 000          | 25 000        | 35 000      |
| 9          | 20 000          | 30 000        | 40 000      |

## Progress
v1.0.0 - PROJECT COMPLETE!
* Initial Public Release. 

v0.10.6
* Implemented balancing for Easy and Normal difficulties.

v0.10.5 
* Removed staff_b.cel due to visual artifacts caused by incorrect cel parameters. Figuring out which parameters to set would be too tedious.
* Found that m8e.moov freezes a few seconds into playback. No other videos have issues. I will regenerate m8e.moov.
* Fixed a few awkward sentences and an aesthetic error : ana1_2-01, m9_open_shasha_3-01, m9_end_shasha_1-01
* For the sake of consistency, replaced all mentions in text/video of "Geil" with "Gail".

v0.10.4 - DUBBED THE CREDITS.
* Dubbed the credits in English.

v0.10.3 - SUBBED ALL CUTSCENES!
* Added subtitles to all cutscenes.
* Fixed incorrectly named cel image files which caused B.B.'s lines in Chapter 8 to be out of order and incoherent.

v0.10.2 - CHAPTER LOADING SCREENS COMPLETE!
* Translated the loading screens for all chapters. 

v0.10.1 - MISCELLANEOUS DIALOGUE COMPLETE! 
* Friendly Fire Comments Translated.
* Allied Unit Death/Retreat Comments Translated.
* Ninja Summon Event Translated.

v0.10.0 - CHAPTER 10 COMPLETE!
* Chapter 10 Part 1 Translated.
* Chapter 10 Part 2 Translated.

v0.9.0 - CHAPTER 9 COMPLETE!
* Chapter 9 Part 1 Translated.
* Chapter 9 Part 2 Translated.
* Chapter 9 Part 3 Translated.

v0.8.2 - CHAPTER 8 COMPLETE!
* Chapter 8 Part 3 Translated.

v0.8.1
* Chapter 8 Part 1 Translated.
* Chapter 8 Part 2 Translated.

v0.8.0
* Chapter 8 Briefing Translated.
* Chapter 8 Part 1, 2 and 3 - Text ready for .cel creation.

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
* Fixed getitem bombsol.cel ("Dismantling Bomb" -> "Bomb Defused") 

v0.3.1 - CHAPTER 3 COMPLETE!
* Chapter 3 Part 2 Translated.
* Chapter 3 Part 3 Translated.

v0.3.0
* Chapter 3 Briefing Translated.
* Chapter 3 Part 1 Translated.

v0.2.1 - CHAPTER 2 COMPLETE!
* Chapter 2 Translated.

v0.2.0
* Chapter 2 Briefing Translated.
* Translated the title screen for Chapter 2.

v0.1.6
* Chapter 2 Briefing Text Translated but .cel's not yet created

v0.1.5 
* BBPBT v0.3 -> Fully implemented difficulty select. Difficulties are not yet balanced. 
* Played through Chapter 1 and improved the dialogue (modified some non-sensical/cheesy lines). 
* Translated the title screen for Chapter 1.

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
