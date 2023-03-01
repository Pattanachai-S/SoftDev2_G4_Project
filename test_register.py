from django.test import Client, TestCase

class ContactFormTest(TestCase):
    
    def test_contact_form_submission(self):
        # Create a test client
        client = Client()

        # Make a POST request to the contact form URL with valid form data
        response = client.post('/contact/', {'name': 'John Doe', 'email': 'johndoe@example.com', 'message': 'Hello world!'})

        # Check that the response status code is 302 Found (indicating a redirect after successful form submission)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect to the thank-you page
        response = client.get(response.url)

        # Check that the thank-you page contains the expected text
        self.assertContains(response, 'Thank you for your message!')
