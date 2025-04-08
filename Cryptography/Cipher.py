class Cipher:
    def encrypt123(s):
        s=s.upper()
        output=""
        for ch in s:
            num=ord(ch)-64
            output=output+str(num)+" "
        return output
    def decrypt123(s):
      output=""
      nums=s.split()
      for n in nums:
        x=int(n)+64
        output=output+chr(x)
      return output
    def encrypt_rot3(s):
        s=s.upper()
        output=""
        for ch in s:
            if ch !=" ":
                num=ord(ch)+3
                if num>90:
                    num=num-26
                output=output+chr(num)
            else: output=output+" "
        return output
    def decrypt_rot3(s):
        s=s.upper()
        output=""
        for ch in s:
            if ch !=" ":
                num=ord(ch)-3
                if num<65:
                    num=num+26
                output=output+chr(num)
            else: output=output+" "
        return output
    def rot13(s):
      s=s.upper()
      output=""
      for ch in s:
        if ch!=" ":
          num=ord(ch)+13
          if num>90:
            num=num-26
          output=output+chr(num)
        else: output=output+" "
      return output
    def encrypt_rotn(s,n):
        s=s.upper()
        output=""
        for ch in s:
            if ch !=" ":
                num=ord(ch)+n
                if num>90:
                    num=num-26
                output=output+chr(num)
            else: output=output+" "
        return output
    def decrypt_rotn(s,n):
        s=s.upper()
        output=""
        for ch in s:
            if ch!=" ":
                num=ord(ch)-n
                if num<65:
                    num=num+26
                output=output+chr(num)
            else: output=output+" "
        return output
    map1={"A":"H","B":"L","C":"B","D":"J",
           "E":"D","F":"Q","G":"S","H":"A",
           "I":"P","J":"Y","K":"G","L":"R",
           "M":"X","N":"K","O":"M","P":"V",
           "Q":"C","R":"I","S":"T","T":"F",
           "U":"N","V":"Z","W":"U","X":"W",
           "Y":"E","Z":"O"," ":" "}
    reverse_map1={v:k for k,v in map1.items()}
    def map_cipher(s,direction):
        s=s.upper()
        output=""
        for ch in s:
            if direction=="e":
                output=output+Cipher.map1[ch]
            elif direction=="d":
                output=output+Cipher.reverse_map1[ch]
        return output
    def rot_more(s):
        output=""
        for ch in s:
            if ch!="\n":
              num=ord(ch)+47
              if num>125:
                num=num-94
              output=output+chr(num)
            elif ch=="\r":
                pass
            else: output=output+chr(10)
        return output
    def vigenere(s,k,f):
        output=""
        s=s.upper()
        s="".join(s.split())
        k=k.upper()
        k_rep=(k*(len(s)//len(k)))+k[:len(s)%len(k)]
        for i in range(len(s)):
            if s[i].isalpha():
                shift=ord(k_rep[i].upper())-ord("A")
                if f=="e":
                    output+=chr((ord(s[i])+shift-ord("A"))%26+ord("A"))
                if f=="d":
                    output+=chr((ord(s[i])-shift-ord("A"))%26+ord("A"))
            else: pass
        return output
