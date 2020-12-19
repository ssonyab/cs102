import os
import pathlib
import typing as tp


def repo_find(workdir: tp.Union[str, pathlib.Path] = ".") -> pathlib.Path:
    path = os.path.realpath(path)

    if os.path.isdir(os.path.join(path, ".git")):
        return GitRepository(path)

    # If we haven't returned, recurse in parent, if w
    parent = os.path.realpath(os.path.join(path, ".."))

    if parent == path:
        # Bottom case
        # os.path.join("/", "..") == "/":
        # If parent==path, then path is root.
        if required:
            raise Exception("No git directory.")
        else:
            return None

    # Recursive case
    return repo_find(parent, required)


def repo_create(workdir: tp.Union[str, pathlib.Path]) -> pathlib.Path:
    """Create a new repository at path."""

    repos = GitRepository(path, True)

    # First, we make sure the path either doesn't exist or is an
    # empty dir.

    if os.path.exists(repos.worktree):
        if not os.path.isdir(repos.worktree):
            raise Exception("%s is not a directory!" % path)
        if os.listdir(repos.worktree):
            raise Exception("%s is not empty!" % path)
    else:
        os.makedirs(repos.worktree)

    assert repos_dir(repos, "branches", mkdir=True)
    assert repos_dir(repos, "objects", mkdir=True)
    assert repos_dir(repos, "refs", "tags", mkdir=True)
    assert repos_dir(repos, "refs", "heads", mkdir=True)

    # .git/description
    with open(repos_file(repos, "description"), "w") as f:
        f.write(
            "Unnamed repository; edit this file 'description' to name the repository.\n"
        )

    # .git/HEAD
    with open(repos_file(repos, "HEAD"), "w") as f:
        f.write("ref: refs/heads/master\n")

    with open(repos_file(repos, "config"), "w") as f:
        config = repos_default_config()
        config.write(f)

    return repos
