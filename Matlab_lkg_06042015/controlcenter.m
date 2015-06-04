%The code will take in a string, splice it and convert it to three numbers
%that represent the accelerations in the x,y, and z direction. The distance
%of those speed at time are calculated and returned to the calling program.

%declare variable
t=.1;
prevx = 0;
prevy = 0;
prevz = 0;
targetx = 12;
targety = 12;
targetz = 5;
prevheading = 0;

%receive input string from file
accel = input('Enter location: ', 's'); %test case
%accel2 = ('-32.44,6.60,241.12');
%Loop the instructional set until target is reached
while((prevx ~= targetx) && (prevy ~= targety) && (prevz ~= targetz))

    %split the string into three parts
    [ax,ay,az]=stringsplice(accel)


    %convert to number
    speedx=str2double(ax)
    speedy=str2double(ay)
    speedz=str2double(az)

    %calculate the distance
    [distx,disty,distz]=dist(speedx,speedy,speedz,t)

    

    %find the distance between previous and current, and distance from current
    distmag = dmag(distx,prevx,disty,prevy,distz,prevz)
    targetmag = dmag(distx,targetx,disty,targety,distz,targetz)
    targetangle = atand((targety-disty)/(targetx-distx))

    
    
    %determine next move towards target(left, right, up, down, forward, or
    %back)

    if ((distx-targetx)<0)
        %send turn left command
        display('Turn left')
        if((distmag-targetmag)<0)
            %send command to go forward
            display('Go forward')
            if ((distz-targetz)<0)
                %send command to dive down
                display('Dive Down')
            else
                %send command to rise up
                display('Rise up')
            end
        else
            % send command to go back
            display('Go back')
        end
    else
        %send turn right command
        display('Turn right')
    end
    
    %store the distances as previous values
    prevx=distx;
    prevy=disty;
    prevz=distz;
    accel = input('Enter location: ', 's'); %get test case location
end
