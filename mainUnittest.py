
import unittest
import requests
from fpdf import FPDF
from datetime import datetime
import json
from fastapi.applications import FastAPI

class TestReportPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Test Report', 0, 1, 'C')
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')



class mainUnittest(unittest.TestCase):


    def test_getSingleProduct(self):

        url = 'http://127.0.0.1:8000/getSingleProduct/67d2c16bbef850c9c28a2433' # this is the endpoint to call

       

        # Making a GET request to the /sample endpoint

        response = requests.get(url)


        # Assert the response status code is 200

        self.assertEqual(response.status_code, 200)

    def test_getAll(self):

        url = 'http://127.0.0.1:8000/getAll' # this is the endpoint to call

       

        # Making a GET request to the /sample endpoint

        response = requests.get(url)


        # Assert the response status code is 200

        self.assertEqual(response.status_code, 200)

    def test_addNew(self):

        url = 'http://127.0.0.1:8000/addNew' # this is the endpoint to call

       

        # Making a GET request to the /sample endpoint

        response = requests.get(url)


        # Assert the response status code is 200

        self.assertEqual(response.status_code, 200)

    def test_deleteOne(self):

        url = 'http://127.0.0.1:8000/deleteOne' # this is the endpoint to call

       

        # Making a GET request to the /sample endpoint

        response = requests.get(url)


        # Assert the response status code is 200

        self.assertEqual(response.status_code, 200)

    def test_startsWith(self):

        url = 'http://127.0.0.1:8000/startsWith/b' # this is the endpoint to call

       

        # Making a GET request to the /sample endpoint

        response = requests.get(url)


        # Assert the response status code is 200

        self.assertEqual(response.status_code, 200)

    def test_paginate(self):

        url = 'http://127.0.0.1:8000/paginate/AUTO002/AUTO011' # this is the endpoint to call

       

        # Making a GET request to the /sample endpoint

        response = requests.get(url)


        # Assert the response status code is 200

        self.assertEqual(response.status_code, 200)

    def test_convert(self):

        url = 'http://127.0.0.1:8000/convert/67d2c16bbef850c9c28a2433' # this is the endpoint to call

       

        # Making a GET request to the /sample endpoint

        response = requests.get(url)


        # Assert the response status code is 200

        self.assertEqual(response.status_code, 200)

def generate_simple_report(test_results, filename="test_report.pdf"):
    pdf = TestReportPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    
    pdf.cell(0, 10, 'Test Results Summary:', 0, 1)
    pdf.ln(5)
    
    for test, result in test_results.items():
        if result == "PASS":
            pdf.set_text_color(0, 128, 0)  # Green for pass
        else:
            pdf.set_text_color(255, 0, 0)  # Red for fail
            
        pdf.cell(0, 10, f'{test}: {result}', 0, 1)
        pdf.set_text_color(0, 0, 0)  # Reset to black
    
    pdf.output(filename)

    


def generate_api_documentation(app: FastAPI, output_path: str = "README.txt"):
    """Generate API documentation README file"""
    try:
        # Get OpenAPI schema from running server
        response = requests.get("http://127.0.0.1:8000/openapi.json")
        openapi_schema = response.json()
        
        content = [
            "API ENDPOINTS DOCUMENTATION",
            "=" * 30,
            f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
            "ENDPOINTS:\n"
        ]
        
        for path, methods in openapi_schema["paths"].items():
            for method, details in methods.items():
                content.append(f"• {method.upper()} {path}")
                
                if "summary" in details:
                    content.append(f"  Summary: {details['summary']}")
                
                if "parameters" in details:
                    content.append("  Parameters:")
                    for param in details["parameters"]:
                        param_info = param.get("schema", {})
                        content.append(
                            f"  - {param['name']} ({param['in']}): "
                            f"{param_info.get('type', '')} "
                            f"{'(required)' if param.get('required', False) else ''}"
                        )
                
                if "requestBody" in details:
                    content.append("  Request Body:")
                    for media_type, schema in details["requestBody"]["content"].items():
                        if "schema" in schema and "$ref" in schema["schema"]:
                            ref = schema["schema"]["$ref"].split("/")[-1]
                            content.append(f"  - {media_type}: {ref}")
                
                content.append("")
        
        content.extend([
            "\nAPI DOCUMENTATION:",
            "=" * 30,
            "For interactive API documentation, visit:",
            "1. FastAPI Docs: http://127.0.0.1:8000/docs",
            "2. ReDoc: http://127.0.0.1:8000/redoc\n",
            "For the OpenAPI schema: http://127.0.0.1:8000/openapi.json"
        ])
        
        with open(output_path, "w") as f:
            f.write("\n".join(content))
        
        print(f"API documentation generated at {output_path}")
    except Exception as e:
        print(f"Failed to generate API documentation: {str(e)}")

if __name__ == '__main__':
    # Generate API documentation first
    # Note: This assumes your FastAPI server is already running
    generate_api_documentation(None)  # We don't need the app instance since we're querying the live server
    
    # Then run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(mainUnittest)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Prepare results for PDF
    test_results = {}
    test_names = [test._testMethodName for test in loader.loadTestsFromTestCase(mainUnittest)]
    
    for test_name in test_names:
        if test_name in [fail[0]._testMethodName for fail in result.failures]:
            test_results[test_name] = "FAIL"
        elif test_name in [error[0]._testMethodName for error in result.errors]:
            test_results[test_name] = "ERROR"
        else:
            test_results[test_name] = "PASS"
    
    # Generate PDF report
    generate_simple_report(test_results)
    print("PDF report generated as 'test_report.pdf'")