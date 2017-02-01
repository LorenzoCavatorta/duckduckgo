from behave import given, when, then

@given('that I search DuckDuckGo with term: "{search_term}"')
def search_duckduckgo(context, search_term):
    context.result = context.adapter.get_search_result(search_term)

@when('I parse the arithmetic result')
def fetch_result(context):
    context.answer = context.adapter.parse_arithmetic_result(context.result)

@then('the result is "{expected_result}"')
def check_result(context, expected_result):
    assert context.answer == int(expected_result)
