from techtest.models.article import Article
from techtest.models.region import Region
from techtest.models.author import Author
from techtest.connector import engine, BaseModel, db_session

BaseModel.metadata.create_all(engine)

with db_session() as session:
    au = Region(code='AU', name='Australia')
    uk = Region(code='UK', name='United Kingdom')
    us = Region(code='US', name='United States of America')
    author1 = Author(first_name='Agatha', last_name='Christie')
    author2 = Author(first_name='J.R.R', last_name='Tolkien')

    session.add_all([
        au,
        uk,
        us,
        Article(
            title='Post 1',
            content='This is a post body',
            regions=[au, uk],
            authors=[author1]
        ),
        Article(
            title='Post 2',
            content='This is the second post body',
            regions=[au, us],
            authors=[author2, author1]
        )
    ])
