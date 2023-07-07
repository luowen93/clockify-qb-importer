import tkinter as tk
from tkinter import filedialog
from aligned_vision_qb import create_invoice
class FileDropApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Drop App")
        self.master.geometry("400x400")

        self.file_label = tk.Label(self.master, text="Select file")
        self.file_label.pack(pady=20)

        self.date_label = tk.Label(self.master, text="Invoice date")
        self.date_label.pack(pady=5)
        self.date_entry = tk.Entry(self.master)
        self.date_entry.pack()

        self.number_label = tk.Label(self.master, text="Invoice number")
        self.number_label.pack(pady=5)
        self.number_entry = tk.Entry(self.master)
        self.number_entry.pack()

        self.csv_label = tk.Label(self.master, text="Input CSV")
        self.csv_label.pack(pady=5)
        self.csv_entry = tk.Entry(self.master)
        self.csv_entry.pack()

        self.customer_label = tk.Label(self.master, text="Customer")
        self.customer_label.pack(pady=5)
        self.customer_entry = tk.Entry(self.master)
        self.customer_entry.insert(0, "Aligned Vision Inc")
        self.customer_entry.pack()

        self.file_button = tk.Button(self.master, text="Browse", command=self.browse_file)
        self.file_button.pack(pady=10)

        self.create_button = tk.Button(self.master, text="Create Invoice", command=self.submit_data)
        self.create_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_label.configure(text=file_path)
        self.csv_entry.insert(0,file_path)

    def submit_data(self):
        date = self.date_entry.get()
        number = self.number_entry.get()
        csv = self.csv_entry.get()
        customer = self.customer_entry.get()

        # Do something with the data
        create_invoice(csv,customer,date,number)

root = tk.Tk()
file_drop_app = FileDropApp(root)
root.mainloop()
