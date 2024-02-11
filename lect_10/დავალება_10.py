'''
დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის გამოყენებით "https://fakestoreapi.com/products" მისამართზე,
შეამოწმებს სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:

'''

# ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები
# ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ
# გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით
# დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით


import requests

def get_products():
    try:
        api_url = "https://fakestoreapi.com/products"
        response = requests.get(api_url)

        if response.status_code != 200:
            print(f'ERROR: cant get data. Status: {response.status_code}')
            return False

        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"ERROR: {http_err}")
    except requests.exceptions.ConnectionError as con_err:
        print(f"Connection error: {con_err}")
    except Exception as err:
        print("Something wrong! {err}")

def parse_data():
    products = get_products()

    products_price = []
    products_category = []
    products_description = []
    products_rating = []
    

    for product in products:

        products_price.append(product['price'])
        min_price = min(products_price)
        max_price = max(products_price)
        avg_price = sum(products_price)/len(products_price)

        if product['category'] not in products_category:
            products_category.append(product['category'])
        products_category.sort()

        products_description.append({'id': product['id'], 'title': product['title']})
        products_description.sort(key = lambda x: x['title'])

        products_rating.append(product['rating'])
        products_rating.sort(key = lambda x: x['rate'])

    print(f"Minimum price: {min_price},\nMaximum price: {max_price},\nAverage price: {avg_price}\n")
    print(f"Sorted category list: {products_category}\n")
    print(f"Sorted product description: {products_description}\n")
    print(f"Sorted products rating: {products_rating}\n")

parse_data()