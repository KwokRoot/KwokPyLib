# pip install sqlalchemy

"""
Python orm 框架 `sqlalchemy` .
"""

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import registry
import json

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/test", echo=True)

# 建表
from sqlalchemy import orm, Column, Integer, String

Base = orm.declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer)

# Base.metadata.create_all(engine)


# # 增
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker(bind=engine)
# # 使用上下文管理器
# with Session() as session:
#     with session.begin():
#         new_user = User(name="Alice", age="18")
#         session.add(new_user)
#         session.commit()


# 查
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
with Session() as session:
    all = session.query(User).all()
    print([i.name for i in all])

    users = session.query(User)\
        .filter(
        User.name.like('Ali%'),  # 名字以"张"开头
        User.age > 16
    ).order_by(User.id.desc()).limit(1).all()
    print(users[0].name)


# 更
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# with Session() as session:
#     session.query(User).filter(User.id == 2).update({"name": "Bruce", "age": 20})
#     session.commit()


# # 删
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# with Session() as session:
#     user = session.query(User).order_by(User.id.desc()).first()
#     session.delete(user)
#     session.commit()


# # 实体类 映射 表对象 的方式 管理实体
# metadata = MetaData()
# user2Table = Table('users2', metadata,
#                      Column('id', Integer, primary_key=True, autoincrement=True),
#                      Column('name', String(200)),
#                      Column('age', Integer)
#                      )
#
# class User2(object):
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age
#
# # 1、创建注册表实例
# mapper_registry = registry()
# # 2、使用实例方法进行映射，类在前，表在后
# mapper_registry.map_imperatively(User2, user2Table)
# # 3、创建所有表
# metadata.create_all(engine)
#
# with Session() as session:
#     session.add(User2(None, "Alice", 20))
#     session.commit()
#
#     print(session.query(User2).count())
#     print(session.query(user2Table).count())

