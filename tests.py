import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector() 

    #тест: максимально возможная длина названия книги 40 символов
    @pytest.mark.parametrize(
        'name', 
        [
            'A', 
            'Оно', 
            'Название книги длиной 39 символов Книга', 
            'Название книги длиной 40 символов Книга1'
        ]
    )
    
    def test_add_new_book_with_valid_name_is_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert name in collector.get_books_genre() 

    #тест: попытка добавления в коллекцию книги с названием длиной 0 символов и 41 символ  
    @pytest.mark.parametrize(
        'Invalid_name', 
        [
            '',  
            'Название книги длиной 41 символ Книга1234', 
            'Название книги длиной 42 символа Книга1234'
        ]
    )
    
    def test_add_new_book_with_invalid_name_is_not_added(self, Invalid_name):
        collector = BooksCollector()
        collector.add_new_book(Invalid_name)

        assert Invalid_name not in collector.get_books_genre() 



    # тест: установка жанра книге и получение жанра книги по её имени
    def test_set_book_genre_add_genre_to_book(self):
        collector = BooksCollector()
        collector.add_new_book('Пираты Карибского моря')
        collector.set_book_genre('Пираты Карибского моря', 'Фантастика')

        assert collector.get_book_genre('Пираты Карибского моря') == 'Фантастика'

    # тест: получение списка книг с определенным жанром
    def test_get_books_with_specific_genre_get_comedy_books(self):
        collector = BooksCollector()
        collector.add_new_book('Зачарованные')
        collector.set_book_genre('Зачарованные', 'Комедии')
        collector.add_new_book('Покоряя вершины')
        collector.set_book_genre('Покоряя вершины', 'Детективы')

        result = collector.get_books_with_specific_genre('Комедии')
        assert 'Зачарованные' in result
        assert 'Покоряя вершины' not in result

    #тест: невозможность добавить одну и ту же книгу дважды
    def test_add_new_book_double_add_is_not_possible(self):
        collector = BooksCollector()
        collector.add_new_book('Зачарованные')
        collector.add_new_book('Зачарованные')
        
        #проверяем, что в словаре только одна запись 
        assert len(collector.get_books_genre()) == 1

    #тест: возвращение книг, подходящих детям, в списке
    def test_get_books_for_children_returns_valid_books(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Винни-Пуха')
        collector.set_book_genre('Приключения Винни-Пуха', 'Мультфильмы')
        collector.add_new_book('Ледниковый период')
        collector.set_book_genre('Ледниковый период', 'Фантастика')

        children_books = collector.get_books_for_children()
        assert 'Приключения Винни-Пуха' in children_books
        assert 'Ледниковый период' in children_books
        assert len(children_books) == 2

    #тест: исключение книг с возрастным рейтингом
    def test_get_books_for_children_exludes_adult_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')

        children_books = collector.get_books_for_children()
        assert 'Чужой' not in children_books
        assert 'Десять негритят' not in children_books
        assert len(children_books) == 0

    #тест: добавление книг в избранное
    def test_add_book_in_favorites_added_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Зачарованные')
        collector.add_book_in_favorites('Зачарованные')

        assert 'Зачарованные' in collector.get_list_of_favorites_books()

    #тест: удаление книг из избранного
    def test_delete_books_from_favorites_deleted_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Зачарованные')
        collector.add_book_in_favorites('Зачарованные')

        collector.delete_book_from_favorites('Зачарованные')

        assert 'Зачарованные' not in collector.get_list_of_favorites_books()

    #тест: нельзя повторно добавить книгу в избранное, если она там уже есть
    def test_add_book_in_favorites_double_add_is_not_possible(self):
        collector = BooksCollector()
        collector.add_new_book('Зачарованные')
        collector.add_book_in_favorites('Зачарованные')
        collector.add_book_in_favorites('Зачарованные')

        favourites = collector.get_list_of_favorites_books()
        
        assert favourites.count('Зачарованные') == 1
        assert len(favourites) == 1

 




