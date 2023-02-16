import requests, re, os, csv, json
from bs4 import BeautifulSoup

USER_AGENT = 'PostmanRuntime/7.29.2'
HEADER = {
    'User-Agent': USER_AGENT
}

HTML_URL = 'https://tiki.vn'
API_URL = 'https://tiki.vn/api/v2/products'

PRODUCT_ATTRIBUTES = [
    'id','master_id','sku','name','short_url'
    ,'type','short_description','price','list_price','original_price'
    ,'discount','discount_rate','rating_average','review_count','inventory_status'
    ,'inventory_type','productset_group_name','seller','has_buynow','day_ago_created'
    ,'all_time_quantity_sold','warranty_policy','authors','current_seller','other_sellers'
    ,'price_comparison','specifications','categories'
]

def request_data(url, headers, format):
    response = requests.get(url, headers=headers)
    results = response.content.decode()
    if format == 'json':
        return json.loads(results)
    elif format == 'bsoup':
        return BeautifulSoup(results, 'html.parser')
    else:
        raise Exception('Format not supported')


def getting_categories_products(data, product_attributes):
    if not isinstance(data, dict):
        raise Exception(
            'Only support for dictionary'
        )
    product_data = {key:value for key,value in data.items() if key in product_attributes}
    categories = data.get('breadcrumbs', [None])[:-1]
    return {
        'categories': categories
        ,'product':product_data
    }

def mining_categories(categories_products):
    categories = categories_products.get('categories').items()
    product = categories_products.get('product').items()
    for category in categories.items():
        yield category.get('url'), product|category.get('category_id'), category


def crawling_product(
    result_folder_path: str
    ,product_id:str
)->list:
    """Get data of a product by provided product ID

    Args:
        result_folder_path (str): Directory save product data
        product_id (str): ID of product, should be a string

    Returns:
        list: A list of categories URL
    """
    URL = f'{API_URL}/{product_id}'
    data = request_data(
        url=URL
        ,headers=HEADER
        ,format='json'
    )
    categories_products = getting_categories_products(
        data=data
        ,product_attributes=PRODUCT_ATTRIBUTES
    )

    mined_data_generator = mining_categories(categories_products)
    return mined_data_generator

def crawling_category(
    category_url: str
)->list:
    """Get product IDs of provided category

    Args:
        category_url (str): The url of category

    Returns:
        list: A list of all product IDs of the category
    """
    pass

def crawling_process(
    begining_url: str
    ,result_folder_path: str
)->None:
    """Main process to crawling data

    Args:
        begining_url (str): The entry url to get data of product
        result_folder_path (str): Directory save products data
    """
    pass

