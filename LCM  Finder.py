# 📌 Program to find the LCM of two numbers

def lcm(a, b):
    # Choose the greater number as a starting point
    if a > b:
        greater = a
    else:
        greater = b
    
    # Keep increasing until we find the LCM
    while True:
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        greater += 1
    return lcm

print("🔢 Welcome to the LCM Finder! 🎯")
num1 = int(input("👉 Enter the first number: "))
num2 = int(input("👉 Enter the second number: "))

print(f"✅ The LCM of {num1} and {num2} is: {lcm(num1, num2)} 🎉")
