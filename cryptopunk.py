#!/bin/python3

# 11/28/2021
# Made by DanChan
# NFT Stealer (CryptoPunk)


import requests
import os

# Check if "images" folder exists, if not, create it

if not os.path.exists('./images'):
    os.mkdir('./images')

# Iterate through numbers 0000 - 9999
for i in range(10000):
    formatted_number = f"{i:04d}"

    # Check if image already exists, if it does, skip it
    if os.path.exists(f'./images/{formatted_number}.png'):
        print(f"CryptoPunk #{formatted_number} already downloaded, skipping")
        
    else:
        # Make the request to the URL to get the image
        image = requests.get(f"https://www.larvalabs.com/public/images/cryptopunks/punk{formatted_number}.png")

        # If the URL returns status code "200 Successful", save the image into the "images" folder.
        if image.status_code == 200:
            file = open(f"./images/{formatted_number}.png", "wb+")
            file.write(image.content)
            file.close()
            print(f"CryptoPunk #{formatted_number} successfully downloaded!")
        
        # If the URL returns a status code other than "200 Successful", alert the user and don't save the image
        else:
            print(f"CryptoPunk #{formatted_number} returned HTTP Status {image.status_code}, skipping")
