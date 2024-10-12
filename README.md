# Ransomware Simulation Project

## Overview

This project simulates a ransomware attack by generating random files, encrypting them, and displaying a ransom note to the user. It is designed for educational purposes only, to demonstrate how ransomware might operate. 

## Features

- **Random File Generation**: The program creates a specified number of random files in a designated directory.
- **File Encryption**: All files in the target directory are encrypted using symmetric encryption.
- **Decryption Capability**: Users can decrypt the files using a provided key.
- **Ransom Note**: After encryption, a ransom message is displayed to the user.

## Key Components

### 1. Random File Generation

- The program generates random files with various extensions, including common document, image, and compressed file formats.
- The generated files are created in a specified directory, which can be customized.

### 2. Encryption Method

- **Encryption Algorithm**: The program uses the **Fernet** symmetric encryption from the `cryptography` library.
  - **Fernet** provides a secure way to encrypt and decrypt data using a symmetric key. 
  - It employs AES (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode for encryption, which is widely regarded as a secure and efficient encryption method.
  - Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key.
- **Dynamic Encryption Key**: 
  - A unique key is generated at runtime for encrypting files. This key is used to encrypt and decrypt files during the session.
  - The dynamic key is stored in memory and is not saved to disk.
  
### 3. Universal Decryption Key

- **Universal Key**: 
  - A universal decryption key is generated, which is a static key that can be used to decrypt files after encryption. The universal decryption key for this project is **`NLxDQ`**.
  - This key is saved to a text file for future reference and can be reused in subsequent runs of the program.

### 4. Ransom Note

- After encrypting the files, a ransom note is displayed to the user, indicating that their files have been encrypted and requesting a payment in Bitcoin to unlock them.

## File Structure

- The project consists of the main script that handles the file generation, encryption, and GUI.
- A background image can be added for visual enhancement.

## Setup Instructions

1. **Install Required Libraries**:
   - Ensure you have the following libraries installed:
     ```bash
     pip install cryptography pillow randomfiletree
     ```

2. **Modify Target Directory**:
   - Change the `TARGET_DIRECTORY` variable in the code to specify where you want to generate and encrypt files. Make sure the directory exists:
     ```python
     TARGET_DIRECTORY = Path("D:/CIS pbl/test folder")
     ```

3. **Run the Application**:
   - Execute the script using Python. The GUI will appear, allowing you to start the attack or decrypt files.

## Usage

- **Start the Attack**: Click the "Start the Attack" button to generate random files and encrypt all files in the target directory.
- **Decrypt Files**: To decrypt files, click the "Decrypt Files" button and enter the universal key when prompted.
- **About**: Click the "About" button to view information about the project.

## Important Notes

- This project is created for educational purposes only. 
- Use this software responsibly and ensure you have permission to work with any files you encrypt.
- Make sure to test in a controlled environment to avoid unintended data loss.
