#!/usr/bin/env python

# Submitter: Ahmed Shah
#
# About: Unit 7 - TomeRater
#
# Build out a new application for literature review!
# Define data types to represent users, books, and reviews.
# Implement the interactions between these objects and write
# code that logically couples them together. Use the skills
# you’ve learned to translate an idea into software!

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def TomeRater(self):
        pass

    def isbn_does_not_exist_check(self, isbn_to_check):
        for book in self.books:
            if isbn_to_check == book.get_isbn():
                print("ISBN {isbn} already exists".format(isbn=isbn_to_check))
                return False
        return True

    def email_characters_check(self, email_to_check):
        if ("@" in email_to_check) and (any(substring in email_to_check for substring in [".com", ".edu", ".org"])):
            return True
        else:
            print("email {email_to_check} does not have a @ and a .com, .edu, or .org".
                  format(email_to_check=email_to_check))
            return False

    def create_book(self, title, isbn):
        if self.isbn_does_not_exist_check(isbn):
            # print("create_book: {title} - {isbn}".format(title=title, isbn=isbn))
            return Book(title, isbn)
        else:
            print("ISBN {isbn} already exists. Book not added".format(isbn=isbn))

    def create_novel(self, title, author, isbn):
        if self.isbn_does_not_exist_check(isbn):
            # print("create_book: {title} - {isbn}".format(title=title, isbn=isbn))
            return Fiction(title, author, isbn)
        else:
            print(str(isbn) + " already exists (" + title + "")

    def create_non_fiction(self, title, subject, level, isbn):
        if self.isbn_does_not_exist_check(isbn):
            # print("create_book: {title} - {isbn}".format(title=title, isbn=isbn))
            return Non_Fiction(title, subject, level, isbn)
        else:
            print(str(isbn) + " already exists (" + title + "")

    def add_book_to_user(self, book, email, rating=None):

        # for user in self.users.items():
        #    print("add_book_to_user - user:{user}".format(user=user.get_email()))

        if email in self.users.keys():
            # print("add_book_to_user - email in self.users.items(): " + email)
            # print("add_book_to_user - book:{book}".format(book=book.get_isbn()))
            book.add_rating(rating)

            self.users[email].read_book(book, rating)

            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, user_books=None):
        # print("add_user: self.users:{email}".format(email=email))
        if (email not in self.users.keys()) and (self.email_characters_check(email) is True):
            if user_books is None:
                self.users[email] = User(name, email)
                # print("no book-> " + email + " " + str(self.users[email]))
            else:
                self.users[email] = User(name, email)
                for book in user_books:
                    self.add_book_to_user(book, email)
                    # print(name + " " + str(self.users[email]) + book.title)

        else:
            print("User {name} already exists or email {email} incorrect".format(name=name, email=email))

    def print_catalog(self):
        print("\n------ Catalog of Books Available -----")
        for book in self.books:
            print(book)

    def print_users(self):
        print("\n-------------- List of Users ----------")
        for user in self.users.items():
            print(user)

    def most_read_book(self):
        most_read_book = next(iter(self.books))
        most_read_value = self.books[most_read_book]
        for book, times_read in self.books.items():
            if most_read_value < times_read:
                most_read_book = book
                most_read_value = times_read
        return most_read_book

    def highest_rated_book(self):
        previous_highest_rated = next(iter(self.books))
        for book in self.books:
            if previous_highest_rated.get_average_rating() < book.get_average_rating():
                previous_highest_rated = book
        return previous_highest_rated

    def most_positive_user(self):
        previous_highest_rated = next(iter(self.users.values()))
        for user in self.users.values():
            if previous_highest_rated.get_average_rating() < user.get_average_rating():
                previous_highest_rated = user
        return "{email} with an average rating of {rating} on all books they have reviewed".format(
            email=previous_highest_rated.get_email(), rating=previous_highest_rated.get_average_rating())


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{user}'s email has been updated to {email}".format(user=self.name, email=self.email))

    def __repr__(self):
        return "User: {user}, email: {email}, books read: {number_of_books_read}". \
            format(user=self.name, email=self.email, number_of_books_read=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        sum = 0
        number_of_rated_books = 0
        for value in self.books.keys():
            if self.books[value] is not None:
                sum += int(self.books[value])
                number_of_rated_books += 1
        return sum / number_of_rated_books


class Book(object):
    def __init__(self, title, isbn):
        self.title = str(title)
        self.isbn = int(isbn)
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("ISBN for <{book_title}> has been updated to {isbn}".format(book_title=self.title, isbn=self.isbn))

    def add_rating(self, rating):
        if type(rating) is int:
            if 0 <= rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def __eq__(self, book_object):
        if self.title == book_object.title and self.isbn == book_object.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        if len(self.ratings) == 0:
            return None
        else:
            return sum(self.ratings) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):

        return "{title} {isbn} | average rating:{avg_rating} | ratings: {ratings}". \
            format(title=self.title, isbn=self.isbn, avg_rating=self.get_average_rating(), ratings=self.ratings)


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author} | average rating:{avg_rating} | ratings: {ratings}". \
            format(title=self.title, author=self.author, avg_rating=self.get_average_rating(), ratings=self.ratings)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = str(subject)
        self.level = str(level)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject} | average rating:{avg_rating} | ratings: {ratings}". \
            format(title=self.title, level=self.level, subject=self.subject, avg_rating=self.get_average_rating(),
                   ratings=self.ratings)
