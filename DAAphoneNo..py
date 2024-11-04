import tkinter as tk
from tkinter import messagebox, scrolledtext

class QuickSort:
    @staticmethod
    def sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]  
        less = [x for x in arr[1:] if x[0] <= pivot[0]]
        greater = [x for x in arr[1:] if x[0] > pivot[0]]
        return QuickSort.sort(less) + [pivot] + QuickSort.sort(greater)

class PhoneBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Phone Book App")

        # Set window size and center it
        window_width = 500
        window_height = 400
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.master.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        self.master.configure(bg="#e6f5ff")  # Light background color

        self.names = []
        self.phone_numbers = []

        # Custom fonts
        self.title_font = ("Arial", 16, "bold")
        self.label_font = ("Arial", 12)
        self.entry_font = ("Arial", 11)
        self.button_font = ("Arial", 12, "bold")

        # Title Label
        title_label = tk.Label(self.master, text="Phone Book Application", font=self.title_font, fg="#004d99", bg="#e6f5ff")
        title_label.pack(pady=10)

        # Input section
        input_frame = tk.Frame(self.master, bg="#e6f5ff")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Name:", font=self.label_font, bg="#e6f5ff").grid(row=0, column=0, padx=5, pady=10, sticky="e")
        self.name_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.name_var, font=self.entry_font, relief="ridge").grid(row=0, column=1, padx=5, pady=10, ipadx=10, ipady=3)

        tk.Label(input_frame, text="Phone Number:", font=self.label_font, bg="#e6f5ff").grid(row=1, column=0, padx=5, pady=10, sticky="e")
        self.phone_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.phone_var, font=self.entry_font, relief="ridge").grid(row=1, column=1, padx=5, pady=10, ipadx=10, ipady=3)

        # Buttons with custom styles
        button_frame = tk.Frame(self.master, bg="#e6f5ff")
        button_frame.pack(pady=10)

        add_btn = tk.Button(button_frame, text="Add Entry", command=self.add_entry, bg="#009933", fg="white", font=self.button_font, relief="raised", bd=3)
        add_btn.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=5)

        sort_btn = tk.Button(button_frame, text="Sort Names", command=self.sort_names, bg="#0066cc", fg="white", font=self.button_font, relief="raised", bd=3)
        sort_btn.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=5)

        # Change button color on hover
        def on_enter_add(e):
            add_btn['background'] = '#33cc33'
        def on_leave_add(e):
            add_btn['background'] = '#009933'

        def on_enter_sort(e):
            sort_btn['background'] = '#3399ff'
        def on_leave_sort(e):
            sort_btn['background'] = '#0066cc'

        add_btn.bind("<Enter>", on_enter_add)
        add_btn.bind("<Leave>", on_leave_add)

        sort_btn.bind("<Enter>", on_enter_sort)
        sort_btn.bind("<Leave>", on_leave_sort)

        # Display area
        display_frame = tk.Frame(self.master, bg="#e6f5ff")
        display_frame.pack(pady=10)

        self.display_area = scrolledtext.ScrolledText(display_frame, width=50, height=10, font=self.entry_font, bg="#ffffff", relief="sunken", bd=2)
        self.display_area.pack(padx=10, pady=10)

    def add_entry(self):
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()

        if not name or not phone:
            messagebox.showwarning("Input Error", "Please enter both name and phone number.")
            return

        # Validate that the phone number is exactly 10 digits long
        if len(phone) != 10 or not phone.isdigit():
            messagebox.showerror("Phone Number Error", "Phone number must be exactly 10 digits.")
            return

        self.names.append(name)
        self.phone_numbers.append(phone)
        self.display_entries()
        self.name_var.set("")
        self.phone_var.set("")

    def sort_names(self):
        combined = list(zip(self.names, self.phone_numbers))
        sorted_combined = QuickSort.sort(combined)

        self.names, self.phone_numbers = zip(*sorted_combined) if sorted_combined else ([], [])
        self.display_entries()

    def display_entries(self):
        self.display_area.delete(1.0, tk.END)
        for name, phone in zip(self.names, self.phone_numbers):
            self.display_area.insert(tk.END, f"{name}: {phone}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneBookApp(root)
    root.mainloop()
