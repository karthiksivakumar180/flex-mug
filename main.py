from fastapi import FastAPI,Query
import json
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def function_filter_data(postcode):
  # Read data from JSON file
  with open('postcode.json', 'r') as file:
      data = json.load(file)

  # Convert data to Pandas DataFrame
  df = pd.json_normalize(data)
  # postcode_to_search = postcode  # Update this with the postcode you want to search for
  postcode_to_search=postcode.replace(" ", "")

  # Filter DataFrame based on the postcode
  # filtered_df = df[df['postcode'] == postcode_to_search]
  filtered_df = df[df['postcode'].str.replace(' ', '') == postcode_to_search]

#   # Perform search operation
#   search_criteria = {
#       'postcode': postcode,  # Example search criteria (name)
#   }

#   filtered_df = df
#   for key, value in search_criteria.items():
#       if value is not None:
#           filtered_df = filtered_df[filtered_df[key] == value]
  #
  filtered_data_list = filtered_df.to_dict(orient='records')
  return filtered_data_list

        
@app.get("/request/Address/recco")
def get_postcode_data(postcode: str = Query(..., min_length=6, max_length=7,strip_whitespace=True)):
    static_data=function_filter_data(postcode)
  
    return static_data
