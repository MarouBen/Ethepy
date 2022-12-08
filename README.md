# ETHEPY
#### Video Demo:  <[https://www.youtube.com/watch?v=okA5s25EZts&t=2s]()>

### Description:
Hello world, Welcome to ETHEPY, Marouane BEN ABBOU's CS50P final project.
In quick terms, Ethepy is a app fully in Python that allows the user to get predictions about specific cryptocurencies for a specified duration.
Used library:
* Pandas
* yfinance
* prophet
* tweepy
* plotly
* fpdf
* matplotlib
and other dependecies and common libraries

Many people try to buy cryptocurrency, but most are always mistrustful, including myself, thinking that the market could go down by a lot in just one day and lose your money easily. Seeing how prophet by meta prediction was close to accurate made me want to do this project for myself before anyone else.
Getting Ethepy to be completely functional wasn't an easy task. I needed two main things: a way to make legitimate predictions and how to put that information into some kind of graph. When I discovered prophet made my meta and plotly, which made my project idea fesable.

That was the fisrt part of my project ,i realised then that prophet make prediction based solely on the graph but in reality that not the only thing that affect the crypto market but also the sentiment of people on social media. This is where i got the idea to make the second part of the project get data from twitter about how people feel regarding a certain cryptocurrency.

Finnaly come the last part of my project is to put all the information into a pdf which got me to find Fpdf a realy usefull library that allow you to create pdfs and style them.


### How the program works:

To get this program to work, I used a couple of libraries. Each of those helped achieve a certain task :

* yfinance: Yahoo finance API used to obtain open prices and dates for a specific cryptocurrency selected by the user.
* Pandas: allowed me to organize data from yfinance in clean tables.
* Prophet: The main library that allowed for the prediction of future Crypto prices.
* Plotly: Plotly was the glue that held all the forcasting data together, allowing me to create and style a plot with data from YFinance and Prophet.
* matplotlib : has the same purpos as Plotly but i used this one for the twitter data scraping part since it's more efficient
* tweepy : this is the twitter API that allowed me to scrap 2000 tweet from twitter for my sentiment analisys
* fpdf : finnaly fpdf allowed me to create a pdf that contain all the previous information into a compact format

First you will need to type the name(example: Etherium) or the symbol(example: ETH) of the cryptocurrency you want, then the number of months which you want to forecast. After that, you will get to chose if you want to see a preview of the forecast on your browsear. At last, you will get all the analisys in a pdf format in a pdf directory.

### How to Install and Run Ethepy:

1. Wont work on python latest version i used 3.10.7

2. Clone the repesitory : `git clone https://github.com/MarouBen/Project-2-Ethepy.git`

3. You'll need the previous libraries install, use `pip install -r requirments.txt` or any other method

4. Open the file and run `py project.py`

### How to use Ethepy:

Once you have installed all the necessary libraries, run the program, and voila, you have your predictions and your twitter sentiment analisys in a pdf format.


### License
MIT License

Copyright (c) [2022] [Marouane BEN ABBOU]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


