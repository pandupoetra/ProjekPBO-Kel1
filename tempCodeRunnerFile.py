import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import random
import string

class KRLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RAIL-TIX")
        self.root.geometry("800x600")
        self.root.configure(bg="#ecf0f1")

        self.departure_city = None
        self.destination_city = None
        self.ticket_count = ""
        self.gender = None
        self.profile_data = {
            'name': '',
            'user_id': '',
            'gender': '',
            'dob': '',
            'email': ''
        }

        self.setup_ui()

    def setup_ui(self):
        # Sidebar
        self.sidebar = tk.Frame(self.root, bg="#2c3e50", width=200, height=600)
        self.sidebar.pack(side="left", fill="y")

        self.sidebar_title = tk.Label(self.sidebar, text="RAIL-TIX", font=("Helvetica", 14, "bold"), bg="#2c3e50", fg="white")
        self.sidebar_title.pack(pady=20)

        self.Dashboard_btn = self.create_sidebar_button("Dashboard", self.Dashboard)
        self.pesan_btn = self.create_sidebar_button("Pesan", self.show_pesan)
        self.profile_btn = self.create_sidebar_button("Profil", self.show_profile)
        self.histori_btn = self.create_sidebar_button("Histori", self.show_histori)
        self.signout_btn = self.create_sidebar_button("Sign Out", self.sign_out)

        # Top bar
        self.topbar = tk.Frame(self.root, bg="#ecf0f1", height=50)
        self.topbar.pack(side="top", fill="x")

        self.search_entry = tk.Entry(self.topbar, font=("Helvetica", 12), width=40, bd=0)
        self.search_entry.pack(pady=10, padx=20, side="left")

        self.search_button = tk.Button(self.topbar, text="🔍", font=("Helvetica", 12), bg="#ecf0f1", fg="#2c3e50", bd=0, command=self.search)
        self.search_button.pack(pady=10, padx=10, side="left")

        self.user_icon = tk.Label(self.topbar, text="👤", bg="#ecf0f1", font=("Helvetica", 16))
        self.user_icon.pack(pady=10, padx=10, side="right")

        # Main content
        self.main_content = tk.Frame(self.root, bg="#ecf0f1")
        self.main_content.pack(side="right", fill="both", expand=True)

        self.content_label = tk.Label(self.main_content, text="Welcome to RAIL TIX", font=("Helvetica", 24), bg="#ecf0f1")
        self.content_label.pack(pady=20)

        self.content_label = tk.Label(self.main_content, text="Reservasi dan Informasi Layanan Tiket Kereta", font=("Helvetica", 18), bg="#ecf0f1")
        self.content_label.pack(pady=20)

        # Add image to dashboard
        self.add_dashboard_image()
        
    def add_dashboard_image(self):
        img = Image.open("E:/KAI Project/KAI Project/project3/KAI/KAI TIN/KAI Project (2)/KAI Project/ss.jpg") # Replace with your image path
#        img = img.resize((300, 200), Image.ANTIALIAS)
        self.img_photo = ImageTk.PhotoImage(img)

        self.img_label = tk.Label(self.main_content, image=self.img_photo, bg="#ecf0f1")
        self.img_label.pack(pady=10)

    def create_sidebar_button(self, text, command):
        button = tk.Button(self.sidebar, text=text, font=("Helvetica", 12), bg="#34495e", fg="white", bd=0, relief="flat", highlightthickness=0, command=command)
        button.pack(fill="x", pady=5)
        button.bind("<Enter>", lambda e: button.config(bg="#1abc9c"))
        button.bind("<Leave>", lambda e: button.config(bg="#34495e"))
        return button
    


    def search(self):
        messagebox.showinfo("Search", f"You searched for: {self.search_entry.get()}")

    def show_pesan(self):
        self.show_ticket_form()

    def generate_user_id(self):
        characters = string.ascii_letters + string.digits
        user_id = ''.join(random.choices(characters, k=7))
        return user_id

    def show_profile(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(self.main_content, bg='#7297b5', height=100)
        header_frame.pack(fill='x')

        header_label = tk.Label(header_frame, text='Profil Pengguna', font=('Open Sans', 20, 'bold'), bg='#7297b5', fg='white')
        header_label.pack(pady=30)

        form_frame = tk.Frame(self.main_content, bg='alice blue')
        form_frame.pack(pady=10, padx=20, fill='both', expand=True)

        # Membuat frame untuk input Nama
        nama_frame = tk.Frame(form_frame, bg='alice blue')
        nama_frame.pack(pady=10, fill='x')
        nama_label = tk.Label(nama_frame, text='Nama', font=('Open Sans', 12), bg='alice blue')
        nama_label.pack(side='left', padx=10)
        self.nama_entry = tk.Entry(nama_frame, bg='#afd6e1', font=('Open Sans', 12), width=20)
        self.nama_entry.pack(side='right', padx=10)

        # Membuat frame untuk input ID Pengguna
        id_frame = tk.Frame(form_frame, bg='alice blue')
        id_frame.pack(pady=10, fill='x')
        id_label = tk.Label(id_frame, text='ID Pengguna', font=('Open Sans', 12), bg='alice blue')
        id_label.pack(side='left', padx=10)
        self.id_entry = tk.Entry(id_frame, bg='#afd6e1', font=('Open Sans', 12), width=20)
        self.id_entry.pack(side='right', padx=10)
        self.id_entry.insert(0, self.generate_user_id())
        self.id_entry.config(state='readonly')

        # Membuat frame untuk input Jenis Kelamin
        gender_frame = tk.Frame(form_frame, bg='alice blue')
        gender_frame.pack(pady=10, fill='x')
        gender_label = tk.Label(gender_frame, text='Jenis Kelamin', font=('Open Sans', 12), bg='alice blue')
        gender_label.pack(side='left', padx=10)
        self.gender_label = tk.Label(gender_frame, text=self.gender or "Pilih Jenis Kelamin", font=('Open Sans', 12), bg='#afd6e1')
        self.gender_label.pack(side='right', padx=10)
        gender_button = tk.Button(gender_frame, text="Pilih", font=('Open Sans', 10), command=self.show_gender_selection_popup)
        gender_button.pack(side='left', padx=10)

        # Membuat frame untuk input Tanggal Lahir dengan DateEntry
        dob_frame = tk.Frame(form_frame, bg='alice blue')
        dob_frame.pack(pady=10, fill='x')
        dob_label = tk.Label(dob_frame, text='Tanggal Lahir', font=('Open Sans', 12), bg='alice blue')
        dob_label.pack(side='left', padx=10)
        self.dob_entry = DateEntry(dob_frame, font=('Open Sans', 12), bg='#afd6e1', year=2000, date_pattern='dd/mm/yyyy')
        self.dob_entry.pack(side='right', padx=10)

        # Membuat frame untuk input Email
        email_frame = tk.Frame(form_frame, bg='alice blue')
        email_frame.pack(pady=10, fill='x')
        email_label = tk.Label(email_frame, text='Email', font=('Open Sans', 12), bg='alice blue')
        email_label.pack(side='left', padx=10)
        self.email_entry = tk.Entry(email_frame, bg='#afd6e1', font=('Open Sans', 12), width=20)
        self.email_entry.pack(side='right', padx=10)

        # Menambahkan tombol "Konfirmasi" di bawah form
        confirm_button = tk.Button(self.main_content, text="Konfirmasi", font=('Open Sans', 12, 'bold'), bg='#9fedd7', fg='Black', relief='flat', command=self.save_profile)
        confirm_button.pack(pady=20)

        # Menambahkan tombol "Lihat Profil" di bawah form
        lihat_profil_button = tk.Button(self.main_content, text="Lihat Profil", font=('Open Sans', 12, 'bold'), bg='#9fedd7', fg='black', relief='flat', command=self.show_saved_profile)
        lihat_profil_button.pack(pady=20)
    def save_profile(self):
        self.profile_data['name'] = self.nama_entry.get()
        self.profile_data['user_id'] = self.id_entry.get()
        self.profile_data['gender'] = self.gender
        self.profile_data['dob'] = self.dob_entry.get()
        self.profile_data['email'] = self.email_entry.get()
        messagebox.showinfo("Profil", "Data profil telah disimpan!")

    def show_saved_profile(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(self.main_content, bg='#7297b5', height=100)
        header_frame.pack(fill='x')

        header_label = tk.Label(header_frame, text='Profil Pengguna', font=('Open Sans', 20, 'bold'), bg='#7297b5', fg='white')
        header_label.pack(pady=30)

        profile_frame = tk.Frame(self.main_content, bg='alice blue')
        profile_frame.pack(pady=10, padx=20, fill='both', expand=True)

        def create_profile_label(frame, text, value):
            field_frame = tk.Frame(frame, bg='alice blue', pady=5, padx=5)
            field_frame.pack(pady=10, fill='x')
            label = tk.Label(field_frame, text=text, font=('Open Sans', 12), bg='alice blue')
            label.pack(side='left', padx=10)
            value_label = tk.Label(field_frame, text=value, font=('Open Sans', 12), bg='alice blue')
            value_label.pack(side='right', padx=10)

        create_profile_label(profile_frame, 'Nama:', self.profile_data['name'])
        create_profile_label(profile_frame, 'ID Pengguna:', self.profile_data['user_id'])
        create_profile_label(profile_frame, 'Jenis Kelamin:', self.profile_data['gender'])
        create_profile_label(profile_frame, 'Tanggal Lahir:', self.profile_data['dob'])
        create_profile_label(profile_frame, 'Email:', self.profile_data['email'])

    def show_gender_selection_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Jenis Kelamin")
        popup.geometry("300x400")
        popup.configure(bg='white')

        header_label = tk.Label(popup, text="Jenis Kelamin", font=('Open Sans', 16, 'bold'), bg='white')
        header_label.pack(pady=10)

        button_frame = tk.Frame(popup, bg='white')
        button_frame.pack(pady=10, padx=20, fill='both', expand=True)

        genders = ['Laki Laki', 'Perempuan', 'Tidak Diketahui']
        colors = ['#aed6f1', '#aed6f1', '#aed6f1']

        for gender, color in zip(genders, colors):
            button = tk.Button(button_frame, text=gender, font=('Open Sans', 12), bg=color, fg='black', relief='flat', command=lambda g=gender: self.select_gender(g, popup))
            button.pack(pady=10, fill='x')

        confirm_button = tk.Button(button_frame, text="Konfirmasi", font=('Open Sans', 12, 'bold'), bg='#9fedd7', fg='black', relief='flat', command=popup.destroy)
        confirm_button.pack(pady=10, fill='x')

    def select_gender(self, gender, popup):
        self.gender = gender
        self.gender_label.config(text=self.gender)
        popup.destroy()

    def show_histori(self):
        self.content_label.config(text="Messages Page")

    def sign_out(self):
        self.root.destroy()

    def Dashboard(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        self.content_label = tk.Label(self.main_content, text="Welcome to the Dashboard", font=("Helvetica", 24), bg="#ecf0f1")
        self.content_label.pack(pady=20)

    def set_departure_city(self, city):
        self.departure_city = city
        self.show_ticket_form()

    def set_destination_city(self, city):
        self.destination_city = city
        self.show_ticket_form()

    def show_ticket_form(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(self.main_content, bg='#7297b5', height=100)
        header_frame.pack(fill='x')

        header_label = tk.Label(header_frame, text='Pesan Tiket', font=('Open Sans', 20, 'bold'), bg='#7297b5', fg='white')
        header_label.pack(pady=30)

        form_frame = tk.Frame(self.main_content, bg='white')
        form_frame.pack(pady=10, padx=20, fill='both', expand=True)

        def create_label(frame, text):
            field_frame = tk.Frame(frame, bg='#afd6e1', pady=5, padx=5)
            field_frame.pack(pady=10, fill='x')

            label = tk.Label(field_frame, text=text, font=('Open Sans', 12), bg='#afd6e1')
            label.pack(side='left', padx=10)
            return field_frame

        def create_date_entry_field(frame, text):
            field_frame = create_label(frame, text)
            date_entry = DateEntry(field_frame, font=('Open Sans', 12), background='darkblue', foreground='white', borderwidth=2)
            date_entry.pack(side='right', padx=10)

        departure_frame = create_label(form_frame, 'Kota Keberangkatan:')
        self.departure_label = tk.Label(departure_frame, text=self.departure_city or "Pilih Kota", font=('Open Sans', 12), bg='#afd6e1')
        self.departure_label.pack(side='right', padx=10)
        departure_button = tk.Button(departure_frame, text="Pilih", font=('Open Sans', 10), command=lambda: self.show_city_selection_popup("Kota Keberangkatan", self.set_departure_city))
        departure_button.pack(side='left', padx=10)

        destination_frame = create_label(form_frame, 'Kota Tujuan:')
        self.destination_label = tk.Label(destination_frame, text=self.destination_city or "Pilih Kota", font=('Open Sans', 12), bg='#afd6e1')
        self.destination_label.pack(side='right', padx=10)
        destination_button = tk.Button(destination_frame, text="Pilih", font=('Open Sans', 10), command=lambda: self.show_city_selection_popup("Kota Tujuan", self.set_destination_city))
        destination_button.pack(side='left', padx=10)

        create_date_entry_field(form_frame, 'Tanggal Keberangkatan')

        ticket_count_frame = create_label(form_frame, 'Jumlah Tiket')
        self.ticket_count_label = tk.Label(ticket_count_frame, text=self.ticket_count or "0", font=('Open Sans', 12), bg='#afd6e1')
        self.ticket_count_label.pack(side='right', padx=10)
        ticket_count_button = tk.Button(ticket_count_frame, text="Pilih", font=('Open Sans', 10), command=self.show_ticket_count_popup)
        ticket_count_button.pack(side='left', padx=10)

        pesan_button = tk.Button(self.main_content, text="Pesan", font=('Open Sans', 12, 'bold'), bg='#9fedd7', fg='black', relief='flat')
        pesan_button.pack(pady=20)

    def show_city_selection_popup(self, title, callback):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("300x300")
        popup.configure(bg='white')

        header_label = tk.Label(popup, text=title, font=('Open Sans', 16, 'bold'), bg='white')
        header_label.pack(pady=10)

        button_frame = tk.Frame(popup, bg='white')
        button_frame.pack(pady=10, padx=20, fill='both', expand=True)

        cities = ['Jakarta', 'Bandung', 'Purwokerto', 'Semarang', 'Yogyakarta', 'Surakarta', 'Malang', 'Surabaya']
        rows, cols = 4, 2

        for i, city in enumerate(cities):
            button = tk.Button(button_frame, text=city, font=('Open Sans', 12), bg='#aed6f1', fg='black', relief='flat', command=lambda c=city: self.select_city(callback, c, popup))
            button.grid(row=i//cols, column=i%cols, padx=10, pady=10, sticky='nsew')

    def select_city(self, callback, city, popup):
        callback(city)
        popup.destroy()

    

    def show_ticket_count_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Jumlah Tiket")
        popup.geometry("300x430")
        popup.configure(bg='Alice Blue')

        def add_digit(digit):
            self.ticket_count += digit
            self.ticket_count_label.config(text=self.ticket_count)

        def confirm():
            if not self.ticket_count:
                self.ticket_count = "0"
            self.ticket_count_label.config(text=self.ticket_count)
            popup.destroy()

        header_label = tk.Label(popup, text="Jumlah Tiket", font=('Open Sans', 16, 'bold'), bg='white')
        header_label.pack(pady=10)

        button_frame = tk.Frame(popup, bg='white')
        button_frame.pack(pady=10, padx=20, fill='both', expand=True)

        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('0', 4, 1), ('Konfirmasi', 5, 1)
        ]

        for (text, row, col) in buttons:
            if text == 'Konfirmasi':
                button = tk.Button(button_frame, text=text, font=('Open Sans', 12), bg='#9fedd7', fg='black', relief='flat', command=confirm)
            else:
                button = tk.Button(button_frame, text=text, font=('Open Sans', 12), bg='#aed6f1', fg='black', relief='flat', command=lambda t=text: add_digit(t))
            button.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')

        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(3):
            button_frame.grid_columnconfigure(j, weight=1)

    
    def show_histori(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(self.main_content, bg='#7297b5', height=100)
        header_frame.pack(fill='x')

        header_label = tk.Label(header_frame, text='Histori Pemesanan', font=('Open Sans', 20, 'bold'), bg='#7297b5', fg='white')
        header_label.pack(pady=30)

        histori_frame = tk.Frame(self.main_content, bg='alice blue')
        histori_frame.pack(pady=10, padx=20, fill='both', expand=True)

        histori_label = tk.Label(histori_frame, text='Histori pemesanan tiket Anda akan ditampilkan di sini.', font=('Open Sans', 12), bg='alice blue')
        histori_label.pack(pady=20)

    def Dashboard(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()
        self.content_label = tk.Label(self.main_content, text="Welcome to RAIL TIX", font=("Helvetica", 24), bg="#ecf0f1")
        self.content_label.pack(pady=20)

        self.content_label = tk.Label(self.main_content, text="Reservasi dan Informasi Layanan Tiket Kereta", font=("Helvetica", 18), bg="#ecf0f1")
        self.content_label.pack(pady=20)

        # Add image to dashboard
        self.add_dashboard_image()

    def sign_out(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = KRLApp(root)
    root.mainloop()
