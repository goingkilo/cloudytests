package com.mycompany.app;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

public class ChromeTest{
	
	public static void main(String[] args) {
		WebDriver driver = new ChromeDriver(); 

		driver.get("http://127.0.0.1:8080/login.html");

		WebElement element = driver.findElement(By.name("user"));
		element.sendKeys("Cheese!");
		element.submit();


		WebElement githubname = driver.findElement(By.name("login"));
		WebElement githubpasd = driver.findElement(By.name("password"));

		githubname.sendKeys("goingkilo");
		githubpasd.sendKeys("frog7jumper");

		WebElement githubsubmit = driver.findElement(By.name("commit"));
		githubsubmit.submit();



		WebElement rcloudCMD = driver.findElement(By.id("new-md-cell-button"));
		//WebElement rcloudCMD = driver.findElement(By.id("term_demo")); //className("cmd"));
		rcloudCMD.sendKeys("1 + 1");
		rcloudCMD.sendKeys(Keys.RETURN);

		rcloudCMD.click();



		System.out.println("Page title is: " + driver.getTitle());

		(new WebDriverWait(driver, 10)).until(new ExpectedCondition<Boolean>() {
			public Boolean apply(WebDriver d) {
				return d.getTitle().toLowerCase().startsWith("cheese!");
			}
		});

		System.out.println("Page title is: " + driver.getTitle());
		System.out.println("done");

		driver.quit();
	}
}
