import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter
# homework 17-1
url = 'http://api.github.com/search/repositories?q=language:perl&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

response_dict = r.json()

print(response_dict.keys())

if response_dict['incomplete_results'] == 1:
	print('OK')
elif response_dict['incomplete_results'] == 'False':
	print('False')
else:
	print(response_dict['incomplete_results'])

print("Total repositories:",response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

repo_dict = repo_dicts[0]
print("repo_dicts[0]")
print(repo_dicts[0])
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)

print("\n Selected information about each repo")
for repo_dict in repo_dicts:
	print('Name:',repo_dict['name'])
	print("Owner:",repo_dict['owner']['login'])
	print('Stars:',repo_dict['stargazers_count'])
	print('Repository:',repo_dict['html_url'])
	print('Created:',repo_dict['created_at'])
	print('Updated:',repo_dict['updated_at'])
	print('Description:',repo_dict['description'])

names, plot_dicts= [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	plot_dict = {
		'value': repo_dict['stargazers_count'],
		'label': repo_dict['description'] if repo_dict['description'] else 'None',
		'xlink': repo_dict['html_url'],
	}
	plot_dicts.append(plot_dict)

my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
print('wtfffffffffffffffffffffffff')
print(plot_dicts)
chart.add('',plot_dicts)
print(len(plot_dicts))
print('--------------------------------------')
print(names)
for n,plot_dict in enumerate(plot_dicts[:20]):
	print('The number is ',n)
	print("\n")
	print(plot_dict['value'])
	print(plot_dict['label'])
	print(plot_dict['xlink'])
	print("\n")
chart.render_to_file('python_repos.svg')