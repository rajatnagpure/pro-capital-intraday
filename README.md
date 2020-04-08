# pro-capital-intraday


1) Add BuildPacks


On Heroku, open your App. Click on the Settings tab and scroll down to Buildpacks. Add the following:


Python (Select it from the officially supported buildpacks)


Headless Google Chrome: https://github.com/heroku/heroku-buildpack-google-chrome


Chromedriver: https://github.com/heroku/heroku-buildpack-chromedriver


2) Add config variables


Scroll to the config vars section. Here, we will add the paths to Chrome and the Chromedriver. Add the following config vars:


CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver


GOOGLE_CHROME_BIN = /app/.apt/usr/bin/google-chrome
