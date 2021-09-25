import os


os.system("tput setaf 5")
print("\t\t\tWelcome to My Menu")
os.system("tput setaf 7")

os.system("espeak-ng 'welcome'")


print("\t\t\t------------------"	)
print()

print("where u want to run ur program  (local/remote): " , end='')
myhost = input()
print(myhost)

if myhost == "remote":
	remote_ip = input("Enter ur remote host ip : ")

print()

while True:
	print("""
	Funny Linux commands
	Press 1 : sl
	Press 2 : Cowsay
	Press 3 : cowsay ghostbusters
	Press 4 : cowsay stegosaurus
	Press 5 : cowthink
	press 6 : fortune
	press 7 : fortune and cowsay command
	press 8 : oneko
	press 9 : exit
	""")

	# espeak-ng

	print("enter ur choice : ", end='')
	ch = input()

	print(ch)

	if myhost == "local":
		if int(ch) == 1:
			os.system("sl")

		elif int(ch) == 2:
			os.system("cowsay 'Hey Hello,How are you?'")

		elif int(ch) == 3:
			os.system("cowsay -f ghostbusters Who you Gonna Call")

		elif int(ch) == 4:
			os.system("cowsay -f stegosaurus ...Ohh my god what is this????")

		elif int(ch) == 5:
			os.system("cowthink Hmmm ,wow!!!!")

		elif int(ch) == 6:
			os.system("fortune | cowsay")

		elif int(ch) == 7:
			os.system,("fortune | cowsay -f turtle")
		
		elif int(ch) == 8:
			os.system("oneko -dog")		
			
		elif int(ch) == 9:
			exit()

		else:
			print("not supported")

	input("Do you want to Continue,please Enter.....")
	os.system("clear")
