import httpx
from time import sleep
from os import environ
from data import fb_url, FB_TOKEN


def get_comments() -> list:
    comments_list = []  
    dados = {'fields': 'comments.limit(100)', 'limit': '100', 'access_token': FB_TOKEN}

    try:
        retries = 0
        while retries < 5:
            response = httpx.get(f'{fb_url}/{environ.get("PAGE_ID")}/posts', params=dados, timeout=10)

            if response.status_code == 200:
                response_data = response.json()
                for item in response_data.get('data', []):
                    comments_data = item.get('comments', {}).get('data', [])
                    if len(comments_data) >= 1:
                        for comment in comments_data:
                            if 'id' in comment:
                                comments_list.append({'comment': comment['message'], 'id': comment['id']})
            
                # Check for pagination
                if 'paging' in response_data and 'next' in response_data['paging']:
                    after = response_data['paging']['cursors'].get('after', '')
                    dados['after'] = after
                    retries += 1
                else:
                    break
            
            else:
                print(f"Failed to get posts: {response.status_code}")
                          
            sleep(1) # Wait for 1 seconds before making the next request

    except httpx._exceptions as e:
        print(f"Request error: {e}")

    return comments_list

