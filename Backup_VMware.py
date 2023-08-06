from plyer import notification
import shutil
import ctypes


# Backups of the directory of the Kali installation and copies it to a directory called Kali_Backup
# If successful, will create a Windows notification

def backup():
    success_msg = 'Your automated backup has successfully completed.'

    # r'C:\path\to\directory' lets us avoid having to escape with backslashes 
    source_directory = r'C:\path\to\directory'
    destination_directory = r'C:\path\to\directory'

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
    run_script_prompt()
