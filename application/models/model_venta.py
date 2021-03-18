import web
import config

db = config.db


def get_all_venta():
    try:
        return db.select('venta')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_venta(idventa):
    try:
        return db.select('venta', where='idventa=$idventa', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_venta(idventa):
    try:
        return db.delete('venta', where='idventa=$idventa', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_venta(idusuario,total,idformapago,fecha_venta):
    try:
        return db.insert('venta',idusuario=idusuario,
total=total,
idformapago=idformapago,
fecha_venta=fecha_venta)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_venta(idventa,idusuario,total,idformapago,fecha_venta):
    try:
        return db.update('venta',idventa=idventa,
idusuario=idusuario,
total=total,
idformapago=idformapago,
fecha_venta=fecha_venta,
                  where='idventa=$idventa',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
