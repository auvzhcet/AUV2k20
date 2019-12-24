 #include<Servo.h>

int pinServo = 9; //servo is attached to this pin
int servoDelay = 25;
char x;
int w = 0;

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
  //read input
  x = Serial.read();
  if(x == 'w' && w < 300){
    w=w+50;
  }
  else if (x == 's' && w > (-300)){ 
    w=w-50;
  }
     
  my.writeMicroseconds(1500 +w);
  Serial.println(w);
}
 
 
