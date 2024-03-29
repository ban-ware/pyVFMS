/*
   Copyright (c) 2015, Majenko Technologies
   All rights reserved.

   Redistribution and use in source and binary forms, with or without modification,
   are permitted provided that the following conditions are met:

 * * Redistributions of source code must retain the above copyright notice, this
     list of conditions and the following disclaimer.

 * * Redistributions in binary form must reproduce the above copyright notice, this
     list of conditions and the following disclaimer in the documentation and/or
     other materials provided with the distribution.

 * * Neither the name of Majenko Technologies nor the names of its
     contributors may be used to endorse or promote products derived from
     this software without specific prior written permission.

   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
   DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
   ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
   ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/* Create a WiFi access point and provide a web server on it. */

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <FS.h>
#include "index.h"

#ifndef APSSID
#define APSSID "gzliESPap"
#define APPSK  "gzliESPap"
#endif

/* Set these to your desired credentials. */
const char *ssid = APSSID;
const char *password = APPSK;

ESP8266WebServer server(80);

class user {
 public:
   String logged_in_user = "";
   void handleRoot();
   void setup();
};
const int red = 15;
const int green = 12;
const int blue = 13;

/* Just a little test message.  Go to http://192.168.4.1 in a web browser
   connected to this access point to see it.
*/
void handleRoot() {
  user user;
  File file1 = SPIFFS.open("/logged_in_user.txt", "r");
  if (!file1){
  Serial.println("failed to read stored user");
  return;
  }
  while (file1.available())
    user.logged_in_user+=(char)file1.read();
  Serial.println(user.logged_in_user);
    String s = MAIN_page;
    server.send(200, "text/html", s);
  for (uint8_t i = 0; i < server.args(); i++) {
    if ( server.argName(i).equals("red") && server.arg(i).equals("1") ){
      if(user.logged_in_user == "chris" || user.logged_in_user == "dustin" || 
          user.logged_in_user == "riley"){
      digitalWrite(red, 1);
    }}
    if ( server.argName(i).equals("red") && server.arg(i).equals("0") ){
      if(user.logged_in_user == "chris" || user.logged_in_user == "dustin" || 
          user.logged_in_user == "riley"){
      digitalWrite(red, 0);
    }}
    if ( server.argName(i).equals("green") && server.arg(i).equals("1") ){
      if(user.logged_in_user == "chris"|| user.logged_in_user == "riley"){
      digitalWrite(green, 1);
    }}
    if ( server.argName(i).equals("green") && server.arg(i).equals("0") ){
      if(user.logged_in_user == "chris" || user.logged_in_user == "riley"){
      digitalWrite(green, 0);
    }}
    if ( server.argName(i).equals("blue") && server.arg(i).equals("1") ){
      if(user.logged_in_user == "chris"){
      digitalWrite(blue, 1);
    }}
    if ( server.argName(i).equals("blue") && server.arg(i).equals("0") ){
      if(user.logged_in_user == "chris"){
      digitalWrite(blue, 0);
    }}
  }
}

void handleNotFound() {
  digitalWrite(red, 1);
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";

  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }

  server.send(404, "text/plain", message);
  digitalWrite(red, 0);
}

void setup() {
  user user;
  delay(1000);
  pinMode(red, OUTPUT);
  digitalWrite(red, 0);
  pinMode(green, OUTPUT);
  digitalWrite(green, 0);
  pinMode(blue, OUTPUT);
  digitalWrite(blue, 0);
  
  Serial.begin(115200);
  Serial.println();
  Serial.print("Configuring access point...");
  /* You can remove the password parameter if you want the AP to be open. */
  WiFi.softAP(ssid, password);
    if(!SPIFFS.begin()){
      Serial.println("An Error has occurred while mounting SPIFFS");
      return;
  }

  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  server.on("/", handleRoot);
  server.on("/inline", []() {
    server.send(200, "text/plain", "this works as well");
  });
  server.onNotFound(handleNotFound);

  delay(3000);
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}
