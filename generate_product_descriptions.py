import requests

HEMINGWAI_API_KEY = 'SIGNUP_AT_TEXTCORTEX_TO_GET_YOUR_KEY'
HEMINGWAI_GATEWAY = 'https://api.textcortex.com/hemingwai/generate_text'


def generate_product_descriptions(product_title, features, brand_name, product_category, character_length, creativity,
                                  source_language, n_gen):
    """
    :param product_title: What is the title of the product that you are selling?
    :param features: What features does your product have? This can be left empty if you don't have enough data
    :param brand_name: What is the name of the brand?
    :param product_category: What is the category of the product that you are selling?
    :param character_length: Defines the length of generated meta descriptions
    :param creativity: A number between 0 and 1. 0 is the lowest creativity, 1 is the highest.
    :param source_language: Use 'en' for English, for other languages use the correct language code
    :param n_gen: Defines how many alternatives will be generated.
    :return:
    """
    try:
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {
            "prompt": product_title,
            "category": "Product Description",
            "parameters": f"Category: [{product_category}] Brand: {brand_name} Features: {features}",
            "character_count": character_length,
            "source_language": source_language,
            "creativity": creativity, # Sets creativity, number between 0 and 1. Default is 0.65
            "api_key": HEMINGWAI_API_KEY,
            "n_gen": n_gen
        }
        req = requests.post(HEMINGWAI_GATEWAY, json=data, headers=headers)
        if req.status_code == 403:
            print('API Key is wrong')
            return
        if req.status_code == 402:
            print('Reached API Limits, increase limits by contacting us at dev@textcortex.com or upgrade your account')
            return
        return req.json()['ai_results']
    except Exception as e:
        print(e)
        print('An error occured while making the request')


response = generate_product_descriptions(product_title='Cat Grooming Set', brand_name='Paw Power',
                                         features="'Ultra soft', 'Material: recycled Plastic'",
                                         product_category='Pet Supplies', character_length=300,
                                         creativity=0.7, source_language='en', n_gen=2)
# Response includes rich data with focus keywords in it, let's check out the results
i = 1
for row in response:
    print("Generated Text " + str(i) + ": " + row['generated_text'])
    i += 1