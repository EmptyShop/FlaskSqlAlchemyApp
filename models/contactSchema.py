from utils.ma import ma

class ContactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'fullname', 'email', 'phone')