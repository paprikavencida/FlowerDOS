# FlowerDOS 0.1.0
# Chroma Flower Software

print("==============================")
print("       FlowerDOS v0.1")
print("  Experimental command-line")
print("==============================")

name = input("What is your name? ")

if name == "paprika":
    print("Welcome back, paprika!")
else:
    print("Welcome to FlowerDOS, " + name + "!")

print("System initialized.")

while True:
    print("FlowerDOS is running")

    if command == "exit":
        break
