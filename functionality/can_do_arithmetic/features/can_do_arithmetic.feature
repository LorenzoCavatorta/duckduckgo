Feature: DuckDuckGo can do arithmetic

Scenario Outline: DuckDuckGo can add
    GIVEN that I search DuckDuckGo with term: "<term1> + <term2>"
    WHEN I parse the arithmetic result
    THEN the result is "<result>"
        Examples:
        |term1|term2|result|
        |2    |2    |4     |
        |3    |8    |11    |
        |123  |341  |464   |

Scenario Outline: DuckDuckGo can subtract
    GIVEN that I search DuckDuckGo with term: "<term1> - <term2>"
    WHEN I parse the arithmetic result
    THEN the result is "<result>"
        Examples:
        |term1|term2|result|
        |7    |2    |5     |
        |12   |3    |9     |
        |464  |341  |123   |

Scenario Outline: DuckDuckGo can multiply
    GIVEN that I search DuckDuckGo with term: "<term1> * <term2>"
    WHEN I parse the arithmetic result
    THEN the result is "<result>"
        Examples:
        |term1|term2|result|
        |3    |2    |6     |
        |8    |3    |24    |
        |8    |13   |104   |

Scenario Outline: DuckDuckGo can divide
    GIVEN that I search DuckDuckGo with term: "<term1> / <term2>"
    WHEN I parse the arithmetic result
    THEN the result is "<result>"
        Examples:
        |term1|term2|result|
        |12   |4    |3     |
        |8    |4    |2     |
        |104  |13   |8     |