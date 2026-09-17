'''
Program 85
Please write a program to compress and decompress the string "hello world!hello
world!hello world!hello world!".
'''
import zlib

string = "hello world!hello world!hello world!hello world!"

compressed_string = zlib.compress(string.encode())

decompressed_string = zlib.decompress(compressed_string).decode()


print("Original string : ", string)
print("Compressed String :", compressed_string)
print("Decompressed String :", decompressed_string)