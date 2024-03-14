import requests
import yaml

def get_book_info(isbn_list):
    books_data = []
    for isbn in isbn_list:
        api_url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
        try:
            response = requests.get(api_url)
            
            if response.status_code == 200:
                data = response.json()
                
                if data['totalItems'] >= 1:
                    for item in data['items']:
                        book_info = {}

                        book_info['id'] = item['id']
                        book_info['title'] = item['volumeInfo']['title']
                        book_info['isbn'] = item['volumeInfo']['industryIdentifiers'][0]['identifier']
                        
                        if 'pageCount' in item['volumeInfo']:
                            book_info['pages'] = item['volumeInfo']['pageCount']
                        else:
                            book_info['pages'] = "N/A"
                        
                        books_data.append(book_info)

        except Exception as error:
            print(f"Error: {error}")
    
    with open('data.yml', 'w') as outfile:
        yaml.dump(books_data, outfile, default_flow_style=False, sort_keys=False)


isbn_list = [9780141036144,
9780099518471,
9780099560432,
9781784971571,
9780884271956]

get_book_info(isbn_list)