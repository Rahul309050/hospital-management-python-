

def welcome():
	print("WELCOME TO HOSPITAL\n1.RegisteringPatient details\n2.RegisteringDoctor details\n3.RegisteringWorker details]\n4.total patient details\n5.total doctor details\n6.total worker details\n7.Exit")


   


def gainAccess(Username=None, Password=None):
	Username = input("Enter your username:")
	Password = input("Enter your Password:")

	if not len(Username or Password) < 1:

		if True:
			db = open("database.txt", "r")
			d = []
			f = []
			for i in db:
				a, b = i.split(",")
				b = b.strip()
				c = a, b
				d.append(a)
				f.append(b)
			data = dict(zip(d, f))
			# print(data)

			try:
				if data[Username]:
					try:
						if Password == data[Username]:
							print("Login success!")
							print("Hi", Username)
							welcome()
						else:
							print("Incorrect password or username")
					except:
						print("Incorrect password or username")

				else:
					print("Password or username doesn't exist")
			except:
				print("Password or username doesn't exist")

		else:
			print("Error logging into the system")

	else:
		print("Please attempt login again")
		gainAccess()

		# b = b.strip()
# accessDb()


def register(Username=None, Password1=None, Password2=None):
	Username = input("Enter a username:")
	Password1 = input("Create password:")
	Password2 = input("Confirm Password:")

	db = open("database.txt", "r")
	d = []
	for i in db:
		a, b = i.split(",")
		b = b.strip()
		c = a, b
		d.append(a)

	if not len(Password1) <= 8:
		db = open("database.txt", "r")

		if not Username == None:
			if len(Username) < 1:
				print("Please provide a username")
				register()
			elif Username in d:
				print("Username exists")
				register()

			else:

				if Password1 == Password2:
					db = open("database.txt", "a")
					db.write(Username+", "+Password1+"\n")
					print("User created successfully!")
					print("Please login to proceed:")


				else:
					print("Passwords do not match")
                    
					gainAccess()

	else:
		print("Password too short")
  

def home(option=None):
	print('---------------------------------------------\nHOSPITAL MANAGEMENT SYSTEM\n---------------------------------------------\nGOD WISHES YOU')

	option = input("Press 1 for login\nPress 2 for Signup\n")
	if option == "1":
		gainAccess()
    
  
	elif option == "2":
		register()
	else:
    		print("Please enter a valid parameter, this is case-sensitive")

home()



choice=int(input('ENTER YOUR CHOICE:'))
pb = open("database2.dat", "a")


if choice==1:
      p_name=input('Enter Patient Name:')
      p_age=int(input('Enter Age:'))
      p_problems=input('Enter the Problem/Disease:')
      p_phono=int(input('Enter Phone number:'))
      rel=(p_name+","+str(p_age)+","+p_problems+","+str(p_phono)+"\n")
      print("successfully registered")
      pb.close()
    #   welcome()
      
      
      
elif choice==2:
      d_name=input('Enter Doctor Name:')
      d_age=int(input('Enter Age:'))
      d_department=input('Enter the Department:')
      d_phono=int(input('Enter Phone number:'))
      
      rec=(d_name+","+str(d_age)+","+d_department+","+str(d_phono)+"\n")
      print("successfully registered")
      pb.close()
 
  
  
  
elif choice==3:
      w_name=input('Enter Worker Name:')
      w_age=int(input('Enter Age:'))
      w_workname=input('Enter type of work:')
      w_phono=int(input('Enter Phone number:'))
      
      reb=(w_name+","+str(w_age)+","+w_workname+","+str(w_phono)+"\n")
      print("successfully registered")
      pb.close()
      
elif choice==4:
      print("total patient details")
      pb = open("database2.dat", "r",newline='\r\n')
      for line in pb:
          print(line)

elif choice==5:
    print("Total doctor details")
    pb = open("database2.dat", "r",newline='\r\n')
    for line in pb:
        print(line)
        

elif choice==6:
    print("Total worker details")
    pb = open("database2.dat", "r",newline='\r\n')
    for line in pb:
        print(line)


elif choice==7:
      exit()
     

