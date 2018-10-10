from flask_restplus import fields

model_message = {
    'msg_id': fields.Integer(required=False, description='Index of Message', example='1'),
    'text': fields.String(required=True, description='Message', example='Very good movie!')
}
