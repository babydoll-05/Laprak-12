def baca_log(filename):
    daftar_email = {} 
    total_pesan = 0 

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('From '):
                email = line.split()[1]
                daftar_email[email] = daftar_email.get(email, 0) + 1
                total_pesan += 1  

    return daftar_email, total_pesan

nama_file = input("Masukkan nama file: ")

email_, pesan = baca_log(nama_file)
print(email_)