# Installing Linux on Lenovo N21 Chromebooks

- Switch to developer mode
  - `Esc + Refresh (F3) + Power`
  - `Ctrl + D` out of "Chrome OS is missing `"Enter` until you see "OS verification is OFF", `Ctrl + D` until you see "Your system is transitioning to Developer Modes" and reboot 

- Enable debugging features (lower right on the first login screen)
  - set developer password (all passwords should be the same for rikersbot)

- Change default user password
  - `Ctrl + Alt + F2` to enter the sytem shell
  - log in as `root` and enter the dev password
  - run `chromeos-setdevpasswd` and set to the same as dev password
  - `Ctrl + Alt + F1` to return to the login screen and finish setting up the default account

- Install Crouton
  - install crouton extension
  - download crouton
  - `Ctrl + Alt + t` to enter crosh
  - `cd /home/user/[long number]/Downloads`

- Install Debian (this will take a while)
  - `sudo sh ~/Downloads/crouton -r stretch -t lxde -n debian`

> `-r` is the release. We need to set this to stretch, which is the testing branch of Debian. If the -r switch is > not passed Ubuntu will be installed.
>
> `-t` is the target command that specifies what GUI interface you want installed by default. Gnome is the 
> default gui for kali however it does not work on my HP Chromebook 14″. KDE works and is a  good alternative to > Gnome.
>
> `-n` is the name parameter. We define the -n switch here so we can give the chroot a custom name of debian.

- launch lxde from crosh
  - `Ctrl+Alt+t` to launch crush, then `shell`, and `sudo startlxde`
  - you can flip through running chroot desktops by pressing `ctrl+alt+shift+Back/Forward`

- prepare the dev environment
  - install atom, ipython, and ipython notebook, in the lxde terminal run `sudo apt-get install ipython ipython-notebook`