from tkinter import Tk, Toplevel, Frame, Canvas, Label, Entry, Button, PhotoImage, messagebox, ttk
import tkinter as tk
from PIL import Image, ImageTk
from customtkinter import CTkButton
from tkcalendar import DateEntry
from datetime import datetime
import random
import string

class KRLView:
    def __init__(self, root):
        self.root = root
        self.root.title("Pemesanan Tiket KRL")
        self.root.configure(bg='#fff')
        self.root.geometry('925x500+300+200')
        self.root.resizable(False, False)

        self.title_font = ("Microsoft YaHei UI Light", 23, "bold")
        self.label_font = ("Microsoft YaHei UI Light", 11)

        self.username_entry = None
        self.password_entry = None
        self.signup_username_entry = None
        self.signup_password_entry = None
        self.signup_conform_password_entry = None
        self.from_station_var = None
        self.from_station_combobox = None
        self.to_station_var = None
        self.to_station_combobox = None
        self.date_entry = None
        self.quantity_spinbox = None
        self.name_entry = None
        self.id_entry = None
        self.gender_var = None
        self.dob_entry = None
        self.phone_entry = None
        self.email_entry = None
        self.ticket_price_label = None

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login_screen(self, controller):
        self.clear_screen()

        img = PhotoImage(file=r'E:/KAI Project/KAI Project/project3/KAI/KAI TIN/KAI Project (2)/KAI Project/login.png')

        Label(self.root, image=img, bg='white').place(x=50, y=50)

        frame = Frame(self.root, width=350, height=350, bg="white")
        frame.place(x=480, y=70)

        heading = Label(frame, text='Login', fg='#57a1f8', bg='white', font=self.title_font)
        heading.place(x=100, y=5)

        def on_enter(e):
            self.username_entry.delete(0, 'end')

        def on_leave(e):
            name = self.username_entry.get()
            if name == '':
                self.username_entry.insert(0, 'Username')

        self.username_entry = Entry(frame, width=25, fg='black', border=0, bg="white", font=self.label_font)
        self.username_entry.place(x=30, y=80)
        self.username_entry.insert(0, 'Username')
        self.username_entry.bind('<FocusIn>', on_enter)
        self.username_entry.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        def on_enter(e):
            self.password_entry.delete(0, 'end')

        def on_leave(e):
            if self.password_entry.get() == '':
                self.password_entry.insert(0, 'Password')

        self.password_entry = Entry(frame, width=25, fg='black', border=0, bg="white", font=self.label_font, show='*')
        self.password_entry.place(x=30, y=150)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind('<FocusIn>', on_enter)
        self.password_entry.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        Button(frame, width=39, pady=7, text="Login", bg='#57a1f8', fg='white', border=0, command=controller.login).place(x=35, y=204)
        label = Label(frame, text="Belum memiliki akun?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=270)

        sign_in = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=controller.show_signup_screen)
        sign_in.place(x=215, y=270)

        self.root.mainloop()

    def show_signup_screen(self, controller):
        self.clear_screen()

        img = PhotoImage(file=r'E:/KAI Project/KAI Project/project3/KAI/KAI TIN/KAI Project (2)/KAI Project/signin.png')
        Label(self.root, image=img, border=0, bg='white').place(x=50, y=90)

        frame = Frame(self.root, width=350, height=390, bg='#fff')
        frame.place(x=480, y=50)

        heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=self.title_font)
        heading.place(x=100, y=5)

        def on_enter(e):
            self.signup_username_entry.delete(0, 'end')

        def on_leave(e):
            if self.signup_username_entry.get() == '':
                self.signup_username_entry.insert(0, 'Username')

        self.signup_username_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=self.label_font)
        self.signup_username_entry.place(x=30, y=80)
        self.signup_username_entry.insert(0, 'Username')
        self.signup_username_entry.bind("<FocusIn>", on_enter)
        self.signup_username_entry.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        def on_enter(e):
            self.signup_password_entry.delete(0, 'end')

        def on_leave(e):
            if self.signup_password_entry.get() == '':
                self.signup_password_entry.insert(0, 'Password')

        self.signup_password_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=self.label_font, show='*')
        self.signup_password_entry.place(x=30, y=150)
        self.signup_password_entry.insert(0, 'Password')
        self.signup_password_entry.bind("<FocusIn>", on_enter)
        self.signup_password_entry.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        def on_enter(e):
            self.signup_conform_password_entry.delete(0, 'end')

        def on_leave(e):
            if self.signup_conform_password_entry.get() == "":
                self.signup_conform_password_entry.insert(0, 'Conform Password')

        self.signup_conform_password_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=self.label_font, show='*')
        self.signup_conform_password_entry.place(x=30, y=220)
        self.signup_conform_password_entry.insert(0, 'Conform Password')
        self.signup_conform_password_entry.bind("<FocusIn>", on_enter)
        self.signup_conform_password_entry.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

        Button(frame, width=15, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=controller.signup).place(x=120, y=280)
        label = Label(frame, text='Sudah punya akun?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=90, y=340)

        signin = Button(frame, width=6, text='Login', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=controller.show_login_screen)
        signin.place(x=200, y=340)

        self.root.mainloop()

    def show_menu(self, controller):
        self.clear_screen()

        menu_screen = Toplevel(self.root)
        menu_screen.title('Menu Utama')
        menu_screen.geometry('925x500+300+200')
        menu_screen.configure(bg="#fff")
        menu_screen.resizable(False, False)

        image_path = PhotoImage(file=r'C:\Users\Lenovo\Documents\SEMESTER 2\KAI TIN\KAI Project (2)\KAI Project\login.png')
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((925, 500), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        canvas = Canvas(menu_screen, width=925, height=500)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, anchor="nw", image=bg_photo)

        frame = Frame(menu_screen, width=500, height=400, bg="alice blue")
        frame.pack_propagate(False)
        frame.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

        heading = Label(frame, text='Welcome to RAIL-TIX', font=('Open Sans', 23, 'bold'))
        heading.pack(pady=(15, 6))

        subheading = Label(frame, text='Reservasi dan Informasi Layanan Tiket Kereta', font=('Open Sans', 14))
        subheading.pack(pady=(10, 4))

        button_profile = CTkButton(master=frame, text="Profil Pengguna", corner_radius=32,
                                   fg_color="#57a1f8", hover_color="#4158D0", text_color="white",
                                   width=200, height=60, font=("Microsoft YaHei UI Light", 18),
                                   command=controller.show_user_profile_screen)
        button_profile.place(relx=0.06, rely=0.5, anchor="w")

        button_booking = CTkButton(master=frame, text="Pemesanan Tiket", corner_radius=32,
                                   fg_color="#57a1f8", hover_color="#4158D0", text_color="white",
                                   width=200, height=60, font=("Microsoft YaHei UI Light", 18),
                                   command=controller.show_booking_screen)
        button_booking.place(relx=0.55, rely=0.5, anchor="w")

        button_logout = CTkButton(master=frame, text="Logout", corner_radius=32,
                                  fg_color="#57a1f8", hover_color="#4158D0", text_color="white",
                                  width=200, height=60, font=("Microsoft YaHei UI Light", 18),
                                  command=controller.show_login_screen)
        button_logout.place(relx=0.55, rely=0.84, anchor="w")

        button_reservations = CTkButton(master=frame, text="Data Reservasi", corner_radius=32,
                                        fg_color="#57a1f8", hover_color="#4158D0", text_color="white",
                                        width=200, height=60, font=("Microsoft YaHei UI Light", 18),
                                        command=controller.show_reservation_management_screen)
        button_reservations.place(relx=0.055, rely=0.84, anchor="w")

        menu_screen.mainloop()

    def show_booking_screen(self, controller):
        self.clear_screen()

        tk.Label(self.root, text="Pemesanan Tiket", font=self.title_font, bg='#f2f2f2').grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.root, text="Kota Keberangkatan:", font=self.label_font).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.from_station_var = tk.StringVar()
        self.from_station_combobox = ttk.Combobox(self.root, textvariable=self.from_station_var, values=controller.krl.stations)
        self.from_station_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        Label(self.root, text="Kota Tujuan:", font=self.label_font).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.to_station_var = tk.StringVar()
        self.to_station_combobox = ttk.Combobox(self.root, textvariable=self.to_station_var, values=controller.krl.stations)
        self.to_station_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        Label(self.root, text="Tanggal Keberangkatan:", font=self.label_font).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.date_entry = DateEntry(self.root, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        Label(self.root, text="Jumlah Tiket:", font=self.label_font).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.quantity_spinbox = tk.Spinbox(self.root, from_=1, to=10, width=5)
        self.quantity_spinbox.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        calculate_price_button = Button(self.root, text="Calculate Price", command=controller.calculate_ticket_price)
        calculate_price_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.ticket_price_label = Label(self.root, text="", font=self.label_font)
        self.ticket_price_label.grid(row=6, column=0, columnspan=2, pady=10)

        book_ticket_button = Button(self.root, text="Pesan", command=controller.book_ticket)
        book_ticket_button.grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Kembali ke Menu", command=controller.show_menu, bg='#f44336', fg='white', font=self.label_font).grid(row=8, columnspan=2, pady=10)

    def show_ticket_price(self, price):
        if self.ticket_price_label:
            self.ticket_price_label.config(text=f"Total Price: {price} IDR")

    def show_reservation_management_screen(self, controller):
        self.clear_screen()

        tk.Label(self.root, text="Manajemen Reservasi", font=self.title_font, bg='#f2f2f2').grid(row=0, column=0, columnspan=3, pady=10)
        tk.Button(self.root, text="Back to Menu", command=controller.show_menu, bg='#f44336', fg='white', font=self.label_font).grid(row=1, column=0, columnspan=3, pady=10)

        columns = ("No", "Nama Pengguna", "ID Pengguna", "Kota Keberangkatan", "Kota Tujuan", "Tanggal Pemesanan", "Jumlah Tiket", "Harga Tiket")
        tree = ttk.Treeview(self.root, columns=columns, show="headings")
        tree.heading("No", text="No")
        tree.heading("Nama Pengguna", text="Nama Pengguna")
        tree.heading("ID Pengguna", text="ID Pengguna")
        tree.heading("Kota Keberangkatan", text="Kota Keberangkatan")
        tree.heading("Kota Tujuan", text="Kota Tujuan")
        tree.heading("Tanggal Pemesanan", text="Tanggal Pemesanan")
        tree.heading("Jumlah Tiket", text="Jumlah Tiket")
        tree.heading("Harga Tiket", text="Harga Tiket")

        tree.column("No", width=30)
        tree.column("Nama Pengguna", width=100)
        tree.column("ID Pengguna", width=100)
        tree.column("Kota Keberangkatan", width=120)
        tree.column("Kota Tujuan", width=120)
        tree.column("Tanggal Pemesanan", width=120)
        tree.column("Jumlah Tiket", width=100)
        tree.column("Harga Tiket", width=100)

        bookings = controller.krl.get_bookings()
        for i, booking in enumerate(bookings, start=1):
            tree.insert("", "end", values=(i, booking["name"], booking["id_number"], booking["from_station"], booking["to_station"], booking["date"], booking["quantity"], booking["total_price"]))

        tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    def show_user_profile_screen(self, controller):
        self.clear_screen()

        user = controller.krl.users.get(controller.username)
        if not user:
            messagebox.showerror("Error", "Pengguna tidak ditemukan.")
            return

        tk.Label(self.root, text="Profil Pengguna", font=self.title_font, bg='#f2f2f2').grid(row=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Nama:", font=self.label_font, bg='#f2f2f2').grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.insert(0, user.get("name", ""))
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.id_entry = tk.Entry(self.root)

        tk.Label(self.root, text="Jenis Kelamin:", font=self.label_font, bg='#f2f2f2').grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.gender_var = tk.StringVar()
        self.gender_var.set(user.get("gender", ""))
        tk.OptionMenu(self.root, self.gender_var, "Laki-laki", "Perempuan").grid(row=3, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.root, text="Tanggal Lahir:", font=self.label_font, bg='#f2f2f2').grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.dob_entry = DateEntry(self.root, date_pattern='dd/mm/yyyy')
        if user.get("date_of_birth"):
            dob = datetime.strptime(user["date_of_birth"], '%d/%m/%Y')
            self.dob_entry.set_date(dob)
        self.dob_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.root, text="Nomor Telepon:", font=self.label_font, bg='#f2f2f2').grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.insert(0, user.get("phone_number", ""))
        self.phone_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.root, text="Email:", font=self.label_font, bg='#f2f2f2').grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = tk.Entry(self.root)
        self.email_entry.insert(0, user.get("email", ""))
        self.email_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.root, text="Username:", font=self.label_font, bg='#f2f2f2').grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.username_entry = tk.Entry(self.root)
        self.username_entry.insert(0, controller.username)
        self.username_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.root, text="Password:", font=self.label_font, bg='#f2f2f2').grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.insert(0, user.get("password", ""))
        self.password_entry.grid(row=8, column=1, padx=10, pady=5, sticky="w")

        tk.Button(self.root, text="Update Profile", command=controller.update_profile, bg='#4CAF50', fg='white', font=self.label_font).grid(row=9, columnspan=2, pady=10)
        tk.Button(self.root, text="Kembali ke Menu", command=controller.show_menu, bg='#f44336', fg='white', font=self.label_font).grid(row=10, columnspan=2, pady=10)

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
        lihat_profil_button = tk.Button(self.main_content, text="Lihat Profil", font=('Open Sans', 12, 'bold'), bg='#9fedd7', fg='black',relief='flat', command=self.show_saved_profile)
        lihat_profil_button.pack(pady=10)
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
