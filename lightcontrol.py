import tkinter as tk
import serial
import time


arduino = serial.Serial('COM3', 9600)
time.sleep(2)  

# Tkinter setup
root = tk.Tk()
root.title("LED Controller - Richa Style ")
root.geometry("400x300")
root.configure(bg="#1e1e2f")

# Status Label (dynamic)
status_label = tk.Label(root, text="Welcome, Richa! ", fg="white", bg="#1e1e2f", font=("Comic Sans MS", 16))
status_label.pack(pady=20)

# Function to turn LED ON
def led_on():
    arduino.write(b'1')
    status_label.config(
        text=" The LED is now ON — Shine bright like a diamond!",
        fg="yellow"
    )
    root.configure(bg="#2e2f00")

# Function to turn LED OFF
def led_off():
    arduino.write(b'0')
    status_label.config(
        text=" LED turned OFF — Darkness suits the night ",
        fg="lightblue"
    )
    root.configure(bg="#001f3f")

# Buttons
on_button = tk.Button(
    root, text=" Turn ON LED", command=led_on,
    bg="#00cc66", fg="white", font=("Arial", 14, "bold"), padx=10, pady=5
)
on_button.pack(pady=10)

off_button = tk.Button(
    root, text="💤 Turn OFF LED", command=led_off,
    bg="#cc0033", fg="white", font=("Arial", 14, "bold"), padx=10, pady=5
)
off_button.pack(pady=10)

# Exit button 
exit_button = tk.Button(
    root, text=" Exit", command=root.destroy,
    bg="gray", fg="white", font=("Arial", 12)
)
exit_button.pack(pady=20)

root.mainloop()
