import uuid
bus=[]
agent=[]
booked_tickets=[]
while (True):
    first_screen="1.Admin login\n2.Agent login\n3.Exit"
    print(first_screen)
    choice1=int(input())
    if (choice1==1):
        admin_screen="1.Add bus\n2.Add Agent\n3.Logout"
        print(admin_screen)
        choice2=int(input())
        if choice2==1:
            busname=input("busname:")
            From=input("From:")
            To=input("To:")
            total_seat=int(input("total_seat:"))
            price=eval(input("price:"))
            bus_id=str(uuid.uuid4())
            instance={
                "busname":busname,
                "From":From,
                "To":To,
                "total_seat":total_seat,
                "price":price,
                "bus_id":bus_id,
                "available_seat":total_seat
            }
            print(instance)
            bus.append(instance)
        elif choice2==2:
            agent_name=input("agent_name:")
            mobile_number=input("mobile_number:")
            password=input("password:")
            agent_code=str(uuid.uuid4())
            instance={
                "agent_name":agent_name,
                "mobile_number":mobile_number,
                "password":password,
                "agent_code":agent_code
            }
            print(instance)
            agent.append(instance)
        elif choice2==3:
            continue
    elif (choice1==2):
        print("enter the login credentials")
        agent_code=input("agent_code:")
        password=input("password:")
        for i in agent:
            if i["agent_code"]==agent_code and i["password"]==password:
                print("Successfully logged in...")
                while(True):
                    last_screen="1.List the bus details\n2.Book ticket\n3.Show my booking\n4.Logout"
                    print(last_screen)
                    choice3=int(input())
                    if choice3==1:
                        print(bus)
                    if choice3==2:
                        bus_id=input("bus_id:")
                        print("Bus details:")
                        for j in bus:
                            if j["bus_id"]==bus_id:
                                print(j["busname"])
                                print(j["From"])
                                print(j["To"])
                                print(j["available_seat"])
                                no_of_ticket=int(input("no_of_ticket:"))
                                if (no_of_ticket<=j["available_seat"]):
                                    total_fare=no_of_ticket*j["price"]
                                    print(total_fare)
                                    print("confirm_booking:1.Yes\n2.No")
                                    confirm=int(input())
                                    if confirm==1:
                                        j["available_seat"]-=no_of_ticket
                                        booked_tickets.append({
                                            "bus_name":j["busname"],
                                            "From":j["From"],
                                            "To":j["To"],
                                            "No_of_ticket_booked":no_of_ticket,
                                            "total_fare":total_fare,
                                            "agent_code":i["agent_code"]
                                        })
                                    else:
                                        break
                                else:
                                    print("Tickets not availble")
                    if choice3==3:
                        for k in booked_tickets:
                            if k["agent_code"]==i["agent_code"]:
                                print(k)
                    if choice3==4:
                        print("logged out !!!")
                        break
        else:
            print("Invalid credentials")
    else:
        break
