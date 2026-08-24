---
title: vtt-Autotag-Tool python script for Descript exported subtitle .vtt files
date: 2025-04-22T18:10:00+13:00
draft: false

---

Apps like Descript, when you export .vtt subtitle files, will not tag the speakers on every 42 character line output, they only voice tag on speaker changes. This does not currently allow podcasting distributors like Pinecast to recognize the speakers and format the transcript accordingly. These platforms expect speaker tagging on ALL separate 42 character subtitle lines.
For a Disability podcast like [Disability Disrupters](https://pinecast.com/feed/disability-disrupters) that must have captions and transcriptions available for each Episode, this missing feature for Descript is a major manual time waster for me, per Episode.
[Here's where I lodged the bug report with Descript in August 2024, before solving it with my janky python script](https://descript.canny.io/feature-requests/p/voice-tags-in-vtt) - upvote if you agree that Descript should solve this, so we don't have to do these crazy script hacks.
<p>This python script has made my 1-2 hour manual voice tag process a 5 minute process, which is why I am sharing this.
<p>
NOTE: this python script is supplied, as is (it works for me, feel free to modify it for your own use)

# Pre-Requisites
* The Descript speakers in the transcript before Export, need to already be labelled **&lt;v SPEAKERNAME&gt;**
	* the python script looks for **&lt;v SPEAKERNAME&gt;** to add speaker tags to the .vtt file where they are missing, this made the python script simpler for me to construct than pure speaker names
	* Basically, when you import speaker audio into Descript and transcribe, name that speaker from the get-go **&lt;v SPEAKERNAME&gt;**
* Install python on your PC (one-time setup)
* Create a **vtt-Autotag** folder and add the **vtt-Autotag-Tool.py** script there
* **Macrons are not processed well** - note what line in the file those are (as ? characters) and add back in after processing
* Add your .vtt file (exported from Descript - with 42 character setting) into the same folder as the vtt-Autotag-Tool.py script
* run the python script from the same folder that the IN-Epx.vtt is in
	* py .\vtt-AutoTag-Tool.py
* The output .vtt file will be called **xxxx -tagged.vtt**. This is what you can upload as a Pinecast transcript 

# vtt-AutoTag-Tool.py script
[The python script and a test .vtt file](https://github.com/bitrat/bitrat-blog-starter/tree/main/vtt-Autotag) (an actual Descript .vtt exported file that shows the issue the script will solve) can be downloaded from my repository on github

{{< highlight html >}}

"""
VTT auto-tagger for the Disruptors podcast transcripts.

What it guarantees:
  * KEEPS every <v Speaker> voice tag. It removes ONLY the ": " that Descript
    writes after the tag, turning "<v Dr Pam>: Hi" into "<v Dr Pam>Hi".
  * Carries the last-seen <v Speaker> tag onto Descript's untagged
    continuation cues, so EVERY cue starts with a speaker tag.
  * Reads and writes UTF-8, so macrons (ā ē ī ō ū) and ellipses (…) survive.

Run it with no arguments in the folder with your .vtt files, or pass a filename.
"""

import glob
import os
import re
import sys

OUT_SUFFIX = " - tagged.vtt"
DEFAULT_TAG = "<v Speaker>"
TAG_RE = re.compile(r"^<v[^>]*>")     # a voice tag at the start of a line
TS_RE = re.compile(r"^\d{2}:\d{2}")    # a cue-timing line

# Recovery table for files already damaged by a non-UTF-8 save.
BYTE_FIXES = {"\xa6": "…", "\x8a": "…"}   # stray bytes were ellipses
MACRON_FIXES = {
    "M?ori": "Māori", "wh?nau": "whānau", "Wh?nau": "Whānau",
    "K?piti": "Kāpiti", "M?nawatia": "Mānawatia", "M?ngere": "Māngere",
    "k?inga": "kāinga",
}


def read_text(path):
    """Return clean text. Prefer UTF-8; if the file is already damaged,
    fall back to a lossless read + repair rather than crashing."""
    raw = open(path, "rb").read()
    try:
        return raw.decode("utf-8"), False
    except UnicodeDecodeError:
        text = raw.decode("latin-1")           # 1:1, never fails
        for bad, good in BYTE_FIXES.items():
            text = text.replace(bad, good)
        for bad, good in MACRON_FIXES.items():
            text = text.replace(bad, good)
        return text, True


def strip_descript_note(text):
    return re.sub(
        r"^NOTE\r?\n[^\r\n]*[Dd]escript[^\r\n]*\r?\n(\r?\n)?",
        "", text, flags=re.MULTILINE,
    )


def strip_tag_colon(text):
    """'<v Name>: ' -> '<v Name>'  (removes the colon, KEEPS the tag)."""
    return text.replace(">: ", ">")


def fill_tags(lines, default_tag=DEFAULT_TAG):
    current_tag = default_tag
    out = []
    prev_was_timestamp = False
    for line in lines:
        if TS_RE.match(line):
            prev_was_timestamp = True
            out.append(line)
            continue
        if prev_was_timestamp:
            m = TAG_RE.match(line)
            if m:
                current_tag = m.group(0)   # remember the <v Speaker> prefix
                out.append(line)           # keep the tagged line as-is
            else:
                out.append(current_tag + line)   # tag the continuation cue
        else:
            out.append(line)
        prev_was_timestamp = False
    return out


def tag_one(in_file, out_file):
    text, repaired = read_text(in_file)
    text = strip_descript_note(text)
    text = strip_tag_colon(text)
    fixed = fill_tags(text.splitlines(keepends=True))
    tags = sum(1 for l in fixed if l.startswith("<v "))
    with open(out_file, "w", encoding="utf-8", newline="") as f:
        f.writelines(fixed)
    note = "  [repaired damaged input]" if repaired else ""
    print(f"  {in_file}  ->  {out_file}  ({len(fixed)} lines, {tags} tagged){note}")


def default_out(in_file):
    return os.path.splitext(in_file)[0] + OUT_SUFFIX


def main():
    args = sys.argv[1:]
    if len(args) >= 2:
        tag_one(args[0], args[1]); return
    if len(args) == 1:
        tag_one(args[0], default_out(args[0])); return
    inputs = [f for f in sorted(glob.glob("*.vtt")) if not f.endswith(OUT_SUFFIX)]
    if not inputs:
        sys.exit("No .vtt files found here. Put this script next to your "
                 "transcripts, or pass a filename.")
    print(f"Tagging {len(inputs)} file(s):")
    for in_file in inputs:
        tag_one(in_file, default_out(in_file))


if __name__ == "__main__":
    main()
     
{{< /highlight >}}

