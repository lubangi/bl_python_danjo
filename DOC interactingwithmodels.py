# (my_env) lionnel@LIONNELs-MacBook-Pro blog_directory % python3 manage.py shell
# Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from blog.models import Post
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# ModuleNotFoundError: No module named 'blog'
# >>> from blogapp.models import Post
# >>> Post.Status.choices
# [('DF', 'Draft'), ('PB', 'Published')]
# >>> Post.Status.labels
# ['Draft', 'Published']
# >>> Post.Status.values
# ['DF', 'PB']
# >>> Post.status.names
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'DeferredAttribute' object has no attribute 'names'
# >>> Post.Status.names
# ['DRAFT', 'PUBLISHED']
# >>> 