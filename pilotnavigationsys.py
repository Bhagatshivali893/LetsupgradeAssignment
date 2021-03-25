#here user/pilot will enter the altitude of the plane in feet
alt=int(input("Enter the altitude of the plane in feets:"));

# for landing the Plane we need range of altitude in between 3000ft to 6000ft 
if(alt==3000):
    print("Hey Pilot you can land your plane, Its safe landing");
elif(alt>3000 and alt<6000):
    print("Hey Pilot you can try for landing the plane");
elif(alt>6000):
    print("Hey Pilot you cannot land your plane. So please Go Around");
else:
    print("Sorry the range of altitude doesn't match");

