# INTRODUCTION
FlawlessFear is an desktop anti-theft application developed in Python for notebook users to defend against theft or assault by criminals.

Although this application is focused on fighting crime, it can also be useful in case you lose your laptop or if it was stolen and you still don't know it.

At the moment the application only takes photos when it detects a face at the time of initialization, it is saved locally and sent to your email if it has internet access, but the idea is to extend it to capture enough information (such as exact location, capture audio or video and receive it in your mail) that can either be used to track the laptop for you or can be used to make a respective report to the police (although the incompetent police will not investigate anything anyway).

The application is and always will be free, but the implementation of the use of various services implies the use of servers or using APIs such as Google Maps for coordinates and geolocation, so the development cost will be really complicated.

# YOU NEED

Python 3.11 ~~not really~~ (just type "python --version" in your terminal to check the version)

# INSTALLATION

## LINUX

1. Open terminal

```
git clone https://github.com/Ferxas/FlawlessFear.git
```
```
cd FlawlessFear
```
```
pip install -r requirements.txt
```
```
python3 flawlessFear.py
```
# TO-DO LIST

- Create a GUI
- implement friendly tracking services for the user experience
- Add more features like send to other devices


# RELEASE NOTES

1.0.0 - First release.
=======
>>>>>>> d4cd0f6373746665ae5ab171e9f7ed2f26888437
