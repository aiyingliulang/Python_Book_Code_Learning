# coding=utf-8
favorite_languages = {
    'jen':['python','java'],
    'sarah':['c'],
    'edward':['ruby','c++'],
    'dan':['python']}
for name,languages in favorite_languages.items():
    if len(languages) == 1:
        print('\n'+name.title()+"'s favorite language is :")
        for language in languages:
            print('\t'+language.title())
    else:
        print('\n' + name.title() + "'s favorite language are:")
        for language in languages:
            print('\t'+language.title())
