# Path through pythonchallenge.com

This is my repository contains steps to solve the all challenges of http://pythonchallenge.com

### Level 1

You should calculate `pow(2, 38)` to get the correct URI address

The next link is http://www.pythonchallenge.com/pc/def/274877906944.html

### Level 2

The second challenge contains Caesar cipher. You can use `task02.py` to decode the cipher.

The next link is http://www.pythonchallenge.com/pc/def/ocr.html

### Level 3

Task gives you two ways how to solve its:

* Using OCR (but itsn't possible because quality of text)

* Using programming to decode source text from the page

You can execute `task03.py` to clean up the garbage and to find the next segment of url.

The next link is http://www.pythonchallenge.com/pc/def/equality.html


### Level 4

The task is pretty simple. It makes us to fresh the mind of regular expressions. Please launch 
`task04.py` to find sequence on the page.

The next link is http://www.pythonchallenge.com/pc/def/linkedlist.php


### Level 5

This task was very interesting for me. You should process pages recursively to find the next link segment.

I used the Requests python library (it's a standard de-facto for hi-level libraries to work with http-client)

My PC had been worked about 10 mintes to execute needed segment =)

The next link is http://www.pythonchallenge.com/pc/def/peak.html


### Level 6

I looked into source code of the page and found strange tag which src attribute is `banner.p`. 
This file contains sequence of rows. I really couldn't recognize what is it and was forced to find
a solution in the Internet.

The solution is quite simple. The file contains the object encoded by standard Pickle. This object 
is a list of the lists of the turples. Each turple contains character and number of repetitions.
In this case it was simple put the pseudocode image out to the console.


![output](https://github.com/alexshin/pythonchallenge/blob/master/assets/channel.png)

As you can guess the next link is http://www.pythonchallenge.com/pc/def/channel.html


### Level 7

There was a quite difficult to guess this quizz. First at all you should guess to rename file
in the url string from `channel.html` to `channel.zip`.

File `channel.zip` contains dozens of files but only readme.txt is with hints.

Then the solution is similar with "Level 5". You walk through files recursively and collect the
comments (yes, zip-archive can have comments for the files).

Result is:
![output](https://github.com/alexshin/pythonchallenge/blob/master/assets/hockey.png)

The next link is http://www.pythonchallenge.com/pc/def/hockey.html