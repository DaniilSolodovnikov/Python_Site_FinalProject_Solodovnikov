import unittest
from App.views import add_ad_to_database, create_ad
import logging


class TestAddAdToDatabase(unittest.TestCase):
    def test_add_ad(self):
        # определить тестовые данные
        ad_data = {
            'title': 'Test Ad',
            'description': 'This is a test ad',
            'category': 'Clothing',
            'rental_price': 20.00
        }

        # вызвать тестируемую функцию
        result = add_ad_to_database(ad_data)

        # проверить, соответствует ли результат ожиданиям
        self.assertEqual(result, 'Объявление добавлено успешно')


class TestCreateAd(unittest.TestCase):
    def test_create_ad(self):
        # определить тестовые данные
        ad_data = {
            'title': 'Test Ad',
            'description': 'This is a test ad',
            'category': 'Clothing'
        }

        # вызвать тестируемую функцию
        result = add_ad_to_database(ad_data)

        # проверить, соответствует ли результат ожиданиям
        self.assertEqual(result, 'Объявление создано')


class TestApproveAd(unittest.TestCase):
    def test_approve_ad(self):
        # определить тестовые данные
        ad_data = {
            'title': 'Test Ad',
            'description': 'This is a test ad',
            'category': 'Clothing'
        }

        # вызвать тестируемую функцию
        result = add_ad_to_database(ad_data)

        # проверить, соответствует ли результат ожиданиям
        self.assertEqual(result, 'Объявление одобрено')


if __name__ == '__main__':
    unittest.main()


# Настроить регистратор
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Зарегистрировать ошибку
logging.error('Это сообщение об ошибке.')

# Записать некоторую отладочную информацию
logging.debug('Это отладочное сообщение.')