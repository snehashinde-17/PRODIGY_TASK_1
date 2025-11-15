import tkinter as tk
from tkinter import messagebox

# Function to perform encryption or decryption
def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26  # Normalize the shift value to stay within the alphabet

    for char in text:
        if char.isalpha():  # Process alphabet characters only
            shift_base = 65 if char.isupper() else 97
            if mode == "Encrypt":
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == "Decrypt":
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabet characters remain the same
    return result

# Function to handle the button click event
def process_cipher():
    message = entry_message.get()
    shift = entry_shift.get()

    # Validate input
    if not message:
        messagebox.showerror("Input Error", "Please enter a message.")
        return

    if not shift.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid shift value (numeric).")
        return

    shift = int(shift)
    mode = mode_var.get()

    # Call the caesar_cipher function
    result = caesar_cipher(message, shift, mode)

    # Display the result
    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher App")
root.geometry("400x300")

# Create widgets
label_message = tk.Label(root, text="Enter message:")
label_message.pack(pady=5)

entry_message = tk.Entry(root, width=40)
entry_message.pack(pady=5)

label_shift = tk.Label(root, text="Enter shift value:")
label_shift.pack(pady=5)

entry_shift = tk.Entry(root, width=40)
entry_shift.pack(pady=5)

label_mode = tk.Label(root, text="Choose mode:")
label_mode.pack(pady=5)

mode_var = tk.StringVar(value="Encrypt")  # Default value is "Encrypt"
radio_encrypt = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt")
radio_encrypt.pack()

radio_decrypt = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt")
radio_decrypt.pack()

button_process = tk.Button(root, text="Process", command=process_cipher)
button_process.pack(pady=10)

label_result = tk.Label(root, text="Result:")
label_result.pack(pady=5)

entry_result = tk.Entry(root, width=40)
entry_result.pack(pady=5)

# Run the app
root.mainloop()
