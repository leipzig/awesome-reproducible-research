from crossref.restful import Works
import argparse
import datetime

parser = argparse.ArgumentParser(description='doi and table filler arguments')
parser.add_argument('--doi',help='the doi of the manuscript')
parser.add_argument('--type',help='the manuscript type: study, theory, or review')
args = parser.parse_args()

works = Works()

# {
#     'indexed': {
#         'date-parts': [
#             [2020, 2, 26]
#         ],
#         'date-time': '2020-02-26T18:23:23Z',
#         'timestamp': 1582741403836
#     },
#     'reference-count': 0,
#     'publisher': 'BMJ',
#     'issue': '7659',
#     'license': [{
#         'URL': 'http://www.bmj.org/licenses/tdm/1.0/terms-and-conditions.html',
#         'start': {
#             'date-parts': [
#                 [2008, 6, 26]
#             ],
#             'date-time': '2008-06-26T00:00:00Z',
#             'timestamp': 1214438400000
#         },
#         'delay-in-days': 0,
#         'content-version': 'tdm'
#     }],
#     'content-domain': {
#         'domain': [],
#         'crossmark-restriction': False
#     },
#     'short-container-title': ['BMJ'],
#     'published-print': {
#         'date-parts': [
#             [2008, 6, 28]
#         ]
#     },
#     'DOI': '10.1136/bmj.39590.732037.47',
#     'type': 'journal-article',
#     'created': {
#         'date-parts': [
#             [2008, 6, 26]
#         ],
#         'date-time': '2008-06-26T22:28:39Z',
#         'timestamp': 1214519319000
#     },
#     'page': '1472-1474',
#     'source': 'Crossref',
#     'is-referenced-by-count': 340,
#     'title': ['What is missing from descriptions of treatment in trials and reviews?'],
#     'prefix': '10.1136',
#     'volume': '336',
#     'author': [{
#         'given': 'Paul',
#         'family': 'Glasziou',
#         'sequence': 'first',
#         'affiliation': []
#     }, {
#         'given': 'Emma',
#         'family': 'Meats',
#         'sequence': 'additional',
#         'affiliation': []
#     }, {
#         'given': 'Carl',
#         'family': 'Heneghan',
#         'sequence': 'additional',
#         'affiliation': []
#     }, {
#         'given': 'Sasha',
#         'family': 'Shepperd',
#         'sequence': 'additional',
#         'affiliation': []
#     }],
#     'member': '239',
#     'published-online': {
#         'date-parts': [
#             [2008, 6, 26]
#         ]
#     },
#     'container-title': ['BMJ'],
#     'original-title': [],
#     'language': 'en',
#     'link': [{
#         'URL': 'http://data.bmj.org/tdm/10.1136/bmj.39590.732037.47',
#         'content-type': 'unspecified',
#         'content-version': 'vor',
#         'intended-application': 'text-mining'
#     }, {
#         'URL': 'https://syndication.highwire.org/content/doi/10.1136/bmj.39590.732037.47',
#         'content-type': 'unspecified',
#         'content-version': 'vor',
#         'intended-application': 'similarity-checking'
#     }],
#     'deposited': {
#         'date-parts': [
#             [2018, 2, 21]
#         ],
#         'date-time': '2018-02-21T18:07:45Z',
#         'timestamp': 1519236465000
#     },
#     'score': 1.0,
#     'subtitle': [],
#     'short-title': [],
#     'issued': {
#         'date-parts': [
#             [2008, 6, 26]
#         ]
#     },
#     'references-count': 0,
#     'journal-issue': {
#         'published-online': {
#             'date-parts': [
#                 [2008, 6, 26]
#             ]
#         },
#         'published-print': {
#             'date-parts': [
#                 [2008, 6, 28]
#             ]
#         },
#         'issue': '7659'
#     },
#     'alternative-id': ['10.1136/bmj.39590.732037.47'],
#     'URL': 'http://dx.doi.org/10.1136/bmj.39590.732037.47',
#     'relation': {},
#     'ISSN': ['0959-8138', '1468-5833'],
#     'issn-type': [{
#         'value': '0959-8138',
#         'type': 'print'
#     }, {
#         'value': '1468-5833',
#         'type': 'electronic'
#     }]
# }



pub=works.doi(args.doi.replace('https://doi.org/',''))

print(pub)
date_time_str=pub['created']['date-time']
date_time_obj = datetime.datetime.strptime(date_time_str,"%Y-%m-%dT%H:%M:%SZ")
yyyymmdd=date_time_obj.strftime('%Y-%m-%d')
yyyy=date_time_obj.strftime('%Y')
title=pub['title']

class md:
    def theory(self):
        content="""<tr><td><p><a href="https://doi.org/{0}">Foo & Bar <meta property="datePublished" content="{1}">{2}</a></td><td><p><span title="{3}">{4}</span></p></td><td><p>{5}</p></td><td><p>{6}</p></td></tr>""".format(doi,yyyymmdd,yyyy,abstract,title,field,category)
