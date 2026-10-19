def check_word_structure(message):
    # Message ko words mein tod lo
    words = message.split()
    
    # Agar koi word hi nahi hai (khali hai)
    if not words:
        return "Flagged: No words found"
    
    # Agar pehla word hi 3 letter se chota hai (jaise "hi", "ok")
    elif len(words) == 1 and len(words[0]) < 3:
        return "Flagged: Single word is too short"
        
    else:
        return "Message Approved: Looks Good"

# --- Test Cases ---
print(check_word_structure("ok"))         
# Expected: Flagged (Single short word)

print(check_word_structure("a b c"))      
# Expected: Message Approved (Kyunki multiple words hain)

print(check_word_structure("python"))     
# Expected: Message Approved (Valid word)




























    














