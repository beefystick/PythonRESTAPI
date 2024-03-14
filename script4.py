import requests

def get_author_info():
    author = input("What author would you like to look into? :")
    
    api_url = f'https://www.googleapis.com/books/v1/volumes?q=author:{author}'
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data['totalItems'] >= 1:
                totalitems = data['totalItems']
                print(f'{totalitems} matches for your query!')
                
                for item in data['items']:
                    book_id = item['id']
                    title = item['volumeInfo']['title']
                    isbn = item['volumeInfo']['industryIdentifiers'][0]['identifier']
                    print(f"Book ID: {book_id}\nTitle: {title}\nISBN: {isbn}\n")

    except Exception as error:
        print(f"Error: {error}")



get_author_info()