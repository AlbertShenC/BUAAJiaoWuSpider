# -*- coding: utf-8 -*-
import scrapy
import json


class GetinfoSpider(scrapy.Spider):
    name = 'getInfo'
    allowed_domains = ['*']
    start_urls = [
        'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=0&disciplineid=0&enrollid=0&pageindex=' + str(
            i) + '&pagesize=12&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false/'
        for i in range(0, 105)]

    def start_requests(self):
        url_set = ['http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1176&disciplineid=0&enrollid=0&pageindex=1&pagesize=16&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1001&disciplineid=0&enrollid=0&pageindex=1&pagesize=35&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1007&disciplineid=0&enrollid=0&pageindex=1&pagesize=38&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1012&disciplineid=0&enrollid=0&pageindex=1&pagesize=86&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1021&disciplineid=0&enrollid=0&pageindex=1&pagesize=40&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1145&disciplineid=0&enrollid=0&pageindex=1&pagesize=81&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1039&disciplineid=0&enrollid=0&pageindex=1&pagesize=32&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1050&disciplineid=0&enrollid=0&pageindex=1&pagesize=41&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1059&disciplineid=0&enrollid=0&pageindex=1&pagesize=106&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1068&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1144&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1075&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1084&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1094&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1100&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1108&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1113&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1114&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1123&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1128&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1129&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1132&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1134&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1148&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1135&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1138&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1139&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1149&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1150&disciplineid=0&enrollid=0&pageindex=1&pagesize=12&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1146&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1151&disciplineid=0&enrollid=0&pageindex=1&pagesize=12&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1153&disciplineid=0&enrollid=0&pageindex=1&pagesize=12&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1155&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1154&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false',
                   'http://teacher.buaa.edu.cn/system/resource/tsites/advancesearch.jsp?collegeid=1166&disciplineid=0&enrollid=0&pageindex=1&pagesize=200&rankid=0&honorid=0&pinyin=&profilelen=100&teacherName=&searchDirection=&viewmode=8&viewid=65073&siteOwner=1211900872&viewUniqueId=u10&showlang=zh_CN&ellipsis=...&alignright=false'
                   ]
        department_set = ['微电子学院',
                          '材料科学与工程学院',
                          '电子信息工程学院',
                          '自动化科学与电气工程学院',
                          '能源与动力工程学院',
                          '航空科学与工程学院',
                          '计算机学院',
                          '机械工程及自动化学院',
                          '经济管理学院',
                          '数学与系统科学学院',
                          '生物与医学工程学院',
                          '人文社会科学学院',
                          '外国语学院',
                          '交通科学与工程学院',
                          '可靠性与系统工程学院',
                          '宇航学院',
                          '飞行学院',
                          '仪器科学与光电工程学院',
                          '物理科学与核能工程学院',
                          '法学院',
                          '软件学院',
                          '中法工程师学院',
                          '新媒体艺术与设计学院',
                          '化学学院',
                          '化学与环境学院',
                          '马克思主义学院',
                          '无人机研究所',
                          '工程训练中心',
                          '体育部',
                          '空间与环境学院',
                          '北斗丝路学院',
                          '北航学院',
                          '医工交叉创新研究院',
                          '网络空间安全学院',
                          '机关及其他单位'
                          ]

        for i in range(0, len(url_set)):
            yield scrapy.Request(
                url=url_set[i],
                meta={'department': department_set[i]}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        with open('teacher.csv', 'a', encoding='utf-8') as f:
            for i in range(0, len(json.loads(response.text)['teacherData'])):
                f.write(json.loads(response.text)['teacherData'][i]['name'] + ',')
                f.write('北京航空航天大学,')
                f.write(response.meta['department'] + ',')

                tutor = False
                if json.loads(response.text)['teacherData'][0]['doctorTutor'] != '':
                    f.write(json.loads(response.text)['teacherData'][0]['doctorTutor'])
                    tutor = True
                if json.loads(response.text)['teacherData'][0]['gtutor'] != '':
                    if tutor == True:
                        f.write('+')
                    f.write(json.loads(response.text)['teacherData'][0]['gtutor'])
                    tutor = True
                if json.loads(response.text)['teacherData'][0]['prorank'] != '':
                    if tutor == True:
                        f.write('+')
                    f.write(json.loads(response.text)['teacherData'][0]['prorank'])
                    tutor = True
                if tutor == False:
                    f.write('N/A')
                f.write(',')

                if json.loads(response.text)['teacherData'][i]['sex'] != '':
                    f.write(json.loads(response.text)['teacherData'][i]['sex'] + ',')
                else:
                    f.write('N/A,')

                f.write(json.loads(response.text)['teacherData'][i]['url'] + ',')
                f.write(' http://teacher.buaa.edu.cn' + json.loads(response.text)['teacherData'][i]['picUrl'] + '\n')
            f.close()

