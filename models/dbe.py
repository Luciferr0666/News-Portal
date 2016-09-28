# -*- coding: utf-8 -*-
db.define_table('category',
                Field('name',requires=IS_NOT_EMPTY()),
                format='%(name)s'
                
                )
db.category.name.requires = IS_NOT_IN_DB(db, db.category.name) 

db.define_table('news',
                Field('heading','string', requires=IS_UPPER()),
                Field('tagline','string',requires=IS_NOT_EMPTY()),
                Field('description','string',requires=IS_NOT_EMPTY()),
                Field('category', 'list:string' ),
                Field('article_body','text',requires=IS_NOT_EMPTY()),
                Field('article_footer','text',requires=IS_NOT_EMPTY()),
                Field('tag', 'string', requires=IS_NOT_EMPTY()),
                Field('rating','integer',default=100,readable=False,writable=False),
                Field('picture','upload'),
                Field('caption','string',requires=IS_NOT_EMPTY()),
                Field('Youtube','string'),
                Field('pic_1', 'upload'),
                Field('pic_2','upload'),
                Field('pic_3','upload'),
                Field('likes','integer',default=0,readable=False,writable=False),
                Field('dislikes','integer',default=0,readable=False,writable=False),
                auth.signature
                )
db.define_table('blog_comment',
                Field('news', 'reference news'),
                Field('Comments','text',requires=IS_NOT_EMPTY()),
                auth.signature
                )

db.define_table('ownership',
                Field('news','reference news'),
                Field('category', 'reference category')
                )
db.news.category.requires = IS_IN_SET(('Politics', 'Entertainment','Sports', 'Business', 'Technology'), multiple=True)


db.define_table('tags',
                Field('giventag','string'),
                Field('refcategory','string'),
                Field('linkid','integer')
                )
