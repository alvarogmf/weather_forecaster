from selenium import webdriver
import time
import datetime
from datetime import date, timedelta
import schedule
import imageio
import os

TODAY = date.today()
TOMORROW = date.today() + datetime.timedelta(days=1)
DAY_AFTER_TOMORROW = date.today() + datetime.timedelta(days=2)

while True:
    task = str(
        input("Specify the day to pull data. today, tomorrow or day_after:"))
    input_today = task == 'today'
    input_tomorrow = task == 'tomorrow'
    input_day_after = task == 'day_after'

    if input_today or input_tomorrow or input_day_after:
        break
    else:
        print("Sorry, your response was not valid.")
        continue

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def pull_weather(date):
    TARGET_TIMES = [14, 21]
    # TO BE UPDATED IN FUTURE ITERATIONS. Change to 1 or 2 depending on Winter or Sumer Time, respectively.
    utc_diff = 2
    deleting_folder = os.listdir('screenshots/')
    for f in deleting_folder:
        os.remove('screenshots/'+f)
    for i in TARGET_TIMES:
        print(f'Retrieving data for {date} at {i}:00...')
        browser = webdriver.Chrome(
            r'C:\Users\alvaromoradillo\Desktop\Python\weather_forecaster\chromedriver', options=options)
        browser.get(
            f'https://maps.darksky.net/@precipitation_rate,{date},{i - utc_diff},40.788,-0.363,6')
        time.sleep(5)  # Give it some time to load the images
        print('Taking screenshot...')
        browser.save_screenshot(f'screenshots/{date}_{i}_weather.png')
        browser.quit()
        print(f'Weather forecast for {date} at {i}:00 screenshot taken!')


def create_gif(date):
    TARGET_TIMES = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    utc_diff = 2
    deleting_folder = os.listdir('gif_screenshots/')
    for f in deleting_folder:
        os.remove('gif_screenshots/'+f)
    for i in TARGET_TIMES:
        browser = webdriver.Chrome(
            r'C:\Users\alvaromoradillo\Desktop\Python\weather_forecaster\chromedriver', options=options)
        browser.get(
            f'https://maps.darksky.net/@precipitation_rate,{date},{i - utc_diff},40.788,-0.363,6')
        time.sleep(7)  # Give it some time to load the images
        browser.save_screenshot(f'gif_screenshots/{date}_{i}_weather.png')
        browser.quit()
    images = []
    folder = os.listdir('gif_screenshots/')
    for filename in folder:
        images.append(imageio.imread('gif_screenshots/'+filename))
    imageio.mimsave('screenshots/weather_forecast_gif.gif',
                    images, duration=0.75)
    print('gif created!')


print('initializing...')


if task == 'today':
    pull_weather(TODAY)
    create_gif(TODAY)
    print('Data for TODAY retreived!')
elif task == 'tomorrow':
    pull_weather(TOMORROW)
    create_gif(TOMORROW)
    print('Data for TOMORROW retreived!')
elif task == 'day_after':
    pull_weather(DAY_AFTER_TOMORROW)
    create_gif(DAY_AFTER_TOMORROW)
    print('Data for the DAY AFTER TOMORROW retreived!')
else:
    print('There was an error with the input')
