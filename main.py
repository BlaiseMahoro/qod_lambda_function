import requests
import constants


def get_qod():
    api_token = constants.QOD_API_TOKEN
    r = requests.get(constants.QOD_BASE_URL + 'qod.json?category=inspire&api_key=' + api_token)
    print(r.content)
    data = r.json()
    
    if r.status_code != 200:
        print(data['message'])
        error_msg = 'An error occured while calling ' + data['message']
        raise(error_msg)
    return data


def makeFileForQOD(contents):
    quote = contents['quotes'][0]
    print(quote)
    quote_id = quote['id']
    author = quote['author']
    quote_text = quote['quote']
    title = quote['title'] 
    file_name = 'file_' + quote_id + '.html'
    f = open(file_name, 'w')
  
    # the html code which will go in the file 
    html_template = f"""<html>
    <head>
    <title>{title}</title>
    <style>
   div{{
    background-image: url("https://picsum.photos/600");
    background-repeat: no-repeat;
    height:600px;
    width:600px;
    position:relative;
    margin: auto;
    padding: 10px;
    }}

    p{{
        background-color: rgba(248, 247, 216, 0.7);
        position: absolute;
        top: 0;
        left: 0;
        width: 600px;
        text-align: center;
        vertical-align: center;
        color: #111;font-family: 'Open Sans', sans-serif; 
        font-size: 18px; 
        font-weight: bold; 
        letter-spacing: -1px; 
        line-height: 1; 
        text-align: center;
        margin-top: 0px;
    }}


    body{{
        background-color: rgba(198, 198, 163, 0.667);
    }}
    </style>
    </head>
    <body>
    <h2 style="text-align: center;">{title}</h2>
    <div>
    <p>{quote_text} -- {author}</p>
    </div>
    
    </body>
    </html>
    """

    # writing the code into the file
    f.write(html_template)

    # close the file
    f.close()


def process():
   
    qod = get_qod()
 
    makeFileForQOD(qod['contents'])

process()

