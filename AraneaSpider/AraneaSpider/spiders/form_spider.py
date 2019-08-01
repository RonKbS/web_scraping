from scrapy.http import FormRequest
from scrapy.spiders import Spider


class FormSpider(Spider):

    name = 'horseForm'

    start_urls = ['https://treehouse-projects.github.io/horse-land/form.html']

    def parse(self, response):
        # use chrome-tools to see what fields are in the form for url above
        formData ={
            'firstname': 'Ken',
            'lastname': 'Alger',
            'jobtitle': 'Teacher'
        }
        # submit button used by default to send in the data
        return FormRequest.from_response(
            response,
            formnumber=0,
            formdata=formData,
            callback=self.after_post
        )
        # FormRequest can also be used to handle login-forms

    def after_post(self, response):
        # printout that form was processed and response itself
        print('\n\n***************\nForm Processed.\n')
        print(response)
        print('\n\n***************\nForm Processed.\n')
