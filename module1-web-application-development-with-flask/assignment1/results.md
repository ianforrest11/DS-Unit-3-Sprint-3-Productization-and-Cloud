>>> DB.session.commit()

>>> quer = User.query.filter(User.name == 'ian').first()

>>> quer
<USER ian>

>>> quer.name
'ian'

>>> quer.id
1

>>> quer.tweets
[<TWEET hi>, <TWEET hi>, <TWEET hi>]

>>> quer2 = User.query.filter(User.name == 'ian2').first()

>>> quer2
<USER ian2>

>>> quer2.name
'ian2'

>>> quer2.id
2

>>> quer2.tweets
[<TWEET hi>, <TWEET hi>, <TWEET hi>]
