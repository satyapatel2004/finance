import yfinance as yf 
import inquirer
from sys import exit
import pandas 



#gets the stock ticker from the user: 
def get_stock():
    global tickrInfo 
    global tickr  
    
    try:
        tickrIn = input("enter your Ticker: ")
        tickr = yf.Ticker(tickrIn)

        #creates a dictionary with the ticker's information. 
        tickrInfo = tickr.get_info() 
        analysis() 

         
    except ValueError: 
        print("Incorrect Ticker!") 
        get_stock()

#types of analysis the user can complete (in progress)
def analysis():
    questions = [
        inquirer.List(
            "analysis", 
            message="What type of analysis do you want to do?",
            choices=["Stock Analysis", "Other", "Other2", "Other3"],
        ),
    ]
    answer = inquirer.prompt(questions)

    if answer['analysis'] == "Stock Analysis":
        print(tickrInfo['sharesOutstanding'])
        stock_analysis()

def stock_analysis():

    questions = [
        inquirer.List(
            "stockAnalysis", 
            message="How do you want to analyze",
            choices=["P/B", "P/E", "PEG", "Dividend Yield", "Back"],
        ),
    ]
    answer = inquirer.prompt(questions)

    if answer['stockAnalysis'] == "P/B":
        for key in tickrInfo:
            if key == 'priceToBook':
                print("the price to book ratio is " + tickrInfo[key])
    
    if answer['stockAnalysis'] == "P/E":
        for key in tickrInfo:
            if key == 'sharesOutstanding':
                outstandingShares = tickrInfo[key]

            if key == 'grossProfits':
                profit = tickrInfo[key]

            if key == 'previousClose':
                marketPrice = tickrInfo[key]

        earningsPerShare = float(outstandingShares)/float(profit) 
        print("The Price to Earnings Ratio is: " + str(float(marketPrice)/earningsPerShare))

    if answer['stockAnalysis'] == "PEG":
        for key in tickrInfo:
            if key == 'pegRatio':
                print("The PEG Ratio is " + tickrInfo[key])

    if answer['stockAnalysis'] == "Dividend Yield":
        for key in tickrInfo:
            if key == 'dividendYield':
                print("the Divident Yield is " + tickrInfo[key])
                
        else: print("Dividend Yield Unavailable\n")

    if answer['stockAnalysis'] == "Back":
        analysis()
       
def main():
    get_stock()

#Test change to see if git does anything...! 
#Changes made during Cleanup

main() 
