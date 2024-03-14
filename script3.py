import requests

def get_book_title(isbn_list):

    for isbn in isbn_list:
        api_url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                if data['totalItems'] >= 1:
                    title = data['items'][0]['volumeInfo']['title']
                    print(f'The book with ISBN: {isbn} is named "{title}"')
        except Exception as error:
            print(f"Error: {error}")


isbn_list = [9780141036144,

9780099518471,

9780099560432,

9781784971571]


get_book_title(isbn_list)