import os
from dotenv import load_dotenv
from substack import Api
from substack.post import Post

load_dotenv()
api = Api(
    email=os.getenv("EMAIL"),
    password=os.getenv("PASSWORD"),
    publication_url=os.getenv("PUBLICATION_URL"),
)

print(os.getenv("EMAIL"))
print(os.getenv("USER_ID"))
post = Post(
    title="How to publish a Substack post using the Python API",
    subtitle="This post was published using the Python API",
    user_id=os.getenv("USER_ID")
)

post.add({'type': 'paragraph',
         'content': 'This is how you add a new paragraph to your post!'})

post.add({'type': 'heading',
         'content': 'I used the python-substack library!'})

post.add({'type': 'paragraph',
          'content': 'https://github.com/ma2za/python-substack'})

draft = api.post_draft(post.get_draft())

api.prepublish_draft(draft.get("id"))

api.publish_draft(draft.get("id"))

print('posted!')
