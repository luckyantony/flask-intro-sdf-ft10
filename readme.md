<!-- Querying database -->
<!-- sql => structured query language -->
insert => adding new record
update
delete
select => SELECT * FROM database_name

all = []

<!-- flask-sqlalchemy methods -->
all => to get all records
filter
filter_by
delete
order_by
get
update
add


<!-- db instance -->
sesssion
add => adding new record
commit => to save changes

<!-- class Post:
   def __init__(self, post_title, post_content, id = None):
       self.post_title = post_title
       self.post_content = post_content
       self.id = id

post1 = Post('Travel', "The dubai trip was interesting") -->

serialize our data => formating our data so that it can be tranfered over the internet
json => data format that makes it easy to be transered over the internet

[<Post 1>] => we can not transfer this over the internet, what will is to convert it into a dictionary(serialize) then convert it into a json object

flask sqlalchemy relationship => one-to-one, one-to-many, many-to-many
seed our database
create our first endpoint(API)

{
    "id" : 1,
    "post_title": "weather",
    "post_content": "It's rainy today"
}
<!-- SerializerMixin -->
to_dict()
serialize_rule

<!-- serializing relationship -->
user=> user-posts