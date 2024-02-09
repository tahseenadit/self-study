import vertexai
import os

from vertexai.language_models import TextGenerationModel
from fastapi import (
    Depends,
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()
# Set up CORS middleware options
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows all origins to access your API. For security reasons, in a production environment, you should specify the actual origins you want to allow.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class InputData(BaseModel):
    input: str

class ResponseModel(BaseModel):
    response: str


# Mount the static files, but at a path other than root
app.mount("/static", StaticFiles(directory="../public"), name="static")

@app.get("/")
def read_root():
    # Return the index.html file
    return FileResponse('../public/index.html')


@app.post('/generate-text')
def generate_text(data: InputData):
    # Initialize Vertex AI
    vertexai.init(project="data-enablement-dp-poc", location="europe-west1")

    # Define the model parameters
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40
    }

    # Load the model
    model = TextGenerationModel.from_pretrained("text-bison")

    # Get input data from the request
    input_data = data.input

    input_str = f"""
    
    Generate the yaml file from the given input for data quality scan.

    input: - sampling percent is 50, row filter is \"country_rk in (\'SE\', \'NL\') and corporate_brand_rk = 0\"
    - customer_rk, customer-rk-null, RK must not be null, COMPLETENESS, 1.0, \" \"
    - business_partner_id, bpid-unique, BP ID must be unique, UNIQUENESS, 1.0,  \" \"
    - age, age-correct, Age must be up to date with birth_year column, based on the current date, CONSISTENCY, 0.99, row_condition_expectation, age = DATE_DIFF(CURRENT_DATE(\'Europe/Stockholm\'), birth_date, YEAR)
    output: 
    sampling_percent: 50
    row_filter: country_rk in (\'SE\', \'NL\') and corporate_brand_rk = 0

    rules:
      - column: customer_rk
        name: customer-rk-null
        description: RK must not be null
        dimension: COMPLETENESS
        threshold: 1.0
        non_null_expectation: \"\"

      - column: business_partner_id
        name: bpid-unique
        description: BP ID must be unique
        dimension: UNIQUENESS
        threshold: 1.0
        uniqueness_expectation: \"\"

      - column: age
        name: age-correct
        description: Age must be up to date with birth_year column, based on the current date
        dimension: CONSISTENCY
        threshold: 0.99
        row_condition_expectation:
        sql_expression: >
            age = DATE_DIFF(CURRENT_DATE(\'Europe/Stockholm\'), birth_date, YEAR)


    input: - sampling percent is 90, row filter is \"country_rk_2 in (\'SE\', \'DE\') and corporate_brand = 10\"
    - customer, customer-null, must not be null, COMPLETENESS, 0.9, \" \"
    - business, bpid-u, must be unique, UNIQUENESS, 0.9,  \" \"
    - age_col, age, Age must be up to date with birth_year column, based on the current date, CONSISTENCY, 1.0, row_condition_expectation, age_col = DATE_DIFF(CURRENT_DATE(\'Europe/Stockholm\'), birth_date, YEAR)
    output: 
    sampling_percent: 90
    row_filter: country_rk_2 in (\'SE\', \'DE\') and corporate_brand = 10

    rules:
      - column: customer
        name: customer-null
        description: must not be null
        dimension: COMPLETENESS
        threshold: 0.9
        non_null_expectation: \"\"

      - column: business
        name: bpid-u
        description: must be unique
        dimension: UNIQUENESS
        threshold: 0.9
        uniqueness_expectation: \"\"

      - column: age_col
        name: age
        description: Age must be up to date with birth_year column, based on the current date
        dimension: CONSISTENCY
        threshold: 1.0
        row_condition_expectation:
        sql_expression: >
            age = DATE_DIFF(CURRENT_DATE(\'Europe/Stockholm\'), birth_date, YEAR)

    input: {input_data}
    output:
    """

    # Generate response from the model
    response = model.predict(input_str, **parameters)

    # Return the response
    return ResponseModel(response=response.text)

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))