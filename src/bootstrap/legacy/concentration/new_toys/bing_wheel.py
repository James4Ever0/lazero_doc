import time
from pythonbasics import getSearched as getLinked
from dbM import up


def ml(x):
    return [z for y in x for z in y]


def main():
    keyword = input("输入关键字:")
    # only supports one page.
    # page = input("输入查找页数:")
    # url = get_url(keyword)
    # p=int(page)
    # results=ml([getLinked(keyword) for d in range(p)])
    results = getLinked(keyword)
    # results = parse_page(url, page)
    # # 写入文件
    # file = open("data.json", 'w+', encoding='utf-8')
    # it is not that fast.
    file = -1
    t = int(time.time())
    for result in results:
        up(t, file, keyword, result)
        file -= 1
        # waht if we want to use the result?
        print(result)
    #     file.write(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
