# -*- coding: utf-8 -*-
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import yaml


class WP_Poster:
    def __init__(self, login_yml):
        ## -----*----- コンストラクタ -----*----- ##
        self.wp_login = yaml.load(open(login_yml), Loader=yaml.SafeLoader)


    def post_article(self, title, content, photo=None, post_type=None, post_status='publish'):
        ## -----*----- 記事を投稿 -----*----- ##
        client = Client(self.wp_login['url'],
                        self.wp_login['username'],
                        self.wp_login['password']
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
        if post_type != None: post.post_type = post_type
        if photo != None: post.thumbnail = attachment_id

        # 送信
        client.call(posts.NewPost(post))
