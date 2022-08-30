import easygui
import irsdk
import json
import csv


class PreQualifyingResultsReader:

    def __init__(self, filename, teamfilename=None, destination="results.csv"):
        self.source_file_name = filename
        self.source_team_file_name = teamfilename
        self.destination_file_directory = destination
        self.read_team_file()
        self.handle_results()

    def handle_results(self):
        with open(self.source_file_name) as file:
            entry_data = [("Driver ID","Driver Name", "Best Lap Time", "Team Name", "Car ID")]  # Creating an empty array to store the data for each entry
            file_data = json.load(file)  # Reading json file
            session_results_data = file_data["session_results"]  # Focusing only on session results section
            if session_results_data[1]["simsession_name"] == "QUALIFY":  # Pre-qualifying is typically in Qualifying
                target_session_number = 1
            else:  # If qualifying didn't occur in your session, then take practice instead.
                target_session_number = 0

            target_session_data = session_results_data[target_session_number]  # Focusing on the pre-qualifying session
            target_session_results = target_session_data[
                "results"]  # Focusing on the results of the pre-qualifying session
            for i in target_session_results:
                driver_id = i["cust_id"]
                driver_name = i["display_name"]
                driver_best_lap = i["best_lap_time"]
                driver_best_lap = self.convert_laptime(driver_best_lap)  # Converting the laptime to a human format
                car_id = i["car_id"]
                team_name = self.find_team_name(driver_id, driver_name)
                temp = (
                    driver_id, driver_name, driver_best_lap, team_name,
                    car_id)  # Tuple of relevant driver data to make it a 2D list
                entry_data.append(temp)  # Appending the data for each entry to the array

        with open(self.destination_file_directory, "w", newline='') as file:
            writer = csv.writer(file, delimiter=";")  # CSV writer module
            writer.writerows(entry_data)  # Writing the data to the file

    def convert_laptime(self, laptime):
        number = str(laptime)
        try:
            if len(number) == 6:
                minutes = int(number[0:2]) // 60;
                seconds = int(number[0:2]) % 60;
                milliseconds = int(number[2:5]);
                result = (f'{seconds}.{milliseconds}')
                if seconds < 10:
                    seconds = str(f'0{seconds}')
                result = str(f'{minutes}:{seconds}.{milliseconds}')
                return result
            elif len(number) == 7:
                minutes = int(number[0:3]) // 60;
                seconds = int(number[0:3]) % 60;
                milliseconds = number[3:6]
                if seconds < 10:
                    seconds = str(f'0{seconds}')
                result = str(f'{minutes}:{seconds}.{milliseconds}')
                return result
            else:
                return "Error"
        except Exception:
            return "Error"

    def find_team_name(self, id=None, name=None):
        def linear_search(target, dictionary):
            for i in dictionary:
                if target in dictionary[i]:
                    return i
            return None

        if id is None and name is None:
            return "Error"
        elif id is not None and name is None:
            return linear_search(id, self.team_file_data)
        else:
            return linear_search(name, self.team_file_data)

    def read_team_file(self):
        with open(self.source_team_file_name) as file:
            self.team_file_data = json.load(file)


results_reader = PreQualifyingResultsReader("iracing-result-50707167.json", "teams.json", "results1.csv")
