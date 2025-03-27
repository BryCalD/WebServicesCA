
import unittest, requests




class mainUnitttest(unittest.TestCase):


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

    




if __name__ == '__main__':

    unittest.main()