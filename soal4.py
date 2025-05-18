def hitung_domain(email):
    return email.split('@')[-1]

def hitung_domain_email(filename):
    counts = {}

    with open(filename, 'r') as file:
        for line in file: 
            if line.startswith('From '):
                email = line.split()[1]
                domain = hitung_domain(email)
                counts[domain] = counts.get(domain, 0) + 1
    return counts

nama_file = input("Masukkan nama file: ")
counts = hitung_domain_email(nama_file)

print(counts)