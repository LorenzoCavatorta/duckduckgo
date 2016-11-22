from behave import given, when, then

@given('that I search DuckDuckGo with term: "{search_term}"')
def search_duckduckgo(context, search_term):
    assert False

@when('I parse the arithmetic result')
def fetch_result(context):
    assert False

@then('the result is "{expected_result}"')
def check_result(context, expected_result):
    assert False
