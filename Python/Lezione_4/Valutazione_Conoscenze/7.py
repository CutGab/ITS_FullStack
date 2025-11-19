# Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
# For example:

# Test	Result
# print(check_parentheses("()()"))
# True
# print(check_parentheses("(()))("))
# False

def check_parentheses(parentesi: str):

    parentesi_completate = 0

    for i in parentesi:
        if i == "(":
            parentesi_completate += 1
        else:
            parentesi_completate -= 1
            
        if parentesi_completate < 0:
            return False
        
    return parentesi_completate == 0

print(check_parentheses("()()"))

print(check_parentheses("(()))("))

print(check_parentheses(")("))

print(check_parentheses("((("))