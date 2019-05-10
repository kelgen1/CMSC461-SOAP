create table office
    (office_name varchar(15),
    city varchar(15),
    square_footage numeric(6),
    primary key(office_name));

create table agency
    (agency_id numeric(15),
    agency_name varchar(15),
    street_address varchar(20),
    city varchar(15),
    phone_number varchar(12),
    primary key(agency_id));

create table manage
    (rental_id numeric(15),
    office_name varchar(15),
    end_date varchar(8),
    rent_amount numeric(12,2),
    primary key(rental_id),
    foreign key (office_name) references office
            on delete cascade);

create table agreements
    (agency_id numeric(15),
    rental_id numeric(15),
    primary key(agency_id, rental_id),
    foreign key (agency_id) references agency
    foreign key (rental_id) references rentals
            on delete cascade
    );



