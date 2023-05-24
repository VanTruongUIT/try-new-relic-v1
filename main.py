import logging
import newrelic.agent
newrelic.agent.initialize('newrelic.ini')


# application = newrelic.agent.register_application(timeout=10)
application = newrelic.agent.application()
if not application.active:
    application.activate(10)
event_type = "Killed_Query"
params = {'query_info': 'select * from all_things;',
          'killed_time': '2016-05-18 00:59:00', 'host': 'my_host'}
newrelic.agent.record_custom_event(event_type, params, application=application)
