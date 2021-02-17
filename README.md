# AmazonBot
## This is designed for Xbox Series X
This is still a working progress 

***

## To Set up On Pi

Make sure python 3.6 or greater is installed

1. Then run:

    * `sudo apt-get install git`

    * `sudo apt-get install chromium-chromedriver`

    * `git clone https://github.com/Jacrac04/AmazonBot.git`

    * `cd AmazonBot`

    * `pip install requirements.txt`

2. Rename `example_config.ini` to `config.ini` 

3. Inside `config.ini` set your username and password

4. Then run:
    * `python3 main.py`

***

## To Set up On Windows

1. Make sure python 3.6 or greater is installed

2. Download Chrome Driver for your chrome version from: https://chromedriver.chromium.org/downloads

3. Download this repository

4. Unzip it and install `requirements.txt`

5. Rename `example_config.ini` to `config.ini` 

6. Inside `config.ini` set `CHROME_DRIVER_LOCATION` to the location of your `chromedriver.exe`

7. Inside `config.ini` set your username and password

8. Then run `main.py`

***

## Todo

- [x] Finsih general buying part
  - [ ] Test general buying part
- [ ] Improve the main part (add multiple buys etc)
- [ ] Read email for verfication
- [ ] Message when in stock 
- [ ] Discord bot module
