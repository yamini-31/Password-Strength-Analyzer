# Password-Strength-Analyzer
A Password Strength Checker project, based on the SHA1 algorithm , the tool provides immediate feedback on password strength and breach count without storing actual passwords.
This is a simple Python script that allows you to check the strength of your passwords by querying the "Have I Been Pwned" API to see if they have been compromised in any data breaches. It helps you make informed decisions about the security of your passwords.

## How it Works
The script takes one or more passwords as input and calculates a SHA-1 hash of each password. It then sends the first five characters of the hash to the "Have I Been Pwned" API to retrieve a list of hashes that match those first five characters. It then compares the remaining characters of the hash with the retrieved data to see if there is a match. If a match is found, it means the password has been compromised in the past, and the script provides information about the number of times the password has been found in data breaches.

## Features
Check the strength of one or more passwords.
Provides information about whether a password has been compromised.
Suggests changing passwords that have been found in data breaches.

## Running the Code

You have two options to run this code:

### Option 1: Google Colab (Recommended)

1. Click [here](https://colab.research.google.com/your_project.ipynb) to open the code in Google Colab.
2. Sign in with your Google account if prompted.
3. Run the code cells one by one.

### Option 2: Local Environment

1. Clone this repository to your local machine.
2. Install any dependencies with `pip install -r requirements.txt` (if needed).
3. Run the code using your preferred Python interpreter.

Choose the option that suits you best.

## Dependencies
requests: Python library for making HTTP requests.
hashlib: Python library for hashing data.

## Contribution
If you'd like to contribute to this project, please fork the repository and create a pull request with your changes. We welcome contributions and bug reports.

## DO check your Password, Guys!!!
