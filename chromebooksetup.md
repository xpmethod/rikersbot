We are using Lenovo N21 Chromebooks

- Switch to developer mode
-- testing double indent

- Start in Developer mode by holding Esc + Refresh (F3) + Power button

- Press Ctrl + D 

- Press Enter
    - Computer displays "OS verification is OFF", beeps, goes dark, "Your system is transitioning to Developer Modes", reboots 

- Standard chromebook setup
    - Log in to Rikersbot [at] gmail.com 
    - Check version of Google Chrome OS (should update to most recent version on its own) 
    
- Settings> Advanced Settings > Powerwash. Wait for it to reboot, then click "Enable Debugging Features" > Proceed on the start up screen

- Enter Rikersbot [at] gmail [dot] com password, should display "You have successfullly enabled debugging features on this Chrome device." 
-ctrl-alt-f2 to enter shell

- Install Debian 
`sh ~/Downloads/crouton -r stretch -t lxde -n debian`

`-r` is the release. We need to set this to stretch, which is the testing branch of Debian. If the -r switch is not passed Ubuntu will be installed.

`-t` is the target command that specifies what GUI interface you want installed by default. Gnome is the default gui for kali however it does not work on my HP Chromebook 14″. KDE works and is a  good alternative to Gnome.

`-n` is the name parameter. We define the -n switch here so we can give the chroot a custom name of debian.

- launch lxde from crosh
`Ctrl+Alt+t` to launch crush, then `shell`, and `sudo startlxde`

- you can flip through running chroot desktops by pressing `ctrl+alt+shift+Back/Forward`

- install atom, ipython, and ipython notebook
in the lxde terminal run `sudo apt-get install ipython ipython-notebook`
