# PiRRR
Pug's iRacing Results Reader is meant to make it easier for league owners to export results from completed iRacing sessions.

What does it do:
- Pre-qualifying Results (Looks for qualifying session if applicable, else it uses the 1st session and it returns best lap times for each driver with car IDs to make sure no one is using the wrong car)
- Can match drivers to the correct teams by looking for them in a list of teams if provided

## Usage
### Manual Version
Using the iRacing UI, download the results of the session you want to read (Export results button). Run the application and provide the directories of your custom team file and the destination of the results file (optional)

### iRSDK Version
Joining a session and pressing the export results button with the custom team file and destination name directories (optional) will return the same results.

### iRacing /data API Version
WIP

### Custom Team File
Here is a template for the custom team file. Team name is the key and the value is an array of driver names (use display names for the particular session you're in).

![image](https://user-images.githubusercontent.com/46400065/187563886-e0408fc4-1763-406f-8bc9-40905bbc6fc4.png)

