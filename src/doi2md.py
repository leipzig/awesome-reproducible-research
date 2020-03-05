from crossref.restful import Works
import arxiv
import argparse
import datetime


#python src/doi2md.py --doi 10.1371/journal.pone.0216125 --type theory --field Science --category "Statistical reproducibility"
#mv readme.new.md readme.md
#edit as needed
parser = argparse.ArgumentParser(description='doi and table filler arguments')
parser.add_argument('--doi',help='the doi of the manuscript e.g. 10.1136/bmj.39590.732037.47')
parser.add_argument('--type',help='the manuscript type: study, theory, or tools')
parser.add_argument('--field',help='the study field e.g. Cancer Biology')
parser.add_argument('--approach',help='the manuscript approach e.g. Refactor')
parser.add_argument('--size',help='the study size e.g 8 studies')
parser.add_argument('--tools',help='the tools reviewed e.g. MLflow, Polyaxon')
parser.add_argument('--category',help='the manuscript theory category e.g. Statistical reproducibility')
args = parser.parse_args()




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


#arxiv
# [{
#     'id': 'http://arxiv.org/abs/2002.11626v1',
#     'guidislink': True,
#     'updated': '2020-02-06T17:12:29Z',
#     'updated_parsed': time.struct_time(tm_year = 2020, tm_mon = 2, tm_mday = 6, tm_hour = 17, tm_min = 12, tm_sec = 29, tm_wday = 3, tm_yday = 37, tm_isdst = 0),
#     'published': '2020-02-06T17:12:29Z',
#     'published_parsed': time.struct_time(tm_year = 2020, tm_mon = 2, tm_mday = 6, tm_hour = 17, tm_min = 12, tm_sec = 29, tm_wday = 3, tm_yday = 37, tm_isdst = 0),
#     'title': 'A Realistic Guide to Making Data Available Alongside Code to Improve\n  Reproducibility',
#     'title_detail': {
#         'type': 'text/plain',
#         'language': None,
#         'base': 'http://export.arxiv.org/api/query?search_query=&id_list=2002.11626&start=0&max_results=1000&sortBy=relevance&sortOrder=descending',
#         'value': 'A Realistic Guide to Making Data Available Alongside Code to Improve\n  Reproducibility'
#     },
#     'summary': "Data makes science possible. Sharing data improves visibility, and makes the\nresearch process transparent. This increases trust in the work, and allows for\nindependent reproduction of results. However, a large proportion of data from\npublished research is often only available to the original authors. Despite the\nobvious benefits of sharing data, and scientists' advocating for the importance\nof sharing data, most advice on sharing data discusses its broader benefits,\nrather than the practical considerations of sharing. This paper provides\npractical, actionable advice on how to actually share data alongside research.\nThe key message is sharing data falls on a continuum, and entering it should\ncome with minimal barriers.",
#     'summary_detail': {
#         'type': 'text/plain',
#         'language': None,
#         'base': 'http://export.arxiv.org/api/query?search_query=&id_list=2002.11626&start=0&max_results=1000&sortBy=relevance&sortOrder=descending',
#         'value': "Data makes science possible. Sharing data improves visibility, and makes the\nresearch process transparent. This increases trust in the work, and allows for\nindependent reproduction of results. However, a large proportion of data from\npublished research is often only available to the original authors. Despite the\nobvious benefits of sharing data, and scientists' advocating for the importance\nof sharing data, most advice on sharing data discusses its broader benefits,\nrather than the practical considerations of sharing. This paper provides\npractical, actionable advice on how to actually share data alongside research.\nThe key message is sharing data falls on a continuum, and entering it should\ncome with minimal barriers."
#     },
#     'authors': ['Nicholas J Tierney', 'Karthik Ram'],
#     'author_detail': {
#         'name': 'Karthik Ram'
#     },
#     'author': 'Karthik Ram',
#     'arxiv_comment': 'Both authors contributed equally to the work, 35 pages, 7 figures, 3\n  tables',
#     'links': [{
#         'href': 'http://arxiv.org/abs/2002.11626v1',
#         'rel': 'alternate',
#         'type': 'text/html'
#     }, {
#         'title': 'pdf',
#         'href': 'http://arxiv.org/pdf/2002.11626v1',
#         'rel': 'related',
#         'type': 'application/pdf'
#     }],
#     'arxiv_primary_category': {
#         'term': 'cs.DL',
#         'scheme': 'http://arxiv.org/schemas/atom'
#     },
#     'tags': [{
#         'term': 'cs.DL',
#         'scheme': 'http://arxiv.org/schemas/atom',
#         'label': None
#     }],
#     'pdf_url': 'http://arxiv.org/pdf/2002.11626v1',
#     'affiliation': 'None',
#     'arxiv_url': 'http://arxiv.org/abs/2002.11626v1',
#     'journal_reference': None,
#     'doi': None
# }]




class md:
    def __init__(self, args):
        works = Works()
        #print(args.doi)
        if 'arxiv' in args.doi:
            #maybe you prepended it, maybe not
            self.doi=args.doi.replace('https://arxiv.org/abs/','')
            self.link='https://arxiv.org/abs/'+self.doi
            self.arxiv()
        else:
            self.doi=args.doi.replace('https://doi.org/','')
            self.link='https://doi.org/'+self.doi
            self.crossref()

        #user-supplied
        self.type=args.type
        self.field=args.field
        self.approach=args.approach
        self.size=args.size
        self.category=args.category

    def arxiv(self):
        pub = arxiv.query(id_list=[self.doi])[0]
        if pub is None:
            print("Arxiv doesn't know about this doi")
        if pub.get('updated') is not None:
            date_time_str=pub.get('updated')
            date_time_obj = datetime.datetime.strptime(date_time_str,"%Y-%m-%dT%H:%M:%SZ")
            self.yyyymmdd=date_time_obj.strftime('%Y-%m-%d')
            self.yyyy=date_time_obj.strftime('%Y')
        self.title=pub.get('title')
        self.abstract=pub.get('summary')
        if len(pub['authors'])==1:
            self.author = pub['authors'][0].split(' ')[-1]
        elif len(pub['author'])==2:
            self.author = pub['authors'][0].split(' ')[-1]+' & '+pub['authors'][1].split(' ')[-1]
        else:
            self.author = pub['authors'][0].split(' ')[-1]+' et al'

    def crossref(self):
        pub=works.doi(self.doi)
        if pub is None:
            print("Crossref doesn't know about this doi")
        if pub.get('created') is not None:
            if pub.get('created').get('date-time') is not None:
                date_time_str=pub.get('created').get('date-time')
                date_time_obj = datetime.datetime.strptime(date_time_str,"%Y-%m-%dT%H:%M:%SZ")
                self.yyyymmdd=date_time_obj.strftime('%Y-%m-%d')
                self.yyyy=date_time_obj.strftime('%Y')
        elif pub.get('published-online') is not None:
            if pub.get('published-online').get('date-parts') is not None:
                dl=pub.get('published-online').get('date-parts')[0]
                self.yyyymmdd=dl[0]+'-'+dl[1]+'-'+dl[2]
                #         'date-parts': [
                #             [2008, 6, 26]
        
        self.title=pub.get('title')[0]
        self.abstract=pub.get('abstract')
        
        if len(pub['author'])==1:
            self.author = pub['author'][0]['family']
        elif len(pub['author'])==2:
            self.author = pub['author'][0]['family']+' & '+pub['author'][1]['family']
        else:
            self.author = pub['author'][0]['family']+' et al'

    def study(self):
        return("""<tr>
					<td>
						<p>
							<a href="{0}">{1}
							<meta property="datePublished" content="{2}">{3}</a>
						</p>
					</td>
					<td>
						<p>
							<span title="{4}">{5}</span>
						</p>
					</td>
					<td>
						<p>
							{6}
						</p>
					</td>
					<td>
						<p>
							{7}
						</p>
					</td>
				</tr>
				<!--study_placeholder-->
""".format(self.link,self.author,self.yyyymmdd,self.yyyy,self.title,self.field,self.approach,self.size))

    def theory(self):
        return("""<tr>
					<td>
						<p>
							<a href="{0}"><span title="{1}">{2} <meta property="datePublished" content="{3}">{4}</span></a>
						</p>
					</td>
					<td>
						<p>
							<span title="{5}">{6}</span>
						</p>
					</td>
					<td>
						<p>
							{7}
						</p>
					</td>
					<td>
						<p>
							{8}
						</p>
					</td>
				</tr>
				<!--theory_placeholder-->
""".format(self.link,self.title,self.author,self.yyyymmdd,self.yyyy,self.abstract,self.title,self.field,self.category))

    def tools(self):
        return("""<tr>
					<td>
						<p>
							<a href="{0}">{1}
							<meta property="datePublished" content="{2}">{3}</a>
						</p>
					</td>
					<td>
						<p>
							<span title="{4}">{5}</span>
						</p>
					</td>
					<td>
						<p>
							{6}
						</p>
					</td>
				</tr>
				<!--tools_placeholder-->
""".format(self.link,self.author,self.yyyymmdd,self.yyyy,self.abstract,self.title,self.tools))

if args.doi:
    mymd = md(args)
    if args.type is not None:
        content=getattr(mymd, args.type)()
        with open("readme.md") as f:
            newText=f.read().replace('<!--{}_placeholder-->'.format(args.type), content)
        with open("readme.new.md", "w") as f:
            f.write(newText)
