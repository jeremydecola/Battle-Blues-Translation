import subprocess
import sys
import os
import psutil
import time
import pyautogui
import pyperclip as clipboard
from distutils.dir_util import copy_tree
from distutils import log
project_root = os.path.dirname(os.path.abspath(__file__))

def up_one_dir(path):
    path = path.split("\\")
    path_up_one = ""
    for i in range(len(path)-1):
        path_up_one+=path[i]+"\\"
    return path_up_one

def get_filename(path):
    path = path.split("\\")
    filename = path[len(path)-1]
    return filename

#DECOMPILE THE GAME
def decompile(path):
    root = up_one_dir(path)
    process = subprocess.Popen("OperaFS.exe", shell=True, stdout=subprocess.PIPE)

    time.sleep(1)
    pyautogui.press(['enter'])# Press the enter key
    time.sleep(1)
    clipboard.copy(path)
    pyautogui.hotkey('ctrl', 'v')  # ctrl+v to paste text from clipboard
    #pyautogui.write(path, interval=0.01)
    pyautogui.press(['enter'])# Press the enter key

    #initialize path size and change counter
    prev_path_size = 0
    same_counter = 0
    #loop until 3 seconds have passed without a growth in the size of the directory
    while(same_counter < 3):
        if (os.path.getsize(root) == prev_path_size):
            same_counter+= 1
        else:
            same_counter = 0
        time.sleep(1)
        prev_path_size = os.path.getsize(root)
    #safe to assume de-compilation is complete
    pyautogui.hotkey('alt','f4')# Alt+F4 to close OperaFS
    print("De-Compilation complete!")
    while (psutil.pid_exists(process.pid)):
        print("...")
        time.sleep(1)

#PATCH THE GAME
def patch(path, difficulty, verbose):
    root = up_one_dir(path)
    filename = get_filename(path)
    tmp = filename.split(".")
    path2 = root +"PARCE_"+tmp[0]
    if verbose==1:
        log.set_verbosity(log.INFO)
        log.set_threshold(log.INFO)
    print("Copying translation...")
    copy_tree(project_root +"\\src", path2, verbose=1)

    print("Rebalancing difficulty...")
    # Easy Difficult
    if difficulty == 1:
        copy_tree(project_root +"\\balance\\easy", path2, verbose=1)
        print("Easy difficulty set.")
    # Normal Difficult
    elif difficulty == 2:
        copy_tree(project_root + "\\balance\\normal", path2, verbose=1)
        print("Normal difficulty set.")
    # Hard Difficult
    elif difficulty == 3:
        copy_tree(project_root + "\\balance\\hard", path2, verbose=1)
        print("Hard difficulty set.")
    #Impossible Difficult -> No patching required
    else:
        print("Impossible difficulty set.")
    print("Patching complete!")

#COMPILE THE GAME
def compile(path):
    root = up_one_dir(path)
    filename = get_filename(path)
    tmp = filename.split(".")
    path2 = root + "PARCE_" + tmp[0]
    path3 = root + tmp[0] + "_patched.iso"
    process2 = subprocess.Popen("OperaFS.exe", shell=True, stdout=subprocess.PIPE)
    time.sleep(1)
    pyautogui.press(['tab'])# Press the enter key
    time.sleep(1)
    pyautogui.press(['enter'])# Press the enter key
    time.sleep(1)
    pyautogui.press(['tab'])# Press the enter key
    time.sleep(1)
    clipboard.copy(path2)
    pyautogui.hotkey('ctrl', 'v')  # ctrl+v to paste text from clipboard
    #pyautogui.write(path2, interval=0.01)
    pyautogui.press(['enter'])# Press the enter key
    time.sleep(1)
    clipboard.copy(path3)
    pyautogui.hotkey('ctrl', 'v')  # ctrl+v to paste text from clipboard
    #pyautogui.write(path3, interval=0.01)
    time.sleep(1)
    pyautogui.press(['enter'])# Press the enter key
    #initialize path size and change counter
    prev_path_size = 0
    same_counter = 0
    #loop until 3 seconds have passed without a growth in the size of the directory
    while(same_counter < 3):
        if (os.path.getsize(root) == prev_path_size):
            same_counter+= 1
        else:
            same_counter = 0
        time.sleep(1)
        prev_path_size = os.path.getsize(root)

    #safe to assume compilation is complete
    pyautogui.hotkey('alt','f4')# Alt+F4 to close OperaFS
    print("Compilation complete!")
    while (psutil.pid_exists(process2.pid)):
        print("...")
        time.sleep(5)

#SIGN + REGENERATE ROM_TAGS IN ORDER TO ALLOW THE GAME TO RUN ON AN ORIGINAL (UNMODIFIED) 3DO BIOS
def sign(path):
    root = up_one_dir(path)
    filename = get_filename(path)
    tmp = filename.split(".")
    path3 = root + tmp[0] + "_patched.iso"
    process3 = subprocess.Popen("3DOEncrypt.exe genromtags " + path3,
                            shell=True, stdout=subprocess.PIPE)
    while (psutil.pid_exists(process3.pid)):
        print("Signing iso/img")
        time.sleep(5)
    print("Signing complete!")
    if (process3.returncode == 1):
        sys.exit('Failed to sign iso/img image.')
    print("Patching succesfully complete!")