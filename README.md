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

wp = WP_Poster('yaml file path')
wp.post_article('title', 'content', 'image path')
```

### Yaml Example
```yaml
url: https://your site/xmlrpc.php
username: your username
password: your password
```
