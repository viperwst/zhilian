import scrapy
import re, json
import time
import requests


class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['zhaopin.com']

    def start_requests(self):
        cookies = 'x-zp-client-id=04d980ae-e023-4a26-82f5-3d48d5554689; locationInfo_search={%22code%22:%22763%22%2C%22name%22:%22%E5%B9%BF%E5%B7%9E%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; sts_deviceid=177be2dca0b4d1-0bed25ccccea1c-73e356b-2073600-177be2dca0c5d2; _uab_collina=161380340815196410752901; adfbid2=0; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1613803399,1614334803; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fsou.zhaopin.com%2F; ZPCITIESCLICKED=|763; LastCity%5Fid=763; LastCity=%E5%B9%BF%E5%B7%9E; selectCity_search=763; urlfrom=121113803; urlfrom2=121113803; adfbid=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22709010713%22%2C%22first_id%22%3A%22177be2da6b02b5-043dfc4786c3c1-73e356b-2073600-177be2da6b1636%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%2C%22%24latest_utm_campaign%22%3A%22ty%22%2C%22%24latest_utm_content%22%3A%22qg%22%2C%22%24latest_utm_term%22%3A%226921574%22%7D%2C%22%24device_id%22%3A%22177be2da6b02b5-043dfc4786c3c1-73e356b-2073600-177be2da6b1636%22%7D; Hm_lvt_363368edd8b243d3ad4afde198719c4a=1614335526,1615197071,1615198908; ssxmod_itna2=QqmxcQKmq7u4nDlSx+obOWqaED0i0DCuDDtrQ3D6ERBZD05pvq03QeWyX0N3cD8h4pbceobItGqKWdeQ4xVrxERAumPQ3x40leni65olKC0HQpxSLKaca8HakTysPbvh8l0FKlrC/70X93oi68uD/3fNyD3QGU4EctQ6oP40dXmq/+SLxAGuGnho/84bQ==Rb=qTpno6PecoNWDftkLdBiLd434=mREIshfEhoBNKuwDrDq0zO=6N5n6ueKiTAWgXKKqL1w+ViL0hjzjl9U6uNjFhiIYvDPbxhlc4HSvc79DmjMf46T5lwb4WTfTTemtcRtnoKDno+YNUfK3liQ7D00WVxdUMdP4s5Did8OHTdf4Oxd=Zk7DldLDDwrPqBxOGKNY+se+0euObt=ih6lDI2GblDDjKDeuq4D=; Hm_lpvt_363368edd8b243d3ad4afde198719c4a=1615446490; select_city_name=%E5%B9%BF%E5%B7%9E; select_province_code=548; select_province_name=%E5%B9%BF%E4%B8%9C; select_city_code=702; at=a518818029d34e78b1bf295541c7024b; rt=5154a2163023433ab0b38e319ef2e8d0; ssxmod_itna=YqAxyDuQitDti=6x0d4YIEP7wZZi5KFqNdOODlc=xA5D8D6DQeGTT0e=D0Q=ATfLhxWNnhYu4sf4fTaRIdiQjoNQDU4i8DCTrNzD4+KGwD0eG+DD4DWAx03DoxGAysrdKiODQ40kDmq07yO5DWxDFAOhtPh9G7hFC7cy1VxD1YevPFGKD9x0CDlcqsfq8DD5A+fqDEG+7M65DvxDk4/IFVxGdZiD3PQra8Qx4Z8hxVB0t=QhKKAreQTGoeQ0tS7iq=iDxvWcX4D=; ZL_REPORT_GLOBAL={%22//www%22:{%22seid%22:%222cf035ac81304046bc4b3db0e1717284%22%2C%22actionid%22:%22dfdd082e-3176-48a6-875c-445ecea398a1-cityPage%22}%2C%22jobs%22:{%22recommandActionidShare%22:%22a8992689-423b-4295-8222-925f5c0988c9-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; sts_sid=178256053555e0-0ea29f6efa43b6-5771133-2073600-178256053567ad; acw_tc=2760825f16155347715114238ebe6e2f6e3290762d91f049c75c25b7e432a9; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1615534903; sts_evtseq=2'
                  # 'x-zp-client-id=04d980ae-e023-4a26-82f5-3d48d5554689; locationInfo_search={%22code%22:%22763%22%2C%22name%22:%22%E5%B9%BF%E5%B7%9E%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; sts_deviceid=177be2dca0b4d1-0bed25ccccea1c-73e356b-2073600-177be2dca0c5d2; _uab_collina=161380340815196410752901; adfbid2=0; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1613803399,1614334803; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fsou.zhaopin.com%2F; ZPCITIESCLICKED=|763; LastCity%5Fid=763; LastCity=%E5%B9%BF%E5%B7%9E; selectCity_search=763; ssxmod_itna2=QqUx2D97D=DtqDIP0LpOI7G8Dg7GqDRnGQQhDnKSiwhKDsKCiYDL7uS/4akWyeSPGFl2Tv0xc4EeR0pK5G407=xjKD2GYD==; urlfrom=121113803; urlfrom2=121113803; adfbid=0; sts_sid=1781127ad9f21-0a06ef6cd8fdcb-53e356a-2073600-1781127ada057b; at=2cf035ac81304046bc4b3db0e1717284; rt=f2877516299f41aab57a94e48ae1da7e; ZP_OLD_FLAG=false; ssxmod_itna=QqmxyQqWqGuD0QDzxAxewn4j2fjGCQjK/bWRRDBLT4iNDnD8x7YDvm+E7zmYzYWlGhhWxvDRy3hNFZoOo+Qghx0aDbqGkPS2qiicDCeDIDWeDiDGb=DFxYoDecULO0D3qGrDzqGCDKLt1DiPD7OIPNemOx8pOXOczcc5Dn=0kF7hOD75Dux0H3ngqIxDCz4SqDmb3GpHzDCKDjx7k7c5DUnqPEiDPbQpKbQ0UF70Ns00tQYhKKArqQT25OixoQAxxHwRW/3D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22709010713%22%2C%22first_id%22%3A%22177be2da6b02b5-043dfc4786c3c1-73e356b-2073600-177be2da6b1636%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%2C%22%24latest_utm_campaign%22%3A%22ty%22%2C%22%24latest_utm_content%22%3A%22qg%22%2C%22%24latest_utm_term%22%3A%226921574%22%7D%2C%22%24device_id%22%3A%22177be2da6b02b5-043dfc4786c3c1-73e356b-2073600-177be2da6b1636%22%7D; acw_tc=2760826816151989036166026eb31c1fc72980e9bc574ae5366ab9e766fe8e; ZL_REPORT_GLOBAL={%22//www%22:{%22seid%22:%222cf035ac81304046bc4b3db0e1717284%22%2C%22actionid%22:%226e3caf3d-fa00-4d25-91ad-88838e0ad059-cityPage%22}%2C%22jobs%22:{%22recommandActionidShare%22:%2283ea60a7-4bda-482e-9670-bf51184dd3e7-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; Hm_lvt_363368edd8b243d3ad4afde198719c4a=1614335526,1615197071,1615198908; Hm_lpvt_363368edd8b243d3ad4afde198719c4a=1615198908; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1615198920; sts_evtseq=19'
        self.cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        # self.headers = {
            # 'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", }
        yield scrapy.Request(
            'https://www.zhaopin.com/',
            callback=self.parse,
            cookies=self.cookies,
            # headers=self.headers
        )

    def parse(self, response):
        # 自动添加第一次请求的cookie
        start_city = 480
        end_city = 950
        print("开始爬取")
        # for i in range(start_city, end_city):
            # print("城市ID：", i)
            # for a in range(1,30):
            #     for b in range(1,30):
            #         for c in range(1, 30):
            #             jt = '&jt={0}000000000000%2C{0}000{1}00000000%2C{0}000{1}00{2}0000&p=1'.format(a,b,c)
            #             url_city = "https://sou.zhaopin.com/?jl={0}{1}".format(i,jt)
        url_city = 'https://sou.zhaopin.com/?jl=763&jt=9000000000000%2C9000300000000%2C9000300110000'
        yield scrapy.Request(
            url=url_city,
            callback=self.parse_page,
            cookies=self.cookies,
            # headers=self.headers
        )

    def parse_page(self, response):
        datas = response.xpath("//div[@class='joblist-box__item clearfix']")
        # actionid = re.findall("actionid: '(.*?)'",response.text)[0]
        for data in datas:
            url = data.xpath("./a/@href").extract_first()
            print(url)
            # url = url + actionid
            # print(url)
            request = scrapy.FormRequest(url,callback=self.parse_zp,cookies=self.cookies)
            # request.meta["publish_time"] = response.xpath(".//time/@title").extract()[0].replace("年","-").replace("月","-").replace("日","")
            yield request
        # page = 2
        # next_page = response.xpath(
        #     "//div[@class='pagination clearfix']//div[@class='pagination__pages']//button[@class='btn soupager__btn soupager__btn--disable']/text()").extract_first()
        # if next_page == "下一页":
        #     # print("正在爬取1：")
        #     yield scrapy.Request(
        #         url=response.request.url,
        #         callback=self.parse_page,
        #         cookies=self.cookies,
        #     )
        # elif response.xpath(
        #         "//div[@class='sou-main']//div[@class='sou-main__center clearfix']//div[@class='positionList-hook']//div[@class='page-empty__tips']//span/text()").extract_first() != None:
        #     print("未搜索到:", response.request.url)
        #     return
        # else:
        #     # print("正在爬取2：")
        #     for i in range(2, 40, 1):
        #         url_page = response.request.url + "&p={0}".format(page)
        #         page += 1
        #         yield scrapy.Request(
        #             url=url_page,
        #             callback=self.parse_page,
        #             cookies=self.cookies,
        #         )



    def parse_zp(self, response):
        company = {}
        industries = []
        name = response.xpath("//a[@class='company__title']/text()").extract_first()
        print(name)



        # item = {}
        # list_body = response.xpath("//div[@class='joblist-box__item clearfix']")
        # print("URL：", response.request.url)
        # for body in list_body:
        #     url = response.xpath("./a/@href").extract()
        #     print(url)
            # # 工作名字
            # item['title'] = body.xpath(
            #     ".//div[@class='iteminfo__line iteminfo__line1']//div[@class='iteminfo__line1__jobname']//span[@class='iteminfo__line1__jobname__name']/text()").extract_first()
            # list_li = body.xpath(".//div[@class='iteminfo__line iteminfo__line2']//ul//li")
            # # 学历
            # item['Education'] = list_li[2].xpath("./text()").extract_first()
            # # 工作地点
            # item['job_location'] = list_li[0].xpath("./text()").extract_first()
            # # 工作时间
            # item['job_time'] = list_li[1].xpath("./text()").extract_first()
            # # 工资
            # money = body.xpath(
            #     ".//div[@class='iteminfo__line iteminfo__line2']//div[@class='iteminfo__line2__jobdesc']//p/text()").extract_first()
            # item['money'] = money.split()
            # # 工作需要
            # info = body.xpath(
            #     ".//div[@class='iteminfo__line iteminfo__line3']//div[@class='iteminfo__line3__welfare']//div")
            # info_list = []
            # for i in info:
            #     info_list.append(i.xpath("./text()").extract_first())
            # item['job_info'] = " ".join(info_list)
            # # #公司名
            # item['Company_name'] = body.xpath(
            #     "//div[@class='iteminfo__line iteminfo__line1']//div[@class='iteminfo__line1__compname']//span[@class='iteminfo__line1__compname__name']/text()").extract_first()
            # company = body.xpath(
            #     ".//div[@class='iteminfo__line iteminfo__line2']//div[@class='iteminfo__line2__compdesc']//span")
            # # 公司人数
            # item['company_number'] = company[1].xpath("./text()").extract()
            # # 公司类型
            # item['company_type'] = company[0].xpath("./text()").extract()
            # yield item
