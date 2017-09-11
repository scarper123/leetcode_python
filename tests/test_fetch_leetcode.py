#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-08 14:02
# @Author  : Shanming Liu
import json
import os
import re

import requests

from util import generate_file_name

BASEDIR = os.path.dirname(os.path.abspath(__file__))
SAVE_PATH = os.path.join(BASEDIR, "leetcode")

discussSolutionCategoryIdPattern = re.compile(r'discussSolutionCategoryId: \"(\d+)\"')


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
    return (item['slug'] for item in json.loads(requests.get(url).content)['categories']['0'])


def main():
    categories = get_all_categories()
    for category in categories:
        problem_titles = get_problems_by_category(category)
        for title in problem_titles:
            discussion_id = get_problem_category_id(title)
            for solution_file, solution_slug in get_problem_discussion(discussion_id):
                solution_content = get_solution(solution_slug)
                write_content_into_file(category, title, solution_file, solution_content)
            return


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
