'''
Provides a simpler way to create commandline arguments.
'''

import argparse, typing

__version__ = '0.0.1'

class Argument:
	def __init__(
		self,
		name: str,
		short_name: typing.Optional[str],
		type: type[typing.Union[bool, str]],
		default: typing.Union[typing.Any, typing.Optional[bool]],
		multiple: typing.Optional[bool],
		help: str,
	):
		self.name = name
		self.short_name = short_name or name
		self.type = type
		self.default = default
		self.required = default is None
		self.multiple = multiple or False
		self.nargs = '?' if type == bool else '*' if multiple else None
		self.help = help

class BooleanAction(argparse.Action):
	def __init__(
		self,
		option_strings,
		dest,
		nargs='?',
		const=True,
		default=None,
		type=str,
		choices=None,
		required=False,
		help=None,
		metavar=None,
	):
		super(BooleanAction, self).__init__(
			option_strings,
			dest,
			nargs=nargs,
			const=const,
			default=default,
			type=type,
			choices=choices,
			required=required,
			help=help,
			metavar=metavar
		)

	def __call__(
		self,
		parser,
		namespace,
		values,
		option_string=None
	):
		setattr(
			namespace, self.dest, True if values is None else not any(
				str(values).lower().startswith(i)
				for i in ['f', 'n']
			),
		)

class Parser:
	def __init__(self, args: list[Argument]):
		self.argparse = argparse.ArgumentParser()
		for arg in args:
			if arg.type == bool:
				self.argparse.add_argument(
					f'--{arg.name}',
					f'-{arg.short_name}',
					action=BooleanAction,
					default=arg.default,
					help=arg.help,
					dest=arg.name,
				)
			else:
				self.argparse.add_argument(
					f'--{arg.name}',
					f'-{arg.short_name}',
					nargs=arg.nargs,
					default=arg.default,
					type=arg.type,
					required=arg.required,
					help=arg.help,
				)

	def __call__(self) -> argparse.Namespace:
		return self.argparse.parse_args()
