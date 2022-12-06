from fpdf import FPDF
import os

# save FPDF() class into a variable pdf
pdf = FPDF()
 
def Creat_pdf(name):
    print("Writing pdf...")
    # Add a page
    pdf.add_page()
    
    # Font of the name of the project
    pdf.set_font("Arial", size = 25)
    # Cell that containe title
    pdf.cell(w = 200, h = 10, ln=1, txt = "Ethepy", align="C")

    pdf.set_font("Arial", size = 10)
    pdf.cell(w = 200, h = 9, ln=2, txt = "Project made by Marouane BEN ABBOU", align="C")

    # Cell contaning the title
    pdf.set_font("Arial", size = 18)
    pdf.cell(w = 200, h = 15, ln=2, txt = f" {name.capitalize()} analysis", align="L")

    # A little summary of the project idea
    pdf.set_font("Arial", size = 12)
    pdf.multi_cell(w = 200, h = 5, txt = f"This project purpose is to help you decide if you may want to invest on any cryptocurrency when having little to no prior experience. This page will provide you with two useful information to make your decision, first a prediction of the price plot made by Meta prophet deep learning, second an analysis of {name} news by scraping more than 2000 latest tweets.", align="L")

    # The first part the forecasting
    pdf.set_font("Arial", size = 18)
    pdf.cell(w = 200, h = 15, ln=2, txt = " Forecast", align="L")
    pdf.image(name=f"Plots/{name}.jpeg", w=200, h=100)

    # Second part the data-scraping
    pdf.set_font("Arial", size = 18)
    pdf.cell(w = 200, h = 10, ln=2, txt = " Sentiment", align="L")
    pdf.image(name=f"Plots/sentiment of {name}.jpeg", w=120, h=80)
    pdf.set_font("Arial", size = 12)
    pdf.cell(w = 200, h = 6, txt="#NoFinacialAdvice use the information you get here to do your own deduction")

    # Creat the pdf
    if not os.path.exists("pdf"):
        os.mkdir("pdf")
    pdf.output(f"pdf/{name.capitalize()}.pdf")
    print(f"{name.capitalize()}.pdf created")
