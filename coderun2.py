def findMinimum(n, a, b):
  pria=[]
  wanita=[]
  hasil_operasi=[]

  for i in range(n):
    if a[i]==0:
      pria.append(b[i])
    else:
      wanita.append(b[i])

  for k in pria:
        for l in wanita:
            hasil = k - l
            akhir = abs(hasil)
            hasil_operasi.append(akhir)
  for m in range(len(hasil_operasi)):
    print("hasil operasi ke-",m+1,": ", hasil_operasi[m])
  
  print ("Hasil pengurangan terkecil: ",min(hasil_operasi)) 

  
findMinimum(5,
[0 , 0 , 1 , 0 , 1],
[1 , 13 , 9 , 7 , 15])