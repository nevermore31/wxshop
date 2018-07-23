from app import db

class shopping_cart(db.Model):
    '''
    购物车表
    '''
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user_base.id'),unique=True)   #用户/买家ID
    goods_sku_id = db.Column(db.Integer,db.ForeignKey('goods_sku.id'))   #商品SKU_ID
    count = db.Column(db.Integer,default=1)
    create_at = db.Column(db.DateTime)  # 信息创建时间
    update_at = db.Column(db.DateTime)  # 信息修改时间


class order_base(db.Model):
    '''
    订单基础表
    '''
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user_base.id'),unique=True)   #用户/买家ID
    coupon_id = db.Column(db.Integer,db.ForeignKey('coupon_id'))    #优惠券id
    order_num = db.Column(db.Integer,unique=True)     #订单号
    goods_price = db.Column(db.Float)    #订单所有商品总价
    transport_price = db.Column(db.Float)    #订单物流运费
    sum_price = db.Column(db.Float)     #订单总金额
    display = db.Column(db.Boolean)     #展示标识
    satisfaction = db.Column(db.SmallInteger,nullable=True)     #订单满意度,满分100分
    complaint = db.Column(db.String(255),nullable=True)     #订单投诉内容
    support_goods_service = db.Column(db.Boolean)   #支持售后标识,根据订单创建时间计算

    '''0:卖家代付款(订单生成),1:卖家待发货,2:买家待收货(发货完成),3:买家延迟收货,4:卖家确认收货未评价(订单完成)
       5:买家评论待回复,6买家评论已回复(订单评论回复完成),7:投诉订单,8售后待处理,9售后已处理(订单完成售后)'''
    status = db.Column(db.SmallInteger,default=0)   #订单状态
    create_at = db.Column(db.DateTime)  # 信息创建时间
    update_at = db.Column(db.DateTime)  # 信息修改时间

    order_goods = db.relationship('order_goods',backref='order_base',lazy='dynamic')
    order_log = db.relationship('order_log',backref='order_base',lazy='dynamic')
    order_pay = db.relationship('order_pay',backref='order_base',lazy='dynamic')
    order_transport = db.relationship('order_transport',backref='order_base',lazy='dynamic')


class order_goods(db.Model):
    '''
    订单商品表
    '''
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.Integer,default=0,index=True)   #订单ID
    goods_sku_id = db.Column(db.Integer,db.ForeignKey('goods_sku.id'))   #商品SKU_ID
    count = db.Column(db.SmallInteger)   #商品数量
    discount = db.Column(db.SmallInteger)   #商品折扣百分比
    unit_price = db.Column(db.Float)   #商品单价
    reduced_price = db.Column(db.Float)   #商品减少的价格
    sum_price = db.Column(db.Float)   #商品总价

    '''0:正常出售,1:投诉商品,2:换货商品,3:退货商品'''
    status = db.Column(db.SmallInteger)   #商品出售状态

    create_at = db.Column(db.DateTime)    #信息创建时间
    update_at = db.Column(db.DateTime)    #信息修改时间

    order_goods_comment = db.relationship('order_goods_comment',backref='order_goods',lazy='dynamic')
    order_goods_return = db.relationship('order_goods_return',backref = 'order_goods',lazy='dynacmi')
    order_goods_exchange = db.relationship('order_goods_exchange',backref = 'order_goods',lazy='dynacmi')


class order_log(db.Model):
    '''
    订单操作日志表
    '''
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.Integer,db.ForeignKey('order_base.id'))     #订单ID
    admin_id = db.Column(db.Integer,db.ForeignKey('admin_role.id'))     #操作管理员id
    status = db.Column(db.SmallInteger)     #订单状态
    remark =db.Column(db.String(255),nullable=True)     #备注
    create_at = db.Column(db.DateTime)  # 信息创建时间


class order_pay(db.Model):
    '''
    订单支付表
    '''
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.Integer,db.ForeignKey('order_base.id'))    #订单ID
    pay_price = db.Column(db.Float)     #支付金额
    pay_type = db.Column(db.SmallInteger)    #支付类型(暂时只支持微信支付)

    '''0:等待支付,1:支付失败,2:支付成功'''
    status = db.Column(db.SmallInteger)     #支付状态
    third_pay_num =db.Column(db.String(255),unique=True)     #第三方支付订单号
    create_at = db.Column(db.DateTime)  # 信息创建时间
    update_at = db.Column(db.DateTime)  # 信息修改时间

    order_pay_log = db.relationship('order_pay_log',backref='order_pay',lazy='dynamic')


class order_pay_log(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    pay_id = db.Column(db.Integer,db.ForeignKey('order_pay.id'))    #支付id
    status = db.Column(db.SmallInteger)     #订单状态
    remark = db.Column(db.String(255),nullable=True)    #日志备注
    create_at = db.Column(db.DateTime)  # 信息创建时间


class order_transport(db.Model):
    '''
    订单物流表
    '''
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.Integer,db.ForeignKey('order_base.id'),unique=True)    #订单ID
    buyer_name = db.Column(db.String(50))   #买家/收件人姓名
    buyer_mobile = db.Column(db.String(20))    #买家/收件人电话
    city_id = db.Column(db.Integer,db.ForeignKey('city.id'))    #省市ID
    address = db.Column(db.String(125))     #详细收货地址
    transport_company = db.Column(db.String(20))    #第三方物流公司
    transport_num = db.Column(db.String(125))   #第三方物流订单号
    create_at = db.Column(db.DateTime)  # 信息创建时间
    update_at = db.Column(db.DateTime)  # 信息修改时间
    last_edit_id = db.Column(db.Integer,db.ForeignKey('admin_role.id'),nullable=False)   #最后修改信息的管理员id


class city(db.Model):
    '''省市表'''
    id = db.Column(db.Integer,primary_key=True)
    country = db.Column(db.String(20),unique=True)   #国家
    province = db.Column(db.String(20),unique=True)  #省份
    city = db.Column(db.String(20),unique=True)      #城市
    create_at = db.Column(db.DateTime)  # 信息创建时间
    update_at = db.Column(db.DateTime)  # 信息修改时间
    last_edit_id = db.Column(db.Integer,db.ForeignKey('admin_role.id'),nullable=False)    #最后修改信息的管理员id

    order_transport = db.relationship('order_transport',backref='city.id',lazy='dynamic')


class order_goods_comment(db.Model):
    '''
    订单商品评价表
    '''
    id = db.Column(db.Integer,primary_key=True)
    order_goods_id = db.Column(db.Integer,db.ForeignKey('order_goods.id'))    #订单商品ID
    comment = db.Column(db.Text,nullable=True)  #评论内容
    reply_id = db.Column(db.Integer,index=True)    #递归
    admin_id = db.Column(db.Integer,db.ForeignKey('admin_role.id'),nullable=False)
    create_at = db.Column(db.DateTime)  # 信息创建时间
    update_at = db.Column(db.DateTime)  # 信息修改时间


class order_goods_return(db.Model):
    '''
    订货商品退货表
    '''
    id = db.Column(db.Integer,primary_key=True)
    order_goods_id = db.Column(db.Integer,db.ForeignKey('order_goods.id'))    #订单商品ID
    count = db.Column(db.Integer)  #退货商品数量
    unit_price = db.Column(db.Float)   #退货商品单价
    sum_price = db.Column(db.Float)    #退货商品总价
    reason = db.Column(db.Text,nullable=True)      #退货理由
    photos = db.Column(db.String(300),nullable=True)     #图片地址
    transport_price = db.Column(db.Float)     #客户发货运费

    '''0:退货申请待处理,1:退货确认待收货,2:收货确认待退款,3:退款完成'''
    status = db.Column(db.SmallInteger)   #退款状态
    create_at = db.Column(db.DateTime)  # 信息创建时间
    update_at = db.Column(db.DateTime)  # 信息修改时间

    order_goods_return_log = db.relationship('order_goods_return_log',backref='order_goods_return',lazy='dynamic')

class order_goods_return_log(db.Model):
    '''
    订单商品退货操作日志
    '''
    id = db.Column(db.Integer,primary_key=True)
    return_id = db.Column(db.Integer,db.ForeignKey('order_goods_return.id'))    #退货ID
    admin_id = db.Column(db.Integer,db.ForeignKey('admin_role.id'))        #管理员ID
    status = db.Column(db.SmallInteger)     #状态码
    remark = db.Column(db.Text,nullable=True)    #备注
    create_at = db.Column(db.DateTime)  # 信息创建时间


class order_goods_exchange(db.Model):
    '''
    订单商品换货表
    '''
    id = db.Column(db.Integer,primary_key=True)
    order_goods_id = db.Column(db.Integer,db.ForeignKey('order_goods.id'))    #订单商品ID
    count = db.Column(db.Integer)  #退货商品数量
    reason = db.Column(db.Text, nullable=True)  # 退货理由
    photos = db.Column(db.String(300), nullable=True)  # 图片地址
    transport_price = db.Column(db.Float)  # 客户发货运费

    '''0:换货申请待处理,1:换货确认待卖家收货,2:卖家收货确认待发货,3:卖家发货完成待买家确认收货,4:换货完成'''
    status = db.Column(db.SmallInteger)   #退款状态
    create_at = db.Column(db.DateTime)  # 信息创建时间
    update_at = db.Column(db.DateTime)  # 信息修改时间

    order_goods_exchange_log = db.relationship('order_goods_exchange_log',backref='order_goods_return',lazy='dynamic')


class order_goods_exchange_log(db.Model):
    '''订单商品换货操作日志'''
    id = db.Column(db.Integer, primary_key=True)
    return_id = db.Column(db.Integer, db.ForeignKey('order_goods_exchange.id'))  # 退货ID
    admin_id = db.Column(db.Integer, db.ForeignKey('admin_role.id'))  # 管理员ID
    status = db.Column(db.SmallInteger)  # 状态码
    remark = db.Column(db.Text, nullable=True)  # 备注
    create_at = db.Column(db.DateTime)  # 信息创建时间











