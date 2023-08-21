create database esercizio_4_m4;

use esercizio_4_m4;

create table Aeroporto (
città varchar(255),
nazione varchar(255),
num_piste tinyint unsigned,
primary key (città)
);

create table Aereo (
tipo_aereo varchar(255),
num_passeggeri smallint unsigned,
qta_merci int unsigned,
primary key (tipo_aereo)
);  

create table Volo (
id_volo char(5),
giorno_sett enum("lunedì","martedì","mercoledì","giovedì","venerdì","sabato","domenica"),
città_part varchar(255),
ora_part time,
città_arrivo varchar(255),
ora_arrivo time,
tipo_aereo varchar(255),
primary key (id_volo),
constraint FK_Aereo_Volo foreign key (tipo_aereo) references Aereo(tipo_aereo) on update cascade on delete no action,
constraint FK_Città_Part_Aeroporto_Volo foreign key (città_part) references Aeroporto(città) on update cascade on delete no action,
constraint FK_Città_Arrivo_Aeroporto_Volo foreign key (città_arrivo) references Aeroporto
);

select città from Aeroporto where num_piste is null;

select tipo_aereo from Volo where città_part="Torino";

select città_part from Volo where città_arrivo="Bologna";

select città_part,città_arrivo from Volo where id_volo="AZ274";

select tipo_aereo,giorno_sett,ora_part from Volo where città_part LIKE "B%O%" AND città_arrivo LIKE "%E%A";
