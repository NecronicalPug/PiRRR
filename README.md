# PiRRR
![small_PiRRR](https://user-images.githubusercontent.com/46400065/188030123-2c6e3fe4-ec3c-46bd-a4fc-a8844e73b7b5.png)

Pug's iRacing Results Reader is meant to make it easier for league owners to export results from completed iRacing sessions.

What does it do:
- Pre-qualifying Results (JSON Version = Looks for quali session else it takes the 1st session, IRSDK Version = Takes current session)
- Full Results (Goes through all sessions and exports most of the relevant data)
- Can match drivers to the correct teams by looking for them in a list of teams if provided
- Choice of output in .csv/.xlsx

## Usage
Simply download and run the .exe in Releases.

For all three versions you can select custom team files and destination files; file extensions are added automatically.
Personally I'd recommend using the JSON versions as they offer more data and are a bit easier to read however the IRSDK version provides the same
data although there are formatting imperfections that may show up.

### JSON Version
Using the iRacing UI, download the results of the session you want to read (Export results button in the iRacing UI) and choose the results file.
PreQ Version = Looks for qualifying session, else it uses the 1st session
Full Version = Takes all sessions

### iRSDK Version
Joining a session and pressing the IRSDK button while iRacing connection status says True exports results.
PreQ Version - Takes the session you're currently in and data up to right now.
Full Version - Takes all the sessions and data up to right now.

### /data API Version
By providing your iRacing login details and the desired session ID, you can fetch the session results via the iRacing website instead of manually exporting them
from the iRacing UI. No login details are stored once the app is closed, the cookies file is used to reduce login attempts to the website.

It is the JSON version without the manual results fetching.

![image](https://user-images.githubusercontent.com/46400065/189555254-3073476e-1c21-4b87-9242-3fc129440c49.png)


### Custom Team File
Here is a template for the custom team file. Team name is the key and the value is an array of driver names (use display names for the particular session you're in).

![image](https://user-images.githubusercontent.com/46400065/187563886-e0408fc4-1763-406f-8bc9-40905bbc6fc4.png)

#### Example of JSON PreQ Version:
![image](https://user-images.githubusercontent.com/46400065/188755581-5fc7d4d3-f810-4072-b1d1-ca56c1c0da4e.png)

#### Example of JSON Full Version
![image](https://user-images.githubusercontent.com/46400065/188755663-484f6abc-f665-4654-bfa6-c41618c154a0.png)

### Example of IRSDK PreQ Version:
![image](https://user-images.githubusercontent.com/46400065/188755753-116521db-97cc-4350-a9b9-7cf691815a94.png)

### Example of IRSDK Full Version
![image](https://user-images.githubusercontent.com/46400065/188338504-ed183b54-c5d8-47e1-a3f6-420f0bf85810.png)


## Modifications
If you'd like to modify the code, download the source code and run the following in Windows Terminal:
```
pip install -r requirements.txt
```
Source code was written with PyCharm on Python 3.10.
