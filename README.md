# PiRRR
![small_PiRRR](https://user-images.githubusercontent.com/46400065/188030123-2c6e3fe4-ec3c-46bd-a4fc-a8844e73b7b5.png)

Pug's iRacing Results Reader is meant to make it easier for league owners to export results from completed iRacing sessions.

What does it do:
- Pre-qualifying Results (Looks for qualifying session if applicable, else it uses the 1st session and it returns best lap times for each driver with car IDs to make sure no one is using the wrong car)
- Full Results 
- Can match drivers to the correct teams by looking for them in a list of teams if provided
- Choice of output in .csv/.xlsx

## Usage

For both versions you can select custom team files and destination files; file extensions are added automatically.
Personally I'd recommend using the JSON versions as they offer more data and are a bit easier to read however the IRSDK version provides the same
basic data although formatting most of it takes way too much effort for what it's worth due to inconsistencies so you'll have to excuse some of the imperfections. 
(none are critical)

### JSON Version
Using the iRacing UI, download the results of the session you want to read (Export results button) and choose the results file.

### iRSDK Version
Joining a session and pressing the IRSDK button while iRacing connection status says True exports results.

### Custom Team File
Here is a template for the custom team file. Team name is the key and the value is an array of driver names (use display names for the particular session you're in).

![image](https://user-images.githubusercontent.com/46400065/187563886-e0408fc4-1763-406f-8bc9-40905bbc6fc4.png)

#### Example of JSON PreQ Version:
![image](https://user-images.githubusercontent.com/46400065/187984924-08e0b227-59ab-46d6-94bf-4141a1e0b434.png)

#### Example of JSON Full Version
![image](https://user-images.githubusercontent.com/46400065/187984982-ff854a52-3504-4067-b234-b976c9730475.png)

### Example of IRSDK Full Version
![image](https://user-images.githubusercontent.com/46400065/188338504-ed183b54-c5d8-47e1-a3f6-420f0bf85810.png)
