# Jumlah orang yang ada
n = 7

# Jumlah orang yang dipilih ke kelompok 
r = 4

# Faktorial dari 7 
faktorial_7 = 7*6*5*4*3*2*1

# Faktorial dari 4
faktorial_4 = 4*3*2*1

# Faktorial dari (n-r) adalah 3
faktorial_3 = 3*2*1

# Perhitungan berapa jumlah caranya dengan rumus C(n,r) = n! / (r! * (n-r)!) 
total_Cara = int((faktorial_7)/(faktorial_4*faktorial_3))
print("jadi total cara yang digunakan oleh Darsono adalah :",total_Cara)