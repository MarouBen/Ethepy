# ETHEPY
#### Video Demo:  <[URL HERE]()>

### Description:
Hello world, Welcome to ETHEPY, Marouane BEN ABBOU's CS50P final project.
In quick terms, Ethepy is a back-end program fully in Python that allows the user to get predictions about specific cryptocurencies for a specified duration.
Used library:
* Pandas
* yfinance
* datetime
* prophet
* plotly
* warnings
* sys

Many people try to buy cryptocurrency, but most are always mistrustful, including myself, thinking that the market could go down by a lot in just one day. Seeing how prophet by meta prediction was close to accurate made me want to do this project for myself before anyone else.
Getting Ethepy to be completely functional wasn't an easy task. I needed two main things: a way to make legitimate predictions and how to put that information into some kind of graph. When I discovered Fbprophet made my meta and plotly, which made my project idea fesable.


### How the webpage works:

To get this program to work, I used a couple of libraries. Each of those helped achieve a certain task :
* yfinance: Yahoo finance API used to obtain open prices and dates for a specific cryptocurrency selected by the user.
* Pandas: allowed me to organize data from yfinance in clean tables.
* Prophet: The main library that allowed for the prediction of future Crypto prices.
* Plotly: Finally, plotly was the glue that held everything together, allowing me to create and style a plot with data from YFinance and Prophet.
First you will need to type the name(example: Etherium) or the symbol(example: ETH) of the cryptocurrency you want, then the number of months which you want to forecast. After that, you will get a preview of the graph. At last, you will be able to save it or not.

### How to Install and Run Ethepy:

1. Wont work on python latest version i used 3.10.7

2. Clone the repesitory : `git clone https://github.com/MarouBen/Project-2-Ethepy.git`

3. You'll need the previous libraries install, use `pip install -r requirments.txt` or any other method

4. Open the file and run `python project.py`

### How to use Ethepy:

Once you have installed all the necessary libraries (if you want to install the librairies manually check notes.md ), run the program, and voila, you have your predictions (change the width and height if you have a smaller screen in the styling function).


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


