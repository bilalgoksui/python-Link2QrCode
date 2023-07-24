import tkinter as tk
import qrcode

def generate_qr_code():
    link = entry_link.get()
    qr = qrcode.make(link)
    qr.save("qrcode.png")
    status_label.config(text="QR code created and saved: qrcode.png")

app = tk.Tk()
app.title("Link to QR Code Converter")
app.geometry("300x150")

label = tk.Label(app, text="Enter a link to generate a QR code:")
label.pack(pady=10)

entry_link = tk.Entry(app, width=30)
entry_link.pack(pady=5)

generate_button = tk.Button(app, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
