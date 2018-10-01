# canvas_edx_oauth
Authenticate canvas instance with open edx

Download canvas.py from this repository and copy into /edx/app/edxapp/venvs/edxapp/local/lib/python2.7/site-packages/social_core/backends/

Restart LMS
/edx/bin/supervisorctl restart edxapp:lms

Add oauth2 provider config

https://<lmsurl>/admin/third_party_auth/oauth2providerconfig/

- Check Enabled
- Set icon image (download favicon.ico image from this repository)
- Name: Canvas
- Enable Visible
- Enable Drop existing session
- Backend name: canvas-oauth2
- Provider slug: canvas-oauth2
- Client ID: canvas_id
- Client Secret: canvas_secret
Other Settings:
{
    "PROFILE_EXTRA_PARAMS": {
        "fields": "id, name, primary_email"
    }
}



Note:

To get client id and sercret key from canvas instance, you need to set Redirect URI (Legacy) as https://<lmsurl>/auth/complete/canvas-oauth2/
