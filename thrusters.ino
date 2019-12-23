#include<Servo.h>

int angle=0;  //starting angle 
int pinServo=9; //servo is attached to this pin
int potentioReading; //variable to save potentiometer Reading
int potPin=A0; //connection pin of  potentiometer
int servoDelay=25;
char x;
int w=0;

Servo my;

void setup()
{
 
  Serial.begin(9600);
  my.attach(pinServo);
  my.writeMicroseconds(1500);
  delay(1000);
}

void loop()
{
  //read serial input
  x=Serial.read();  
  
  if(x=='w' && w<300)
  {
    w=w+50;
  }
  else if (x=='s' && w>(-300))
  { 
    w=w-50;
  }

  potentioReading=analogRead(potPin);
  angle=(180./1023.)*potentioReading;
  my.writeMicroseconds(1500+w);
  
  Serial.println(w);
}
 
 
