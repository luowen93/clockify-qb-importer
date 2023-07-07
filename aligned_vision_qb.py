import pandas as pd
import argparse
from datetime import datetime
import calendar
from dateutil.relativedelta import relativedelta
from typing import Optional, List

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", default=None, type=str)
    parser.add_argument("invoice_date", default="", type=str)
    parser.add_argument('invoice_number',type = int)
    parser.add_argument("--customer", default="Aligned Vision Inc", type=str)
    args = parser.parse_args()
    return vars(args) # Return as a dict

def end_of_next_month(date_obj:datetime)-> str:
    """
    Input: Date object
    Output: Date object that is the end of the next month
    """
    new_date = date_obj + relativedelta(days=28)  
    month = new_date.month
    year = new_date.year
    start, end = calendar.monthrange(year, month)
    new_date_str = f"{month}-{end}-{year}"
    new_date_str = datetime.strptime(new_date_str, "%m-%d-%Y")
    return new_date_str.strftime("%m-%d-%Y")

def process_dataframe(invoice_csv:str):
    """
    Processes the dataframe for intermediate calculations
    """
    df = pd.read_csv(invoice_csv)
    df["item_description"] = df["Project"] + "-" + df["Client"]  # Add new description for project-client
    vals = df.groupby("item_description").sum()
    vals.to_csv('check.csv')
    vals["Rate"] = vals["Amount (USD)"] / vals["Time (decimal)"] # Calculate the rate as measures
    vals = vals[['Time (decimal)','Amount (USD)','Rate']]
    return vals

def xlsx2dict(fp:str):
    df = pd.read_excel(fp)
    df = df[df['Project'].isna() == False] # Get only the summary values
    df['Rate'] = df['Amount (USD)']/df['Time (decimal)']
    df= df[['Project','Time (decimal)', 'Rate', 'Amount (USD)']]
    df = df[:-1]
    vals = df.values

    # List of dicts
    d = [{'project':v[0], 'hours': v[1], 'rate': v[2], 'total':v[3]}for v in vals]

    return d

def read_qb_columns() -> List:
    df_columns = pd.read_csv("qb_columns.csv", header=None)
    headings = list(df_columns.values[0])
    return headings

def create_invoice(input_xlsx:str,customer:str,invoice_date:str,invoice_number = int) -> None:
    # Convert to standard date format
    invoice_date = datetime.strptime(invoice_date,"%m-%d-%Y")
    due_date = end_of_next_month(invoice_date) # Get the next month
    invoice_date = invoice_date.strftime('%m-%d-%Y')
    headings = read_qb_columns() # Read the standard qb headings\
    vals = xlsx2dict(input_xlsx) # Read into list of dictionaries

    # Standard terms for invoice
    terms = "Net 30"
    hours = "Hours"

    l = list()
    for v in vals:
        project = v['project']
        hours = v['hours']
        rate = v['rate']
        total = v['total']

        l.append(
            [
                invoice_number,
                customer,
                invoice_date,
                due_date,
                terms,
                None,
                None,
                hours,
                project,
                hours,
                rate,
                total,
                0,
                "USD",
            ]
        )

    df_final = pd.DataFrame(l, columns=headings)
    df_final.to_csv(f"Invoice_{invoice_number}_qb.csv",index=False)
    
if __name__=="__main__":
    args = parse_args()
    create_invoice(**args)