# -*- coding: utf-8 -*-
import os
import re
import scrapy


class GetcourseSpider(scrapy.Spider):
    name = 'getCourse'
    allowed_domains = ['*']
    start_urls = ['http://buaa.edu.cn/']
    jsession_id = "C03C0DD512177E57D2538463815A8243"

    def start_requests(self):
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Cookie": "JSESSIONID=" + self.jsession_id,
            "Host": "10.200.21.61:7001",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        cookie = {
            "JSESSIONID": self.jsession_id
        }
        print("Start Request")

        meta = []
        meta.append({"file_name": "数学与自然科学", "year": "2015-20161"})
        meta.append({"file_name": "数学与自然科学", "year": "2015-20162"})
        meta.append({"file_name": "数学与自然科学", "year": "2015-20163"})
        meta.append({"file_name": "数学与自然科学", "year": "2016-20171"})
        meta.append({"file_name": "数学与自然科学", "year": "2016-20172"})
        meta.append({"file_name": "数学与自然科学", "year": "2016-20173"})
        meta.append({"file_name": "数学与自然科学", "year": "2017-20181"})
        meta.append({"file_name": "数学与自然科学", "year": "2017-20182"})
        meta.append({"file_name": "数学与自然科学", "year": "2017-20183"})
        meta.append({"file_name": "数学与自然科学", "year": "2018-20191"})
        meta.append({"file_name": "数学与自然科学", "year": "2018-20192"})
        meta.append({"file_name": "数学与自然科学", "year": "2018-20193"})
        for i in range(0, len(meta)):
            yield scrapy.Request(url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxk?pageXkmkdm=JCL",
                                 cookies=cookie,
                                 headers=header,
                                 meta=meta[i],
                                 callback=self.chooseShuXue,
                                 dont_filter=True)  # 基础课

        meta = []
        meta.append({"file_name": "工程基础课", "year": "2015-20161"})
        meta.append({"file_name": "工程基础课", "year": "2015-20162"})
        meta.append({"file_name": "工程基础课", "year": "2015-20163"})
        meta.append({"file_name": "工程基础课", "year": "2016-20171"})
        meta.append({"file_name": "工程基础课", "year": "2016-20172"})
        meta.append({"file_name": "工程基础课", "year": "2016-20173"})
        meta.append({"file_name": "工程基础课", "year": "2017-20181"})
        meta.append({"file_name": "工程基础课", "year": "2017-20182"})
        meta.append({"file_name": "工程基础课", "year": "2017-20183"})
        meta.append({"file_name": "工程基础课", "year": "2018-20191"})
        meta.append({"file_name": "工程基础课", "year": "2018-20192"})
        meta.append({"file_name": "工程基础课", "year": "2018-20193"})
        for i in range(0, len(meta)):
            yield scrapy.Request(url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxk?pageXkmkdm=JCL",
                                 cookies=cookie,
                                 headers=header,
                                 meta=meta[i],
                                 callback=self.chooseGongChengJiChu,
                                 dont_filter=True)  # 基础课

        meta = []
        meta.append({"file_name": "语言类", "year": "2015-20161"})
        meta.append({"file_name": "语言类", "year": "2015-20162"})
        meta.append({"file_name": "语言类", "year": "2015-20163"})
        meta.append({"file_name": "语言类", "year": "2016-20171"})
        meta.append({"file_name": "语言类", "year": "2016-20172"})
        meta.append({"file_name": "语言类", "year": "2016-20173"})
        meta.append({"file_name": "语言类", "year": "2017-20181"})
        meta.append({"file_name": "语言类", "year": "2017-20182"})
        meta.append({"file_name": "语言类", "year": "2017-20183"})
        meta.append({"file_name": "语言类", "year": "2018-20191"})
        meta.append({"file_name": "语言类", "year": "2018-20192"})
        meta.append({"file_name": "语言类", "year": "2018-20193"})
        for i in range(0, len(meta)):
            yield scrapy.Request(url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxk?pageXkmkdm=JCL",
                                 cookies=cookie,
                                 headers=header,
                                 meta=meta[i],
                                 callback=self.chooseYuYan,
                                 dont_filter=True)  # 基础课

        meta = []
        meta.append({"file_name": "外语类", "year": "2015-20161"})
        meta.append({"file_name": "外语类", "year": "2015-20162"})
        meta.append({"file_name": "外语类", "year": "2015-20163"})
        meta.append({"file_name": "外语类", "year": "2016-20171"})
        meta.append({"file_name": "外语类", "year": "2016-20172"})
        meta.append({"file_name": "外语类", "year": "2016-20173"})
        meta.append({"file_name": "外语类", "year": "2017-20181"})
        meta.append({"file_name": "外语类", "year": "2017-20182"})
        meta.append({"file_name": "外语类", "year": "2017-20183"})
        meta.append({"file_name": "外语类", "year": "2018-20191"})
        meta.append({"file_name": "外语类", "year": "2018-20192"})
        meta.append({"file_name": "外语类", "year": "2018-20193"})
        for i in range(0, len(meta)):
            yield scrapy.Request(url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxk?pageXkmkdm=JCL",
                                 cookies=cookie,
                                 headers=header,
                                 meta=meta[i],
                                 callback=self.chooseWaiYu,
                                 dont_filter=True)  # 基础课

        meta = []
        meta.append({"file_name": "英语分级", "year": "2015-20161"})
        meta.append({"file_name": "英语分级", "year": "2015-20162"})
        meta.append({"file_name": "英语分级", "year": "2015-20163"})
        meta.append({"file_name": "英语分级", "year": "2016-20171"})
        meta.append({"file_name": "英语分级", "year": "2016-20172"})
        meta.append({"file_name": "英语分级", "year": "2016-20173"})
        meta.append({"file_name": "英语分级", "year": "2017-20181"})
        meta.append({"file_name": "英语分级", "year": "2017-20182"})
        meta.append({"file_name": "英语分级", "year": "2017-20183"})
        meta.append({"file_name": "英语分级", "year": "2018-20191"})
        meta.append({"file_name": "英语分级", "year": "2018-20192"})
        meta.append({"file_name": "英语分级", "year": "2018-20193"})
        for i in range(0, len(meta)):
            yield scrapy.Request(url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxk?pageXkmkdm=JCL",
                                 cookies=cookie,
                                 headers=header,
                                 meta=meta[i],
                                 callback=self.chooseYingYuFenji,
                                 dont_filter=True)  # 基础课

        meta = []
        meta.append({"file_name": "核心通识", "year": "2015-20161"})
        meta.append({"file_name": "核心通识", "year": "2015-20162"})
        meta.append({"file_name": "核心通识", "year": "2015-20163"})
        meta.append({"file_name": "核心通识", "year": "2016-20171"})
        meta.append({"file_name": "核心通识", "year": "2016-20172"})
        meta.append({"file_name": "核心通识", "year": "2016-20173"})
        meta.append({"file_name": "核心通识", "year": "2017-20181"})
        meta.append({"file_name": "核心通识", "year": "2017-20182"})
        meta.append({"file_name": "核心通识", "year": "2017-20183"})
        meta.append({"file_name": "核心通识", "year": "2018-20191"})
        meta.append({"file_name": "核心通识", "year": "2018-20192"})
        meta.append({"file_name": "核心通识", "year": "2018-20193"})
        for i in range(0, len(meta)):
            yield scrapy.Request(url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxk?pageXkmkdm=TSL",
                                  cookies=cookie,
                                  headers=header,
                                  meta=meta[i],
                                  callback=self.chooseHeXinTongShi,
                                  dont_filter=True) # 通识课

        meta = []
        meta.append({"file_name": "一般通识", "year": "2015-20161"})
        meta.append({"file_name": "一般通识", "year": "2015-20162"})
        meta.append({"file_name": "一般通识", "year": "2015-20163"})
        meta.append({"file_name": "一般通识", "year": "2016-20171"})
        meta.append({"file_name": "一般通识", "year": "2016-20172"})
        meta.append({"file_name": "一般通识", "year": "2016-20173"})
        meta.append({"file_name": "一般通识", "year": "2017-20181"})
        meta.append({"file_name": "一般通识", "year": "2017-20182"})
        meta.append({"file_name": "一般通识", "year": "2017-20183"})
        meta.append({"file_name": "一般通识", "year": "2018-20191"})
        meta.append({"file_name": "一般通识", "year": "2018-20192"})
        meta.append({"file_name": "一般通识", "year": "2018-20193"})
        for i in range(0, len(meta)):
            yield scrapy.Request(url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxk?pageXkmkdm=TSL",
                                  cookies=cookie,
                                  headers=header,
                                  meta=meta[i],
                                  callback=self.chooseYiBanTongShi,
                                  dont_filter=True)  # 通识课

        meta = []
        meta.append({"file_name": "思政军理", "year": "2015-20161"})
        meta.append({"file_name": "思政军理", "year": "2015-20162"})
        meta.append({"file_name": "思政军理", "year": "2015-20163"})
        meta.append({"file_name": "思政军理", "year": "2016-20171"})
        meta.append({"file_name": "思政军理", "year": "2016-20172"})
        meta.append({"file_name": "思政军理", "year": "2016-20173"})
        meta.append({"file_name": "思政军理", "year": "2017-20181"})
        meta.append({"file_name": "思政军理", "year": "2017-20182"})
        meta.append({"file_name": "思政军理", "year": "2017-20183"})
        meta.append({"file_name": "思政军理", "year": "2018-20191"})
        meta.append({"file_name": "思政军理", "year": "2018-20192"})
        meta.append({"file_name": "思政军理", "year": "2018-20193"})
        for i in range(0, len(meta)):
            yield scrapy.Request(url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxk?pageXkmkdm=TSL",
                                  cookies=cookie,
                                  headers=header,
                                  meta=meta[i],
                                  callback=self.chooseSiZhengJunLi,
                                  dont_filter=True)  # 通识课


        meta = []
        meta.append({"file_name": "核心专业", "year": "2015-20161"})
        meta.append({"file_name": "核心专业", "year": "2015-20162"})
        meta.append({"file_name": "核心专业", "year": "2015-20163"})
        meta.append({"file_name": "核心专业", "year": "2016-20171"})
        meta.append({"file_name": "核心专业", "year": "2016-20172"})
        meta.append({"file_name": "核心专业", "year": "2016-20173"})
        meta.append({"file_name": "核心专业", "year": "2017-20181"})
        meta.append({"file_name": "核心专业", "year": "2017-20182"})
        meta.append({"file_name": "核心专业", "year": "2017-20183"})
        meta.append({"file_name": "核心专业", "year": "2018-20191"})
        meta.append({"file_name": "核心专业", "year": "2018-20192"})
        meta.append({"file_name": "核心专业", "year": "2018-20193"})
        for i in range(0, len(meta)):
            yield scrapy.Request(url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxk?pageXkmkdm=ZYL",
                                 cookies=cookie,
                                 headers=header,
                                 meta=meta[i],
                                 callback=self.chooseHeXinZhuanYe,
                                 dont_filter=True)  # 专业课

        meta = []
        meta.append({"file_name": "一般专业", "year": "2015-20161"})
        meta.append({"file_name": "一般专业", "year": "2015-20162"})
        meta.append({"file_name": "一般专业", "year": "2015-20163"})
        meta.append({"file_name": "一般专业", "year": "2016-20171"})
        meta.append({"file_name": "一般专业", "year": "2016-20172"})
        meta.append({"file_name": "一般专业", "year": "2016-20173"})
        meta.append({"file_name": "一般专业", "year": "2017-20181"})
        meta.append({"file_name": "一般专业", "year": "2017-20182"})
        meta.append({"file_name": "一般专业", "year": "2017-20183"})
        meta.append({"file_name": "一般专业", "year": "2018-20191"})
        meta.append({"file_name": "一般专业", "year": "2018-20192"})
        meta.append({"file_name": "一般专业", "year": "2018-20193"})
        for i in range(0, len(meta)):
            yield scrapy.Request(url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxk?pageXkmkdm=ZYL",
                                 cookies=cookie,
                                 headers=header,
                                 meta=meta[i],
                                 callback=self.chooseYiBanZhuanYe,
                                 dont_filter=True)  # 专业课


    def getToken(self, response):
        match_obj = re.match('.*id="token" name="token" value="(.*?)"', response.text, re.DOTALL)
        token_value = ""
        if match_obj:
            token_value = match_obj.group(1)
        else:
            print("Can not find token value when choose " + response.meta['file_name'])
            os._exit(0)
        return token_value


    def chooseShuXue(self, response):
        token_value = self.getToken(response)
        data = []
        data.append({
            "pageSize": "1000",
            "rwh": "",
            "zy": "",
            "qz": "",
            "token": token_value,
            "pageXklb": "xslbxk",
            "pageXkmkdm": "JCL",
            "pageKclb": "A",
            "pageXnxq": response.meta['year'],
            "pageKkxiaoqu": "",
            "pageKkyx": "",
            "pageKcmc": ""
        })  # 数学与自然科学
        cookie = {
            "JSESSIONID": self.jsession_id
        }
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "JSESSIONID=" + self.jsession_id,
            "Host": "10.200.21.61:7001",
            "Origin": "http://10.200.21.61:7001",
            "Referer": "http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        for i in range(0, len(data)):
            yield scrapy.FormRequest(
                url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxkList",  # 其他课程
                formdata=data[i],
                headers=header,
                cookies=cookie,
                meta=response.meta,
                callback=self.parse,
                dont_filter=True
            )


    def chooseGongChengJiChu(self, response):
        token_value = self.getToken(response)
        data = []
        data.append({
            "pageSize": "1000",
            "rwh": "",
            "zy": "",
            "qz": "",
            "token": token_value,
            "pageXklb": "xslbxk",
            "pageXkmkdm": "JCL",
            "pageKclb": "B",
            "pageXnxq": response.meta['year'],
            "pageKkxiaoqu": "",
            "pageKkyx": "",
            "pageKcmc": ""
        })  # 工程基础
        cookie = {
            "JSESSIONID": self.jsession_id
        }
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "JSESSIONID=" + self.jsession_id,
            "Host": "10.200.21.61:7001",
            "Origin": "http://10.200.21.61:7001",
            "Referer": "http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        for i in range(0, len(data)):
            yield scrapy.FormRequest(
                url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxkList",  # 其他课程
                formdata=data[i],
                headers=header,
                cookies=cookie,
                meta=response.meta,
                callback=self.parse,
                dont_filter=True
            )


    def chooseYuYan(self, response):
        token_value = self.getToken(response)
        data = []
        data.append({
            "pageSize": "1000",
            "rwh": "",
            "zy": "",
            "qz": "",
            "token": token_value,
            "pageXklb": "xslbxk",
            "pageXkmkdm": "JCL",
            "pageKclb": "C",
            "pageXnxq": response.meta['year'],
            "pageKkxiaoqu": "",
            "pageKkyx": "",
            "pageKcmc": ""
        })  # 语言类
        cookie = {
            "JSESSIONID": self.jsession_id
        }
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "JSESSIONID=" + self.jsession_id,
            "Host": "10.200.21.61:7001",
            "Origin": "http://10.200.21.61:7001",
            "Referer": "http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        for i in range(0, len(data)):
            yield scrapy.FormRequest(
                url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxkList",  # 其他课程
                formdata=data[i],
                headers=header,
                cookies=cookie,
                meta=response.meta,
                callback=self.parse,
                dont_filter=True
            )

    def chooseWaiYu(self, response):
        token_value = self.getToken(response)
        data = []
        data.append({
            "pageSize": "1000",
            "rwh": "",
            "zy": "",
            "qz": "",
            "token": token_value,
            "pageXklb": "xslbxk",
            "pageXkmkdm": "JCL",
            "pageKclb": "C.",
            "pageXnxq": response.meta['year'],
            "pageKkxiaoqu": "",
            "pageKkyx": "",
            "pageKcmc": ""
        })  # 外语类
        cookie = {
            "JSESSIONID": self.jsession_id
        }
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "JSESSIONID=" + self.jsession_id,
            "Host": "10.200.21.61:7001",
            "Origin": "http://10.200.21.61:7001",
            "Referer": "http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        for i in range(0, len(data)):
            yield scrapy.FormRequest(
                url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxkList",  # 其他课程
                formdata=data[i],
                headers=header,
                cookies=cookie,
                meta=response.meta,
                callback=self.parse,
                dont_filter=True
            )


    def chooseYingYuFenji(self, response):
        token_value = self.getToken(response)
        data = []
        data.append({
            "pageSize": "1000",
            "rwh": "",
            "zy": "",
            "qz": "",
            "token": token_value,
            "pageXklb": "yy",
            "pageXkmkdm": "JCL",
            "pageKclb": "C.",
            "pageXnxq": response.meta['year'],
            "pageKkxiaoqu": "",
            "pageKkyx": "",
            "pageKcmc": ""
        })  # 英语分级
        cookie = {
            "JSESSIONID": self.jsession_id
        }
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "JSESSIONID=" + self.jsession_id,
            "Host": "10.200.21.61:7001",
            "Origin": "http://10.200.21.61:7001",
            "Referer": "http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        for i in range(0, len(data)):
            yield scrapy.FormRequest(
                url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxkList",  # 其他课程
                formdata=data[i],
                headers=header,
                cookies=cookie,
                meta=response.meta,
                callback=self.parse,
                dont_filter=True
            )


    def chooseHeXinTongShi(self, response):
        token_value = self.getToken(response)
        data = []
        data.append({
            "pageSize": "10000",
            "rwh": "",
            "zy": "",
            "qz": "",
            "token": token_value,
            "pageXklb": "tsk",
            "pageXkmkdm": "TSL",
            "pageKclb": "D",
            "pageXnxq": response.meta['year'],
            "pageKkxiaoqu": "",
            "pageKkyx": "",
            "pageKcmc": ""
        })  # 核心通识
        cookie = {
            "JSESSIONID": self.jsession_id
        }
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "JSESSIONID=" + self.jsession_id,
            "Host": "10.200.21.61:7001",
            "Origin": "http://10.200.21.61:7001",
            "Referer": "http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        for i in range(0, len(data)):
            yield scrapy.FormRequest(
                url="http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList", # 通识课
                formdata=data[i],
                headers=header,
                cookies=cookie,
                meta=response.meta,
                callback=self.parse,
                dont_filter=True
            )

    def chooseYiBanTongShi(self, response):
        token_value = self.getToken(response)
        data = []
        data.append({
            "pageSize": "10000",
            "rwh": "",
            "zy": "",
            "qz": "",
            "token": token_value,
            "pageXklb": "qxrx",
            "pageXkmkdm": "TSL",
            "pageKclb": "D",
            "pageXnxq": response.meta['year'],
            "pageKkxiaoqu": "",
            "pageKkyx": "",
            "pageKcmc": ""
        })  # 一般通识
        cookie = {
            "JSESSIONID": self.jsession_id
        }
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "JSESSIONID=" + self.jsession_id,
            "Host": "10.200.21.61:7001",
            "Origin": "http://10.200.21.61:7001",
            "Referer": "http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        for i in range(0, len(data)):
            yield scrapy.FormRequest(
                url="http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList", # 通识课
                formdata=data[i],
                headers=header,
                cookies=cookie,
                meta=response.meta,
                callback=self.parse,
                dont_filter=True
            )

    def chooseSiZhengJunLi(self, response):
        token_value = self.getToken(response)
        data = []
        data.append({
            "pageSize": "10000",
            "rwh": "",
            "zy": "",
            "qz": "",
            "token": token_value,
            "pageXklb": "xslbxk",
            "pageXkmkdm": "TSL",
            "pageKclb": "D",
            "pageXnxq": response.meta['year'],
            "pageKkxiaoqu": "",
            "pageKkyx": "",
            "pageKcmc": ""
        })  # 思政军理
        cookie = {
            "JSESSIONID": self.jsession_id
        }
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "JSESSIONID=" + self.jsession_id,
            "Host": "10.200.21.61:7001",
            "Origin": "http://10.200.21.61:7001",
            "Referer": "http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        for i in range(0, len(data)):
            yield scrapy.FormRequest(
                url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxkList", # 思修军理
                formdata=data[i],
                headers=header,
                cookies=cookie,
                meta=response.meta,
                callback=self.parse,
                dont_filter=True
            )

    def chooseHeXinZhuanYe(self, response):
        token_value = self.getToken(response)
        data = []
        data.append({
            "pageSize": "1000",
            "rwh": "",
            "zy": "",
            "qz": "",
            "token": token_value,
            "pageKclb": "I",
            "pageXklb": "xslbxk",
            "pageXkmkdm": "ZYL",
            "pageXnxq": response.meta['year'],
            "pageKkxiaoqu": "",
            "pageKkyx": "",
            "pageKcmc": ""
        })  # 核心专业
        cookie = {
            "JSESSIONID": self.jsession_id
        }
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "JSESSIONID=" + self.jsession_id,
            "Host": "10.200.21.61:7001",
            "Origin": "http://10.200.21.61:7001",
            "Referer": "http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        for i in range(0, len(data)):
            yield scrapy.FormRequest(
                url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxkList", # 其他课程
                formdata=data[i],
                headers=header,
                cookies=cookie,
                meta=response.meta,
                callback=self.parse,
                dont_filter=True
            )

    def chooseYiBanZhuanYe(self, response):
        token_value = self.getToken(response)
        data = []
        data.append({
            "pageSize": "1000",
            "rwh": "",
            "zy": "",
            "qz": "",
            "token": token_value,
            "pageKclb": "J",
            "pageXklb": "xslbxk",
            "pageXkmkdm": "ZYL",
            "pageXnxq": response.meta['year'],
            "pageKkxiaoqu": "",
            "pageKkyx": "",
            "pageKcmc": ""
        }) # 一般专业
        cookie = {
            "JSESSIONID": self.jsession_id
        }
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "JSESSIONID=" + self.jsession_id,
            "Host": "10.200.21.61:7001",
            "Origin": "http://10.200.21.61:7001",
            "Referer": "http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        for i in range(0, len(data)):
            yield scrapy.FormRequest(
                url="http://10.200.21.61:7001/ieas2.1/xslbxk/queryXsxkList", # 其他课程
                formdata=data[i],
                headers=header,
                cookies=cookie,
                meta=response.meta,
                callback=self.parse,
                dont_filter=True
            )

    def parse(self, response):
        # course_id = response.xpath("//table[@class='bot_line']/tr[position()>1]/td[3]/text()").extract()
        # course_teacher = response.xpath("//table[@class='bot_line']/tr[position()>1]/td[10]/div/a/text()").extract()
        # course_name = response.xpath("//table[@class='bot_line']/tr[position()>1]/td[4]/a/text()").extract()
        # course_classification = response.xpath("//table[@class='bot_line']/tr[position()>1]/td[11]/text()").extract()
        # course_property = response.xpath("//table[@class='bot_line']/tr[position()>1]/td[12]/text()").extract()
        # course_department = response.xpath("//table[@class='bot_line']/tr[position()>1]/td[13]/text()").extract()
        # course_credit = response.xpath("//table[@class='bot_line']/tr[position()>1]/td[14]/text()").extract()
        # print(course_id)

        with open(response.meta['file_name'] + "_" + response.meta['year'] + "_" + self.jsession_id + "_teacher.csv", "w", encoding="utf-8") as f:
            for i in range(2, 10000):
                try:
                    course_id = response.xpath("//table[@class='bot_line']/tr[" + str(i) + "]/td[3]/text()").extract()[0]
                    course_teacher = response.xpath(
                        "//table[@class='bot_line']/tr[" + str(i) + "]/td[10]/div/a/text()").extract()
                    course_name = \
                    response.xpath("//table[@class='bot_line']/tr[" + str(i) + "]/td[4]/a/text()").extract()[0]
                    course_classification = response.xpath(
                        "//table[@class='bot_line']/tr[" + str(i) + "]/td[11]/text()").extract()[0]
                    course_property = \
                    response.xpath("//table[@class='bot_line']/tr[" + str(i) + "]/td[12]/text()").extract()[0]
                    course_department = response.xpath(
                        "//table[@class='bot_line']/tr[" + str(i) + "]/td[13]/text()").extract()[0]
                    course_credit = \
                    response.xpath("//table[@class='bot_line']/tr[" + str(i) + "]/td[14]/text()").extract()[0]

                    f.write(course_id)
                    f.write(",")
                    f.write(course_name)
                    f.write(",")
                    f.write(course_department)
                    f.write(",")
                    f.write(course_property)
                    f.write(",")
                    f.write(course_classification)
                    f.write(",")
                    f.write(course_credit)
                    f.write(",")
                    if len(course_teacher) == 0:
                        f.write("N/A\n")
                    else:
                        for j in range(0, len(course_teacher)):
                            f.write(course_teacher[j])
                            if j != len(course_teacher) - 1:
                                f.write("+")
                    f.write('\n')
                except:
                    break
            f.close()

        pass
