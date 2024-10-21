import httpx
import time
import os
import data


def get_comments() -> list:
    comments_list: list[dict] = []  
    dados = {'fields': 'comments.limit(100)', 'limit': '100', 'access_token': data.FB_TOKEN}

    try:
        retries = 0
        max_retries = 5
        while retries < max_retries:
            response = httpx.get(f'{data.fb_url}/{os.environ.get("PAGE_ID")}/posts', params=dados, timeout=10)

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
                print(f"Error module comments: status_code != 200 {response.status_code}")
                          
            time.sleep(2) # Wait for 2 seconds before making the next request

        if retries == max_retries:
            print("Error module comments: Failed to get comments after maximum retries")

    except httpx._exceptions as e:
        print(f"Error module comments: {e}")

    return comments_list

