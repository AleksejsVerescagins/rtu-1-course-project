import os
import time

def remove_old_files(folder_path, days_threshold=7):
    # Laika iegūšana
    current_time = time.time()

    # Pārlūkojiet visus failus norādītajā mapē
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Pārbauda, ​​vai objekts ir fails
        if os.path.isfile(file_path):
            # Notiek faila pēdējās mainīšanās laika iegūšana
            file_mtime = os.path.getmtime(file_path)

            # Aprēķiniet laika starpību starp pašreizējo laiku un laiku, kad fails tika pēdējoreiz mainīts
            time_difference = current_time - file_mtime

            # Pārbaudiet, vai laika starpība pārsniedz sliekšņa vērtību (sekundēs)
            if time_difference > (days_threshold * 24 * 3600):
                # Izdzēšam failu, jo tas ir vecāks par norādīto slieksni
                os.remove(file_path)
                print(f"Fails {filename} noņemts, jo tas ir vecāks par {days_threshold} dienām.")

if __name__ == "__main__":
    # Norādiet ceļu uz lejupielādes mapi
    download_folder = "C:/Users/Main/Downloads"

    # Mēs dzēšam failus, kas vecāki par 1 nedēļu
    remove_old_files(download_folder)
