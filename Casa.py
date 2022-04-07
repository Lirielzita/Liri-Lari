import config

class Casa(config.db.Model):

    id = config.db.Column(config.db.Integer,primary_key=True)
    formato = config.db.Column(config.db.String(254))

    quartos = config.db.relationship("Quarto", backref="casa")

    proprietarios = config.db.relationship("Proprietario", backref="casa")

    def __str__(self):
        return f'{self.id},{self.formato}'

class Quarto(config.db.Model):

    id = config.db.Column(config.db.Integer, primary_key = True)
    nome = config.db.Column(config.db.String(254))
    dimensoes = config.db.Column(config.db.String(254))

    casa_id = config.db.Column(config.db.Integer,config.db.ForeignKey(Casa.id),nullable = False)

    mobilias = config.db.relationship("Mobilia", backref = "quarto")

    def __str__(self):
        return f'{self.id},{self.nome},{self.dimensoes},{self.casa}'


class Mobilia(config.db.Model):
    
    id = config.db.Column(config.db.Integer, primary_key = True)
    nome = config.db.Column(config.db.String(254))
    funcao =config.db.Column(config.db.String(254))
    material = config.db.Column(config.db.String(254))

    quarto_id = config.db.Column(config.db.Integer, config.db.ForeignKey(Quarto.id), nullable = True)

    def __str__(self):
        return f'{self.id},{self.nome},{self.funcao},{self.material}'

class Proprietario(config.db.Model):

    id = config.db.Column(config.db.Integer, primary_key = True)
    nome = config.db.Column(config.db.String(254))
    email = config.db.Column(config.db.String(254))
    telefone = config.db.Column(config.db.String(254))

    casa_id = config.db.Column(config.db.Integer,config.db.ForeignKey(Casa.id),nullable = False)

    #casa = config.db.relationship("Casa")

    def __str__(self):
        return f'{self.id},{self.nome},{self.email},{self.telefone}'

class Especifico(Mobilia):

    id = config.db.Column(config.db.Integer, config.db.ForeignKey('mobilia.id'), primary_key=True)

    __mapper_args__ = { 
        'polymorphic_identity':'especifico',
    }
    cor = config.db.Column(config.db.Text) 
    def __str__(self):
        return super().__str__() + f", cor={self.cor}"

config.db.create_all()
c1 = Casa(formato="Russa")
config.db.session.add(c1)
config.db.session.commit()
print(c1)

config.db.create_all()
q1 = Quarto(nome = "sala", dimensoes = "6x3", casa = c1)
config.db.session.add(q1)
config.db.session.commit()
print(q1)
    
config.db.create_all()
m1 = Mobilia(nome = "Armário", funcao = "Guardar roupas", material = "Madeira", quarto = q1)
config.db.session.add(m1)
config.db.session.commit()
print(m1)

config.db.create_all()
p1 = Proprietario(nome = "Larissa e Liriel", email = "liriel.larissa@gmail.com", telefone = "33562798", casa = c1)
config.db.session.add(p1)
config.db.session.commit()
print(p1)

config.db.create_all()
e1 = Especifico( nome = "Armário", funcao = "Guardar roupas", material = "Madeira", cor = "branco")
config.db.session.add(e1)
config.db.session.commit()
print(e1)