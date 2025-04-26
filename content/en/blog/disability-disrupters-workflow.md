---
title: Workflow for Disability Disrupters Podcast using Descript
date: 2025-04-26T15:15:00+13:00
draft: false

---

# Workflow steps
## High level overview
Pre-requisites for getting the episode completed:
* Dr Pam's intro and outro
* "Ask Dr Pam" segment
* Interviewee bio
* Runsheet for what Adverts to include
* Edited Episode audio
* Edited Episode transcript (for deaf and deafblind)


## Setup Zoom meeting 
* Zoom meet settings need to be: auto record, set to cloud, people can join anytime
* Once interview finished, wait for recording to process
* Copy "EpxTEMPLATE-Descript" folder and rename to "Episode x - Interview with &lt;Name&gt;"
* Download the RAW audio files from Zoom into "RAW" folder

## Descript
### Edit Interview
* Create new folder in "Episodes\" folder, named "Episode x -Interview with &lt;Name&gt;"
* Create new folder in "Episodes\Episode x -Interview with &lt;Name&gt;" folder, named "Edited"
* Create new audio Project in "Episodes\Episode x -Interview with &lt;Name&gt;" folder "Interview with &lt;Name&gt;"
* RAW interview file - Import audio from Zoom into Descript directly (or download and import each speaker audio separately)
	* Select "Transcribe"
	* add speaker labels &lt;v Dr Pam&gt;**nospace**
	* Underlord - **Remove filler words**
	* Edit transcript
		* At start of audio get rid of "tell us about yourself" question (if this makes sense)
		* At end of audio get rid of "anything else" question (if this makes sense)
	* Apply Studio Sound (if necessary, otherwise skip this step)
* Move Interview from "Episodes\Episode x -Interview with &lt;Name&gt;\" folder into "Episodes\Episode x -Interview with &lt;Name&gt;\Edited" folder

* All RAW Audio resides in "Episodes\Episode x -Interview with &lt;Name&gt;\" folder until it is **Edited**

### Duplicate Template - edit Episode
* In "Template-Projects" folder
	* Duplicate appropriate project template 
	* Move it into "Episodes\Episode x -Interview with &lt;Name&gt;" folder 
		* re-name project to "Episode x - Interview with &lt;Name&gt;"
* From the "Episodes\Episode x -Interview with &lt;Name&gt;\Edited" folder
	* Open edited interview 
	* copy text & paste edited interview audio (do not re-transcribe) below "Interview" marker in "Episode x - Interview with &lt;Name&gt;" audio project
	* Double-check title of entire script is "Episode x -Interview with &lt;Name&gt;"
	* Rename the "Interview" marker in the Transcript to "Interview with &lt;Name&gt;"
	* add Dr Pam's intro, transcribe and edit
	* add "Ask Dr Pam" segment, transcribe and edit	
	* add Dr Pam's outro, transcribe and edit
	* Make sure background music in correct place (in Layer - Large - scroll audio layer)
		* adjust audio boundaries on timeline (insert gaps, make sure audio in full for each section)	

### Export Draft Episode Audio
* Open episode from "Episodes\Episode x -Interview with &lt;Name&gt;" folder
	* Check Markers are properly labelled
	* **Export - Audio** 
		* Local Export
		* Current Composition
		* mp3
		* Metadata – Show title - "Episode x – Disability Disrupters"
		* Metadata – Episode title - "Interview with &lt;Name&gt;"
		* SAVE AS-  "DRAFT-EditedInterview-Episode x - Interview with &lt;Name&gt;"
		* Copy to Shared folder for podcast host to review
	* check size of audio is less than 135 MB (pinecast plan limit)
	* Listen to the DRAFT audio (transition points)

### Review Draft Episode Audio
* Podcast Host reviews "DRAFT-EditedInterview-Episode x - Interview with &lt;Name&gt;"
	* implement changes
	* Save "FINAL-EditedInterview-Episode x - Interview with &lt;Name&gt;"

### Export and process transcript (vtt file)
* **Export - Subtitles**
	* Name file "IN-Epx.vtt" and place into **vtt-Autotag** folder
		* Open "IN-Epx.vtt" and remove "Descript" text
		* Replace all instances of &gt;: with &gt; (Control+H - Replace All)
	* Run Auto-tag py script (to add the speaker labels that are missing in vtt file)
		* cmd.exe from vtt-Autotag folder
		* py .\vtt-AutoTag-Tool.py
	* Rename the resultant "Out-Expx.vtt" file "FINAL-Episode x - Interview with &lt;Name&gt;"
		* Open "Out-Expx.vtt" and remove &lt;v TestPerson&gt; text
		* Put macrons back in (if you had to remove them for script not to fail)
	* Move file to FINAL folder

## Shared Podcast Episodes folder
* Place FINAL audio and transcripts into that folder 

## Pinecast and Podcast Marker generation
* Title "Interview with ... "
* Upload audio mp3
* tick "don't upload art work"
* Choose 1st of Month 12:01 AM
* Get rid of Episode Notes title	
	* Paste show notes (interviewee bios)
	* Generate and Paste Text Markers (2 spaces at end of line):
		* Upload edited audio to https://mp3chapters.github.io/
		* Copy markers
		* paste into Pinecast Episode Notes and type 2 spaces at end of each line (markdown equivalent of newline)
	* Add Footnote credits
* tick link to transcript
* tick link to tip jar
* Save Episode
* Upload episode transcript file
	* NOTE: If you make a mistake and have to re-upload transcript file, delete transcript, then **F5** the transcript page, before you upload a new transcript
* Speaker A - go into edit mode on transcript text, and change Speaker A combo box to the correct speaker

## After Episode has been published (after 8 hours)
* check Apple podcasts (markers good ?)
* check DRNZ website (episode on episode lists page ?)
