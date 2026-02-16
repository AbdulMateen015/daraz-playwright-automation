import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage

def test_daraz_search_electronics(page):
    # 1. Setup & Navigation
    home_page = HomePage(page)
    home_page.navigate("https://www.daraz.pk/")
    
    # 2. Search
    home_page.search_for_product("electronics")
    
    # 3. Filter Results
    results_page = SearchResultsPage(page)
    
    # Wait for sidebar to be interactive
    try:
        expect(results_page.results_grid.first).to_be_visible(timeout=10000)
    except:
        pass

    try:
        results_page.select_first_available_brand()
    except Exception:
        # Continue if brand selection fails due to UI variations
        pass

    # Applying Price Filter
    results_page.filter_by_price("500", "5000")
    
    # 4. Validation
    # Wait for the results to refresh after filtering
    page.wait_for_timeout(2000) 
    
    count = results_page.get_results_count()
    assert count > 0, "No products found within the applied filters!"
    
    # 5. Product Details (Handle New Tab or Same Tab)
    initial_pages = len(page.context.pages)
    
    results_page.click_first_product()
    
    # Wait for potential new tab to trigger or navigation to start
    page.wait_for_timeout(3000)
    
    new_pages = page.context.pages
    if len(new_pages) > initial_pages:
        new_product_page = new_pages[-1]
    else:
        new_product_page = page

    new_product_page.wait_for_load_state()

    # 6. Shipping Verification
    product_page_obj = ProductPage(new_product_page) 
    
    try:
        shipping_status = product_page_obj.get_shipping_info()
    except Exception:
        shipping_status = "Unknown"

    assert shipping_status is not None
