
	
const char MAIN_page[] PROGMEM = R"=====(
<HTML>
<!DOCTYPE html>
<html>
<head>
<style>
h1 {
		font-size: 50px;
}
h2 {
		font-size: 30px;
}
.button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
  cursor: pointer;
}

.button1 {
  background-color: white; 
  color: black; 
  border: 2px solid #4CAF50;
}

.button1:hover {
  background-color: #4CAF50;
  color: white;
}

.button2 {
  background-color: white; 
color: black; 
  border: 2px solid #008CBA;
}

.button2:hover {
  background-color: #008CBA;
  color: white;
}

.button3 {
  background-color: white; 
color: black; 
  border: 2px solid #f44336;
}

.button3:hover {
  background-color: #f44336;
  color: white;
}
</style>
</head>
<body>

<h1>Three Lights</h1>
<h2> <p>Choose the color you would like to see.</p> </h2>
<a style="text-decoration:none;" href="http://192.168.4.1?green=1">
<button class="button1">Green</button>
</a>
<a style="text-decoration:none;" href="http://192.168.4.1?blue=1">
<button class="button2">Blue</button>
</a>
<a style="text-decoration:none;" href="http://192.168.4.1?red=1">
<button class="button3">Red</button>
</a>
<p></p>
<a style="text-decoration:none;" href="http://192.168.4.1?green=0">
<button class="button1">Green</button>
</a>
<a style="text-decoration:none;" href="http://192.168.4.1?blue=0">
<button class="button2">Blue</button>
</a>
<a style="text-decoration:none;" href="http://192.168.4.1?red=0">
<button class="button3">Red</button>
</a>

</body>
</html>
)=====";
