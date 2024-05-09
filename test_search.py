from selene import browser, be, have


def test_right_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('Площадь треугольника').press_enter()
    browser.element('[id="search"]').should(have.no.text('площадь квадрата равна'))


def test_wrong_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('DFGGDSFdgdffgh').press_enter()
    browser.element('[id = "botstuff"]').should(have.text('По запросу DFGGDSFdgdffgh ничего не найдено'))
