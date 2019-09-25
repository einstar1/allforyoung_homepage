from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User


def create_category(name='대외활동', description=''):
    category, is_created = Category.objects.get_or_create(
        name=name,
        description=description,
    )

    return category

def create_post(title, organization, author, category=None):
        blog_post = Post.objects.create(
            title=title,
            organization=organization,
            birthline=birthline,
            deadline=timezone.now(),
            link=link,
            author=author,
            created=timezone.now(),
            updated=timezone.now(),
        )

        return blog_post

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.author_000 = User.objects.create(username='westline', password='nopassword')
    
    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content,'html.parser')
        title = soup.title

        self.assertEqual(title.text, '대외활동의 모든 것')
        
        menu = soup.find('section', id='menu')
        self.assertIn('전체', menu.text)
        self.assertIn('대외활동', menu.text)
        self.assertIn('동아리', menu.text)

class TestModel(TestCase):
    def setUp(self):
        self.client = Client()
        self.author_000 = User.objects.create(username='westline', password='nopassword')

    def test_category(self):
        category = create_category()


    #def test_post(self): 
        
        #post_000 = create.post(
            #title='The first post',
            #organization='SK',
            #birthline='2019-05-01',
            #deadline=timezone.now(),
            #link='www.naver.com',
            #author=self.author_000,
            #created=timezone.now(),
            #updated=timezone.now(),
        #)