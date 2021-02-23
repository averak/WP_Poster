# -*- coding: utf-8 -*-
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts


class WP_Poster:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def post_article(self, title, content, photo=None, post_type=None, post_status='publish'):
        ## -----*----- 記事を投稿 -----*----- ##
        client = Client(self.url,
                        self.username,
                        self.password
                        )

        # 画像投稿
        if photo != None:
            data = {
                'name': photo.split('/')[-1],
                'type': 'image/png',
            }
            with open(photo, 'rb') as img:
                data['bits'] = xmlrpc_client.Binary(img.read())

            response = client.call(media.UploadFile(data))
            attachment_id = response['id']

        # 記事投稿
        post = WordPressPost()
        post.title = title
        post.content = content
        post.post_status = post_status
        if post_type != None:
            post.post_type = post_type
        if photo != None:
            post.thumbnail = attachment_id

        # 送信
        client.call(posts.NewPost(post))
