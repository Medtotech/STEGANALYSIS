#Evelyn Okougbo
#Steganalysis: Hidden Watermark extraction
#10/13/2018


from PIL import Image


global_lsb = ""

def extract_message(global_lsb):
    stego = Image.open("Themoon.png") #open image
    width, height = stego.size

    for i in range(height):
        for j in range(width):
            r, g, b = stego.getpixel((j, i))
            #binary values
            red = bin(r) 
            green = bin(g)
            blue = bin(b)
    
            #get lsb
            lsb_r= red[-1]
            lsb_g= green[-1]
            lsb_b = blue[-1]
             
            """Testing possible combinations"""
            #lsb = lsb_g
            #lsb = lsb_r
            #lsb = lsb_r + lsb_b
            #lsb = lsb_g + lsb_b
            #lsb = lsb_r + lsb_g
            #lsb = lsb_r + lsb_g + lsb_b
       
            lsb =lsb_b
            global_lsb = global_lsb + lsb
            

    message = []
    for i in range(0, len(global_lsb), 8):
        character = chr(int(global_lsb[i:i+8], 2))
        message.append(character)

    
    string = "".join(x for x in message) #join characters
    f = open("copyright.txt","wb") #Write message
    f.write(str(string))
    f.close()

    print "Message extracted!"

                           
extract_message(global_lsb)




        
        




    

    
        

        





                
                
                
                
            
