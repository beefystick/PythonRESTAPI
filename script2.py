import requests

def get_book_title(isbn):
    
    api_url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data['totalItems'] >= 1:
                title = data['items'][0]['volumeInfo']['title']
                print(title)
    except Exception as error:
        print(f"Error: {error}")


isbn_number = 9780884271956
get_book_title(isbn_number)