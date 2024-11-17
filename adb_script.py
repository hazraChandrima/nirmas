# a python script that automatically takes screenshots of a WhatsApp chat in an Android device.
# with the help of Android Debug Bridge (ADB)

# for this, you first need to connect your android device via USB and enable USB debugging (further details mentioned in README.md).
# also, make sure to adjust the coordinates(in lines 88 and 123) according to your Android device.
# The coordinates mentioned in this script are that of Vivo v25 (1080 x 2400).

import subprocess
import time
from PIL import Image, ImageChops
import os
import numpy as np
import shutil
import sys
from colorama import init, Fore, Style
import threading

init()

# Path to the bundled adb.exe
ADB_PATH = os.path.join(os.getcwd(), 'adb-tools', 'adb.exe')


def run_adb_command(command):
    full_command = [ADB_PATH] + command
    subprocess.run(full_command)


def print_colored(text, color, bold=False):
    style = Style.BRIGHT if bold else ""
    print(f"{style}{color}{text}{Style.RESET_ALL}")


def loading_animation():
    animation = "|/-\\"
    idx = 0
    while not loading_done:
        print(f"\r{Fore.YELLOW}Loading {animation[idx % len(animation)]}", end="")
        idx += 1
        time.sleep(0.1)
    print(f"\r{' ' * 20}\r", end="")


def start_loading_animation():
    global loading_done
    loading_done = False
    threading.Thread(target=loading_animation, daemon=True).start()


def stop_loading_animation():
    global loading_done
    loading_done = True
    time.sleep(0.2)


def capture_screenshot(filename):
    start_loading_animation()
    with open(filename, "wb") as file:
        run_adb_command(["exec-out", "screencap", "-p"], stdout=file)
    stop_loading_animation()
    print_colored(f"Captured screenshot: {filename}", Fore.GREEN)


def images_are_equal(img1_path, img2_path, threshold=1000):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    chat_box1 = img1.crop((0, 200, img1.width, img1.height - 200))
    chat_box2 = img2.crop((0, 200, img2.width, img2.height - 200))

    diff = ImageChops.difference(chat_box1, chat_box2)
    diff_array = np.array(diff)
    diff_value = np.sum(diff_array)
    print_colored(f"Difference value: {diff_value}", Fore.CYAN)
    return diff_value < threshold


def perform_swipe():
    try:
        # Adjusted coordinates for my device, Vivo V25 (1080 x 2400)
        run_adb_command(["shell", "input", "swipe", "540", "1200", "540", "2000", "300"])
        print_colored("Performed swipe up gesture", Fore.MAGENTA)
    except Exception as e:
        print_colored(f"Error performing swipe: {e}", Fore.RED)
    time.sleep(1)


def clear_screenshots_folder(folder_path):
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print_colored(f'Failed to delete {file_path}. Reason: {e}', Fore.RED)
        print_colored(f"Cleared contents of {folder_path}", Fore.GREEN)
    else:
        print_colored(f"Screenshots folder {folder_path} does not exist. Creating it.", Fore.LIGHTYELLOW_EX)
        os.makedirs(folder_path)


def main():
    print_colored("WhatsApp Chat Screenshot Capture Tool", Fore.CYAN, bold=True)
    print_colored("======================================", Fore.CYAN)

    chat_name = input(f"{Fore.GREEN}Enter the name of the chat you want to capture: {Style.RESET_ALL}")

    screenshots_folder = "screenshots"
    clear_screenshots_folder(screenshots_folder)

    print_colored("\nInitializing WhatsApp...", Fore.YELLOW)
    run_adb_command(["shell", "am", "force-stop", "com.whatsapp"])
    run_adb_command(["shell", "am", "start", "-n", "com.whatsapp/.Main"])
    time.sleep(2)

    print_colored("Navigating to the specified chat...", Fore.YELLOW)
    run_adb_command(["shell", "input", "tap", "540", "300"])
    time.sleep(1)
    run_adb_command(["shell", "input", "text", chat_name])
    time.sleep(1)
    # Adjusted coordinates for my device, Vivo V25 (1080 x 2400)
    run_adb_command(["shell", "input", "tap", "540", "500"])
    time.sleep(2)

    prev_screenshot = None
    i = 1
    consecutive_equal_count = 0
    max_attempts = 50

    print_colored("\nStarting screenshot capture process...", Fore.LIGHTMAGENTA_EX)
    while i <= max_attempts:
        current_screenshot = f"{screenshots_folder}/screenshot_{i:03d}.png"
        capture_screenshot(current_screenshot)

        if prev_screenshot:
            if images_are_equal(prev_screenshot, current_screenshot):
                consecutive_equal_count += 1
                print_colored(f"Consecutive equal screenshots: {consecutive_equal_count}", Fore.LIGHTBLUE_EX)
                if consecutive_equal_count >= 3:
                    print_colored(
                        f"Reached the top of the chat or no more new content. Stopping after {i} screenshots.",
                        Fore.GREEN)
                    break
            else:
                consecutive_equal_count = 0
                print_colored("New content detected, continuing capture", Fore.GREEN)

        perform_swipe()
        time.sleep(0.5)

        prev_screenshot = current_screenshot
        i += 1

    if i > max_attempts:
        print_colored(f"Reached maximum attempts ({max_attempts}). Stopping.", Fore.LIGHTYELLOW_EX)

    print_colored(f"\nCapture process completed. Total screenshots captured: {i - 1}", Fore.CYAN, bold=True)
    print_colored(f"Screenshots saved in the '{screenshots_folder}' directory.", Fore.CYAN)


if __name__ == "__main__":
    main()
