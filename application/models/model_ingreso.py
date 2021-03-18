import web
import config

db = config.db


def get_all_ingreso():
    try:
        return db.select('ingreso')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_ingreso(idingreso):
    try:
        return db.select('ingreso', where='idingreso=$idingreso', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_ingreso(idingreso):
    try:
        return db.delete('ingreso', where='idingreso=$idingreso', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_ingreso(idproveedor,fecha_ingreso,tipo_comprobante,serie_comprobante,numero_comprobante,total):
    try:
        return db.insert('ingreso',idproveedor=idproveedor,
fecha_ingreso=fecha_ingreso,
tipo_comprobante=tipo_comprobante,
serie_comprobante=serie_comprobante,
numero_comprobante=numero_comprobante,
total=total)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_ingreso(idingreso,idproveedor,fecha_ingreso,tipo_comprobante,serie_comprobante,numero_comprobante,total):
    try:
        return db.update('ingreso',idingreso=idingreso,
idproveedor=idproveedor,
fecha_ingreso=fecha_ingreso,
tipo_comprobante=tipo_comprobante,
serie_comprobante=serie_comprobante,
numero_comprobante=numero_comprobante,
total=total,
                  where='idingreso=$idingreso',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
