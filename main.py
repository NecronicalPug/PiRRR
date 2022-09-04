import sys

import easygui
import irsdk
import json
import csv
import openpyxl

import main_ui
from PySide6 import QtGui, QtCore, QtWidgets


class ResultsReader:
    def set_source_file(self, filename):
        self.source_file_name = filename

    def set_team_file(self, teamfilename=None):
        if not (teamfilename == "None" or teamfilename is None):
            self.source_team_file_name = teamfilename
            self.read_team_file()
        else:
            self.source_team_file_name = None

    def set_destination_file(self, destination="results.csv"):
        self.destination_file_directory = destination

    def set_output_type(self, output_type=".xlsx"):
        self.output_type = output_type

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


class PreQualifyingJSONResultsReader(ResultsReader):
    def handle_results(self):
        if not (self.source_file_name is None):
            with open(self.source_file_name) as file:
                entry_data = [("Driver ID", "Driver Name", "Best Lap Time",
                               "Car ID",
                               "Team Name (if applicable)")]  # Creating an empty array to store the data for each entry
                file_data = json.load(file)  # Reading json file
                session_results_data = file_data["session_results"]  # Focusing only on session results section
                if session_results_data[1]["simsession_name"] == "QUALIFY":  # Pre-qualifying is typically in Qualifying
                    target_session_number = 1
                else:  # If qualifying didn't occur in your session, then take practice instead.
                    target_session_number = 0

                target_session_data = session_results_data[
                    target_session_number]  # Focusing on the pre-qualifying session
                target_session_results = target_session_data[
                    "results"]  # Focusing on the results of the pre-qualifying session
                for i in target_session_results:
                    driver_id = i["cust_id"]
                    driver_name = i["display_name"]
                    driver_best_lap = i["best_lap_time"]
                    driver_best_lap = self.convert_laptime(driver_best_lap)  # Converting the laptime to a human format
                    car_id = i["car_id"]
                    if not (self.source_team_file_name is None):
                        team_name = self.find_team_name(driver_id, driver_name)
                        temp = (
                            driver_id, driver_name, driver_best_lap,
                            car_id, team_name)  # Tuple of relevant driver data to make it a 2D list
                    else:
                        temp = (
                            driver_id, driver_name, driver_best_lap,
                            car_id)  # Tuple of relevant driver data to make it a 2D list
                    entry_data.append(temp)  # Appending the data for each entry to the array

            if self.output_type == ".csv":
                with open(self.destination_file_directory, "w", newline='') as file:
                    writer = csv.writer(file, delimiter=";")  # CSV writer module
                    writer.writerows(entry_data)  # Writing the data to the file
            else:
                workbook = openpyxl.Workbook()
                worksheet = workbook.active
                for i in entry_data:
                    worksheet.append(i)
                workbook.save(self.destination_file_directory)

class FullJSONResultsReader(ResultsReader):

    def read_results(self):

        with open(self.source_file_name) as file:  # Opening file
            everything = []
            data = json.load(file)
            sessionresultsdata = data["session_results"]  # Reading just the session_results out of everything
            for i in sessionresultsdata:
                workaround = []  # Having to use a workaround to write a single word to the array.
                workaround.append(i["simsession_name"])
                header = ["Driver ID","Position", "Name", "Car Number", "Car ID", "Interval", "Fastest Lap", "Average Laps",
                          "Laps Completed","Team Name (if applicable)","","Old iRating", "New iRating", "iRating Change", "Old SR Level",
                          "New SR Level", "SR Change", "Old CPI", "New CPI"]  # Header above all rows.
                everything.append(workaround)
                everything.append(header)

                self.leader_laps_complete = i["results"][0]["laps_complete"]
                for x in i["results"]:  # Looping for each driver to read their data.
                    temparray = []
                    driver_id = x["cust_id"]
                    driver_name = x["display_name"]
                    position = x["finish_position"]
                    position += 1
                    lapscomplete = x["laps_complete"]
                    averagelap = x["average_lap"]
                    averagelap = self.find_lap(averagelap)
                    bestlap = x["best_lap_time"]
                    bestlap = self.find_lap(bestlap)
                    carid = x["car_id"]
                    #carname = self.carids(carid)
                    carnumber = x["livery"]["car_number"]
                    interval = x["interval"]
                    intervalresult = self.find_interval(interval, lapscomplete)
                    newirating = int(x["newi_rating"])
                    oldirating = int(x["oldi_rating"])
                    iratingchange = newirating - oldirating
                    newsublevel = int(x["new_sub_level"])
                    oldsublevel = int(x["old_sub_level"])
                    srchange = newsublevel - oldsublevel;srchange = self.format_sr_change(srchange)
                    oldcpi = x["old_cpi"]
                    newcpi = x["new_cpi"]
                    temparray.append(driver_id)
                    temparray.append(position)
                    temparray.append(driver_name)
                    temparray.append(carnumber)
                    temparray.append(carid)
                    temparray.append(intervalresult)
                    temparray.append(bestlap)
                    temparray.append(averagelap)
                    temparray.append(lapscomplete)  # Appending to temporary array.
                    if not (self.source_team_file_name is None):
                        team_name = self.find_team_name(driver_id, driver_name)
                        temparray.append(team_name)
                    else:
                        temparray.append("")
                    temparray.append("")
                    temparray.append(oldirating)
                    temparray.append(newirating)
                    temparray.append(iratingchange)
                    temparray.append(oldsublevel)
                    temparray.append(newsublevel)
                    temparray.append(srchange)
                    temparray.append(oldcpi)
                    temparray.append(newcpi)
                    everything.append(temparray)

            if self.output_type == ".csv":
                with open(self.destination_file_directory, "w", newline='') as file:
                    writer = csv.writer(file, delimiter=";")  # CSV writer module
                    writer.writerows(everything)  # Writing the data to the file
            else:
                workbook = openpyxl.Workbook()
                worksheet = workbook.active
                for i in everything:
                    worksheet.append(i)
                workbook.save(self.destination_file_directory)

    def format_sr_change(self, srchange):
        if srchange < 0:
            if srchange > -100 and srchange <= -10:
                srchange = str(srchange)
                srchange = (f"-0.{srchange[1:]}")
            elif srchange > -10:
                srchange = str(srchange)
                srchange = (f"-0.0{srchange[1:]}")

            return float(srchange)

        elif srchange > 0:
            srchange = str(srchange)
            if len(srchange) == 1:
                srchange = (f"0.0{srchange}")
            elif len(srchange) == 2:
                srchange = (f"0.{srchange}")
            else:
                srchange = (f"{srchange[0]}.{srchange[1:]}")
            return float(srchange)

        else:
            return (0)

    def carids(self, carid):  # Function to find the car make assigned to car ids in iracing.
        if carid == 43:
            return ("Mclaren MP4-12C")
        elif carid == 59:
            return ("Ford GT3")
        elif carid == 72:
            return ("Mercedes AMG")
        elif carid == 73:
            return ("Audi R8 LMS")
        elif carid == 94:
            return ("Ferrari 488")
        elif carid == 132:
            return ("BMW M4 Prototype")
        elif carid == 133:
            return ("Lamborghini Huracan Evo")
        else:
            return ("Error")

    def find_interval(self,
                      number, laps_completed):  # Used to determine what the interval will be like, sucks that it's so complicated.
        number = str(number)
        if len(number) == 4:
            seconds = 0;
            milliseconds = number[0:3];
            result = (f'{seconds}.{milliseconds}')
            return result
        elif len(number) == 5:
            seconds = number[0];
            milliseconds = number[1:4];
            result = (f'{seconds}.{milliseconds}')
            return result
        elif len(
                number) == 6:  # This is far more complicated than I'd like, but that's what happens when you cross over pure seconds.milliseconds and minutes.seconds.milliseconds.
            seconds = int(number[0:2]);
            milliseconds = number[2:5]
            if seconds < 60:
                result = (f'{seconds}.{milliseconds}')
                return result
            else:  # Adding minutes.
                minutes = int(number[0:2]) // 60;
                seconds = int(number[0:2]) % 60
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
        elif int(number) <= 0:
            if int(number) == 0:
                return "Leader"
            elif int(number) < 0:
                laps_down = self.leader_laps_complete - laps_completed
                return (f'{laps_down} laps')
        else:
            return "Error"

    def find_lap(self, number):
        number = str(number)
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


class MainWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.output_file_format = ".csv"
        self.preq_json_reader = PreQualifyingJSONResultsReader()
        self.full_json_reader = FullJSONResultsReader()
        self.pushButton_3.clicked.connect(self.set_results_file_directory)
        self.pushButton.clicked.connect(self.set_team_file_directory)
        self.pushButton_2.clicked.connect(self.set_destination_file_directory)
        self.pushButton_4.clicked.connect(self.toggle_output_type)
        self.preq_json.clicked.connect(self.run_preq_json_reader)
        self.full_json.clicked.connect(self.run_full_json_reader)

    def run_preq_json_reader(self):
        self.preq_json_reader.set_source_file(str(self.results_file_directory.text()))
        self.preq_json_reader.set_team_file(str(self.team_file_directory.text()))
        self.preq_json_reader.set_destination_file(str(self.destination_file_directory.text()))
        self.preq_json_reader.set_output_type(str(self.output_file_format))
        self.preq_json_reader.handle_results()
        
    def run_full_json_reader(self):
        self.full_json_reader.set_source_file(str(self.results_file_directory.text()))
        self.full_json_reader.set_team_file(str(self.team_file_directory.text()))
        self.full_json_reader.set_destination_file(str(self.destination_file_directory.text()))
        self.full_json_reader.set_output_type(str(self.output_file_format))
        self.full_json_reader.read_results()

    def set_results_file_directory(self):
        dir = easygui.fileopenbox(filetypes=["*.json"])
        self.results_file_directory.setText(dir)

    def set_team_file_directory(self):
        dir = easygui.fileopenbox(filetypes=["*.json"])
        self.team_file_directory.setText(dir)

    def set_destination_file_directory(self):
        self.destination_file_dir = easygui.filesavebox()
        self.destination_file_directory.setText(f"{self.destination_file_dir}{self.output_file_format}")

    def toggle_output_type(self):
        if self.output_file_format == ".csv":
            self.output_file_format = ".xlsx"
            self.output_type.setText(".xlsx")
        else:
            self.output_file_format = ".csv"
            self.output_type.setText(".csv")
        try:
            self.destination_file_dir
        except:
            self.destination_file_directory.setText(f"results{self.output_file_format}")
        else:
            self.destination_file_directory.setText(f"{self.destination_file_dir}{self.output_file_format}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
