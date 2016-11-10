import qrcode





def lezen():
    reservaties = open('text.txt' , 'r')
    code = (reservaties.readlines())
    reservaties.close()



    img = qrcode.make(code)
    print(img)
    img.save('iets.png')


lezen()




