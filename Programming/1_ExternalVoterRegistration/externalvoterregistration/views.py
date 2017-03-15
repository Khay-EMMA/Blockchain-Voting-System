from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from twisted.python import failure

import network.network_calls as NetworkRequest
from psycopg2 import IntegrityError, ProgrammingError


def register_ballot(request):
    if 'ballot_id' in request.GET and 'ballot_name' in request.GET and 'ballot_address' in request.GET:
        ballot_id = int(request.GET['ballot_id'])
        ballot_address = request.GET['ballot_address']
        ballot_name = request.GET['ballot_name']

        try:
            result = NetworkRequest.requestRegisterNewBallot(ballot_id, ballot_name, ballot_address).wait(5)
        except Exception as e:
            result = e

        html = "<p>ballot_id = %s </p>" \
               "<p>ballot_name = %s </p>" \
               "<p>ballot_address = %s </p><br>" \
               "<p>Result = %s </p>" % (ballot_id, ballot_name, ballot_address, result)

        if result == True:
            return HttpResponseRedirect("/")
        else:
            return HttpResponse(html)
    else:
        return HttpResponseRedirect("/")


class Dashboard(View):
    """
    The dashboard page visible immediately after logging in.
    """

    def get(self, request):

        #TODO catch errors http://crochet.readthedocs.io/en/latest/api.html#run-in-reactor-asynchronous-results

        username = None
        form_available_ballots_list = []
        if request.user.is_authenticated():
            username = int(request.user.username)

        try:

            # Get the list of ballots the user is eligable in
            available_ballots_list = NetworkRequest.searchAllAvailableBallots().wait(5)

        except Exception as e:
            # TODO pass err to dashboard.html
            print(e)
            registerd_ballots_list = {}

        return render(request, 'dashboard.html', { 'registerd_ballots_list' : available_ballots_list })
