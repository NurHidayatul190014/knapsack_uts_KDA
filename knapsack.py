def textToBinary(kata_str): #convert text ke binary
    res = ''.join(format(ord(i), '08b') for i in kata_str)
    print("teks ke Binary: " + str(res))
    return str(res)

def binaryToText(s): #convert binary ke text
    binary = ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
    print("Binary ke teks: "+ binary)
    return binary

def generatePublicKey(superincrasing, m ,n):  #membuat public key
    publicKey = []
    for i in superincrasing:
        a = (i * n)%m 
        publicKey.append(a)
    return publicKey

def enkripsi(plaintext, publicKey):
    list_text = [] #membuat text jadi blok
    teks = ""  #menampung teks sementara sebelum di masukkan list
    for i in plaintext: #membagi dan memasukkan text dalam bentuk blok ke var list_text
        teks += i
        if len(teks) == 4:
            list_text.append(teks)
            teks = ""
    
    list_chiperteks = []
    for i in list_text:  #blok dijadikan cipertext
        kriptogram = 0
        indeks = 0
        for j in i: #hitungan menjadi kriptogram
            hitung = (int(j)*publicKey[indeks])
            kriptogram += hitung
            indeks += 1

        list_chiperteks.append(kriptogram) #masukkan kriptogram ke var list_chiperteks
        indeks = 0
        kriptogram = 0

    return list_chiperteks

def dekripsi(privateKey, m, n, list_chiperteks):
    k = 0
    loop = True
    while loop: #mencari nilai n^-1
        n_min1 = (1 + m * k)/n
        loop = not n_min1.is_integer()
        k += 1
    
    # mencari nilai dari enkripsi[x] * n_min1 % m lalu disimpan di list_hasil
    list_hasil = []
    for i in list_chiperteks:
        hasil = i * n_min1 % m
        list_hasil.append(hasil)

    # proses deksripsi ke binary teks
    #hasil mod di buat binary
    plaintext = ""

    for i in list_hasil: #tiap hasil mod dicari biner nya
        hasil_mod = i
        temp_plaintext = []
        for i in range(len(privateKey) - 1, -1, -1): #pengurangan hasil modulus dengan isi private key
            if hasil_mod >= privateKey[i]:
                hasil_mod -= privateKey[i]
                temp_plaintext.append("1")
            else:
                temp_plaintext.append("0")

        # yang ada di temp_plaintext itu masih terbalik biner nya
        #jadi ini di urutkan terus di jadikan satu di var plaintext nya
        for i in range(len(temp_plaintext) - 1, -1, -1):
            plaintext += temp_plaintext[i]

    return plaintext



privateKey= [2, 3, 6, 13]
m = 105
n = 31
publicKey = generatePublicKey(privateKey, m , n)

print("")
print("+++++++ algoritma knapsack (merkle-hellman)+++++")
print("kunci private: ", privateKey)
print("kunci publik: ",publicKey)

# input teks
masuk = str(input("masukkan kata yang diinginkan = "))
print("")

# enkripsi
print("+++++++ enkripsi ++++++")
plaintext = textToBinary(masuk)
list_chiperteks =  enkripsi(plaintext, publicKey)
print("hasil chiperteks: ", list_chiperteks)

#dekripsi
print("")
print("+++++++ dekripsi ++++++")
deskrip = dekripsi(privateKey, m, n, list_chiperteks)
binaryToText(deskrip)
print("")
