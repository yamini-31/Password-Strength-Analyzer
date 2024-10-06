import requests
import hashlib
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def check_password():
    password = entry.get()
    if not password:
        messagebox.showerror("Input Error", "Please enter a password.")
        return
    
    try:
        count = pwned_api_check(password)
        if count:
            messagebox.showwarning("Password Compromised", f'{password} was found {count} times! You should probably change it.')
        else:
            messagebox.showinfo("Password Safe", f'{password} was NOT found. Carry on!')
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
root = tk.Tk()
root.title("Password Checker")
root.geometry("350x200")  # Set window size

# Set style for modern look
style = ttk.Style()
style.theme_use('clam')

# Create and place the label and entry for the password
label = ttk.Label(root, text="Enter Password:", font=("Helvetica", 12))
label.pack(pady=20)

entry = ttk.Entry(root, show="*", font=("Helvetica", 12), width=25)
entry.pack(pady=10)

# Create and place the "Check Password" button
button = ttk.Button(root, text="Check Password", command=check_password)
button.pack(pady=20)

# Run the application
root.mainloop()


