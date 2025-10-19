# writing an code for DateTime Object
from dateutil import parser

start = '09/07/2025 1:30 pm '
end = '09/07/2025 2:00 pm'

start_date = parser.parse(start)
end_date = parser.parse(end)


print(type(start_date))

diff =end_date - start_date
print(diff.total_seconds())
