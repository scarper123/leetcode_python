#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-08 14:02
# @Author  : Shanming Liu
import json
import os
import re
# from multiprocessing.pool import Pool
from concurrent.futures import ProcessPoolExecutor
import requests
from bs4 import BeautifulSoup

from util import generate_file_name, fetch_response

BASEDIR = os.path.dirname(os.path.abspath(__file__))
SAVE_PATH = os.path.join(BASEDIR, "leetcode")

discussSolutionCategoryIdPattern = re.compile(r'discussCategoryId: \"(\d+)\"')


def write_file(file_name, content):
    dirpath = os.path.dirname(file_name)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    with open(file_name, 'wt') as f:
        f.write(content)


def write_content_into_file(category, title, solution_file, content):
    abs_file = os.path.join(SAVE_PATH, category, title, solution_file)
    write_file(abs_file, content)


def get_solution(slug):
    # url = "https://discuss.leetcode.com/api/topic/23004/here-is-a-python-solution-in-o-n-time"
    url = "https://discuss.leetcode.com/api/topic/%s" % slug
    res = requests.get(url)
    # pprint.pprint(res.json())
    return json.loads(res.content)['posts'][0]['content']


def get_problem_discussion(category_id):
    url = "https://discuss.leetcode.com/api/category/%s" % category_id
    res = requests.get(url)
    return ((generate_file_name(item['title']), item['slug']) for item in json.loads(res.content)['topics'] if
            not item['deleted'])


def get_problem_category_id(title):
    content = requests.get("https://leetcode.com/problems/%s" % title).content
    return discussSolutionCategoryIdPattern.search(content).group(1)


def get_problems_by_category(category):
    return (item['stat']['question__title_slug'] for item in
            requests.get("https://leetcode.com/api/problems/%s" % category).json()['stat_status_pairs'])


def get_all_categories():
    url = "https://leetcode.com/problems/api/card-info"
    return [item['slug'] for item in json.loads(requests.get(url).content)['categories']['0']]


def get_content_by_topic(topic):
    url = "https://discuss.leetcode.com/api/topic/%s" % topic['slug']
    res = requests.get(url)
    soup = BeautifulSoup(json.loads(res.content)['posts'][0]['content'], features='html.parser')
    try:
        code = soup.find_all("code")[-1].string
    except:
        code = json.loads(res.content)['posts'][0]['content']
    return code


def write_discussion_into_file(category, title, topics):
    abs_file = os.path.join(SAVE_PATH, category, "%s.txt" % title)
    print('write file -> %s' % abs_file)
    dirpath = os.path.dirname(abs_file)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    with open(abs_file, 'wt') as f:
        for topic in [item for item in topics if not item['deleted']]:
            title = topic['title']
            if '_imported_content' not in topic:
                content = get_content_by_topic(topic)
            else:
                content = topic['_imported_content']

            f.write(title + "\n")
            f.write(content)
            f.write("\n\n")
            f.write('-' * 100)
            f.write('\n')


def parse_problems_html(problems_html):
    for problem_html in problems_html:
        match = discussSolutionCategoryIdPattern.search(problem_html)
        if match:
            yield match.group(1)


def main():
    # process_pool = ProcessPoolExecutor(2)
    process_pool = ProcessPoolExecutor(4)
    categories = get_all_categories()
    problems = list(fetch_response("https://leetcode.com/api/problems/", categories))
    for category, problem in zip(categories, problems):
        problems_title = [item['stat']['question__title_slug'] for item in problem['stat_status_pairs']]

        problems_html = list(fetch_response("https://leetcode.com/problems/", problems_title))

        discussions_id = list(parse_problems_html(problems_html))

        problems_discussion = list(fetch_response("https://discuss.leetcode.com/api/category/", discussions_id))

        for problem_title, problem_html, discussion in zip(problems_title, problems_html, problems_discussion):
            process_pool.submit(write_discussion_into_file, category, problem_title, discussion['topics'])
            # write_discussion_into_file(category, problem_title, discussion['topics'])

    process_pool.shutdown()
    # process_pool.join()

    # for category in categories:
    #     problem_titles = get_problems_by_category(category)
    #     for title in problem_titles:
    #         discussion_id = get_problem_category_id(title)
    #         for solution_file, solution_slug in get_problem_discussion(discussion_id):
    #             solution_content = get_solution(solution_slug)
    #             write_content_into_file(category, title, solution_file, solution_content)
    #         return


if __name__ == '__main__':
    main()
    # get_all_categories()
    # pprint.pprint(get_problems_by_category('algorithms'))
    # print(get_problem_category_id("median-of-two-sorted-arrays"))
    """
    discussSolutionCategoryId: 836"""

    # pprint.pprint(list(get_problem_discussion(get_problem_category_id("median-of-two-sorted-arrays"))))

    """
    'slug': u'100997/python-solution'
    """
    # get_solution('100997/python-solution')
