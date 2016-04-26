# RetweetPiBot
Retweet Bot in Python - Checks periodically and RT from your favorite Twitter handles. Requires Twitter API Integration.

For python modules and Twitter API configuration please refer to  http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/

(Excerpt below...) 
Getting Started
This project uses Python; a simple programming language ideal for DIY projects. We’ll begin by installing Twython on the Pi – a Python module for interfacing with Twitter; setting up a Twitter “application” to get an API key; then go onto make the Pi tweet stuff on our behalf. It’s going to be so much fun!

I’m doing this on Raspian – but it should in theory work on any Linux-based OS you have on the Pi. If you haven’t already, make sure you set up SSH so we can remotely log in and perform console commands.

Installing Twython
It’s a good idea to run updates first. Copy and paste the following commands one at a time – most will require confirmation.

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-setuptools
sudo easy_install pip (or sudo apt-get install python-pip)
sudo pip install twython
Registering a Twitter app
In order to use the Twitter API – that is, the REST interface that we’ll use to post new Tweets and generally interact with Twitter outisde of the twitter website – we’ll need to register a new app. Do that from this link – you needn’t specify a callback URL, and just make up a website if you want.

You’ll see something resembling this once you’re done – these keys are unique to you.
By default, the app is set to read-only, so we won’t be able to publish tweets without changing that to Read and Write. Go to the Settings tab and change the Application type.
Once saved, head back to the Details tab and click the button at the bottom to create an OAuth access token – this gives your application access to your own Twitter account. Refresh, and leave the page open for later – we’ll need to copy paste some of those keys in a minute.

Can You start the script automatically... Sure
sudo crontab -e
Paste in this line, to start at reboot. The script has a 5-mins loop internally to check and retweet. 

@reboot sudo python /home/pi/ReTweetBot.py & >>/dev/null
Change that to * * * * * if you want it to run every minute, and be prepared to lose followers faster than a Twitter account that loses followers quickly.

I will be extending the code to multiple users,etc. Its quite simple. 
Happy Coding...
