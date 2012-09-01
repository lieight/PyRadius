#autogenerated by sqlautocode

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation

engine = create_engine('mysql://root:root@localhost/pyradius?charset=utf8',echo=True)
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata
metadata.bind = engine

class RadArea(DeclarativeBase):
    __tablename__ = 'rad_area'

    __table_args__ = {}

    #column definitions
    area_id = Column(u'area_id', VARCHAR(length=10), primary_key=True, nullable=False)
    area_name = Column(u'area_name', VARCHAR(length=64), nullable=False)
    node_id = Column(u'node_id', VARCHAR(length=32), primary_key=True, nullable=False)

    #relation definitions


class RadCommunity(DeclarativeBase):
    __tablename__ = 'rad_community'

    __table_args__ = {}

    #column definitions
    area_id = Column(u'area_id', VARCHAR(length=10), primary_key=True, nullable=False)
    community_id = Column(u'community_id', VARCHAR(length=10), primary_key=True, nullable=False)
    community_name = Column(u'community_name', VARCHAR(length=64), nullable=False)
    node_id = Column(u'node_id', VARCHAR(length=32), primary_key=True, nullable=False)

    #relation definitions


class RadNas(DeclarativeBase):
    __tablename__ = 'rad_nas'

    __table_args__ = {}

    #column definitions
    acct_secret = Column(u'acct_secret', VARCHAR(length=31), nullable=False)
    auth_secret = Column(u'auth_secret', VARCHAR(length=31), nullable=False)
    id = Column(u'id', VARCHAR(length=32), primary_key=True, nullable=False)
    ip_addr = Column(u'ip_addr', VARCHAR(length=15), nullable=False)
    name = Column(u'name', VARCHAR(length=64), nullable=False)
    status = Column(u'status', INTEGER(), nullable=False)
    time_type = Column(u'time_type', INTEGER(), nullable=False)
    vendor_id = Column(u'vendor_id', INTEGER(), nullable=False)

    #relation definitions


class RadNasNode(DeclarativeBase):
    __tablename__ = 'rad_nas_node'

    __table_args__ = {}

    #column definitions
    ip_addr = Column(u'ip_addr', VARCHAR(length=15), primary_key=True, nullable=False)
    node_id = Column(u'node_id', VARCHAR(length=32), primary_key=True, nullable=False)

    #relation definitions


class RadNode(DeclarativeBase):
    __tablename__ = 'rad_node'

    __table_args__ = {}

    #column definitions
    desc = Column(u'desc', VARCHAR(length=255))
    id = Column(u'id', VARCHAR(length=32), primary_key=True, nullable=False)
    name = Column(u'name', VARCHAR(length=64), nullable=False)

    #relation definitions


class RadOpr(DeclarativeBase):
    __tablename__ = 'rad_opr'

    __table_args__ = {}

    #column definitions
    id = Column(u'id', VARCHAR(length=32), primary_key=True, nullable=False)
    ip_addr = Column(u'ip_addr', VARCHAR(length=15))
    name = Column(u'name', VARCHAR(length=64))
    node_id = Column(u'node_id', VARCHAR(length=32), nullable=False)
    password = Column(u'password', VARCHAR(length=32), nullable=False)
    status = Column(u'status', INTEGER(), nullable=False)
    type = Column(u'type', INTEGER(), nullable=False)

    #relation definitions


class RadOprLog(DeclarativeBase):
    __tablename__ = 'rad_opr_log'

    __table_args__ = {}

    #column definitions
    id = Column(u'id', VARCHAR(length=32), primary_key=True, nullable=False)
    ip_addr = Column(u'ip_addr', VARCHAR(length=15), nullable=False)
    log_desc = Column(u'log_desc', VARCHAR(length=1000))
    log_time = Column(u'log_time', VARCHAR(length=19), nullable=False)
    node_id = Column(u'node_id', VARCHAR(length=32), nullable=False)
    opr_id = Column(u'opr_id', VARCHAR(length=32), nullable=False)
    user_id = Column(u'user_id', VARCHAR(length=32))

    #relation definitions


class RadProduct(DeclarativeBase):
    __tablename__ = 'rad_product'

    __table_args__ = {}

    #column definitions
    bandwidth_code = Column(u'bandwidth_code', VARCHAR(length=32))
    bind_mac = Column(u'bind_mac', INTEGER(), nullable=False)
    bind_vlan = Column(u'bind_vlan', INTEGER(), nullable=False)
    concur_number = Column(u'concur_number', INTEGER(), nullable=False)
    domain_code = Column(u'domain_code', VARCHAR(length=32))
    fee_num = Column(u'fee_num', INTEGER(), nullable=False)
    fee_price = Column(u'fee_price', INTEGER(), nullable=False)
    id = Column(u'id', VARCHAR(length=16), primary_key=True, nullable=False)
    input_max_limit = Column(u'input_max_limit', INTEGER(), nullable=False)
    input_rate_code = Column(u'input_rate_code', VARCHAR(length=32))
    name = Column(u'name', VARCHAR(length=64), nullable=False)
    node_id = Column(u'node_id', VARCHAR(length=32), nullable=False)
    output_max_limit = Column(u'output_max_limit', INTEGER(), nullable=False)
    output_rate_code = Column(u'output_rate_code', VARCHAR(length=32))
    policy = Column(u'policy', INTEGER(), nullable=False)
    status = Column(u'status', INTEGER(), nullable=False)

    #relation definitions


class RadRoster(DeclarativeBase):
    __tablename__ = 'rad_roster'

    __table_args__ = {}

    #column definitions
    begin_time = Column(u'begin_time', VARCHAR(length=19), nullable=False)
    end_time = Column(u'end_time', VARCHAR(length=19), nullable=False)
    id = Column(u'id', VARCHAR(length=32), primary_key=True, nullable=False)
    mac_addr = Column(u'mac_addr', VARCHAR(length=17), nullable=False)
    node_id = Column(u'node_id', VARCHAR(length=32), nullable=False)
    type = Column(u'type', INTEGER(), nullable=False)
    user_name = Column(u'user_name', VARCHAR(length=32))

    #relation definitions


class RadUser(DeclarativeBase):
    __tablename__ = 'rad_user'

    __table_args__ = {}

    #column definitions
    area_id = Column(u'area_id', VARCHAR(length=32), nullable=False)
    auth_begin_date = Column(u'auth_begin_date', VARCHAR(length=10), nullable=False)
    auth_end_date = Column(u'auth_end_date', VARCHAR(length=10), nullable=False)
    balance = Column(u'balance', INTEGER(), nullable=False)
    basic_fee = Column(u'basic_fee', INTEGER(), nullable=False)
    community_id = Column(u'community_id', VARCHAR(length=32), nullable=False)
    create_time = Column(u'create_time', VARCHAR(length=19), nullable=False)
    domain_code = Column(u'domain_code', VARCHAR(length=6))
    id = Column(u'id', VARCHAR(length=32), primary_key=True, nullable=False)
    idcard = Column(u'idcard', VARCHAR(length=32))
    install_address = Column(u'install_address', VARCHAR(length=128), nullable=False)
    ip_address = Column(u'ip_address', VARCHAR(length=15))
    mac_addr = Column(u'mac_addr', VARCHAR(length=17))
    mobile = Column(u'mobile', VARCHAR(length=32))
    node_id = Column(u'node_id', VARCHAR(length=32), nullable=False)
    opr_id = Column(u'opr_id', VARCHAR(length=32))
    password = Column(u'password', VARCHAR(length=64), nullable=False)
    product_id = Column(u'product_id', VARCHAR(length=16), nullable=False)
    salesman_code = Column(u'salesman_code', VARCHAR(length=10))
    status = Column(u'status', INTEGER(), nullable=False)
    time_length = Column(u'time_length', INTEGER(), nullable=False)
    user_cname = Column(u'user_cname', VARCHAR(length=64), nullable=False)
    user_concur_number = Column(u'user_concur_number', INTEGER(), nullable=False)
    user_control = Column(u'user_control', INTEGER(), nullable=False)
    user_desc = Column(u'user_desc', VARCHAR(length=128))
    user_mac = Column(u'user_mac', INTEGER(), nullable=False)
    user_name = Column(u'user_name', VARCHAR(length=32), nullable=False)
    user_vlan = Column(u'user_vlan', INTEGER(), nullable=False)
    vlan_id = Column(u'vlan_id', INTEGER())
    vlan_id2 = Column(u'vlan_id2', INTEGER())

    #relation definitions


class RadUserAcct(DeclarativeBase):
    __tablename__ = 'rad_user_acct'

    __table_args__ = {}

    #column definitions
    acct_fee = Column(u'acct_fee', INTEGER(), nullable=False)
    acct_session_time = Column(u'acct_session_time', INTEGER(), nullable=False)
    acct_start_time = Column(u'acct_start_time', VARCHAR(length=19), nullable=False)
    acct_stop_time = Column(u'acct_stop_time', VARCHAR(length=19), nullable=False)
    acct_time = Column(u'acct_time', VARCHAR(length=19), nullable=False)
    actual_fee = Column(u'actual_fee', INTEGER(), nullable=False)
    id = Column(u'id', VARCHAR(length=32), primary_key=True, nullable=False)
    is_deduct = Column(u'is_deduct', INTEGER(), nullable=False)
    node_id = Column(u'node_id', VARCHAR(length=32), nullable=False)
    user_id = Column(u'user_id', VARCHAR(length=32), nullable=False)

    #relation definitions


class RadUserBill(DeclarativeBase):
    __tablename__ = 'rad_user_bill'

    __table_args__ = {}

    #column definitions
    bill_desc = Column(u'bill_desc', VARCHAR(length=512), nullable=False)
    bill_time = Column(u'bill_time', VARCHAR(length=19), nullable=False)
    fee_type = Column(u'fee_type', INTEGER(), nullable=False)
    fee_value = Column(u'fee_value', INTEGER(), nullable=False)
    id = Column(u'id', VARCHAR(length=32), primary_key=True, nullable=False)
    node_id = Column(u'node_id', VARCHAR(length=32), nullable=False)
    opr_id = Column(u'opr_id', VARCHAR(length=32), nullable=False)
    status = Column(u'status', INTEGER(), nullable=False)
    user_id = Column(u'user_id', VARCHAR(length=32), nullable=False)

    #relation definitions


class RadUserOrder(DeclarativeBase):
    __tablename__ = 'rad_user_order'

    __table_args__ = {}

    #column definitions
    auth_begin_date = Column(u'auth_begin_date', VARCHAR(length=10), nullable=False)
    auth_end_date = Column(u'auth_end_date', VARCHAR(length=10), nullable=False)
    id = Column(u'id', VARCHAR(length=32), primary_key=True, nullable=False)
    operate_time = Column(u'operate_time', VARCHAR(length=19), nullable=False)
    product_id = Column(u'product_id', VARCHAR(length=16), nullable=False)
    user_name = Column(u'user_name', VARCHAR(length=32), nullable=False)

    #relation definitions


