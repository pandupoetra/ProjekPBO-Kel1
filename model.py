import uuid

class KRL:
    def __init__(self):
        self.stations = ["Jakarta", "Depok", "Bogor", "Bekasi"]
        self.prices = {
            ("Jakarta", "Depok"): 5000,
            ("Jakarta", "Bogor"): 8000,
            ("Jakarta", "Bekasi"): 7000,
            ("Depok", "Bogor"): 3000,
            ("Depok", "Bekasi"): 6000,
            ("Bogor", "Bekasi"): 9000
        }
        self.bookings = []
        self.users = {"user": {"password": "password", "name": "", "id_number": "", "gender": "", "date_of_birth": "", "phone_number": "", "email": ""}}
        self.load_users()

    def get_price(self, from_station, to_station):
        if (from_station, to_station) in self.prices:
            return self.prices[(from_station, to_station)]
        elif (to_station, from_station) in self.prices:
            return self.prices[(to_station, from_station)]
        else:
            return None

    def book_ticket(self, username, from_station, to_station, date, quantity):
        name = username['name']
        id_number = username['id_number']
        if not name or not id_number:
            return False, "Nama atau nomor ID tidak ditemukan. Harap perbarui profil Anda."

        price = self.get_price(from_station, to_station)
        if price is None:
            return False, "Rute tidak tersedia."

        total_price = price * quantity

        booking = {
            "name": name,
            "id_number": id_number,
            "from_station": from_station,
            "to_station": to_station,
            "date": date,
            "quantity": quantity,
            "total_price": total_price
        }
        self.bookings.append(booking)
        return True, f"Tiket berhasil dipesan! Harga total tiket dari {from_station} ke {to_station} adalah {total_price} IDR."

    def get_bookings(self):
        return self.bookings

    def validate_login(self, username, password):
        user = self.users.get(username)
        if user and user['password'] == password:
            return True
        return False

    def add_user(self, username, password):
        if username in self.users:
            return False, "Username sudah ada."
        self.users[username] = {"password": password, "name": "", "id_number": "", "gender": "", "date_of_birth": "", "phone_number": "", "email": ""}
        return True, "Pendaftaran berhasil."
    
    def save_user_to_file(self, username, password):
        with open('users.txt', 'a') as file:
            file.write(f"{username},{password}\n")

    def load_users(self):
        try:
            with open('users.txt', 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    self.users[username] = {"password": password, "name": "", "id_number": "", "gender": "", "date_of_birth": "", "phone_number": "", "email": ""}
        except FileNotFoundError:
            pass

    def update_profile(self, username, name, id_number, gender, date_of_birth, phone_number, email, new_username, new_password):
        if username not in self.users:
            return False, "Pengguna tidak ditemukan."
        user = self.users[username]
        user['name'] = name
        if not user['id_number']:
            user['id_number'] = str(uuid.uuid4())  # Generate unique ID if it doesn't exist
        user['gender'] = gender
        user['date_of_birth'] = date_of_birth
        user['phone_number'] = phone_number
        user['email'] = email
        user['username'] = new_username
        user['password'] = new_password

        # If username is updated, handle the change in the key
        if username != new_username:
            self.users[new_username] = self.users.pop(username)
        
        self.save_all_users_to_file()

        return True, "Profil berhasil diperbarui."
    
    def save_all_users_to_file(self):
        with open('users.txt', 'w') as file:
            for username, user_data in self.users.items():
                file.write(f"{username},{user_data['password']}\n")
