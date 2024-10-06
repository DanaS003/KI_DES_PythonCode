# Tabel untuk Initial Permutation pada binary string. Jadi misal ada 64 bit biner, maka yang awalnya berada di urutan ke 58 akan dialihkan ke urutan 1
initial_perm_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Permutasi PC1 untuk mengurangi key dari 64-bit ke 56-bit
pc1_table = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]

# Jadwal shift untuk rotasi pada key, round 1 tiap kelompok key yang sudah dibagi 2 shift 1 satuan ke kiri, round 3 shift 2 satuan ke kiri
shift_per_round = [1, 1, 2, 2,
                  2, 2, 2, 2,
                  1, 2, 2, 2,
                  2, 2, 2, 1]

# Permutasi PC2 untuk mengurangi key dari shifted-56-bit ke 48-bit
pc2_table = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

# Expansion table untuk memperluas 32-bit ke 48-bit
e_exp_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# S-Box untuk substitusi dalam enkripsi DES (lengkap untuk S-Box 1 hingga 8)
# Langkah" : Dari 48-bit dari tabel e_exp akan dipecah menjadi 8 kelompok masing masing 6 bit
# misalkan ada 101100, selanjutnya dipisah 2 bit kiri kanan daan 4 bit sisanya, 10 adalah 2, 0110 adalah 6
# cek baris 2 kolom 6 = 2 atau 1011 (misalkan S-box 1)
# Jadi, yang awalnya adalah 101100(4-bit) akan menjadi 0010 (4-bit)
s_boxes = [
    # S-box 1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S-box 2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S-box 3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S-box 4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S-box 5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S-box 6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S-box 7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S-box 8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# P-box tabel
perm_box_table = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# Permutasi akhir
ip_inverse_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Fungsi untuk mengubah string menjadi binary
def string_to_binary(user_input):
    binary_representation = ''
    i = 0  # Inisialisasi counter untuk indeks
    while i < len(user_input):  # Gunakan while untuk loop melalui setiap karakter
        char = user_input[i]
        binary_char = format(ord(char), '08b')  # ASCII 8 bit
        binary_representation += binary_char
        i += 1  # Increment counter untuk melanjutkan ke karakter berikutnya
    return binary_representation[:64].ljust(64, '0')  # Maks panjang 64-bit dan tambahkan 0 di depan jika belum 64

# Fungsi untuk mengubah binary menjadi string ASCII
def binary_to_ascii(binary_str):
    ascii_str = ''.join([chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)])
    return ascii_str

# Fungsi konversi Hexadecimal ke Binary
def hex_to_binary(s):
    mp = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
          '4': "0100", '5': "0101", '6': "0110", '7': "0111",
          '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
          'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
    bin_str = ""
    for i in range(len(s)):
        if s[i] in mp:
            bin_str += mp[s[i]]
        else:
            bin_str += format(ord(s[i]), '08b')
    return bin_str


# Fungsi konversi Binary ke Hexadecimal
def binary_to_hex(s):
    mp = {"0000": '0', "0001": '1', "0010": '2', "0011": '3',
          "0100": '4', "0101": '5', "0110": '6', "0111": '7',
          "1000": '8', "1001": '9', "1010": 'A', "1011": 'B',
          "1100": 'C', "1101": 'D', "1110": 'E', "1111": 'F'}
    hex_str = ""
    for i in range(0, len(s), 4):
        hex_str += mp[s[i:i + 4]]
    return hex_str

# Fungsi untuk memformat biner menjadi blok-blok 8 angka
def format_binary(binary_str, block_size=8):
    return ' '.join(binary_str[i:i + block_size] for i in range(0, len(binary_str), block_size))

# Permutasi awal (Initial Permutation)
def initial_perm_on_binary(binary_representation):
    ip_result = [None] * 64
    for i in range(64):
        ip_result[i] = binary_representation[initial_perm_table[i] - 1]
    ip_result_str = ''.join(ip_result)
    return ip_result_str

# Fungsi untuk konversi key menjadi biner menggunakan while loop
def key_in_binary_conv(original_key):
    if len(original_key) != 8:
        raise ValueError("Kunci harus berupa string dengan panjang 8 karakter (text)")
    
    binary_representation_key = ''
    i = 0  # Inisialisasi counter untuk indeks
    while i < len(original_key):  # Menggunakan while loop
        char = original_key[i]
        binary_key = format(ord(char), '08b')  # Konversi karakter ke ASCII 8-bit biner
        binary_representation_key += binary_key
        i += 1  # Increment counter untuk melanjutkan ke karakter berikutnya
    
    return binary_representation_key

# Fungsi untuk menghasilkan round key
def generate_round_keys(original_key):
    binary_representation_key = key_in_binary_conv(original_key)
    # Permutasi awal dengan PC1
    pc1_key_str = ''.join(binary_representation_key[bit - 1] for bit in pc1_table)
    
    # Pisahkan hasil permutasi menjadi dua bagian: left_key_part dan right_key_part
    left_key_part = pc1_key_str[:28]
    right_key_part = pc1_key_str[28:]
    
    round_keys = []
    
    for round_num in range(16):
        # Lakukan pergeseran pada setiap bagian berdasarkan jumlah shift di setiap ronde
        left_key_part = left_key_part[shift_per_round[round_num]:] + left_key_part[:shift_per_round[round_num]]
        right_key_part = right_key_part[shift_per_round[round_num]:] + right_key_part[:shift_per_round[round_num]]
        
        # Gabungkan kembali bagian kiri dan kanan
        combined_key_parts = left_key_part + right_key_part
        
        # Lakukan permutasi dengan PC2 untuk menghasilkan round key
        round_key = ''.join(combined_key_parts[bit - 1] for bit in pc2_table)
        round_keys.append(round_key)
    
    return round_keys

# Fungsi untuk enkripsi dengan opsi output dalam format biner atau hex
def encryption(user_input, original_key, output_format="bin"):
    convert_user_input_to_biner = string_to_binary(user_input)
    round_keys = generate_round_keys(original_key)  # key pertama
    ip_result_str = initial_perm_on_binary(convert_user_input_to_biner)
    
    # Pisahkan hasil permutasi awal menjadi bagian kiri dan kanan
    left_biner_perm = ip_result_str[:32]
    right_biner_perm = ip_result_str[32:]

    # Tampilkan L0 dan R0
    print(f"Initial Left (L0): {left_biner_perm}")
    print(f"Initial Right (R0): {right_biner_perm}")

    for round_num in range(16):
        # Ekspansi dari 32 ke 48 bit
        expanded_result = [right_biner_perm[i - 1] for i in e_exp_table]
        expanded_result_str = ''.join(expanded_result)
        round_key_str = round_keys[round_num]

        # Lakukan XOR antara hasil ekspansi dan kunci putaran
        xor_result_str = ''.join(
            str(int(expanded_result_str[i]) ^ int(round_key_str[i])) for i in range(48))
        
        six_bit_groups = [xor_result_str[i:i + 6] for i in range(0, 48, 6)]
        s_box_substituted = ''
        
        # Proses substitusi menggunakan S-Box
        for i in range(8):
            row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
            col_bits = int(six_bit_groups[i][1:5], 2)
            s_box_value = s_boxes[i][row_bits][col_bits]
            s_box_substituted += format(s_box_value, '04b')
        
        # Permutasi menggunakan P-Box
        p_box_result = [s_box_substituted[i - 1] for i in perm_box_table]
        new_right_biner_perm = ''.join(
            str(int(left_biner_perm[i]) ^ int(p_box_result[i])) for i in range(32))

        # Tampilkan hasil per ronde termasuk Left dan Right
        print(f"\nRound {round_num + 1} Encryption:")
        print(f"Left (L{round_num + 1}): {left_biner_perm}")
        print(f"Right (R{round_num + 1}): {right_biner_perm}")

        if output_format == "hex":
            print(f"Key: {binary_to_hex(round_key_str)}")
            print(f"Expanded Right: {binary_to_hex(expanded_result_str)}")
            print(f"XOR Result: {binary_to_hex(xor_result_str)}")
            print(f"S-Box Substituted: {binary_to_hex(s_box_substituted)}")
            print(f"P-Box Result: {binary_to_hex(''.join(p_box_result))}")
            print(f"New Right (R{round_num + 1}): {binary_to_hex(new_right_biner_perm)}\n")
        else:
            print(f"Key: {format_binary(round_key_str, 8)}")
            print(f"Expanded Right: {format_binary(expanded_result_str, 8)}")
            print(f"XOR Result: {format_binary(xor_result_str, 8)}")
            print(f"S-Box Substituted: {format_binary(s_box_substituted, 8)}")
            print(f"P-Box Result: {format_binary(''.join(p_box_result), 8)}")
            print(f"New Right (R{round_num + 1}): {format_binary(new_right_biner_perm, 8)}\n")

        # Pertukaran L dan R
        left_biner_perm, right_biner_perm = right_biner_perm, new_right_biner_perm

    # Gabungkan L16 dan R16, lalu lakukan permutasi akhir
    final_result = right_biner_perm + left_biner_perm
    final_cipher = ''.join([final_result[ip_inverse_table[i] - 1] for i in range(64)])

    # Pilih format akhir berdasarkan preferensi
    if output_format == "hex":
        final_cipher_hex = binary_to_hex(final_cipher)
        print(f"\nFinal Cipher (Hex): {final_cipher_hex}")
        return final_cipher_hex
    else:
        print(f"\nFinal Cipher (Binary): {final_cipher}")
        return final_cipher

# Fungsi untuk dekripsi
def decryption(final_cipher, original_key, output_format="bin"):
    round_keys = generate_round_keys(original_key)
    ip_dec_result_str = initial_perm_on_binary(final_cipher)
    
    # Pisahkan hasil permutasi awal menjadi bagian kiri dan kanan
    left_biner_perm = ip_dec_result_str[:32]
    right_biner_perm = ip_dec_result_str[32:]

    # Tampilkan L0 dan R0
    print(f"Initial Left (L0): {left_biner_perm}")
    print(f"Initial Right (R0): {right_biner_perm}")

    for round_num in range(16):
        # Ekspansi dari 32 ke 48 bit
        expanded_result = [right_biner_perm[i - 1] for i in e_exp_table]
        expanded_result_str = ''.join(expanded_result)
        round_key_str = round_keys[15 - round_num]

        # Lakukan XOR antara hasil ekspansi dan kunci putaran
        xor_result_str = ''.join(
            str(int(expanded_result_str[i]) ^ int(round_key_str[i])) for i in range(48))
        
        six_bit_groups = [xor_result_str[i:i + 6] for i in range(0, 48, 6)]
        s_box_substituted = ''
        
        # Proses substitusi menggunakan S-Box
        for i in range(8):
            row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
            col_bits = int(six_bit_groups[i][1:5], 2)
            s_box_value = s_boxes[i][row_bits][col_bits]
            s_box_substituted += format(s_box_value, '04b')
        
        # Permutasi menggunakan P-Box
        # Permutasi menggunakan P-Box
        p_box_result = ''.join([s_box_substituted[i - 1] for i in perm_box_table])  # P-Box result as string

        # XOR hasil P-Box dengan Left (L) dari ronde sebelumnya
        new_right_biner_perm = ''.join(
        str(int(left_biner_perm[j]) ^ int(p_box_result[j])) for j in range(32)  # XOR dengan bit-by-bit
        
        )
        # Tampilkan hasil per ronde termasuk Left dan Right
        print(f"\nRound {round_num + 1} Decryption:")
        print(f"Left (L{round_num + 1}): {left_biner_perm}")
        print(f"Right (R{round_num + 1}): {right_biner_perm}")

        if output_format == "hex":
            print(f"Key: {binary_to_hex(round_key_str)}")
            print(f"Expanded Right: {binary_to_hex(expanded_result_str)}")
            print(f"XOR Result: {binary_to_hex(xor_result_str)}")
            print(f"S-Box Substituted: {binary_to_hex(s_box_substituted)}")
            print(f"P-Box Result: {binary_to_hex(''.join(p_box_result))}")
            print(f"New Right (R{round_num + 1}): {binary_to_hex(new_right_biner_perm)}\n")
        else:
            print(f"Key: {format_binary(round_key_str, 8)}")
            print(f"Expanded Right: {format_binary(expanded_result_str, 8)}")
            print(f"XOR Result: {format_binary(xor_result_str, 8)}")
            print(f"S-Box Substituted: {format_binary(s_box_substituted, 8)}")
            print(f"P-Box Result: {format_binary(''.join(p_box_result), 8)}")
            print(f"New Right (R{round_num + 1}): {format_binary(new_right_biner_perm, 8)}\n")

        # Pertukaran L dan R
        left_biner_perm, right_biner_perm = right_biner_perm, new_right_biner_perm

    # Gabungkan L16 dan R16, lalu lakukan permutasi akhir
    final_result = right_biner_perm + left_biner_perm
    final_cipher = ''.join([final_result[ip_inverse_table[i] - 1] for i in range(64)])

    if output_format == "hex":
        print(f"\nFinal Decrypted Cipher (Hex): {binary_to_hex(final_cipher)}")
        return binary_to_hex(final_cipher)
    else:
        print(f"\nFinal Decrypted Cipher (Binary): {final_cipher}")
        return binary_to_ascii(final_cipher)

def main():
    while True:
        try:
            # Meminta input format dari pengguna
            input_format = input("Masukkan format input (text/hex): ").lower()
            if input_format not in ["text", "hex"]:
                raise ValueError("Format input tidak valid. Masukkan 'text' atau 'hex'.")

            # Meminta output format
            output_format = input("Masukkan format output per ronde (bin/hex): ").lower()
            if output_format not in ["bin", "hex"]:
                raise ValueError("Format output tidak valid. Masukkan 'bin' atau 'hex'.")

            # Meminta input pengguna
            user_input = input("Masukkan input (1 sampai 8 karakter jika text, 16 karakter jika hex): ")
            original_key = input("Masukkan kunci 8 karakter: ")
            if len(original_key) != 8:
                raise ValueError("Kunci harus berisi 8 karakter.")

            # Konversi input jika format adalah hex
            if input_format == "hex":
                if len(user_input) != 16:
                    raise ValueError("Input hex harus berisi 16 karakter.")
                user_input = hex_to_binary(user_input)
            elif input_format == "text":
                if not (1 <= len(user_input) <= 8):
                    raise ValueError("Input text harus berisi 1 hingga 8 karakter.")
                user_input = string_to_binary(user_input)

            # Enkripsi
            enc = encryption(user_input, original_key, output_format)
            print("\nTeks terenkripsi:", enc)

            # Konversi hasil enkripsi ke biner (untuk input format text)
            if input_format == "text":
                enc_to_binary = string_to_binary(enc)
            else:
                enc_to_binary = hex_to_binary(enc)

            # Dekripsi
            dec = decryption(enc_to_binary, original_key, output_format)
            print("\nTeks yang didekripsi:", dec)

            ulang = input("\nApakah Anda ingin menjalankan program lagi? (ya/tidak): ").lower()
            if ulang != 'ya':
                print("Program selesai. Terima kasih!")
                break

        except ValueError as e:
            print(f"Kesalahan: {e}")
            print("Silakan coba lagi.\n")

main()
