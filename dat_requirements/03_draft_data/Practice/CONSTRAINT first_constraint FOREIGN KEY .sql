CONSTRAINT first_constraint FOREIGN KEY (person_ID) REFERENCES example(person_ID)

create table example_fk(
    ex varchar(10),
    person_ID int,
    CONSTRAINT first_constraint FOREIGN KEY (person_ID) REFERENCES example(person_ID)
)