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

    @pytest.mark.parametrize('book_name', ['a', 'ok', 'aleksey', 'a' * 40])
    def test_add_new_book_name_length(self, book_name):
        collector1 = BooksCollector()
        collector1.add_new_book(book_name)
        assert book_name in collector1.books_genre 

    def test_set_book_name_genre_book(self):
        collector2 = BooksCollector()
        collector2.add_new_book('Мой космос')
        collector2.set_book_genre('Мой космос', 'Фантастика')
        assert collector2.get_book_genre('Мой космос') == 'Фантастика'


    def test_get_book_name_genre_book(self):
        collector3 = BooksCollector()
        collector3.add_new_book('Хищник')
        collector3.set_book_genre('Хищник', 'Ужасы')
        genre = collector3.get_book_genre('Хищник')
        assert genre == 'Ужасы'

    
    def test_get_books_with_specific_genre_name_specific_genre(self): 
        collector4 = BooksCollector()
        collector4.add_new_book('Агата Кристи')
        collector4.set_book_genre('Агата Кристи', 'Детективы')
        collector4.add_new_book('Шерлок Холмс')
        collector4.set_book_genre('Шерлок Холмс', 'Детективы')
        collector4.add_new_book('Звёздные войны')
        collector4.set_book_genre('Звёздные войны', 'Фантастика')
        assert collector4.get_books_with_specific_genre('Детективы') == ['Агата Кристи', 'Шерлок Холмс']


    def test_get_books_genre_books_genre(self):
        collector5 = BooksCollector()
        collector5.add_new_book('Соник')
        collector5.set_book_genre('Соник', 'Мультфильмы')
        books_genre = collector5.get_books_genre()
        assert 'Соник' in collector5.get_books_genre()
        assert books_genre['Соник'] == 'Мультфильмы'


    def test_get_books_for_children_genre_children_rating(self):
        collector6 = BooksCollector()
        collector6.add_new_book('Приключения Шурика')
        collector6.set_book_genre('Приключения Шурика', 'Комедии')
        collector6.add_new_book('Чужой 3')
        collector6.set_book_genre('Чужой 3', 'Ужасы')
        assert collector6.get_books_for_children() == ['Приключения Шурика']


    def test_add_book_in_favorites_add_in_favorite(self):
        collector7 = BooksCollector()
        collector7.add_new_book('Дюна')
        collector7.add_book_in_favorites('Дюна')
        assert 'Дюна' in collector7.get_list_of_favorites_books()


    def test_delete_book_from_favorites_delete_from_favorite(self):
        collector8 = BooksCollector()
        collector8.add_new_book('Колобок')
        collector8.add_book_in_favorites('Колобок')
        collector8.delete_book_from_favorites('Колобок')
        assert 'Колобок' not in collector8.get_list_of_favorites_books()


    def test_get_list_of_favorites_books_favorites(self):
        collector9 = BooksCollector()
        collector9.add_new_book('Человек-паук')
        collector9.add_book_in_favorites('Человек-паук')
        assert collector9.get_list_of_favorites_books() == ['Человек-паук']
