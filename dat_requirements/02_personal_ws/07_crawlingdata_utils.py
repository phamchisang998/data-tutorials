import csv, json, os, re, requests
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
    ,'price_comparison','specifications','categories','breadcrumbs'
]

def crawling_product(
    result_folder_path: str
    ,product_id: str
) -> list:
    """Get data of a product by provided product ID

    Args:
        result_folder_path (str): Directory save product data
        product_id (str): ID of product

    Returns:
        list: A list of categories URL
    """
    pass

def crawling_category(
    category_url: str
) -> list:
    """Get product IDs belong to provided category

    Args:
        category_url (str): The url of category

    Returns:
        list: A list of all product IDs of the category
    """
    pass

def crawling_process(
    begining_url: str
    ,result_folder_path: str
) -> None:
    """Main process to crawling data

    Args:
        begining_url (str): The entry url to get data of product
        result_folder_path (str): Directory to save the mined data
    """
    pass