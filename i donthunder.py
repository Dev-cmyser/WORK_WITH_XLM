def increment_string(strng):
    
    if strng == "" :
        return "1"
    ls_char = strng[-1]
    try:
        int(ls_char)
    except ValueError:
        return strng + "1"    
    new_str = ""
    num =""
    count = 0
    for i in strng:
        
        try:
            i = int(i)
            
            if i == 0:
                new_str = new_str + str(i)
                
            if i != 0:
                num = num + str(i)
                count += 1
        except ValueError:
            new_str = new_str + i
            
        

        
    print(num)
            
    print(new_str)
    
    if count == 0:
        h = len(new_str)
        
        return new_str[:h-1] +"1"
    
    if num == "":
        return new_str + "1"
    if len(num) < len(str(int(num)+1)):  
        s = ""
        
        for i in new_str:

            if i == "0":
                i = ""
            s = s +i
        
        return s + str( int(num) + 1)
    return new_str + str( int(num) + 1)   