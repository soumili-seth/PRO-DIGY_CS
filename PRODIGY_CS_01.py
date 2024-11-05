def scissors_cipher_encrypt(text, rails):
   
    rails_list = [''] * rails
    
    dir = 1  
    rail = 0  
    
   
    for char in text:
        
        rails_list[rail] += char
        

        rail += dir
        
        if rail == rails - 1 or rail == 0:
            dir *= -1
    
   
    encrypted_text = ''.join(rails_list)
    
    return encrypted_text

def scissors_cipher_decrypt(encrypted_text, rails):
   
    rail_lengths = [0] * rails
    
   
    dir = 1  
    rail = 0  
    
   
    for _ in range(len(encrypted_text)):
      
        rail_lengths[rail] += 1
        
       
        rail += dir
        
      
        if rail == rails - 1 or rail == 0:
            dir *= -1
    
   
    rails_list = []
    start = 0
    for length in rail_lengths:
        rails_list.append(encrypted_text[start:start + length])
        start += length
    
  
    decrypted_text = [''] * len(encrypted_text)
    
  
    dir = 1  
    rail = 0 
    index = 0  
    
   
    for rail_text in rails_list:
       
        for char in rail_text:
          
            decrypted_text[index] = char
            
           
            index += dir
            
           
            if index == len(encrypted_text) - 1 or index == 0:
                dir *= -1
    
  
    decrypted_text = ''.join(decrypted_text)
    
    return decrypted_text

def main():
   
    text = input("Enter the text to encrypt/decrypt: ")
    rails = int(input("Enter the number of rails: "))
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ")
    
   
    if choice.upper() == 'E':
        encrypted_text = scissors_cipher_encrypt(text, rails)
        print(f"Encrypted text: {encrypted_text}")
    elif choice.upper() == 'D':
        decrypted_text = scissors_cipher_decrypt(text, rails)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
