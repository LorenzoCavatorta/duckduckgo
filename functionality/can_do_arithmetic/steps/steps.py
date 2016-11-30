from behave import given, when, then

@given('that I search DuckDuckGo with term: "{search_term}"')
def search_duckduckgo(context, search_term):
    context.pages.search_page.search(search_term)

@when('I parse the arithmetic result')
def fetch_result(context):
    context.answer = context.pages.result_page.read_the_result()

@then('the result is "{expected_result}"')
def check_result(context, expected_result):
    assert context.answer == expected_result
