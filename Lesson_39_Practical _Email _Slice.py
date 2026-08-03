# -----------------------------
# ---Practical - Email Slice---
# -----------------------------

theName = input('What\'s Your Name ?').strip().capitalize()
theEmail = input('What\'s Your Email ?').strip()

theUserName = theEmail[:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@") + 1:]

print(f"Hello {theName} Your Email IS {theEmail}")
print(f"Your Username Is {theUserName}\n And Your Website {theWebsite}")
