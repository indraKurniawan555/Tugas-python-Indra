print("Rumus menghitung balok dan kubus")
rumus = str(input('masukkan kode 1 untuk balok dan kode 2 untuk kubus : '))    
if(rumus=='1'):   
    print("Menghitung Volume balok")
    p = int(input('Panjang balok : '))
    l = int(input('Lebar balok : '))
    t = int(input('Tinggi balok : '))
    operator= str(input('Untuk menghitung, Jika A = Volume dan B = Luas permukaan, tolong masukkan A atau B : '))
    if(operator=='A'):
        v = p*l*t
        print ("Jika panjang balok",p,"lebar balok",l,"dan tinggi balok",t,"maka volume balok adalah", v)
    elif(operator=='B'):
        L = 2* int(p*l+l*t+p*t)
        print("Jika panjang balok",p,"lebar balok",l,"dan tinggi balok",t,"maka luas permukaan balok adalah", L)
    else:
        print("yang anda masukkan salah, tolong masukkan A atau B")
elif(rumus=='2'):
    print ("Menghitung Luas kubus")
    sisi = int(input('luas sisi : '))
    L = sisi*sisi*sisi
    print("Jika luas sisi kubus adalah",sisi,"maka luas kubus adalah", L )
else:
    print("Maaf yang anda masukkan salah")    




