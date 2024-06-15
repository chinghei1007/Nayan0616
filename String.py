# f-strings
f_name = "John"
l_name = "Doe"
print(f"My name is {f_name} {l_name}")

#join strings
name = " ".join([f_name,l_name])
name2 = f_name+l_name
print (name)
print((name2))

#upper, lower, title
print(name.lower().title())

#strip
name_notStripped = (f"           {f_name} {l_name}         ")
print(f"Before strip: {name_notStripped}")
print(f"After strip: {name_notStripped.strip()}")

#replace
name_replace = "John Doe".replace("doe", "eod")
print(f"This Does not change anything: {name_replace}")
name_replace = name_replace.lower().replace("doe","eod").title()
print(f"This changes with the upper cases deleted: {name_replace}")

#\n\t