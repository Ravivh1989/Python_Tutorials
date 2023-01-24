from github import GitHub

def main():
    g = GitHub('MY TOKEN')
    for repo in g.get_user().get_repos():
        print(repo.name)
        repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))

if __name__ == '__main__':
    main()