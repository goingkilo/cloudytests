Demo:
If all the components work, then you'll see the code launch a browser, ask you for your github credentials, login for you
and run one token command on the R ide

dependencies 
needs chromedriver file from  https://code.google.com/p/selenium/wiki/ChromeDriver


command to execute:
java -jar rcloud_automation.jar <rcloud launch URL> <path to chromedriver>


 rcloud launch URL  : usually http://127.0.0.1:8080/login.html  
 
 path to chromedriver  : full path to chromedirver file 

example :

java -jar rcloud_automation.jar http://127.0.0.1:8080/login.html ./chromedriver


