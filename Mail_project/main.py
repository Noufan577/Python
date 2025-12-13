#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(r"C:\Users\noufa\OneDrive\Desktop\ml\python\Mail_project\Input\Letters\starting_letter.txt") as content:
    a=content.read()
    with open(r"C:\Users\noufa\OneDrive\Desktop\ml\python\Mail_project\Input\Names\invited_names.txt")  as names:
         names=names.readlines()
         count=0
         for i in names:
              count+=1
              s=i.strip()
              with open(rf"C:\Users\noufa\OneDrive\Desktop\ml\python\Mail_project\Output\{s}.txt","w") as result:
                   result.write(a.replace("[name]",s))

print(f"created all {count} files ready for sent")
