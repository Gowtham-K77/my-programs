Skip to main content
Skip to primary sidebar
Skip to footer
Additional menu
Crunchify Header LogoCrunchifyLargest free Technical and Blogging resource site for Beginner. We help clients transform their great ideas into reality!
Guides
 
Java 
Abstract Class & Method
Static Methods & Variables
Java Reflection Tutorial
Java eNum Introduction
What is Java Interface
Top 10 Java Interview Q&A
HTTP GET/POST request
Java8 Tutorials
Java Prod Ready Utilities
 
Spring MVC 
1st Spring MVC Tutorial
1st Spring Boot Tutorial
Apache Tomcat Tutorials
All Spring Boot Tutorials
All Maven Tutorials
Eclipse IDE Tutorials
 
MacOS
 
 Tutorials 
GitHub Tutorials
Ansible Tutorials
IntelliJ IDE Tutorials
JSON Tutorials
JavaScript Tutorials
 
WordPress 
Start Your 1st Blog
15 WP Optimization Tips
Speed up WordPress
SEO Tips & Tricks
Create 1st WP Plugin
WordPress Plugin Hacks
Create Custom Post Type
WordPress Beginner Guide
Google Adsense Tutorials
 
Genesis WP 
Add Grid to HomePage
Modify 404 Page
functions.php Hacks
.htaccess Tricks
style.css Tricks
 
Deals
 
Advertise
 
Contact 
Sitemap
Crunchify    Android Dev Tutorials    How to Create Simple Calculator Android App Using Android Studio
How to Create Simple Calculator Android App Using Android Studio
Last Updated on August 20th, 2017 by   Kuldeep   21 comments



In my previous article I wrote detailed steps on How to create a simple android application. In that particular app I also explained concepts of android button and basic concepts of android.

You can find all my other articles in Android section.

In this article we will create a calculator android app. This is a simple calculator with limited functionality.

Before we go forward it would be nice to go over complete HelloWorld Tutorial. Here is a link again: My first HelloWorld Android App

How to build a simple calculator app – full tutorial
Building a Simple Calculator using Android Studio
Android Development: Creating a Basic Calculator
Create Simple Calculator Android App
How to create a Calculator App for Android
Let’s get started with our calculator android App:
Step-1
Open your Android Studio
Click on Start a New Android Studio Project.
Give your Application Name CrunchifyCalculator  and leave other fields blank as it is, then click NEXT.


Step-2
Select the Minimum SDK API 15: Android 4.0.3(IceCreamSandwich). I selected API 15 (IceCreamSandwich) because it covers almost 94% device and it has almost all the features. If you want to cover 100% device then you can select API 8: Android 2.2(Froyo).


Step-3
Select the Empty Activity and click NEXT.
Leave the activity name MainActivity as it is and leave everything as it is. Click Finish.


Step-4
After clicking Finish, it takes around around ~2 minutes to build Activity and files.
Here is a final project structure for your application.


Step-5
Now we have to add our Java code in our MainActivity.java file.
So open you MainActivity.java file from left side of IDE (app  -> java -> com.crunchify.tutorials.crunchifycalculator -> MainActivity.java)
You can find the explanation of highlighted line below the code.

package com.crunchify.tutorials.crunchifycalculator;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
public class MainActivity extends AppCompatActivity {
    Button button0, button1, button2, button3, button4, button5, button6,
            button7, button8, button9, buttonAdd, buttonSub, buttonDivision,
            buttonMul, button10, buttonC, buttonEqual;
    EditText crunchifyEditText;
    float mValueOne, mValueTwo;
    boolean crunchifyAddition, mSubtract, crunchifyMultiplication, crunchifyDivision;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        button0 = (Button) findViewById(R.id.button0);
        button1 = (Button) findViewById(R.id.button1);
        button2 = (Button) findViewById(R.id.button2);
        button3 = (Button) findViewById(R.id.button3);
        button4 = (Button) findViewById(R.id.button4);
        button5 = (Button) findViewById(R.id.button5);
        button6 = (Button) findViewById(R.id.button6);
        button7 = (Button) findViewById(R.id.button7);
        button8 = (Button) findViewById(R.id.button8);
        button9 = (Button) findViewById(R.id.button9);
        button10 = (Button) findViewById(R.id.button10);
        buttonAdd = (Button) findViewById(R.id.buttonadd);
        buttonSub = (Button) findViewById(R.id.buttonsub);
        buttonMul = (Button) findViewById(R.id.buttonmul);
        buttonDivision = (Button) findViewById(R.id.buttondiv);
        buttonC = (Button) findViewById(R.id.buttonC);
        buttonEqual = (Button) findViewById(R.id.buttoneql);
        crunchifyEditText = (EditText) findViewById(R.id.edt1);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText(crunchifyEditText.getText() + "1");
            }
        });
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText(crunchifyEditText.getText() + "2");
            }
        });
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText(crunchifyEditText.getText() + "3");
            }
        });
        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText(crunchifyEditText.getText() + "4");
            }
        });
        button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText(crunchifyEditText.getText() + "5");
            }
        });
        button6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText(crunchifyEditText.getText() + "6");
            }
        });
        button7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText(crunchifyEditText.getText() + "7");
            }
        });
        button8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText(crunchifyEditText.getText() + "8");
            }
        });
        button9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText(crunchifyEditText.getText() + "9");
            }
        });
        button0.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText(crunchifyEditText.getText() + "0");
            }
        });
        buttonAdd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (crunchifyEditText == null) {
                    crunchifyEditText.setText("");
                } else {
                    mValueOne = Float.parseFloat(crunchifyEditText.getText() + "");
                    crunchifyAddition = true;
                    crunchifyEditText.setText(null);
                }
            }
        });
        buttonSub.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mValueOne = Float.parseFloat(crunchifyEditText.getText() + "");
                mSubtract = true;
                crunchifyEditText.setText(null);
            }
        });
        buttonMul.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mValueOne = Float.parseFloat(crunchifyEditText.getText() + "");
                crunchifyMultiplication = true;
                crunchifyEditText.setText(null);
            }
        });
        buttonDivision.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mValueOne = Float.parseFloat(crunchifyEditText.getText() + "");
                crunchifyDivision = true;
                crunchifyEditText.setText(null);
            }
        });
        buttonEqual.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mValueTwo = Float.parseFloat(crunchifyEditText.getText() + "");
                if (crunchifyAddition == true) {
                    crunchifyEditText.setText(mValueOne + mValueTwo + "");
                    crunchifyAddition = false;
                }
                if (mSubtract == true) {
                    crunchifyEditText.setText(mValueOne - mValueTwo + "");
                    mSubtract = false;
                }
                if (crunchifyMultiplication == true) {
                    crunchifyEditText.setText(mValueOne * mValueTwo + "");
                    crunchifyMultiplication = false;
                }
                if (crunchifyDivision == true) {
                    crunchifyEditText.setText(mValueOne / mValueTwo + "");
                    crunchifyDivision = false;
                }
            }
        });
        buttonC.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText("");
            }
        });
        button10.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunchifyEditText.setText(crunchifyEditText.getText() + ".");
            }
        });
    }
}
Here we have 1 EditText. It defines the type of content.
Let’s understand code little-bit more.

Line 11 – 14: Here we created the reference of Buttons and EditText.
Line 16: Here we created two float variable for as value1 and value2.
Line 21: We override the method onCreate() which is the method of Activity class.
Line 45 – 50: We set onClickListener on Button1. If we click on Button1, EditText will display.
We have implemented the same logic for every button.
Line 115 – 127: Here we have set the click listener on Add button.
Here we put the condition as, if we EditText is Null then we set EditText as empty value. Else we add the two value which are clicked before add button clicked and after add button clicked.
We also set the crunchifyAddition Boolean value to True. This true represent that add button is clicked and this will be used when user click “=” button.
We implement the same logic for other buttons also like buttonSub, ButtonMul, buttonDivision.
Line 156 – 183: Here we set clickListener on “=” button. Here we put condition like if user click Add button the crunchifyAddition value is set True on the click listener of Add button.
According to that, corresponding action will be performed respective to button clicked.
if (crunchifyAddition == true) {
      crunchifyEditText.setText(mValueOne + mValueTwo + "");
      crunchifyAddition = false;
}

if Add button is clicked before the “=” button then Add action will be performed as you can see above.
After the action performed, we set the crunchifyAddition value to false, so that we can perform Add action again.
Below is the layout file, with help to design front end for the calculator:

<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/relative1"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">
    <EditText
        android:id="@+id/edt1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />
    <Button
        android:id="@+id/button1"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignEnd="@+id/button4"
        android:layout_alignRight="@+id/button4"
        android:layout_below="@+id/edt1"
        android:layout_marginTop="94dp"
        android:text="1" />
    <Button
        android:id="@+id/button2"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignTop="@+id/button1"
        android:layout_toLeftOf="@+id/button3"
        android:layout_toStartOf="@+id/button3"
        android:text="2" />
    <Button
        android:id="@+id/button3"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignTop="@+id/button2"
        android:layout_centerHorizontal="true"
        android:text="3" />
    <Button
        android:id="@+id/button4"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@+id/button1"
        android:layout_toLeftOf="@+id/button2"
        android:text="4" />
    <Button
        android:id="@+id/button5"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignBottom="@+id/button4"
        android:layout_alignLeft="@+id/button2"
        android:layout_alignStart="@+id/button2"
        android:text="5" />
    <Button
        android:id="@+id/button6"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/button3"
        android:layout_alignStart="@+id/button3"
        android:layout_below="@+id/button3"
        android:text="6" />
    <Button
        android:id="@+id/button7"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@+id/button4"
        android:layout_toLeftOf="@+id/button2"
        android:text="7" />
    <Button
        android:id="@+id/button8"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/button5"
        android:layout_alignStart="@+id/button5"
        android:layout_below="@+id/button5"
        android:text="8" />
    <Button
        android:id="@+id/button9"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/button6"
        android:layout_alignStart="@+id/button6"
        android:layout_below="@+id/button6"
        android:text="9" />
    <Button
        android:id="@+id/buttonadd"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignEnd="@+id/edt1"
        android:layout_alignRight="@+id/edt1"
        android:layout_alignTop="@+id/button3"
        android:layout_marginLeft="46dp"
        android:layout_marginStart="46dp"
        android:layout_toRightOf="@+id/button3"
        android:text="+" />
    <Button
        android:id="@+id/buttonsub"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignEnd="@+id/buttonadd"
        android:layout_alignLeft="@+id/buttonadd"
        android:layout_alignRight="@+id/buttonadd"
        android:layout_alignStart="@+id/buttonadd"
        android:layout_below="@+id/buttonadd"
        android:text="-" />
    <Button
        android:id="@+id/buttonmul"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/buttonsub"
        android:layout_alignParentEnd="true"
        android:layout_alignParentRight="true"
        android:layout_alignStart="@+id/buttonsub"
        android:layout_below="@+id/buttonsub"
        android:text="*" />
    <Button
        android:id="@+id/button10"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@+id/button7"
        android:layout_toLeftOf="@+id/button2"
        android:text="." />
    <Button
        android:id="@+id/button0"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/button8"
        android:layout_alignStart="@+id/button8"
        android:layout_below="@+id/button8"
        android:text="0" />
    <Button
        android:id="@+id/buttonC"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/button9"
        android:layout_alignStart="@+id/button9"
        android:layout_below="@+id/button9"
        android:text="C" />
    <Button
        android:id="@+id/buttondiv"
        style="?android:attr/buttonStyleSmall"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignEnd="@+id/buttonmul"
        android:layout_alignLeft="@+id/buttonmul"
        android:layout_alignRight="@+id/buttonmul"
        android:layout_alignStart="@+id/buttonmul"
        android:layout_below="@+id/buttonmul"
        android:text="/" />
    <Button
        android:id="@+id/buttoneql"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignEnd="@+id/buttondiv"
        android:layout_alignLeft="@+id/button10"
        android:layout_alignRight="@+id/buttondiv"
        android:layout_alignStart="@+id/button10"
        android:layout_below="@+id/button0"
        android:layout_marginTop="37dp"
        android:text="=" />
</RelativeLayout>


Now, all things should works fine and we are ready to run our calculator android app. To run our app I used my mobile, you can use emulator or your device.

Running our Calculator Android App
Click on Android device manager. After selecting your custom device in Android device manager window, click START.
Click on Run button.
Choose Your device or emulator and click OK.
Now you can see calculator android app running as this screenshot.
Congratulations!! If you have followed all steps and reach this point means you have followed all the steps correctly and your Calculator android app is up and running fine.

Join the Discussion
If you liked this article, then please share it on social media. Still have any questions about an article, leave us a comment.

Share: 
Other Popular Articles...
How to Build Your First Hello World Android App with Android Studio?
How to fix Gradle sync failed, NDK not configured Error in Android Studio?
Some of my Favorite JavaScript Tips and Tricks Tutorials
How to Enable Google Analytics Event Tracking – Web Tracking (ga.js)
Java Collections – hashCode() and equals() – How to Override equals() and hashcode() Method in Java?
Understanding Java Annotations – Java @annotations Tutorial
Android Dev Tutorials

GIVE ME A TRY...
10 Best Mac Apps WordPress Security SEO Basics Optimize WP Plugins we use

About Kuldeep
I'm Kuldeep Ghodasara from Gujarat, India. I'm a Technical Writer & Developer at Crunchify. I started working with wordpress back in 2012 while Googling How to make blog without Coding. I've taken deep dive in Blogging with WordPress and SEO. Crunchify is the medium on which I'll be sharing my knowledge which I've learned from various experiences.

Subscribe To Newsletter…
Stay up to date & never miss an update! Signup for news, latest articles and special offers!! Join 16+ million monthly readers...👋

E-Mail Address
 
You can unsubscribe at any time.

Primary Sidebar
Over 16 million readers
Get fresh content from Crunchify
      

TOP TECH SAVVY GUIDES
 NEW My Top 3 Mac Productivity Apps & 10 IPhone Settings You Need To Turn Off Now!
 Simplest Spring MVC Hello World & Spring Boot Tutorial
 NEW How To Sync Custom Folders With ICloud Drive? & Build RESTful Service Using Jersey JAX-RS
 Top 10 Java Interview Q&A & Sort A HashMap By Key & Value
 Install Ansible On Linux & Race Condition In Java Multi-Threading
 Implement A LinkedList Class From Scratch & Memcached Java Client
BASIC JAVA TECH
Singleton Pattern Java Caching LinkedList Iterator Java Abstract Java Static Intro Java Interface Github OAuth Sorting Algorithm Semaphore & Mutex Java Reflection Java NIO (Non-blocking) SOAP vs REST .zip file by Maven
Kinsta
Modern, Secure & Fast Managed WordPress Hosting. Check it out.

USEFUL WORDPRESS GUIDE
 NEW Start 1st WordPress Blog & 15 Essential Optimization Tips
 Leverage .Htaccess To Speed Up WordPress & Stop Loading Unnecessary Files On Site
 Top 5 Basic SEO Tips & Importance Of Keyword Research
 Better Cleanup WordPress Header Section & Fix CPanel CPU Issue
 Google Form As Ultimate WordPress Contact Form & Load WordPress Fonts Locally (Speed Tips)
 16 Proven Ways To Get Quality Backlinks & Better Upgrade To PHP 7.1
 NEW Secure WordPress Login Area & Cloak Affiliate Links Without WordPress Plugin
WORDPRESS TUNING TIPS
Install WP Locally WordPress CPT Disable Cron Jobs Modify 404 Page Scroll To Top GenesisWP Hooks Add Bitly Shortlink Adsense without Plugin Plugins we Use Top Backup Plugins Domain Authority Tips Interlinking Tips Setup Forum
Footer
Top Tech Categories…
Java & J2EE
Eclipse IDE Tutorials
Android Dev Tutorials
Apache Tomcat Tutorials
Design & Dev
Interview Questions Answers
JavaScript
Spring MVC & Spring Boot Tutorials
Maven
Top Blogging Categories…
SEO 101 Tutorials
WordPress Optimization & Tutorials
Genesis WP
Blogging
Making Money Online
functions.php Hacks
WebHosting
style.css Hacks
WooCommerce

START A BLOG
 
ADVERTISE
 
SITEMAP
 
SETUP
 
FORUM
 
PRO
 
LOGIN / AFFILIATE
 
CART
       
Crunchify Logo    2022 Crunchify, LLC. Hosted at Kinsta  •  Built on Genesis Themes.

About  •  DCMA Disclaimer and Privacy Policy.

Noticed a bug? Let us know.
