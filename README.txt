-- This bot only works with Google Chrome and as such you must have Chrome
   installed

How to Use:
1. You must have the drivers for your installed version of Chrome installed and
   added to your Path variable, skip to step 3 if you have already done this
   a) To do this first visit this link:
      https://sites.google.com/a/chromium.org/chromedriver/downloads and then
      download the version that corresponds to your installed version of Chrome
   b) Unzip the downloaded zip file and you should find a file called
      "chromedriver.exe"
         -- If you are using Windows, then store this file anywhere on your
            computer and continue reading
         -- If you are using Mac or Linux, simply place this file in /usr/bin or
            /usr/local/bin and skip ahead to step 3 (Note: this bot has not been
            tested on any operating system aside from Windows)
   c) In the windows search bar, search for "environment variables" and hit
      enter
   d) A window should pop up called "System Properties", hit the "Environment
      Variables..." button
   e) In either the user variables or system variables section (it should not
      matter which you pick), click on the variable called "Path" and hit edit
   f) Click the "New" button in the window that appears and copy and paste the
      path to the directory where your chromedriver.exe file is stored
   g) Hit "OK" to close all 3 windows
2. To start the bot, run the application.exe file located in dist/application
   directory of this folder
3. Fill out the fields and select your options and then hit the "Submit" button
   to start the bot
   a) In order to do the "Learn" or "Review" exercises for a level, you MUST
      first store the words for that level by using the "Store" option
      -- You do not need to fill out the "Percentage of Accuracy" or "Sessions"
         options if you are simply storing the terms for a level
      -- If you have already stored the terms for a level, you will get an error
         if you try to store the terms for that level again and the process will
         fail
