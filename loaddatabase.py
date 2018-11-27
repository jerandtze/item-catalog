from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Base, BookItem, User

engine = create_engine('sqlite:///bookstoremenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Gerald Goh", email="hysteria81@gmail.com",
             picture='https://plus.google.com/u/0/photos/103754540034105626879/albums/profile/5731836629516512290')
session.add(User1)
session.commit()


# Menu for Crime
genre1 = Genre(user_id=1, title="Crime")

session.add(genre1)
session.commit()

bookItem1 = BookItem(user_id=1, title="A Dark So Deadly",
                     description="No.1 bestselling author of the Logan McRae series.",
                     price="$11.99", coverUrl="""http://goo.gl/v3ejVQ""",
                     author="Stuart MacBride", edition="hardcover", genre=genre1)

session.add(bookItem1)
session.commit()

bookItem2 = BookItem(user_id=1, title="Sweet Little Lies",
                     description="In 1998, Maryanne Doyle disappeared and Dad knew something about it?.",
                     price="$3.71", coverUrl="""http://goo.gl/VHdk5x""",
                     author="Caz Frear", edition="eBook", genre=genre1)

session.add(bookItem2)
session.commit()

bookItem3 = BookItem(user_id=1, title="Friend Request",
                     description="When Louise Williams receives a message from someone left long in the past.",
                     price="$13.49", coverUrl="""http://goo.gl/m5P1sm""",
                     author="Laura Marshall", edition="hardcover", genre=genre1)

session.add(bookItem3)
session.commit()

bookItem4 = BookItem(user_id=1, title="The Cruelest Cut",
                     description="The exciting novel that launched the Jack Murphy thriller series!",
                     price="$0.99", coverUrl="""http://goo.gl/3gdqBD""",
                     author="Rick Reed", edition="eBook", genre=genre1)

session.add(bookItem4)
session.commit()

bookItem5 = BookItem(user_id=1, title="The Furthest Station",
                     description="There's something going bump on the Metropolitan line.",
                     price="$13.59", coverUrl="""http://goo.gl/6N3ps1""",
                     author="Ben Aaronovitch", edition="hardcover", genre=genre1)

session.add(bookItem5)
session.commit()

bookItem6 = BookItem(user_id=1, title="Black Out",
                     description="As the Luftwaffe make their last desperate assault on the city.",
                     price="$3.99", coverUrl="""https://goo.gl/RUSSjK""",
                     author="John Lawton", edition="eBook", genre=genre1)

session.add(bookItem6)
session.commit()

bookItem7 = BookItem(user_id=1, title="Life of Lies",
                     description="Sahara Travis is used to being worshipped by adoring fans.",
                     price="$7.19", coverUrl="""https://goo.gl/VSKkRe""",
                     author="Sharon Sala", edition="hardcover", genre=genre1)

session.add(bookItem7)
session.commit()

bookItem8 = BookItem(user_id=1, title="Exquisite",
                     description="Enter Alice Dark, an aspiring writer who is drifting through life.",
                     price="$7.19", coverUrl="""https://goo.gl/9MWNdZ""",
                     author="Sarah Stovell", edition="hardcover", genre=genre1)

session.add(bookItem8)
session.commit()


# Menu for Drama
genre2 = Genre(user_id=1, title="Drama")

session.add(genre2)
session.commit()

bookItem1 = BookItem(user_id=1, title="Katharine Hepburn",
                     description="Katharine Hepburn was far more than an iconic movie star.",
                     price="$1.99", coverUrl="""https://goo.gl/nbVWXq""",
                     author="Grace May Carter", edition="eBook", genre=genre2)

session.add(bookItem1)
session.commit()

bookItem2 = BookItem(user_id=1, title="A Streetcar Named Desire",
                     description="Fading southern belle Blanche Dubois depends on the kindness of strangers.",
                     price="$11.09", coverUrl="""https://goo.gl/Jwft4A""",
                     author="Tennessee Williams", edition="hardcover", genre=genre2)

session.add(bookItem2)
session.commit()

bookItem3 = BookItem(user_id=1, title="Friend Request",
                     description="When Louise Williams receives a message from someone left long in the past.",
                     price="$13.49", coverUrl="""http://goo.gl/m5P1sm""",
                     author="Laura Marshall", edition="hardcover", genre=genre2)

session.add(bookItem3)
session.commit()

bookItem4 = BookItem(user_id=1, title="LES MISERABLES",
                     description="Les Miserables is an 1862 French novel by author Victor Hugo.",
                     price="$1.99", coverUrl="""https://goo.gl/fstvys""",
                     author="Victor Hugo", edition="eBook", genre=genre2)

session.add(bookItem4)
session.commit()

bookItem5 = BookItem(user_id=1, title="Glengarry Glen Ross",
                     description="David Mamet's scalding comedy is about small-time, cutthroat real esate salesmen.",
                     price="$10.69", coverUrl="""https://goo.gl/rvfvjz""",
                     author="David Mamet", edition="hardcover", genre=genre2)

session.add(bookItem5)
session.commit()

bookItem6 = BookItem(user_id=1, title="The Humans",
                     description="Erik Blake has brought his Pennsylvania family to celebrate Thanksgiving.",
                     price="$11.59", coverUrl="""https://goo.gl/AWqPoR""",
                     author="John Lawton", edition="hardcover", genre=genre2)

session.add(bookItem6)
session.commit()


# Menu for Horror
genre3 = Genre(user_id=1, title="Horror")

session.add(genre3)
session.commit()

bookItem1 = BookItem(user_id=1, title="The Night Parade",
                     description="David Arlen woke up one morning thinking that the worst was over.",
                     price="$10.39", coverUrl="""https://goo.gl/Yv2ajk""",
                     author="Ronald Malfi", edition="hardcover", genre=genre3)

session.add(bookItem1)
session.commit()

bookItem2 = BookItem(user_id=1, title="A Streetcar Named Desire",
                     description="Fading southern belle Blanche Dubois depends on the kindness of strangers.",
                     price="$11.09", coverUrl="""https://goo.gl/Jwft4A""",
                     author="Tennessee Williams", edition="hardcover", genre=genre3)

session.add(bookItem2)
session.commit()

bookItem3 = BookItem(user_id=1, title="Chills",
                     description="It begins with a freak snowstorm in May.",
                     price="$0.99", coverUrl="""https://goo.gl/n6R9U9""",
                     author="Mary SanGiovanni", edition="eBook", genre=genre3)

session.add(bookItem3)
session.commit()

bookItem4 = BookItem(user_id=1, title="The Ways We End",
                     description="Delve into the darkness and join us at the end of the world.",
                     price="$0.99", coverUrl="""https://goo.gl/oCkZSp""",
                     author="Ann Christy", edition="eBook", genre=genre3)


# Menu for Poetry
genre4 = Genre(user_id=1, title="Poetry")

session.add(genre4)
session.commit()

bookItem1 = BookItem(user_id=1, title="Milk and Honey",
                     description="The book is divided into four chapters, and each chapter serves a different purpose.",
                     price="$8.69", coverUrl="""https://goo.gl/ioR6sV""",
                     author="Rupi Kaur", edition="hardcover", genre=genre4)

session.add(bookItem1)
session.commit()

bookItem2 = BookItem(user_id=1, title="The Boy They Tried to Hide",
                     description="The true story of a son, forgotten by society.",
                     price="$9.89", coverUrl="""https://goo.gl/ozz3LM""",
                     author="Shane Dunphy", edition="hardcover", genre=genre4)

session.add(bookItem2)
session.commit()

bookItem3 = BookItem(user_id=1, title="Birdcall Morning",
                     description="Imagine if you left this world in 1994 and returned in 2011y.",
                     price="$1.00", coverUrl="""https://goo.gl/n6R9U9""",
                     author="Mary SanGiovanni", edition="eBook", genre=genre4)

session.add(bookItem3)
session.commit()

bookItem4 = BookItem(user_id=1, title="Mind Platter",
                     description="All that is on my mind, served on a silver platter.",
                     price="$15.79", coverUrl="""https://goo.gl/yZfQNj""",
                     author="Najwa Zebian", edition="hardcover", genre=genre4)

session.add(bookItem4)
session.commit()


# Menu for Thrillers
genre5 = Genre(user_id=1, title="Thrillers")

session.add(genre5)
session.commit()

bookItem1 = BookItem(user_id=1, title="The Mistake",
                     description="An unputdownable psychological thriller with a brilliant twist.",
                     price="$0.99", coverUrl="""https://goo.gl/ioR6sV""",
                     author="K.L. Slater", edition="eBook", genre=genre5)

session.add(bookItem1)
session.commit()

bookItem2 = BookItem(user_id=1, title="The Boy They Tried to Hide",
                     description="The true story of a son, forgotten by society.",
                     price="$9.89", coverUrl="""https://goo.gl/9TbZNm""",
                     author="Shane Dunphy", edition="hardcover", genre=genre5)

session.add(bookItem2)
session.commit()

bookItem3 = BookItem(user_id=1, title="The Surrogate",
                     description="A gripping psychological thriller with an incredible twist.",
                     price="$0.99", coverUrl="""https://goo.gl/XGEQkV""",
                     author="Louise Jensen", edition="eBook", genre=genre5)

session.add(bookItem3)
session.commit()

bookItem4 = BookItem(user_id=1, title="Cold Blood",
                     description="A gripping serial killer thriller that will take your breath away.",
                     price="$3.99", coverUrl="""https://goo.gl/R2bhQp""",
                     author="Robert Bryndza", edition="eBook", genre=genre5)

session.add(bookItem4)
session.commit()


# Menu for Economics
genre6 = Genre(user_id=1, title="Economics")

session.add(genre6)
session.commit()

bookItem1 = BookItem(user_id=1, title="Customers for Life",
                     description="How to Turn That One-Time Buyer Into a Lifetime Customer.",
                     price="$12.39", coverUrl="""https://goo.gl/bN28Nb""",
                     author="K.L. Slater", edition="hardcover", genre=genre6)

session.add(bookItem1)
session.commit()

bookItem2 = BookItem(user_id=1, title="Nudge",
                     description="Improving Decisions About Health, Wealth and Happiness.",
                     price="$11.99", coverUrl="""https://goo.gl/WVRW5S""",
                     author="Richard H Thaler", edition="hardcover", genre=genre6)

session.add(bookItem2)
session.commit()

bookItem3 = BookItem(user_id=1, title="Misbehaving",
                     description="The Making of Behavioural Economics.",
                     price="$11.09", coverUrl="""https://goo.gl/JEvq8d""",
                     author="Richard H Thaler", edition="hardcover", genre=genre6)

session.add(bookItem3)
session.commit()

bookItem4 = BookItem(user_id=1, title="WTF?",
                     description="What's the Future and Why It's Up to Us.",
                     price="$3.99", coverUrl="""https://goo.gl/BzYtm8""",
                     author="Tim O'Reilly", edition="eBook", genre=genre6)

session.add(bookItem4)
session.commit()


# Menu for Accounting
genre7 = Genre(user_id=1, title="Accounting")

session.add(genre7)
session.commit()

bookItem1 = BookItem(user_id=1, title="Customers for Life",
                     description="How to Turn That One-Time Buyer Into a Lifetime Customer.",
                     price="$12.39", coverUrl="""https://goo.gl/bN28Nb""",
                     author="K.L. Slater", edition="hardcover", genre=genre7)

session.add(bookItem1)
session.commit()

bookItem2 = BookItem(user_id=1, title="Nudge",
                     description="Improving Decisions About Health, Wealth and Happiness.",
                     price="$11.99", coverUrl="""https://goo.gl/WVRW5S""",
                     author="Richard H Thaler", edition="hardcover", genre=genre7)

session.add(bookItem2)
session.commit()

bookItem3 = BookItem(user_id=1, title="Misbehaving",
                     description="The Making of Behavioural Economics.",
                     price="$11.09", coverUrl="""https://goo.gl/JEvq8d""",
                     author="Richard H Thaler", edition="hardcover", genre=genre7)

session.add(bookItem3)
session.commit()

bookItem4 = BookItem(user_id=1, title="WTF?",
                     description="What's the Future and Why It's Up to Us.",
                     price="$3.99", coverUrl="""https://goo.gl/BzYtm8""",
                     author="Tim O'Reilly", edition="eBook", genre=genre7)

session.add(bookItem4)
session.commit()


# Menu for Fantasy
genre8 = Genre(user_id=1, title="Fantasy")

session.add(genre8)
session.commit()

bookItem1 = BookItem(user_id=1, title="The Witching Elm",
                     description="Sorcerer Tobias Corvin tumbles through a blizzard.",
                     price="$0.99", coverUrl="""https://goo.gl/T1jRir""",
                     author="C.N. Crawford", edition="eBook", genre=genre8)

session.add(bookItem1)
session.commit()

bookItem2 = BookItem(user_id=1, title="All the Crooked Saints",
                     description="Here is a thing everyone wants: A miracle.",
                     price="$11.99", coverUrl="""https://goo.gl/iE89b2""",
                     author="Maggie Stiefvater", edition="hardcover", genre=genre8)

session.add(bookItem2)
session.commit()

bookItem3 = BookItem(user_id=1, title="Into the Bright Unknown",
                     description="Leah Westfall journey has been one of ever-present peril.",
                     price="$15.59", coverUrl="""https://goo.gl/TwKtz5""",
                     author="Rae Carson", edition="hardcover", genre=genre8)

session.add(bookItem3)
session.commit()

bookItem4 = BookItem(user_id=1, title="The Consort",
                     description="Cyrene has no interest in destiny.",
                     price="$5.99", coverUrl="""https://goo.gl/J62Qob""",
                     author="K.A. Linde", edition="eBook", genre=genre8)

session.add(bookItem4)
session.commit()


print "added book items!"
