# PiRRR
Pug's iRacing Results Reader is meant to make it easier for league owners to export results from completed iRacing sessions.

What does it do:
- Pre-qualifying Results (Looks for qualifying session if applicable, else it uses the 1st session and it returns best lap times for each driver with car IDs to make sure no one is using the wrong car)
- Full Results 
- Can match drivers to the correct teams by looking for them in a list of teams if provided

## Usage

### JSON Version
Using the iRacing UI, download the results of the session you want to read (Export results button). Run the application and provide the directories of your custom team file and the destination of the results file (optional)

### iRSDK Version
Joining a session and pressing the export results button with the custom team file and destination name directories (optional) will return the same results.

Do note that the results are all in .csv. You will have to import it into something like Excel for it to be truly readable, which is a few clicks to do but is still extra effort.

### Custom Team File
Here is a template for the custom team file. Team name is the key and the value is an array of driver names (use display names for the particular session you're in).

![image](https://user-images.githubusercontent.com/46400065/187563886-e0408fc4-1763-406f-8bc9-40905bbc6fc4.png)

#### Example of PreQ Version:
![image](https://user-images.githubusercontent.com/46400065/187984924-08e0b227-59ab-46d6-94bf-4141a1e0b434.png)

#### Example of Full Version
![image](https://user-images.githubusercontent.com/46400065/187984982-ff854a52-3504-4067-b234-b976c9730475.png)
