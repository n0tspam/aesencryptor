### Updated AES Encryptor from Sektor7

I modified some of the code from the original snippets provided in the Malware Essentials course from Sektor7. I made changes around some types that were used for certain payload variables in the C++ file. I also extended the aesencryptor.py helper file so that it replaces the payloads directly to the C++ file because I did not want to repeatedly copy/paste. 
#### Usage:

The aesencryptor.py will now take two parameters like so: `python aesencryptor.py <file with shellcode> <c++ file that you wish to overwrite with your payload>`. 

This will produce a new `.cpp` file prefixed with `enc_` that you can rename to `implant.cpp` and use with `compile.bat`. 
