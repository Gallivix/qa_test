from selene import browser, be, have
from selene.core.wait import Command

def test_valid_login():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('[name=email]').type('qagurubot@gmail.com')
    browser.element('[name=password]').type('somepasshere').press_enter()
    browser.element('.logined-form').should(have.text('QA_GURU_BOT'))

    browser.quit()

def test_wrong_password():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('[name=email]').type('qagurubot@gmail.com')
    browser.element('[name=password]').type('assdaff').press_enter()
    browser.element('.btn-error').should(have.text('Неверный пароль'))

    browser.quit()

def test_empty_password():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('[name=email]').type('qagurubot@gmail.com').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле Пароль'))

    browser.quit()

def test_empty_login():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('[name=password]').type('assdaff').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле E-Mail'))

    browser.quit()

def test_empty_login():
    browser.open('https://ya.ru ')
    browser.element('[name=text]').type('site:example.com "1234567890abcdefghijklmnopqrstuvwxyz" mime:pdf lang:zu date:19000101').press_enter()
    browser.element('.EmptySearchResults-Title').should(have.text('Ничего не нашли'))
    browser.quit()