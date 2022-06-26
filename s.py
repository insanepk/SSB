import os, platform, time

b = platform.architecture()[0]

if b == '64bit':

    print("\n\x1b[1;92mCongratulations Your Device Support This Tool\033[1;37m")

    os.system('xdg-open https://youtu.be/3CVApc0CkhY/');time.sleep(5)

    import SSB

elif b == '32bit':

    print("\n\x1b[1;92mCongratulations Your Device Support This Tool\033[1;37m")

    os.system('xdg-open xdg-open https://api.whatsapp.com/send/?phone=923086271330&text=Hello_mr_insane/');time.sleep(5)

    import SSB
