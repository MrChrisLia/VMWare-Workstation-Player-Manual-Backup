from plyer import notification
import shutil
import ctypes
import datetime


# Backups of the directory of the Kali installation and copies it to a directory called Kali_Backup
# If successful, will create a Windows notification

# Get the current date
current_date = datetime.date.today()

# Format and print the date in "YYYY_MM_DD" format
formatted_date = current_date.strftime('%Y_%m_%d')

def backup():
    success_msg = 'Your automated backup has successfully completed.'

    # r'C:/path/to/directory' lets us avoid having to escape with backslashes 
    source_directory = r'C:\Users\chris\Documents\Virtual Machines\kali-linux-2023.2-vmware-amd64.vmwarevm'
    destination_directory = r'C:\Users\chris\Documents\Virtual Machine Backups\Kali_Backup' + '_' + str(formatted_date)

    shutil.copytree(source_directory, destination_directory)

    notification.notify(
        title='VMWareKali Backup Complete',
        message=success_msg,
        app_name='Backup App',
    )

# Runs the backup function and if it fails, will try to send an error through Windows notifications

def main():
    try:
        backup()
    except (FileExistsError, PermissionError, IsADirectoryError, shutil.Error) as error:
        notification.notify(
            title='VMWareKali Backup Failed',
            message=f'Backup error: {error}',
            app_name='Backup App',
        )

# Creates a yes/no prompt with the Windows API

def run_script_prompt():
    response = ctypes.windll.user32.MessageBoxW(
        0, "Do you want to run the Kali VMWare backup script?", "Kali VMWare Backup", 4 
    )  # 4 corresponds to Yes/No buttons
    if response == 6:  # 6 corresponds to "Yes" button
        main()
    else:
        exit()


if __name__ == '__main__':
    print("[+] The backup will start after accepting the prompt...")
    run_script_prompt()
    print("{+] Backup complete... this window will automatically close in a few seconds... \n[+] Check the notifications for more details.")
    exit()
