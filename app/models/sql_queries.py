user="""
    CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY,
    username varchar (40) NOT NULL,
    password varchar(200) NOT NULL,
    is_admin BOOLEAN  DEFAULT TRUE
    )
    """

table1="""
    create table if not exists collected_items(
    item_id serial primary key,
    item_name varchar(40) not null,
    lost_item_id int unique,
    benovelent_name varchar(40) not null,
    benovelent_id_number int not null,
    time_collected timestamp,
    item_image varchar(120) not null,
    received_by int not null references user(user_id)
    )
    """

tables =[user,table1]