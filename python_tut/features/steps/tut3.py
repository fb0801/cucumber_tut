# -- FILE: features/steps/example_steps_with_step_parameters.py
# HINT: Step-matcher "parse" is the DEFAULT step-matcher class.

# -- FILE: features/steps/example_use_step_matcher_in_steps.py
# HINTS:
#   * "parse" in the DEFAULT step-matcher
#   * Use "use_step_matcher(...)" in "features/environment.py" file
#     to define your own own default step-matcher.

from behave import given, when, use_step_matcher

from behave import then
from behave import *

@then('the result page will include "{text}"')
def step_impl(context, text):
    if text not in context.response:
        fail('%r not in %r' % (text, context.response))



use_step_matcher("cfparse")

@given('some event named "{event_name}" happens')
def step_given_some_event_named_happens(context, event_name):
    pass    # ... DETAILS LEFT OUT HERE.

use_step_matcher("re")

@when('a person named "(?P<name>...)" enters the room')
def step_when_person_enters_room(context, name):
    pass    # ... DETAILS LEFT OUT HERE.