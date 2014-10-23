PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "article" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "title" varchar(255) NOT NULL,
  "content" text NOT NULL,
  "owner" int(11) DEFAULT NULL,
  "date" datetime NOT NULL,
  CONSTRAINT "article_ibfk_1" FOREIGN KEY ("owner") REFERENCES "user" ("id")
);
CREATE TABLE "members" (
  "uid" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar(15) NOT NULL,
  "last_name" varchar(15) NOT NULL,
  "position" varchar(20) NOT NULL DEFAULT 'member',
  "phone" varchar(15) DEFAULT NULL,
  "mail" varchar(30) NOT NULL,
  "payed" tinyint(1) NOT NULL DEFAULT '0'
  
);
INSERT INTO "members" VALUES(1,'Bård','Hanssen','Secretary','90166447','baardjh89@gmail.com',0);
INSERT INTO "members" VALUES(2,'Kristian','Elsebø','Tech','45196252','kristian@keltux.com',0);
INSERT INTO "members" VALUES(3,'Adrian','Østgård','member','92828897','adsoe91@gmail.com',0);
INSERT INTO "members" VALUES(4,'Alexander','Svendsen','member',NULL,'alexander.svendsen@uit.no',0);
INSERT INTO "members" VALUES(5,'Christopher','Haugen','Tech','41601048','cha046@post.uit.no',0);
INSERT INTO "members" VALUES(6,'Erlend','Graff','Board member','97518767','egr008@post.uit.no',0);
INSERT INTO "members" VALUES(7,'Harald','Arntsen','Deputy','97112534','har009@post.uit.no',0);
INSERT INTO "members" VALUES(8,'Jørn','Lomax','Economy','96016061','northlomax@gmail.com',0);
INSERT INTO "members" VALUES(9,'Magnus','Stenhaug','Board member',NULL,'magnus.stenhaug@uit.no',0);
INSERT INTO "members" VALUES(10,'Ragnhild','Holm','Board member','48269833','rho017@post.uit.no',0);
INSERT INTO "members" VALUES(11,'Stig','Karlsen','Board member','99254791','stig.roar.karlsen@gmail.com',0);
INSERT INTO "members" VALUES(12,'Einar','Kristoffersen','Leader','96013956','einkri1991@gmail.com',0);
INSERT INTO "members" VALUES(13,'Espen','Johansen','member',NULL,'esj@cs.uit.no',0);
INSERT INTO "members" VALUES(14,'Ingar','Reinholtsen','member',NULL,'ingar@reinholtsen.no',0);
INSERT INTO "members" VALUES(15,'Richard','Karlsen','member',NULL,'richard.karlsen@gmail.com',0);
INSERT INTO "members" VALUES(16,'Einar','Holsbø','member',NULL,'eho033@post.uit.no',0);
INSERT INTO "members" VALUES(17,'Johannes','Larsen','member','41435451','jla038@post.uit.no',0);
INSERT INTO "members" VALUES(18,'Bjørn','Johansen','member','48237095','bjorn@octanium.net',0);
INSERT INTO "members" VALUES(26,'Jan Tore','Karlsen','member','48284704','jt.karlsen@gmail.com',0);
INSERT INTO "members" VALUES(19,'Christian','Vik','member',NULL,'cvi003@post.uit.no',0);
INSERT INTO "members" VALUES(20,'Runar','Flåten','member',NULL,'runarflaaten@gmail.com',0);
INSERT INTO "members" VALUES(21,'Fredrik','Rasch','member',NULL,'fredrik.h.rasch@post.uit.no',0);
INSERT INTO "members" VALUES(22,'Peter','Haro','member',NULL,'pha015@post.uit.no',0);
INSERT INTO "members" VALUES(23,'Stian','Sjøli','member',NULL,'stianhotboi@gmail.com',0);
INSERT INTO "members" VALUES(24,'Jonas','Lintvedt','member',NULL,'jlintvedt@gmail.com',0);
INSERT INTO "members" VALUES(25,'Ingvild','Myrvang','member',NULL,'imy005@post.uit.no',0);
INSERT INTO "members" VALUES(27,'Thomas','Holden','member',NULL,'tho068@post.uit.no',0);
CREATE TABLE "servers" (
  "sid" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "uid" int(11) NOT NULL,
  "server_name" varchar(20) NOT NULL,
  "ip_address" varchar(15) NOT NULL
);
INSERT INTO "servers" VALUES(1,2,'keltux','129.242.219.2');
INSERT INTO "servers" VALUES(2,3,'adsoe','129.242.219.52');
INSERT INTO "servers" VALUES(3,5,'olympen','129.242.219.3');
INSERT INTO "servers" VALUES(4,6,'goliat','129.242.219.10');
INSERT INTO "servers" VALUES(5,7,'srh','129.242.219.44');
INSERT INTO "servers" VALUES(6,8,'bob','129.242.219.40');
INSERT INTO "servers" VALUES(7,12,'ekr','129.242.219.35');
INSERT INTO "servers" VALUES(8,15,'batman','129.242.219.45');
INSERT INTO "servers" VALUES(9,2,'notfronter','129.242.219.4');
INSERT INTO "servers" VALUES(10,17,'osb','129.242.219.43');
INSERT INTO "servers" VALUES(11,18,'box','129.242.219.42');
CREATE TABLE "user" (
  "id" int(11) NOT NULL ,
  "active" tinyint(1) NOT NULL,
  "email" varchar(255) NOT NULL,
  "password" varchar(50) NOT NULL,
  PRIMARY KEY ("id")
);
CREATE INDEX "user_email" ON "user" ("email");
CREATE INDEX "article_owner" ON "article" ("owner");
COMMIT;
