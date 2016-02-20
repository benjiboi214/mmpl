import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmpl.settings')

import django
django.setup()

from core.models import Post
from django.contrib.auth.models import User

def populate():
    
    add_post(
        username = 'ben',
        category = 'NE',
        title = 'Test Post, Please Ignore',
        body = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ultricies luctus magna, eget maximus enim suscipit quis. Maecenas non leo at ipsum pharetra fringilla. Praesent accumsan magna sed dolor molestie venenatis quis quis tellus. Phasellus quis augue vitae eros pellentesque dictum nec at lacus. In laoreet urna a hendrerit euismod. In vitae tincidunt ex. Proin porttitor rutrum justo, vel volutpat nunc tincidunt vel. Sed dignissim, dui consectetur efficitur commodo, metus leo pretium nunc, vel laoreet enim orci at sapien. Sed a aliquet velit, faucibus accumsan ante.',
        post_type = 'LG',
        hidden = False
    )
    
    add_post(
        username = 'ben',
        category = 'NE',
        title = 'Here is the second post',
        body = 'Maecenas vitae eleifend sem. Etiam quis rutrum tellus. Proin euismod, mauris vitae tempus egestas, tellus velit mattis purus, at viverra turpis ex sed purus. Donec at luctus leo. Sed posuere sit amet mi vitae iaculis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In consequat lectus sed ipsum tempus commodo. Etiam vitae finibus massa, eget egestas sem. Nam elit felis, facilisis a volutpat eget, fermentum vitae odio.',
        post_type = 'LG',
        hidden = False
    )
    
    add_post(
        username = 'ben',
        category = 'NE',
        title = 'Lastly, there is the third post, a little longer',
        body = '''Curabitur tortor tellus, feugiat vel placerat et, finibus tempus erat. Quisque aliquet nisi eu tellus mollis, a cursus velit faucibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Pellentesque lacinia sem auctor aliquet consequat. Nam eu nibh sit amet odio semper rhoncus. Curabitur condimentum maximus massa non ultrices. Etiam non magna sed eros tempor tempus. Cras nunc ligula, finibus sit amet dictum quis, pellentesque mattis tellus. Fusce faucibus fermentum tortor. Nunc consequat elementum interdum. Sed mattis malesuada augue eget tempor. Donec eu arcu vel erat tempor vehicula.

Nunc nec enim et neque dapibus tempor ac nec diam. Mauris quis efficitur quam, at efficitur dui. Etiam mattis aliquet posuere. Sed in blandit sem, non egestas leo. Curabitur pulvinar bibendum dolor eu mollis. Sed fermentum orci at quam condimentum fermentum. Ut et lectus sodales, posuere justo vitae, scelerisque dolor. Phasellus eu sagittis lorem, in varius elit. Nam vitae condimentum odio.''',
        post_type = 'SM',
        hidden = False
    )
    
    add_post(
        username = 'ben',
        category = 'NE',
        title = '2016 Winter Season Starting!',
        body = 'Join our friendly community to learn the art of poking balls with sticks',
        post_type = 'FE',
        hidden = False
    )
    
    add_post(
        username = 'ben',
        category = 'NE',
        title = 'Test Hidden Post',
        body = "Shouldn't see this at all.",
        post_type = 'LG',
        hidden = True
    )

def add_post(username, category, title, body, post_type, hidden):
    author = User.objects.get(username='%s' % username)
    p = Post.objects.get_or_create(author=author, title=title)[0]
    p.category = category
    p.body = body
    p.post_type = post_type
    p.hidden = hidden
    p.save()
    return p

if __name__ == '__main__':
    print "Running the Core DB population script"
    populate()