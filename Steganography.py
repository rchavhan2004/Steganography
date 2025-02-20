import cv2
import os
import string
import re

# Function to check password strength
def check_password_strength(password):
    """
    Check the strength of a given password.
    Returns True if strong, False if weak.
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Za-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

# Function to get a strong password
def get_password():
    password = input("Enter a passcode: ")
    while not check_password_strength(password):
        print("Weak password! A strong password must contain at least 8 characters, "
              "including an uppercase letter, a number, and a special character.")
        password = input("Enter a passcode: ")
    return password

# Read image
img = cv2.imread("spidey.jpg")  # Replace with the correct image path

# Get secret message and strong passcode
msg = input("Enter secret message: ")
password = get_password()  # Password strength check

# Initialize encoding/decoding dictionaries
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Embedding the secret message into the image
m, n, z = 0, 0, 0
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save the image with embedded message
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

# Decryption: Ask for passcode
decryption_pass = input("Enter passcode for Decryption: ")

if password == decryption_pass:
    message = ""
    m, n, z = 0, 0, 0
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
