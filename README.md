# Voice-Command-Ubuntu
#Python Voice Commands for controlling Ubuntu Pop-Shell/Gnome-Shell 

## What it can do?

Activates with:
- "Jarvis" or "Travis"  

  Then responds to the following:

  - work (Tells you what his work is)
  - creator (Reads predefined name of creator) 
  - date (Reads the date)
  - time (Reads the time)
  - play movie (Hits the space bar)
  - open programs (Opens programs with use of xdotool and predefined keyboard shortcuts, but commands also work. eg. Google = 'xdotool key super+b' or 'google-chrome')
  - control window actions (With predefined shortcuts as mentioned)
  - add note & read reminders (Add notes to 'note.txt' file with the date when asked 'note' and then promts for the  actual note. Also reads back when asked 'reminders'
  - search Google (Activated with 'search' and promts user for search term before opening default browser to google search)
  - quit & exit (This will terminate the assistant.)

## How to use it?

- First download the repository.

  -$ git clone https://github.com/CJsps199/Voice-Command-Ubuntu.git
  
- Move into downloaded folder

  -$ cd Voice-Command-Ubuntu

- Now run the program using:

  -$ python main.py
  
# OR
  
- Add program to applications menu

  -$ cp VoiceAssistant.desktop $HOME/.local/share/applications/
  
- Open applications & run "Voice Assitant"


   Optional:
   
- Start assistant on boot:

  - $ cp AutostartVoiceAssistant.desktop $HOME/.config/autostart/
  
  

## Requirements
 Check requirements.txt file
 

***Note: If you are using Ubuntu, then you may get some errors of the form "ALSA lib [...] Unknown PCM". To suppress those errors, see <a href="https://stackoverflow.com/questions/7088672/pyaudio-working-but-spits-out-error-messages-each-time" target="_blank">this Stackoverflow answer</a>.***
