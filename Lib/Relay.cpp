#include "Relay.h"


void Relay(int x)
{
  if(x == 1) digitalWrite(RELAY, HIGH);
  else digitalWrite(RELAY, LOW);
}
