from flask import Blueprint, request, render_template, redirect
from urllib.parse import urlencode

oauth = Blueprint("oauth", __name__)


@oauth.route("/callback/linkedin")
def linkedin_callback():
    return render_template("oauth.html", args=request.args)


@oauth.route("/linkedin")
def linkedin_auth():
    request_args = {"response_type": "code", "client_id": "78cxwrmxeppmqa", "redirect_uri": "https://thm64.com/oauth/linkedin", "state": "hjVWOcyfAK1R2wKGt0ct"}
    return redirect("https://www.linkedin.com/oauth/v2/authorization?" + urlencode(request_args))

