# -*- coding: utf-8 -*-
from neighbour.extensions import db
from neighbour.utils.database import CRUDMixin

# 商品
class Product(db.Model, CRUDMixin):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.TEXT)
    orginal_price = db.Column(db.DECIMAL)
    team_buying_price = db.Column(db.DECIMAL)
    category = db.Column(db.Integer)
    status = db.Column(db.SMALLINT)
    create_time = db.Column(db.Integer)

    # one-to-many
    images = db.relationship('ProductImage',
                             backref='product',
                             primaryjoin='ProductImage.product_id == Product.id',
                             cascade='all, ')

# 商品图片
class ProductImage(db.Model, CRUDMixin):
    __tablename__ = 'product_img'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id))
    img_url = db.Column(db.String(512))
    order = db.Column(db.SmallInteger)



if __name__ == '__main__':
    res = db.create_all()
    print res