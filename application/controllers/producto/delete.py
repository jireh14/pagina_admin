import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, idproducto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(idproducto) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idproducto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(idproducto) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(idproducto, **k):

    @staticmethod
    def POST_DELETE(idproducto, **k):
    '''

    def GET(self, idproducto, **k):
        message = None # Error message
        idproducto = config.check_secure_val(str(idproducto)) # HMAC idproducto validate
        result = config.model.get_producto(int(idproducto)) # search  idproducto
        result.idproducto = config.make_secure_val(str(result.idproducto)) # apply HMAC for idproducto
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, idproducto, **k):
        form = config.web.input() # get form data
        form['idproducto'] = config.check_secure_val(str(form['idproducto'])) # HMAC idproducto validate
        result = config.model.delete_producto(form['idproducto']) # get producto data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            idproducto = config.check_secure_val(str(idproducto))  # HMAC user validate
            idproducto = config.check_secure_val(str(idproducto))  # HMAC user validate
            result = config.model.get_producto(int(idproducto)) # get idproducto data
            result.idproducto = config.make_secure_val(str(result.idproducto)) # apply HMAC to idproducto
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/producto') # render producto delete.html 
