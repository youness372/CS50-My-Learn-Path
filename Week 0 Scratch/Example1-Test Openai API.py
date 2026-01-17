from openai import OpenAI     
client =  OpenAI()     

respons =  client.responses.create  (     
    input =  " Whatis te cs50"    
    model  =  "gbt-5"
)
print  (respons.output_text) 
