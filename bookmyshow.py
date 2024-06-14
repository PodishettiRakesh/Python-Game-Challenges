def initialize_movies():
    shows=[]
    
    while True:
            n=int(input("Number of movies you want to initialize: "))
            if n.isdigit():
                break
            else:
                print("Number of movies should be in digits")
                
    for i in range(n):
        dic={}
        movie=input("enter the movie name to be added: ")
        duration=input("enter the duration : ")
        dic["movies"]=movie
        dic["duration"]=duration
        dic["no.of seats"]=100
        dic["seatsbooked"]=0
        dic["seatsavailable"]=100
        seats=[]

        for i in range(1,11):
            r=[]
            for j in range(1,11):
                r.append(j)
            seats.append(r)
        dic["seats"]=seats

        shows.append(dic)

    return shows
print(initialize_movies())

def display_movies(show):
    for i in range(len(show)):
        print(i+1,"movie")
        print("Movie Name: ",show[i]["movies"])
        print("Duration of movie: ",show[i]["duration"])
        print("number of seats for movie : ",show[i]["no.of seats"])
        print("-----------------------------------------")


def display_seating(show,i):
        print("number of seats for movie : ",show[i]["no.of seats"])
        print("Number of seats booked: ",show[i]["seatsbooked"])
        print("Number of seats available: ",show[i]["seatsavailable"])
        for j in range(len(show[i]["seats"])):
             for z in range(len(show[i]['seats'][0])):
                  print(show[i]["seats"][j][z],end=' ')

             print()


def book_seat(show,i):
    n=int(input("number of seats to be booked: "))
    j=1
    seats_booked=[]
    while j<n+1:
        row=int(input("Enter the row u wanted to book: "))
        col=int(input("Enter the col u wanted to book: "))
        if show[i]["seats"][row][col]!="X":
            show[i]["seats"][row][col]="X"
            show[i]["seatsavailable"]-=1
            show[i]["seatsbooked"]+=1
            seats_booked.append((row,col))
            j+=1
        else:
            print("Book an another seat . It is already booked!!")
  
    return show,i,seats_booked

def view_booking(show,i,seats_booked):
        user_bookings=[]
        for j in range(len(seats_booked)):
           user_bookings.append("seat at "+str(seats_booked[j][0])+"row and "+str(seats_booked[j][1])+"column is booked"+ "for movie"+str(show[i]["movies"]))
        show[i]["seatsavailable"]-=1
        show[i]["seatsbooked"]+=1
        print(" your latest bookings are: ")
        for j in range(len(user_bookings)-1,-1,-1):
             print(user_bookings[j])
        

def display_menu():
     print('           ')
     print("""a. View Movies
              b. Check Seat Availability
              c.Book a seat
              d. View bookings
              e. exit""")
     print("           ")
    


def main():
     print("Welcome to book my show")
     show=initialize_movies()
    
     while True:
        display_menu()
        choose=input("Select the option you wanted to perform: ")

        if choose=="a":
            display_movies(show)


        if choose=="b":
            while True:
                i=int(input("enter the index of the movie you want to book for: "))
                if i.isdigit():
                    break
                else:
                    print("Enter the index value in digits")
            while True:
                if i >len(show):
                        print("No movie is present at that index")
                else:
                   display_seating(show,i)
                break


        if  choose=="c":
            
                while True:
                    i=int(input("enter the index of the movie you want to book for: "))
                    if i.isdigit():
                        break
                    else:
                        print("Enter the index value in digits")
                while True:
                    if i >len(show):
                        print("No movie is present at that index")
                    else:
                        show,i,seats_booked= book_seat(show,i)
                        break


        if choose=="d":
            while True:
                    i=int(input("enter the index of the movie you want to book for: "))
                    if i.isdigit():
                        break
                    else:
                        print("Enter the index value in digits")
        
            while True:
                if i >len(show):
                        print("No movie is present at that index")
                else:
                    view_booking(show,i,seats_booked)
                    break


        if choose=="e":
             print(" you are exiting the app")
             break
        print("----------------------------------")
        

# main()
             
             


               



        
     






