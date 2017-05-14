# Captcha Letters Generator
Generator for captcha letters
# How to use it
To generate captcha letters follow these steps:
- In captcha directory create salt.py with the value for your salt key:
```python
salt = "IamSoSalty"
```
- Provide plain letter files in directory captcha/sources. For example:
 ```
 a_0001.png
 b_0001.png
 ...
 z_0001.png
 ```
 - Run generate_letters.py
 
 As a final result you will have generated letters in captcha/output directory.