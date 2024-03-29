#u1 = User.objects.create(name = 'Shurik')
#u2 = User.objects.create(name = 'Pahan')
#a1 = Author.objects.create(user=u1)
#a2 = Author.objects.create(user=u2)
#c1 = Category.objects.create(name = 'Sports')
#c2 = Category.objects.create(name = 'Animals')
#c3 = Category.objects.create(name = 'Education')
#c4 = Category.objects.create(name = 'Healthy')
#p1 = Post.objects.create(news_type = 'AR',
#                          heading = 'Muscles up',
#                            text = 'Eat bananas pump muscles',
#                              author = a1)
#p2 = Post.objects.create(news_type = 'AR',
#                          heading = 'Riding horses',
#                            text = 'Eat bananas, ride a horses',
#                              author = a1)
#p3 = Post.objects.create(news_type = 'NW',
#                         heading = 'qq',
#                            text = 'Welcome to the club buddy',
#                             author = a2)
#p1.category.set('3')
#p1.category.add('2')
#p2.category.set('4')
#p2.category.add('1')
#p3.category.set('4')
#p3.category.add('3')
#Com 1 = Comment.objects.create(user = u1, text = 'qq guys', post = p1)
#Com 2 = Comment.objects.create(user = u2, text = 'hey', post = p2)
#Com 3 = Comment.objects.create(user = u2, text = 'nice post', post = p3)
#Com 4 = Comment.objects.create(user = u1, text = 'kekw', post = p4)
#p1.like()
#p2.dislike()
#p3.dislike()
#a1.rating_update()
#a2.rating_update()
#best = Author.objects.order_by('rating')
#postkek = Post.objects.all().values('like_rating', 'dislike_rating' ,'heading', 'time_in')
#best_post = Post.objects.order_by('like_rating').values("time_in", "heading",)
#ppp = Post.objects.all()[1]
#ppp.time_in
#ppp.text
#ppp.like_rating
#ppp.dislike_rating
#ppp.author.user