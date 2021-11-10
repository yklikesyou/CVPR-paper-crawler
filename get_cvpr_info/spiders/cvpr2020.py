import scrapy
from get_cvpr_info.items import GetCvprInfoItem


class Cvpr2020Spider(scrapy.Spider):
    name = 'cvpr2020'
    start_urls = ['https://openaccess.thecvf.com/CVPR2020?day=2020-06-1']

    def start_requests(self):
        for url in self.start_urls:
            for page_num in range(3):
                yield scrapy.http.Request(url + str(page_num+6))

    def parse(self, response):
        paper_titles = response.css(
            '#content > dl > dt.ptitle > a::text').getall()
        MAX_NUM = len(paper_titles)+1

        for i in range(1, MAX_NUM):
            cvpr2020_papers = GetCvprInfoItem()
            # print(i, '번째 논문입니다.')
            author_list = []
            paper_authors = response.css(
                f'#content > dl > dd:nth-child({i*3}) > form > a::text').getall()
            for paper_author in paper_authors:
                author_list.append(paper_author)
            authors = ','.join(author_list)
            title = paper_titles[i-1]
            cvpr2020_papers['paper_title'] = title
            cvpr2020_papers['paper_authors'] = authors

            yield cvpr2020_papers
