---
title: Workflow for Disability Disrupters Podcast using Descript
date: 2025-02-08T17:30:00+13:00
draft: false

---

# Workflow steps
Pre-requisites for getting the episode completed:
* Interviewee bio
* Edited Episode audio
* Edited Episode transcript (for deaf and deafblind)
* Dr Pam's intro and outro
* Runsheet for what Adverts to include

## Setup Zoom meeting 
* Zoom meet settings need to be: auto record, set to cloud, people can join anytime
* Once interview finished, wait for recording to process
* Download the RAW audio files from Zoom as a backup ("RAW" folder"

## Descript
* Create new audio Project in "Interviews" folder "Episode x - Interview with "<Name>""
* RAW interview file - Import audio from Zoom into Descript directly (or download and import each speaker audio separately)
	* Select "Transcribe"
	* add speaker labels "<"v Dr Pam">"**nospace**
	* Edit transcript
	* At end of audio get rid of "anything else" question (if this makes sense)
* Apply Studio Sound (if necessary, otherwise skip this step)
* Move Interview from "Interviews" folder into "Interviews\Edited interviews" folder
* In "Template-Projects" folder - Duplicate appropriate project template then Move it to "Episodes\In Progress" folder - re-name to "Episode x - Interview with "<"Name">""
* From the "Interviews\Edited interviews" folder - Open edited interview then copy text & paste edited interview audio (do not transcribe) below "Interview" marker
* Make sure background music in correct place (in Layer)
* Double-check title of entire script is "Episode x -Interview with "<"Name">""
* Rename the "Interview" marker in the Transcript to "Interview with "<"Name">""
* Move Interview from "Interviews\Edited Interviews" to "used-in-a-script" folder
* add Dr Pam's intro, transcribe and edit
	* adjust audio boundaries on timeline (insert gap, make sure audio in full for each section)
* add Dr Pam's outro, transcribe and edit
	* adjust audio boundaries on timeline (insert gap, make sure audio in full for each section)
* Open interview from "Interviews\Edited Interviews\Used-in-a-script" 
	* Check Markers are properly labelled
* Publish - Export - subtitles - edit Episode in Librewriter (check "<"v speaker">" tags)
	* Name vtt file "Episode x - Interview with "<"Name">""
	* Run Auto-tag py script (to add the speaker labels that are missing in vtt file)
* Publish - Export - audio mp3 - name it EditedInterview
	* include markers
	* check size of audio is less than 135 MB (pinecast plan limit)
		
## test-Podcast-Episodes folder
* Place edited audio and transcripts into that folder 

## Produce time/text markers for Pinecast show notes section
* Upload edited audio to https://mp3chapters.github.io/
* Copy markers
* paste into pinecast Episode Notes (see below), or keep a copy of these for later
		
## Pinecast
* Title "Interview with ... "
* Upload audio mp3
* tick "don't upload art work"
* Choose 1st of Month 12:01 AM
* Get rid of Episode Notes title	
	* Paste show notes (interviewee bios)
	* Paste Text Markers (2 spaces at end of line)
	* Add Footnote credits
* tick link to transcript
* tick link to tip jar
* Save Episode
* Upload episode transcript file
* Speaker A - go into edit mode on transcript text, and change Speaker A combo box to the correct speaker

## After Episode has been published (after 8 hours)
* check Apple podcasts (markers good ?)
* check DRNZ website (episode on episode lists page ?)
