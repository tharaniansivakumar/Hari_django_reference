from django.http import HttpResponseForbidden
import jwt
from models import userDetails
from workout import tok_det

class AuthenticationMiddleware(object):
    def process_request(self, request):
        try:
            api = request.get_full_path().split('/')

            if(api[2]!="login"):
                auth = request.META.get('HTTP_AUTHORIZATION')
                token = []
                token = auth.split()
                payload = dict(jwt.decode(token[1], "SECRET_KEY"))
                id = payload["id"]
                ob=tok_det.tok_det()
                ob.setId(id)

                if(userDetails.objects.filter(username=id,token=token[1]).values()):
                    pass
                else:
                    return HttpResponseForbidden("Invalid Access")
                if (api[2] == "logout"):
                    userDetails.objects.filter(username=id).update(token='')

        except Exception as e:
            return HttpResponseForbidden(str(e))