a='''
People find it difficult to differentiate digital forensics with regular forensics. A digital forensic investigation is based on using digital assets to trace and prove a chain of events on other digital devices. Some criminals use techniques such as steganography and cryptography to hide information in plain sight. Steganography and cryptography are sometimes difficult to figure out, and some out-of-the-box thinking is required. We can try using various methods, such as finding hidden codes within things as simple as words, sentences, or pictures. Often, it is the simplest strategies that are overlooked. Reading carefully is important in understanding patterns that may be present. Determining the most effective strategy is what makes a good digital investigator. Investigations are usually time consuming and require patience to solve them. Spending time on these problems is key. 
Passwords are a key piece of information that one must obtain to access restricted content. Regularly, these passwords are not stored securely enough. Often times, these passwords are simply not strong enough and prove to be a weak point. Very strong passwords, such as those that are complicated and long with a mixture of characters, are difficult to crack. Exploiting passwords is one common way an attacker may gain access to restricted information.
'''
b=[]
for c in a:
    if not c==c.lower():
        b.append(c)

print("".join(b))