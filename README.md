# Clipboard-Logger

### Overview
Checks what is on the target marchine's clipboard every 5 seconds and if it's new adds it to a log. This log is emailed to the specifed address every 5 minutes.

### Discussion
Most cyber security professionals are familiar with keyloggers. The basic concept is logging every keystroke on the machine it is running on within a certain amount of time and 
then exporting somehow (mine emailed me). The other day I was thinking if anything else could be extrapalated the same way. Keyloggers only work for credentials if you type in 
the password by hand. Since everyone uses password managers these days (or at least should be) it would stand to reason that if you could get to someone's clipboard within the 
time it takes for that clipboard to get wiped by the password manager, you could get their password. By checking the clipboard for a new entry every five seconds and treating 
everything else about it like a normal keylogger, this "tool" will grab those passwords. It will also grab any other text you happen to add to your clipboard. This was shockingly 
easy to make and I don't know why no one is talking about it.
