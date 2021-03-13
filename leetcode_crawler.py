import json
import requests

session = requests.Session()
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
requests.packages.urllib3.disable_warnings()


class LeetcodeCrawler:
    def __init__(self):
        self.client = None

    def login(self, email, password):
        sign_in_url = 'https://leetcode-cn.com/accounts/login/'
        client = requests.session()
        client.encoding = "utf-8"

        try:
            client.get(sign_in_url, verify=False)

            login_data = {'login': email,
                          'password': password
                          }

            result = client.post(sign_in_url, data=login_data, headers=dict(Referer=sign_in_url))

            if result.ok:
                print("Login successfully!")
        except:
            print("Login failed!")

        self.client = client

    def get_problems_list(self):
        url = "https://leetcode-cn.com/api/problems/all/"
        headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
        # resp = session.get(url, headers=headers, timeout=10)
        resp = self.client.get(url, headers=headers, timeout=10)
        question_list = json.loads(resp.content.decode('utf-8'))
        questions = []
        for question in question_list['stat_status_pairs']:
            # 题目编号
            question_id = question['stat']['question_id']
            # 题目名称
            question_slug = question['stat']['question__title_slug']
            # 题目状态
            question_status = question['status']

            # 题目难度级别，1 为简单，2 为中等，3 为困难
            level = question['difficulty']['level']

            # 是否为付费题目
            if question['paid_only']:
                continue
            # 跳过已经ac的题目
            if question_status == 'ac':
                continue
            questions.append(question_slug)
        return questions

    def get_problem_by_slug(self, slug):
        url = "https://leetcode-cn.com/graphql"
        params = {
            'operationName': "getQuestionDetail",
            'variables': {'titleSlug': slug},
            'query': '''query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    likes
                    questionTitle
                    translatedTitle
                    questionTitleSlug
                    difficulty
                }
            }'''
        }

        json_data = json.dumps(params).encode('utf8')

        headers = {
            'User-Agent': user_agent,
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Referer': 'https://leetcode-cn.com/problems/' + slug
        }
        # resp = session.post(url, data=json_data, headers=headers, timeout=10)
        resp = self.client.post(url, data=json_data, headers=headers, timeout=10)
        content = resp.json()
        return content['data']['question']

    def get_all_problems(self):
        problems_list = self.get_problems_list()
        print(f'problems_list: {len(problems_list)}')
        res = []
        for prob in problems_list:
            r = self.get_problem_by_slug(prob)
            res.append(r)
            res.sort(key=lambda x: x['likes'], reverse=True)
        print(f'saved problems: {len(res)}')
        json.dump(res, open('leetcode.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)


if __name__ == '__main__':
    crawler = LeetcodeCrawler()
    crawler.login('15221104953', 'liyd06646587')
    crawler.get_all_problems()
