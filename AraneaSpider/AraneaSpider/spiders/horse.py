import scrapy

class HorseSpider(scrapy.Spider):

    name = 'ike'

    def start_requests(self):
        #pass in list of URLs you'd like to process
        urls = [
            'https://treehouse-projects.github.io/horse-land/index.html',
            'https://treehouse-projects.github.io/horse-land/mustang.html'
        ]

        return [scrapy.Request(url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        page = url.split('/')[-1]
        filename = 'horses-%s' % page
        print('URL is: {}'.format(url))
        with open(filename, 'wb') as file:
            file.write(response.body)
        print('Saved file %s' % filename)