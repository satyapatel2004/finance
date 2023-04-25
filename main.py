import yfinance as yf 
import inquirer
from sys import exit
import tempfile 
import csv 
import rich
import pprint 
import os 



def get_stock():
    global tickr
    
    try:
        tickrIn = input("enter your Ticker: ")
        tickr = yf.Ticker(tickrIn)
        info(tickr.info)
        analysis() 
         
    except ImportError: 
        print("Incorrect Ticker!") 
        get_stock()

stockInfoFile = tempfile.NamedTemporaryFile() 

def info(tickrInfo):
    with open(stockInfoFile.name, 'w') as f: 
        for key in tickrInfo.keys():
            stockInfoFile.write("%s,%s\n"%(key,tickrInfo[key]))

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
        stock_analysis()

def stock_analysis():

    open(stockInfoFile.name, 'r') as f

    questions = [
        inquirer.List(
            "stockAnalysis", 
            message="How do you want to analyze",
            choices=["P/B", "P/E", "PEG", "Dividend Yield", "Back"],
        ),
    ]
    answer = inquirer.prompt(questions)

    if answer['stockAnalysis'] == "P/B":
        for row in f:
            if row[0] == "priceToBook":
                print("the price to book ratio is: " + row[1])

    
    if answer['stockAnalysis'] == "P/E":
        for row in f:
            if row[0] == "sharesOutstanding":
                outstandingShares = row[1]

            if row[0] == "grossProfits":
                profit = row[1]

            if row[0] == "previousClose":
                marketPrice = row[1]

        earningsPerShare = float(outstandingShares)/float(profit) 
        print("The Price to Earnings Ratio is: " + str(float(marketPrice)/earningsPerShare))

    if answer['stockAnalysis'] == "PEG":
        for row in f:
            if row[0] == "pegRatio":
                print("The PEG Ratio is " + row[1])

    if answer['stockAnalysis'] == "Dividend Yield":
        for row in f:
            if row[0] == "dividendYield":
                print("the Divident Yield is " + row[1])
                
        else: print("Dividend Yield Unavailable\n")

    if answer['stockAnalysis'] == "Back":
        analysis()
       
def main():
    get_stock()

#Test change to see if git does anything...! 
#Changes made during Cleanup

main() 

 




#This is the main file 
# something hash changed