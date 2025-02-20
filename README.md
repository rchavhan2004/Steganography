# Data Hiding in Images Using Steganography

<p align="center">
  <img src="https://github.com/user-attachments/assets/30fd11ca-6cc6-48c0-b1a0-c280229e8ba5" alt="Encryption Icon" width="120">
</p>

<p align="center">
  <strong>🔒 A Secure and Invisible Way to Hide Your Secret Messages in Images</strong>
</p>

---

## ⚡ Overview

The Data Hiding in Images Using Steganography project uses image processing techniques to hide secret messages within an image, ensuring that sensitive information is securely encoded without altering the image’s visible appearance. The hidden data is protected with a passcode to guarantee that only authorized users can retrieve it.

### ✨ Features:
- 🖼️ **Invisible Message Embedding:** Hides messages inside the image without any visible distortion.
- 🔑 **Password Protection:** Ensures that only authorized users can access the hidden message.
- 💡 **Password Strength Validation:** Implements checks to ensure secure password creation.
- 🔓 **Message Decryption:** Restores the hidden message from the image using the correct passcode.

---

## 🛠 Technologies Used

- 🐍 Python
- 📸 OpenCV (cv2)
- 🧩 ASCII Encoding
- 🔐 Passcode Protection and Validation
- 🛡️ Regex (for password strength validation)

---

## 🧩 How It Works

1. **Enter Secret Message:**
   - The user inputs a secret message that will be hidden inside the image.
   
2. **Generate Key:**
   - The user provides a passcode to encrypt and decrypt the hidden message.
   
3. **Embed the Message:**
   - The message is encoded and hidden within the image pixels.
   
4. **Decrypt the Message:**
   - Using the correct passcode, the user can retrieve the hidden message from the image.
---

## 🎨 Example Use Case

### Encrypting a Message:
- Place the image (e.g., image.jpg) in the same directory as the script.
- Input the secret message and a passcode.
- The message is hidden inside the image, saved as encryptedImage.jpg.

### Decrypting the Message:
- Use the correct passcode.
- The hidden message is retrieved and displayed.

---

<p align="center">
  <strong>🔒 Hide. Protect. Decode. 🔓</strong>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/9a49c464-b813-487f-8943-d921bc1af323" alt="Secure Icon" width="80">
</p>
