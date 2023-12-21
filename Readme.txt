How instagram ban Works
Overview
instagram ban is a tool designed to banish users from social media platforms. The current version focuses on Instagram, but the architecture allows for future expansion to other platforms.

1. instagram ban
Login: The script begins by logging into your Instagram account using the provided credentials.

Access Target Profile: It then accesses the profile page of the target Instagram ID.

Extract User ID: The script scrapes the HTML of the target profile page to extract the user ID of the target Instagram ID.

Banhammer Activation: With the obtained user ID, the script proceeds to unleash the banhammer, sending a request to unfollow or "ban" the target Instagram ID.

Victory Announcement: Upon successful execution, the script announces the banishment of the target Instagram ID.

Usage
Cloning the Repository
	git clone https://github.com/1cYinfinity/instagramban.git
        cd instagramban

Installing Dependencies
						# requirements.txt
							beautifulsoup4==4.10.0
							requests==2.26.0

Running the Script
							python3 instaban.py

Follow the prompts to choose the platform and target user to banish.

Customization
The script can be customized by editing banisher.py and adding new banishment logic for other platforms.
Contribution
Feel free to contribute to instagram ban arsenal by opening issues, submitting pull requests, and expanding the banishment capabilities.

Disclaimer
This tool is purely fictional and should not be used for any harmful or illegal activities. The creator and contributors are not responsible for any misuse.

Credits
Created by 1cYinfinity..
