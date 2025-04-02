from behave import *
from django.db import models

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@given('ninja has a third level black-belt')
def step_impl(context):
    pass

@when('attacked by a samurai')
def step_impl(context):
    assert True is not False

@then('ninja should engage the opponent')
def step_impl(context):
    assert context.failed is False


@given('ninja has a third level black-belt')
def step_impl(context):
    pass

@when('attacked by Chuck Norris')
def step_impl(context):
    assert True is not False

@then('ninja should run for his life')
def step_impl(context):
    assert context.failed is False


@given('ninja has a third level black-belt')
def step_impl(context):
    pass

@when('attacked by Chuck Norris')
def step_impl(context):
    assert True is not False

@then('ninja should run for his life')
def step_impl(context):
    assert context.failed is False

@given('a set of specific users')
def step_impl(context):
    for row in context.table:
        model.add_user(name=row['name'], department=row['department'])