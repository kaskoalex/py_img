import requests

img_url='https://www.papagai.de/tour-plan/img/slide-11.jpg'

def download_img(url=''):
    try:
        response = requests.get(url=url)
        
        with open('req1_img.jpg', 'wb') as file:
            file.write(response.content)
            
        return 'Img successfully downloaded!'    
      
    except Exception as _ex: 
        return 'Upps.... Check the URL' 
      
def main():
    print(download_img(url=img_url))  
    
main() 

img_url='https://www.papagai.de/tour-plan/img/slide-12.jpg'
main() 
 
    

    
    
           