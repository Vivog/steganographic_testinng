from steganocryptopy.steganography import Steganography
# Generate crypto key
Steganography.generate_key("")
secret = Steganography.encrypt('key.key', 'img/tst.jpg', 'txt/tst.txt')
# Save secret text to img
# Secret img must be *.png
secret.save('img/tst_s.png')
result = Steganography.decrypt('key.key', 'img/tst_s.png')
print(result)