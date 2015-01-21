#include "constants.h"
/* these functions will cause the dolphin to go right,
left, up, down, forward or back given the angle of the turn
or distance to travel to the next point. Finally,
the settings for the thrusters are defined and 
returned to the main program for relay to the agent*/

*int goRight(int deltaAngle, char speed){
	int turnTime = TURN_RATE*deltaAngle;
	int maneuver[] = {CW_MED_SPEED, IDLE, IDLE, IDLE, turnTime};
		
	switch (speed){
		case "f":
			maneuver[0]= CW_FULL_SPEED;
			break;
		case "m":
			maneuver[0]= CW_MED_SPEED;
			break;
		case "l":
			maneuver[0]= CW_LOW_SPEED;
			break;
		default:
			break;
	}	
	return maneuver;
}

*int goLeft(int deltaAngle, char speed){
	int turnTime;
	turnTime=TURN_RATE*deltaAngle;
	
	int maneuver[] = {IDLE, CW_MED_SPEED, IDLE, IDLE, turnTime};
		
	switch (speed){
		case "f":
			maneuver[1]= CW_FULL_SPEED;
			break;
		case "m":
			maneuver[1]= CW_MED_SPEED;
			break;
		case "l":
			maneuver[1]= CW_LOW_SPEED;
			break;
		default:
			break;
	}	
	return maneuver;
}

*int goUp(int deltaDist, char speed){
	int moveTime = MS_DIST_RATE*deltaDist;	
	int maneuver[] = {IDLE, IDLE, CW_MED_SPEED, CC_MED_SPEED, moveTime};
	
	switch (speed){
		case "f":
			maneuver[2]= CW_FULL_SPEED;
			maneuver[3]= CW_FULL_SPEED;
			maneuver[5]=FS_DIST_RATE*deltaDist;
			break;
		case "m":
			maneuver[2]= CW_MED_SPEED;
			maneuver[3]= CC_FULL_SPEED;
			maneuver[5]=MS_DIST_RATE*deltaDist;
			break;
		case "l":
			maneuver[2]= CW_LOW_SPEED;
			maneuver[3]= CC_FULL_SPEED;
			maneuver[5]=LS_DIST_RATE*deltaDist;
			break;
		default:
			break;
	}	
	return maneuver;
}

*int goDown(int deltaDist, char speed){
	int moveTime;
	int maneuver[] = {IDLE, CW_MED_SPEED, IDLE, IDLE, moveTime};
	
	turnTime=MS_DIST_RATE*deltaAngle;
	switch (speed){
		case "f":
			maneuver[0]= CW_FULL_SPEED;
		case "m":
			maneuver[0]= CW_MED_SPEED;
		case "l":
			maneuver[0]= CW_LOW_SPEED;
		default:
			maneuver[0]= CW_MED_SPEED;
	}	
	return maneuver;
}

*int goForward(int deltaAngle, char speed){
	int turnTime;
	int maneuver[] = {IDLE, CW_MED_SPEED, IDLE, IDLE, turnTime};
	
	turnTime=MS_DIST_RATE*deltaAngle;
	switch (speed){
		case "f":
			maneuver[0]= CW_FULL_SPEED;
		case "m":
			maneuver[0]= CW_MED_SPEED;
		case "l":
			maneuver[0]= CW_LOW_SPEED;
		default:
			maneuver[0]= CW_MED_SPEED;
	}	
	return maneuver;
}

*int goBack(int deltaAngle, char speed){
	int turnTime;
	int maneuver[] = {IDLE, CW_MED_SPEED, IDLE, IDLE, turnTime};
	
	turnTime=MS_DIST_RATE*deltaAngle;
	switch (speed){
		case "f":
			maneuver[0]= CW_FULL_SPEED;
		case "m":
			maneuver[0]= CW_MED_SPEED;
		case "l":
			maneuver[0]= CW_LOW_SPEED;
		default:
			maneuver[0]= CW_MED_SPEED;
	}	
	return maneuver;
}
