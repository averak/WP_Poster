WP-Poster
=========

Post articles to WordPress


## Requirement
- Python3
- python-wordpress-xmlrpc
- PyYAML


## Usage
### Simple Example
```python
from wp_poster import WP_Poster

wp = WP_Poster('url', 'username', 'password')
wp.post_article('title', 'content', 'image path')
```
