"""tformat

Efficient conversion of MS/seconds to human readable equivalents.
See format_time docstring for an in-depth explanation."""

import datetime


def pretty_sequence(s, last=None):
	"""Reduces a sequence into a human-readable, friendly, comma-separated format.
	Last allows usage of a keyword to specify the last element in the list. This should be "and", "or", etc.

	Args:
			s (sequence): The sequence to be converted.
			last (str): A conjunction indicating the last element of the sequence. This should be "and", "or", etc.

	Returns:
			str: The prettified sequence.

	Examples:
			>>> pretty_sequence(["python", "c++", "basic", "assembly"], last="and")
			'python, c++, basic and assembly'
	"""
	if len(s) == 0:
		return ""
	if len(s) == 1:
		return s[0]
	final = ", ".join([str(i) for i in s][:-1])
	if last:
		final += " " + last + " " + str(s[-1])
	else:
		final += ", " + str(s[-1])
	return final


def make_plural(condition, value):
	"""Stupidly makes value plural (adds s) if condition is True"""
	return str(value) + "s" if condition else str(value)


def format_time(seconds, ms=False, pretty=True):
	"""Converts a time into it's human readable equivalent.

	args:
			seconds (int, float or datetime.timedelta): The amount of time that has passed.
			ms (bool): Whether time is in milliseconds, defaults to False.
			pretty (bool): whether the resulting string should be properly formatted.

	returns:
			str

	examples:
			>>> format_time(time.time())
			'2662 weeks, 2 days, 19 hours, 49 minutes and 11 seconds'
	"""
	if ms:
		seconds /= 1000
	if isinstance(seconds, datetime.timedelta):
		seconds = seconds.total_seconds()
	# for our purposes we don't particularly care about negative times
	seconds = abs(int(round(seconds, 0)))
	# this many seconds in a day
	days = seconds // 86400
	seconds %= 86400
	# this many days in a week
	weeks = days // 7
	days %= 7
	# this many seconds in an hour
	hours = seconds // 3600
	seconds %= 3600
	# this many minutes in a second
	minutes = seconds // 60
	seconds %= 60
	lst = []
	if weeks > 0:
		lst.append(make_plural(weeks > 1, str(weeks) + " week"))
	if days > 0:
		lst.append(make_plural(days > 1, str(days) + " day"))
	if hours > 0:
		lst.append(make_plural(hours > 1, str(hours) + " hour"))
	if minutes > 0:
		lst.append(make_plural(minutes > 1, str(minutes) + " minute"))
	if seconds > 0:
		lst.append(make_plural(seconds > 1, str(seconds) + " second"))
	if pretty:
		return pretty_sequence(lst, "and")
	return ", ".join(lst)
