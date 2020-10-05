import selenium
from selenium import webdriver
from time import sleep
import os
from webdriver_manager.chrome import ChromeDriverManager

DRIVER = webdriver.Chrome(ChromeDriverManager().install())
SLEEP_TIME = 3


def find_reviews(URL):
    reviews = []
    for i in range(1,4):
        URL1 = URL + str(i) + '/'
        DRIVER.get(URL1)
        sleep(SLEEP_TIME)
        page_reviews = DRIVER.find_elements_by_class_name('_reachbanner_')
        for idx, review in enumerate(page_reviews):
            reviews.append(review.text)
    return reviews

def find_test_reviews(URL):
    reviwes = {}
    DRIVER.get(URL)
    sleep(SLEEP_TIME)
    pos_reviews = DRIVER.find_elements_by_class_name('_reachbanner_')
    for review in pos_reviews[:5]:
        reviwes[review.text] = 'pos'
    DRIVER.find_element_by_class_name('neg').find_element_by_tag_name('a').click()
    sleep(SLEEP_TIME)
    neg_reviews = DRIVER.find_elements_by_class_name('_reachbanner_')
    for review in neg_reviews[:5]:
            reviwes[review.text] = 'neg'
    return reviwes

if __name__ == '__main__':
    try:
        pos_reviews = find_reviews('https://www.kinopoisk.ru/film/251733/reviews/ord/date/status/good/perpage/10/page/')
        file = open('pos_rev.txt', 'w')
        for r in pos_reviews:
            file.write(r)
            file.write('\n')
        file.close()

        neg_reviews = find_reviews('https://www.kinopoisk.ru/film/251733/reviews/ord/date/status/bad/perpage/10/page/')
        file1 = open('neg_rev.txt', 'w')
        for n in neg_reviews:
            file1.write(n)
            file1.write('\n')
        file1.close()

        test_r = find_test_reviews(
            'https://www.kinopoisk.ru/film/251733/reviews/?status=good&ord=date&rnd=1601811243&page=9')
        json.dump(test_r, open("test_r.json", 'w'))
    except:
        DRIVER.close()
    DRIVER.close()