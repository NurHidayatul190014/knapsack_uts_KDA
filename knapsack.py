def textToBinary(kata_str):
    print("String: " + str(kata_str))
    res = ''.join(format(ord(i), '08b') for i in kata_str)
    print("String to Binary: " + str(res))
    return str(res)

def binaryToText(s):
    print("Binary: "+s)
    binary = ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
    print("Binary to String: "+ binary)
    return binary

#membuat kunci sementara untuk proses dekripsi
def temp_key(key):
    list_key = []

    for i in key:
        list_key.append(i)
    
    return list_key

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
        if len(teks) == 6:
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

    print("list chipper  ", list_chiperteks)

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
    
    print("hasil mod ", list_hasil)

    # proses deksripsi ke binary teks
    #hasil mod di buat binary
    plaintext = ""

    for i in list_hasil:
        hasil_mod = i
        temp = temp_key(privateKey)
        ulang = True

        while ulang:
            key = temp[0]
            count = key

            for i in range(len(temp) - 1, 0, -1):
                count += temp[i]
                
                if count > hasil_mod:
                    temp.remove(temp[i])
                    break
                elif len(temp) == 4:
                    if key + temp[1] == hasil_mod:
                        ulang = False
                        break
                    else:
                        temp = temp_key(privateKey)
                        temp.remove(key)
                elif count == hasil_mod:
                    ulang = False
        print("temp  ", temp)
        for i in privateKey:
            if i in temp:
                plaintext += "1"
            else:
                plaintext += "0"



    print("plaintetxt = ", plaintext)



privateKey= [2, 3, 6, 13, 27, 52]
m = 105
n = 31
publicKey = generatePublicKey(privateKey, m , n)
print(publicKey)

masuk = "hayaku"


plaintext = textToBinary(masuk)
list_chiperteks =  enkripsi(plaintext, publicKey)

dekripsi(privateKey, m, n, list_chiperteks)
