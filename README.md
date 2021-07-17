# Zoom-Automation

Bored of class? Use this simple script to to automate your Zoom meetings, WITHOUT USING PYAUTOGUI, and without installing additional Python packages.
Also check out my gists for the same script on https://gist.github.com/TejoMukesh (those are more complete).
Unlike most other zoom automations, this one works by using the webbrowser module in Python. This eliminates the need for pyautogui, and the default packages installed with Python are sufficient.
You'll have to tweak the script for it to work without hiccups.

Zoom setup- these settings should be set to on:  
'Turn off my video during a meeting'  
'Mute my audio when joining a meeting'  
'Automatically join audio by computer when joining a meeting' 
  
Desktop setup:
 If you're using a laptop, plug it in to avoid the laptop turning off midway.
 Turn off the setting that puts the computer to sleep after a set amount of time(Set the timer to the biggest possible duration).

Chrome/browser setup:
  When opening a zoom invite link for the first time, the browser will ask permission to open the meeting in the Zoom app. You'll have to check the box that says 'always allow xyz to open links of this kind in abc app' so that you can remove yourself from the equation.
  
Code setup:
 Familiarity with Python or any experience with coding will help.
 Python needs to be installed in your computer. This won't be a problem if you're using a Mac. On Linux distros, make sure to use Python 3.x and not Python 2. If using Windows, install IDLE from https://www.python.org/downloads/windows/.
 
{Configuring Code from the main script}

eng =   'https://us04web.zoom.us/j/123456789/pwd=1?'

maths = 'link'

phys = 'link'

bio ='link'

chem = 'link'

The words 'eng','maths' etc. are in reference to the subject of the class. The corresponding link is the Zoom invite link(this means that there is no need to type a password).Make sure the link starts with something like https://us04web.zoom.us/j/123456789/pwd=1 (notice that it says pwd after the last slash{'/'}). Change the subject names according to your needs and add the corresponding link without forgetting the double quotations (or apostrophes, both have the same effect) on both sides of the link(like the previous example).

Next is a dictionary with the name 'class_times' which is essentially the time table of your classes. Corresponding to each day is a list of class timings and subjects. Change timings and subjects accordingly. Keep the syntax in mind. If an error shows up, leave a question here.

And that's it. You can chill now. If there are any errors(and it's entirely possible), please leave a question and I'll help you out ASAP. 
