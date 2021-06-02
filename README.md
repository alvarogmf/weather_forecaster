# Weather Forecaster

This simple tool creates a screenshot of the weather forecast for Spain at 2pm and 9pm, plus a gif file with the hourly forecast of the day.

## Usage
1. As default, the script is configured to retreive data for Spain at the times mentioned above, to change this, get into the script with an editor, and change in line 32 the hours to retreive (also, in lines 34 and 53 the UTC difference), and in lines 43 and 61, at the end of the stringm the Latitude and Longitude of the central point you desire to retreive the data.
 
2. Once set, run the script and will ask as input what day you want the forecast to be retrieved:
  a. today
  b. tomorrow
  c. day_after
  
3. After selection, the program will open Chrome Windows with the forecast and make screenshots of it. Once it's finished, the Terminal will close.

4. The screenshots and gif will be stored in the 'screenshots' tab. Bear in mind that it will be deleted the next time you run the script.


*Examples of screenshots can be found in the folder*

![Example Gif](https://raw.github.com/alvarogmf/weather_forecaster/edit/main/screenshots/weather_forecast_gif.gif)
