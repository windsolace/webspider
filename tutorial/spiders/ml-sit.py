import scrapy


class MLSitSpider(scrapy.Spider):
    name = "mlsit"
    start_urls = [
        'https://manulife-ap-sit-64.adobecqms.net/content/insurance-qa/my/en/individual.html',
    ]

    def parse(self, response):


        # find all site urls through navigation
        navigationMenuItems = response.css(".cmp-navigation__item-link")
        for navigationMenuItem in navigationMenuItems:
            yield {
                'navigationItem': navigationMenuItem.css("span::text").get()
            }

        productteasers = response.css('div.cmp-productteaser')
        # for productteaser in productteasers:
            # yield {
            #     'text': productteaser.css('.cmp-productteaser__title-link p::text').get(),
            # }
            

        iconteasers = response.css('div.cmp-icon-teaser')
        # for iconteaser in iconteasers:
            # yield {
            #     'text': iconteaser.css('.cmp-content-teaser__title-link::text').get(),
            # }


        #yield dict(productteasers=len(productteasers), iconteasers=len(iconteasers))
        #next_page = response.css('li.next a::attr(href)').get()
        #if next_page is not None:
            #yield response.follow(next_page, callback=self.parse)