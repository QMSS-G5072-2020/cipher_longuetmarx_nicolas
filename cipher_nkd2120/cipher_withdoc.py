def cipher(text, shift, encrypt=True):
   """
   Encodes the secret message that has been entered by the user. 
   VERY CONFIDENTIAL!
   Parameters
   ----------
   text : The initial message you want to encrypt
     A string. 
   shift : The number of letter you want to move from. 
       A float. 
   Returns
   -------
   new_text: the encrypted message. 
   Examples
   --------
   >>> from cipher_nkd2120 import cipher
   >>> my_message ="I have secret information"
   >>> my_ket = 3
   >>> cipher(my_message, my_key)
   """

   alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   new_text = ''
   for c in text:
      index = alphabet.find(c)
      if index == -1:
         new_text += c
       else:
          new_index = index + shift if encrypt == True else index - shift
          new_index %= len(alphabet)
          new_text += alphabet[new_index:new_index+1]
   return new_text

   