# -*- coding: utf-8 -*-
import redis

r = redis.StrictRedis(db=12)
r.set("grupos:usuario:paulino:passwd", "pauli")
r.set("grupos:usuario:alcon:passwd","alco")
r.set("grupos:usuario:segura:passwd","segu")
r.set("grupos:usuario:delgado:passwd","delg")
r.set("grupos:usuario:estera:passwd","este")
r.set("grupos:usuario:pedrop:passwd","pedr")
r.set("grupos:usuario:jimenez:passwd","jime")
r.set("grupos:usuario:dejuan:passwd","deju")
r.set("grupos:usuario:josep:passwd","jose")
r.set("grupos:usuario:jerbi:passwd","jerb")
r.set("grupos:usuario:delossantos:passwd","delo")
r.rpush("grupos:grupo:gpo6","juana","silvia","mario","evaristo","cristina","francisco")
r.rpush("grupos:grupo:gpo5", "federico", "maria","fernando","alberto","silvia")
r.rpush("grupos:grupo:gpo4", "alfredo","elena","javier","paula","cristina","victor","juan")
r.rpush("grupos:grupo:gpo3", "eva","hector","martina","gonzalo")
r.rpush("grupos:grupo:gpo2", "carmen","marcelo","antonio","javier","luis","ester")
r.rpush("grupos:grupo:gpo1","estefania","carmen","alberto","salvador","clara","diego")

r.rpush("grupos:usuario:josep:grupos", "gpo2","gpo4","gpo6")
r.rpush("grupos:usuario:jimenez:grupos","gpo2","gpo4","gpo6")
r.rpush("grupos:usuario:delgado:grupos","gpo4","gpo5","gpo3")
r.rpush("grupos:usuario:jerbi:grupos","gpo4","gpo5","gpo3")
r.rpush("grupos:usuario:estera:grupos","gpo1","gpo2","gpo5","gpo6")
r.rpush("grupos:usuario:delossantos:grupos","gpo1","gpo2")
r.rpush("grupos:usuario:alcon:grupos","gpo4","gpo1","gpo6")
r.rpush("grupos:usuario:pedrop:grupos","gpo4","gpo1","gpo6","gpo2")
r.rpush("grupos:usuario:dejuan:grupos","gpo3","gpo2")
r.rpush("grupos:usuario:segura:grupos","gpo3","gpo2","gpo1")




