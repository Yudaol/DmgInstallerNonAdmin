# DmgInstallerNonAdmin

A DMG installer without admin privileges.

## Simple Version

1. Download the release: `Dmginstaller.app`.
2. Extract the contents.
3. Execute the application!

## Advanced Version

1. Download and extract the Python file.
2. Open your terminal and run:
    ```bash
    python3 dmginstaller.py
    ```
    or provide the path to your Python file.

Follow the next steps in the application.

## Building from Python to App

1. Install `py2app`:
    ```bash
    pip3 install py2app
    ```
2. Create the `setup.py` file:
    ```bash
    py2applet --make-setup dmginstaller.py
    ```
3. Build the application:
    ```bash
    python3 setup.py py2app
    ```
4. Find the application in the `dist` folder.

### Note

If the application doesn't appear in Launchpad, open it from your Applications folder first: `/Users/YOURNAME/Applications`.

Enjoy!
