import gradio as gr
from utils import create_invoice

# Inputs
client = gr.inputs.Textbox(default = 'Aligned Vision')
date = gr.inputs.Textbox(label='Date MM-DD-YYYY')
invoice_num = gr.inputs.Textbox()
clockify_excel = gr.inputs.File(label='Excel export of clockify hours')
inputs = [client,date,invoice_num,clockify_excel]

# Outputs
outputs = gr.outputs.File()

# Functions
def process_csv(client,date,invoice_num,excel_file):
    output_fp = create_invoice(excel_file.name,client,date,invoice_num)

    return output_fp

# Objects
iface = gr.Interface(process_csv,inputs=inputs, outputs = outputs)

# Run the interface
iface.launch(inbrowser=True)