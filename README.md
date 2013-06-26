Demo:
If all the components work, then you'll see the code   
- launch a browser   
- login into github for you (java:asks credentials python:needs them in .py file)  
- check if 'Run Notebook' link exists  
- click on the 'New File' link  
- enter a generated file name  
- run two token R commands on the editor box  


dependencies 
needs chromedriver file from  https://code.google.com/p/selenium/wiki/ChromeDriver

*python*
needs selenium : pip install selenium  
(you can get pip via apt-get  )

 needs your github id and password
 also expects chromedriver in ./driver/chromedriver
python chrometest.py

*java*
command to execute:
java -jar rcloud_automation.jar <rcloud launch URL> <path to chromedriver>


 rcloud launch URL  : usually http://127.0.0.1:8080/login.html  
 
 path to chromedriver  : full path to chromedirver file 

example :

java -jar rcloud_automation.jar http://127.0.0.1:8080/login.html ./chromedriver

