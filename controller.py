import subprocess
from model import KRL
from view import KRLView, KRLApp
import tkinter as tk
from tkinter import messagebox

class KRLController:
    def __init__(self, root):
        self.krl = KRL()
        self.test = KRLApp(root)
        self.view = KRLView(root)
        self.username = None
        self.view.show_login_screen(self)

    def login(self):
        username = self.view.username_entry.get()
        password = self.view.password_entry.get()

        if self.krl.validate_login(username, password):
            self.username = username
            self.view.clear_screen()
 #           self.view.show_menu(self)
            self.test.setup_ui()
        else:
            messagebox.showerror("Error", "Username atau password salah.")

    def signup(self):
        username = self.view.signup_username_entry.get()
        password = self.view.signup_password_entry.get()
        conform_password = self.view.signup_conform_password_entry.get()

        if password == conform_password:
            success, message = self.krl.add_user(username, password)
            if success:
                messagebox.showinfo("Sukses", message)
                self.view.show_login_screen(self)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Password dan Konfirmasi Password tidak cocok")


    def calculate_ticket_price(self):
        from_station = self.view.from_station_var.get()
        to_station = self.view.to_station_var.get()
        quantity = self.view.quantity_spinbox.get()

        if not from_station or not to_station or not quantity:
            messagebox.showerror("Error", "Harap isi semua bidang.")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Error", "Jumlah tiket harus berupa angka.")
            return

        price_per_ticket = self.krl.get_price(from_station, to_station)
        if price_per_ticket is None:
            messagebox.showerror("Error", "Rute tidak tersedia.")
            return

        total_price = price_per_ticket * quantity
        self.view.show_ticket_price(total_price)

    def book_ticket(self):
        from_station = self.view.from_station_var.get()
        to_station = self.view.to_station_var.get()
        date = self.view.date_entry.get()
        quantity = self.view.quantity_spinbox.get()

        if not from_station or not to_station or not date or not quantity:
            messagebox.showerror("Error", "Harap isi semua bidang.")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Error", "Jumlah tiket harus berupa angka.")
            return

        user = self.krl.users.get(self.username)
        if not user:
            messagebox.showerror("Error", "Pengguna tidak ditemukan.")
            return

        success, message = self.krl.book_ticket(user, from_station, to_station, date, quantity)
        if success:
            messagebox.showinfo("Sukses", message)
        else:
            messagebox.showerror("Error", message)

    def show_signup_screen(self):
        self.view.show_signup_screen(self)

    def show_login_screen(self):
        self.view.show_login_screen(self)

    def show_menu(self):
        self.view.show_menu(self)

    def show_booking_screen(self):
        self.view.show_booking_screen(self)

    def show_reservation_management_screen(self):
        self.view.show_reservation_management_screen(self)

    def show_user_profile_screen(self):
        self.view.show_user_profile_screen(self)

if __name__ == "__main__":
    root = tk.Tk()
    app = KRLController(root)
    root.mainloop()
