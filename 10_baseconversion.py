# binary to decimal
fh = open("10_baseconversion.txt","w")
numb = input("Enter the number in base 2: ")
answer = int(numb,2)
fh.write(str(numb))
fh.write("\nConversion of above binary number into decimal is: ")
fh.write(str(answer))

#decimal to binary
numb = int(input("Enter the number in base 10: "))
ans = bin(numb)
fh.write("\n")
fh.write(str(numb))
fh.write("\nConversion of above decimal number into binary is: ")
fh.write(str(ans[2:]))
fh.close()