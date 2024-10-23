import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import sqlite3
import hashlib


# Function to connect to the database and verify login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to the database
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()

    # Execute the query to check the username and password
    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, hashed_password))
    result = cur.fetchone()

    # Display message based on login success or failure
    if result:
        messagebox.showinfo("Login", "Login Successful!")
        home_page()  # Navigate to the home page on successful login
    else:
        messagebox.showerror("Login", "Login Failed!")

    conn.close()


# Function to open the home page window after successful login
def home_page():
    root.withdraw()  # Hide the login window

    home_window = tk.Toplevel()  # Create a new window for the home page
    home_window.title("Home Page")
    home_window.geometry("800x600")  # Increase the resolution of the home page
    home_window.configure(bg="#1c1c1c")

    # Create a canvas to hold the background image and components
    canvas_home = tk.Canvas(home_window, width=800, height=600)
    canvas_home.place(x=0, y=0)

    # Use Pillow to open the home page background image
    bg_image_home = Image.open("/Users/M S I/Desktop/Information Security/background.jpg")  # Replace with the correct path
    bg_image_home = bg_image_home.resize((800, 600), Image.Resampling.LANCZOS)  # Resize the image to fit the canvas
    bg_image_home_tk = ImageTk.PhotoImage(bg_image_home)

    # Place the image on the canvas
    canvas_home.create_image(0, 0, image=bg_image_home_tk, anchor="nw")

    # Welcome message on the home page
    home_label = tk.Label(home_window, text="Welcome to the Home Page!", font=("Arial", 24, "bold"), fg="white", bg="#1c1c1c")
    home_label.pack(pady=50)

    # File upload button
    upload_button = tk.Button(home_window, text="Upload File", font=("Helvetica", 12, "bold"), bg="#8B0000", fg="white", command=upload_file)
    upload_button.pack(pady=20)

    # Create a label to display the preview
    global file_preview_label
    file_preview_label = tk.Label(home_window, text="File preview will be shown here", font=("Arial", 10), fg="white", bg="#1c1c1c")
    file_preview_label.pack(pady=20)

    # Exit Button on the home page
    exit_button = tk.Button(home_window, text="Exit", font=("Helvetica", 12, "bold"), bg="#8B0000", fg="white", command=home_window.destroy)
    exit_button.pack(pady=20)

    home_window.mainloop()


# Function to handle file upload and preview
def upload_file():
    # Allow all files for upload
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("All files", "*.*"),)
    )

    if file_path:
        # Preview the file based on its type
        if file_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            preview_image(file_path)
        else:
            messagebox.showinfo("File Selected", f"File selected: {file_path}")
            file_preview_label.config(text=f"File selected: {file_path}")
    else:
        messagebox.showwarning("No File", "No file was selected.")


# Function to preview image files
def preview_image(file_path):
    try:
        # Open and resize the image
        img = Image.open(file_path)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)  # Resize the image for preview

        # Update the preview label with the image
        img_tk = ImageTk.PhotoImage(img)
        file_preview_label.config(image=img_tk, text="")  # Clear text and show the image
        file_preview_label.image = img_tk  # Keep a reference to avoid garbage collection
    except Exception as e:
        messagebox.showerror("Image Error", f"Failed to preview image: {str(e)}")


# Create the main window
root = tk.Tk()
root.title("Login System")

# Set window size and background color
root.geometry("600x500")
root.configure(bg="#1c1c1c")

# Create a canvas to hold the background image and components
canvas = tk.Canvas(root, width=600, height=500)
canvas.place(x=0, y=0)

# Use Pillow to open the login page background image
bg_image = Image.open("/Users/M S I/Desktop/Information Security/background.jpg")  # Replace with the correct path
bg_image = bg_image.resize((600, 500), Image.Resampling.LANCZOS)  # Resize the image to fit the canvas
bg_image_tk = ImageTk.PhotoImage(bg_image)

# Place the image on the canvas
canvas.create_image(0, 0, image=bg_image_tk, anchor="nw")

# Welcome Label (removed the bg parameter to avoid errors)
welcome_label = tk.Label(root, text="WELCOME", font=("Arial", 24, "bold"))
welcome_label.place(x=170, y=20)

# Sign In Label (removed the bg parameter)
sign_in_label = tk.Label(root, text="Sign In", font=("Arial", 20, "bold"))
sign_in_label.place(x=210, y=70)

# Username Label
username_label = tk.Label(root, text="Username:", font=("Helvetica", 12), fg="white", bg="#1c1c1c")
username_label.place(x=100, y=140)

# Username Entry
username_entry = tk.Entry(root, font=("Helvetica", 12), bg="#333333", fg="white", borderwidth=0)
username_entry.place(x=200, y=140, width=200, height=30)

# Password Label
password_label = tk.Label(root, text="Password:", font=("Helvetica", 12), fg="white", bg="#1c1c1c")
password_label.place(x=100, y=190)

# Password Entry
password_entry = tk.Entry(root, font=("Helvetica", 12), bg="#333333", fg="white", borderwidth=0, show="*")
password_entry.place(x=200, y=190, width=200, height=30)

# Login Button with curved corners and dark red background
login_button = tk.Button(root, text="LOGIN", font=("Helvetica", 12, "bold"), bg="#8B0000", fg="white", borderwidth=0, command=login)
login_button.place(x=200, y=250, width=150, height=35)
login_button.config(highlightbackground="#8B0000", highlightthickness=1)

# Forgot Password Label (dark red, no background color)
forgot_password = tk.Label(root, text="Forgot Password?", font=("Arial", 10), fg="#8B0000", cursor="hand2", bg="#1c1c1c")
forgot_password.place(x=200, y=300)

# No Account Label (no background color)
no_account_label = tk.Label(root, text="No account yet?", font=("Arial", 10), fg="white", bg="#1c1c1c")
no_account_label.place(x=170, y=340)

# Sign Up Label (dark red, no background color)
sign_up_label = tk.Label(root, text="SIGN UP NOW", font=("Arial", 10, "bold"), fg="#8B0000", cursor="hand2", bg="#1c1c1c")
sign_up_label.place(x=290, y=340)

root.mainloop()
