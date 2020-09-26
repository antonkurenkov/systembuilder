import telebot
import requests
import json
import os
import subprocess

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class Parser:

	def __init__(self):
		self.url = 'https://raw.githubusercontent.com/antonkurenkov/systembuilder/develop/examples/status.json'


	def parse(self):
		return requests.get(self.url).json()


class Notifier:

	def __init__(self, raw):
		# self.chat_id = 417554679 # anton
		self.chat_id = -420442510 # ksk2020
		self.status = raw['status']
		self.version = raw['version']
		self.datetime = raw['datetime']
		self.bot = telebot.TeleBot(TOKEN)

	def prepare(self):
		author = subprocess.Popen(['git', 'log', '-1', '--pretty=%an'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
		commit = subprocess.Popen(['git', 'log', '-1', '--oneline'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
		commit_id = commit.split()[0]
		commit_message = ' '.join(commit.split()[1:])
		message = f"Author: {author}\nCommit ID: {commit_id}\nMessage: \"{commit_message}\"\n\n"
		for key, value in self.status.items():
			message += f"Образ: {key}\nРезультат сборки: {'Успешно' if value['status'] else value['message']}\nВерсия релиза: {self.version}\nДата сборки: {self.datetime[:10]}\n\n"
		return message
		# return f'''Статус сборки: {self.status[2]["status"]}
		# Версия релиза: {self.status[0]["release"]}
		# Дата релиза: {self.status[1]["datetime"][:10]}'''
		

	def send(self):
		message = self.prepare()
		self.bot.send_message(self.chat_id, message, parse_mode='html')


if __name__ == "__main__":
	parser = Parser()
	status = parser.parse()
	notifier = Notifier(status)
	notifier.send()
