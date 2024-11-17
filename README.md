# NIRMAS 
 Tired of manually screenshotting Instagram profiles/posts and WhatsApp chats? Let NIRMAS do the creepy work for you. It logs in, scrolls, and snatches every image while you pretend you're not a stalker-just don’t blame us if you get caught.

## Table of Contents
1. [Setting Up](#setting-up)
2. [WhatsApp Chat Screenshot Capture Tool](#whatsapp-chat-screenshot-capture-tool)
   - [Features](#features)
   - [Requirements](#requirements)
   - [Prerequisites](#prerequisites)
   - [Steps to Enable USB Debugging on Android](#steps-to-enable-usb-debugging-on-android)
   - [Bundled ADB](#bundled-adb)
   - [Running the script](#running-the-script)
3. [Instagram Posts Screenshot Capture Tool](#instagram-posts-screenshot-capture-tool)
   - [Features](#features-1)
   - [Requirements](#requirements-1)
   - [Prerequisites](#prerequisites-1)
   - [Running the script](#running-the-script-1)
4. [Credits](#credits)

<br/>

## Setting up

1. Clone the repo:
   ```bash
   git clone https://github.com/hazraChandrima/nirmas.git
   cd nirmas
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

4. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
---
<br/>

# WhatsApp Chat Screenshot Capture Tool

This Python script automates the process of capturing screenshots of a WhatsApp chat on an Android device. It uses the **Android Debug Bridge (ADB)** to communicate with the device and Python libraries for image processing and comparison.


## Features
- Automatically navigates to a specified WhatsApp chat.
- Captures screenshots of the chat and saves them locally.
- Detects repeated content to avoid redundant screenshots.
- Performs swipe gestures to scroll through the chat.


## Requirements

### Python Dependencies
Ensure you have Python installed on your system. The script uses the following libraries:
- **Pillow** (for image processing)
- **numpy** (for efficient image difference calculation)
- **colorama** (for colored console output)

To install these dependencies, run:
```bash
pip install -r requirements.txt
```   

## Prerequisites
1. An Android device.
2. WhatsApp installed in the Android device.
3. USB Debugging enabled on the device (steps provided below).
4. A USB cable to connect the device to your computer.

---

### Steps to Enable USB Debugging on Android

### 1. Enable Developer Options
1. Open the **Settings** app on your Android device.
2. Scroll down and tap on **About phone** (or **About device**).
3. Find the **Build number** (may be under **Software information**).
4. Tap the **Build number** **7 times** until you see a message: "You are now a developer!"

### 2. Turn on USB Debugging
1. Go back to the **Settings** app.
2. Open **System** (or **Additional settings** on some devices).
3. Tap on **Developer options**.
4. Scroll down and find **USB Debugging**.
5. Toggle **USB Debugging** to **ON**.
6. Confirm the action when prompted.

---

## Bundled ADB

This repository includes the necessary `adb.exe` executable and related files for Windows systems. 

### No Additional Installation Required
- The script automatically uses the included ADB executable in the `adb-tools/` folder.

### Platform Compatibility
- The included ADB is for **Windows only**. For macOS or Linux, download the appropriate ADB tools from the [official Android Developer website](https://developer.android.com/studio/releases/platform-tools).

If you experience any issues with the included ADB, ensure the device is connected properly and that USB Debugging is enabled.

#

## Running the script 
   ```bash
   python adb_script.py
   ```
---
<br/>

# Instagram Posts Screenshot Capture Tool

This Python script automates the process of taking screenshots of an Instagram profile and its posts (images only) using **Selenium WebDriver** and **Chromedriver**. The script ensures compatibility with your installed Chrome version using `chromedriver_autoinstaller`.


## Features
- Logs into an Instagram account.
- Captures a screenshot of the user profile.
- Captures screenshots of all image posts by scrolling through the profile.
- Saves screenshots in a designated folder.



## Requirements

### Python Dependencies
Ensure you have Python installed on your system. The script uses the following libraries:
- **selenium** (for browser automation)
- **chromedriver-autoinstaller** (for ensuring Chromedriver compatibility)
- **colorama** (for colored console output)
- **Pillow** (for image processing)

To install these dependencies, run:
```bash
pip install -r requirements.txt
```   

## Prerequisites
1. Google Chrome installed on your system.
3. Instagram account credentials (username and password).

#
## Running the script 
   ```bash
   python seln_script.py
   ```
---

### Credits

Thanks to [Ayush Jayaswal](https://github.com/ayusjayaswal)(our team leader for SIH), for the idea, and all the guidance!<br/>
I really got to learn so much...
