import boto3
import __future__ # print_function,  Python 2/3 compatibility
import datetime

from flask_dynamo import Dynamo
from flask import Flask
import flask_api
from flask import request
from flask_api import status, exceptions

# ==============================================================================================
# Method
# ==============================================================================================

def Create_Table(table_name, dynamodb_client, dynamodb_resource):
    myTable = dynamodb_client.create_table(
            
        TableName = table_name,

        AttributeDefinitions=[
            {
                'AttributeName': 'PostID',
                'AttributeType': 'N'
            }                        
        ],

        KeySchema=[
            {
                'AttributeName': 'PostID',
                'KeyType': 'HASH'

            },
        ],      #End KeySchema

        ProvisionedThroughput = {
            'ReadCapacityUnits': 100,
            'WriteCapacityUnits': 100,
        }
    )

    # Wait until the table exists.
    dynamodb_resource.meta.client.get_waiter('table_exists').wait(TableName=table_name)

def Delete_Table(table_name, dynamodb_resource):
    delTable = dynamodb_resource.Table(table_name)
    delTable.delete()

def List_All_Table(dynamodb_client):

    existing_tables = dynamodb_client.list_tables()['TableNames']
    return existing_tables

def Table_Status(table_name, dynamodb_resource):
    myTable = dynamodb_resource.Table(table_name)
    status = myTable.table_status
    return status
    
def Table_Length(table_name, dynamodb_resource):
    myTable = dynamodb_resource.Table(table_name)
    table_length = myTable.item_count
    return table_length

def Scan_Table (table_name, dynamodb_resource):
    all_posts = []
    myTable = dynamodb_resource.Table(table_name)

    scanResponse = myTable.scan(TableName=table_name)
    items = scanResponse['Items']
    items.sort()
    i = 0
    while i < len(items):
        all_posts.append (items[i])
        i += 1
    return all_posts

def Create_Post (table_name, dynamodb_resource, username, posttitle, content, community, urlresource):
    table_length = Table_Length(table_name, dynamodb_resource)
    if table_length == 0:
        last_PostID = 0
    else:
        all_Posts = Get_All_Posts(table_name, dynamodb_resource)
        last_PostID = 1

        for post in all_Posts:
            if post['PostID']> last_PostID:
                last_PostID = post['PostID']

    currentID = last_PostID + 1

    now = datetime.datetime.now()
    strNow = str(now)

    input_json = {
        'PostID'      : currentID, 
        'Username'    : username,
        'PostTitle'   : posttitle,
        'PostDate'    : strNow,
        'Content'     : content,
        'Community'   : community,
        'URLResource' : urlresource,
    }

    myTable = dynamodb_resource.Table(table_name)

    myTable.put_item(Item = input_json)
    return input_json

def Initial_Posts(table_name, dynamodb_resource):
    input_json = Create_Post (table_name, dynamodb_resource, 'User 001', 'Post Title 001', 'Content 001', 'school', 'www.URLResource001.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 002', 'Post Title 002', 'Content 002', 'home', 'www.URLResource002.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 003', 'Post Title 003', 'Content 003', 'workplace', 'www.URLResource003.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 004', 'Post Title 004', 'Content 004', 'school', 'www.URLResource004.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 005', 'Post Title 005', 'Content 005', 'home', 'www.URLResource005.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 006', 'Post Title 006', 'Content 006', 'workplace', 'www.URLResource006.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 007', 'Post Title 007', 'Content 007', 'school', 'www.URLResource007.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 008', 'Post Title 008', 'Content 008', 'home', 'www.URLResource008.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 009', 'Post Title 009', 'Content 009', 'workplace', 'www.URLResource009.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 010', 'Post Title 010', 'Content 010', 'school', 'www.URLResource010.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 011', 'Post Title 011', 'Content 011', 'home', 'www.URLResource011.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 012', 'Post Title 012', 'Content 012', 'workplace', 'www.URLResource012.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 013', 'Post Title 013', 'Content 013', 'school', 'www.URLResource013.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 014', 'Post Title 014', 'Content 014', 'home', 'www.URLResource014.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 015', 'Post Title 015', 'Content 015', 'workplace', 'www.URLResource015.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 016', 'Post Title 016', 'Content 016', 'school', 'www.URLResource016.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 017', 'Post Title 017', 'Content 017', 'home', 'www.URLResource017.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 018', 'Post Title 018', 'Content 018', 'workplace', 'www.URLResource018.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 019', 'Post Title 019', 'Content 019', 'school', 'www.URLResource019.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 020', 'Post Title 020', 'Content 020', 'home', 'www.URLResource020.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 021', 'Post Title 021', 'Content 021', 'workplace', 'www.URLResource021.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 022', 'Post Title 022', 'Content 022', 'school', 'www.URLResource022.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 023', 'Post Title 023', 'Content 023', 'home', 'www.URLResource023.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 024', 'Post Title 024', 'Content 024', 'workplace', 'www.URLResource024.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 025', 'Post Title 025', 'Content 025', 'school', 'www.URLResource025.com')
  

    
    
def Get_Post(table_name, dynamodb_resource, postID):
    try:
        myTable = dynamodb_resource.Table(table_name)

        get_post = myTable.get_item(
            Key = {'PostID':postID}
        )
        post = get_post['Item']
        return post
    except:
        print('Post is not exist')

def Get_All_Posts(table_name, dynamodb_resource):
    all_posts = []
    myTable = dynamodb_resource.Table(table_name)

    scanResponse = myTable.scan(TableName=table_name)
    items = scanResponse['Items']
    i = 0
    while i < len(items):
        all_posts.append (items[i])
        i += 1

    sorted_all_posts = sorted(all_posts, key=lambda k: k['PostID'])
    return sorted_all_posts

def Get_n_Recent_Posts(table_name, dynamodb_resource, n):
    allPosts = Get_All_Posts(table_name, dynamodb_resource)

    table_length = Table_Length(table_name, dynamodb_resource)
    run = table_length - 1
    n_recent_posts = []

    i = 0
    while i < n:
        try:
            n_recent_posts.append(allPosts[run])
            i += 1
            if run > 0:
                run -= 1
            else:
                break
        except:
            run -= 1

            pass
    return n_recent_posts

def Get_n_Recent_Posts_by_Community(table_name, dynamodb_resource, n, community):
    allPosts = Get_All_Posts(table_name, dynamodb_resource)

    table_length = Table_Length(table_name, dynamodb_resource)
    run = table_length - 1
    n_recent_posts_by_community = []

    i = 0
    while i < n:
        try:
            if allPosts[run]['Community'] == community:
                # print('Community = ', community)
                n_recent_posts_by_community.append(allPosts[run])
                i += 1

            if run > 0:
                run -= 1
            else:
                break
        except:
            i += 1
            pass
    # print('n_recent_posts_by_community = ',n_recent_posts_by_community)
    return n_recent_posts_by_community

def Update_Post(table_name, dynamodb_resource, postID, 
                username, posttitle, content, community, urlresource):

    myTable = dynamodb_resource.Table(table_name)

    now = datetime.datetime.now()
    strNow = str(now)

    myTable.update_item(
    Key={
        'PostID': postID,
    },
    UpdateExpression=
        'SET Username=:newusername, PostTitle=:newposttitle, PostDate=:newstrNow, Content=:newcontent, Community=:newcommunity, URLResource=:newurlresource',
    ExpressionAttributeValues={
        ':newusername'      : username,
        ':newposttitle'     : posttitle,
        ':newstrNow'        : strNow,
        ':newcontent'       : content,
        ':newcommunity'     : community,
        ':newurlresource'   : urlresource,
    }
    )

def Delete_Post(table_name, dynamodb_resource, postID):
    myTable = dynamodb_resource.Table(table_name)
    
    myTable.delete_item(
        Key= { 'PostID':postID }
    )

def Delete_All_Posts(table_name, dynamodb_resource):
    postID = 1
    while postID < 100:
        Delete_Post(table_name, dynamodb_resource, postID)
        postID += 1


# ==============================================================================================
# Start Program
# ==============================================================================================

app = flask_api.FlaskAPI(__name__)

table_name = "posts"

# Get the service client.
dynamodb_client = boto3.client('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")


# Get the service resource.
dynamodb_resource = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

app.config['DYNAMO_TABLES'] = [
    dict(
        TableName=table_name,
        KeySchema=[dict(AttributeName='PostID', KeyType='HASH')],
        AttributeDefinitions=[dict(AttributeName='PostID', AttributeType='N')],
        ProvisionedThroughput=dict(ReadCapacityUnits=100, WriteCapacityUnits=100)
    ), 
 ],
# print('app.config = ', app.config['DYNAMO_TABLES'])


@app.cli.command('init')
def init_db():
    print('Please wait until Initial Post Database is Done before runing service on browser')
    existing_tables = List_All_Table(dynamodb_client)

    if table_name in existing_tables:   # posts table exist -> do nothing
        Delete_All_Posts(table_name, dynamodb_resource)
        Delete_Table(table_name, dynamodb_resource)

    Create_Table(table_name, dynamodb_client, dynamodb_resource)

    # describeTable = dynamodb_client.describe_table(TableName=table_name)
    Initial_Posts(table_name, dynamodb_resource)
    print("Initial Post Database is DONE")

# ==============================================================================================
# Routing
# ==============================================================================================

@app.route('/', methods=['GET'])
def home():
    return '''
        <ul>
            <li>
                Display all posts: <br> 
                <a> http://localhost:5000/posts/all</a> 
            </li><br>

            <li>
                Delete post by PostID = 100: <br> 
                <a>http://localhost:5000/posts/delete/100</a> 
            </li><br>

            <li>
                Display post by PostID = 10: <br> 
                <a>http://localhost:5000/posts/10</a> 
            </li><br>

            <li>
                Display default 2 recent posts with create post <br>
                <a>http://localhost:5000/posts</a> <br>

                Please copy this Json structure <br>
                {"Username": "User 100", "PostTitle": "Post Title 100", "Content": "Content 100", "Community": "home", "URLResource": "www.URLResource100.com"}


            </li><br>
            <li>
                Display 15 recent post with create post <br>
                <a>http://localhost:5000/posts?n=15</a><br>

                Please copy this Json structure <br>
                {"Username": "User 100", "PostTitle": "Post Title 100", "Content": "Content 100", "Community": "home", "URLResource": "www.URLResource100.com"}

            </li><br>

            <li>
                Display 5 most recent post in school community <br>
                <a>http://localhost:5000/posts/school/5</a>
            </li>
            <li></li>
            <li></li>

        </ul>
      
        '''
    
    
# Get all posts
@app.route('/posts/all', methods=['GET'])
def all_posts():
    allPosts = Get_All_Posts(table_name, dynamodb_resource)
    return list(allPosts)


# Get post by PostID
@app.route('/posts/<int:PostID>', methods=['GET'])
def post_ID(PostID):

    try:
        post = Get_Post(table_name, dynamodb_resource, PostID)
        return post
    except:
        return '', status.HTTP_204_NO_CONTENT



# Get n recent post
@app.route('/posts', methods=['GET', 'POST'])
def n_recent_posts():
    if request.method == 'GET':
        n = request.args.get('n', 2)
        n = int(n)
        n_recent_posts = Get_n_Recent_Posts(table_name, dynamodb_resource, n)

        return list(n_recent_posts)

       
    print('='*20)
    if request.method == 'POST':
        Username = str(request.data.get('Username', ''))
        PostTitle   = str(request.data.get('PostTitle', ''))
        Content   = str(request.data.get('Content', ''))
        Community   = str(request.data.get('Community', ''))
        URLResource   = str(request.data.get('URLResource', ''))

        input_json = Create_Post (table_name, dynamodb_resource, Username, PostTitle, Content, Community, URLResource)
        return input_json

# Delete Post by PostID
@app.route('/posts/delete/<int:PostID>', methods=['GET', 'DELETE'])
def delete(PostID):
    if request.method == 'DELETE':

        Delete_Post(table_name, dynamodb_resource, PostID)

    else:
        return {'status': 'OK'}



# List the n most recent posts to a particular community
@app.route('/posts/<string:Community>/<int:n>', methods=['GET'])
def post_by_community(Community, n):
    print('Community = ', Community)
    print('n = ', n)
    
    n_recent_posts_by_community = Get_n_Recent_Posts_by_Community(table_name, dynamodb_resource, n, Community)

    return list(n_recent_posts_by_community)


