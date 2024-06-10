# Python Program for Finding User Pages Using 8-Digit Hashes

## Description

This Python program is designed to find user pages on a website that uses 8-digit hashes instead of standard authentication systems for access. The program works as follows:

1. Generate all possible 8-digit hashes.
2. Send each hash to the server and check the response.
3. Identify user pages based on valid responses from the server.
4. Store each invalid hash for further analysis or record-keeping.

## Features
- Generates all possible combinations of 8-digit hashes.
- Sends HTTP requests to the website for each generated hash.
- Analyzes server responses to identify valid hashes.
- Stores invalid hashes for further analysis.

## Requirements
- Required libraries: `requests` (for sending requests to the server), pymongo
- Internet access.

## Warning
Using this program to gain unauthorized access to user information without explicit permission from the website owner is against the law and can result in legal consequences. This program is intended for educational purposes and lawful testing only. The user is responsible for any misuse of this program.
