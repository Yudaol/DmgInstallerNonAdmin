# DmgInstallerNonAdmin
An dmg installer without admin privilege

# simple version
1- download release: Dmginstaller.app

2- extract

3- execute it!!


# hard...
1- Download and extract the python file

2- open your terminal and type this:
```
python3 dmginstaller.py
```
or the path of your python file

and see next step in the app...

# build from python to app
1- install py2app
```
pip3 install py2app
```
2- build the setup.py
```
py2applet --make-setup dmginstaller.py
```
3- build the app
```
python3 setup.py py2app
```
4- find it in the dist folder 







if the app doesn't appear on launchpad you should open it from your app folder first in /Users/YOUNAME/Applications

Enjoy!!!
