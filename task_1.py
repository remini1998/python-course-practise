generator = lambda a, b: [str(pow(a, i)) for i in range(b)]

num = int(input("Please input the number:"))

print(" ".join(generator(num, 5)))
print(",".join(generator(num, 5)))
print("\n".join(generator(num, 5)))
