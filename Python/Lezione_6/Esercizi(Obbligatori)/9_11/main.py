from users import *

u1 = User ("Gabriele", "Cutolo", "GabbyGab", "gabbro@gmail.com")
p1 = Privileges (["Pin messages", "Delete messages", "Check log", "Schedule meeting"])

a1 = Admin (u1, p1)

a1.user.describe_user()
a1.user_privileges.show_privileges()