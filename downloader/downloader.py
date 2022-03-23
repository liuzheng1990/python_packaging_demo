import requests


def download(url, dest_path=None):
    """ Download a resource at `url` to `dest_path`.

    Parameters
    ----------

    url : str
        The URL of the resource to be downloaded.

    dest_path : str, optional
        The local destination path of the resource to be saved. If
        not given, the file will be stored in the current working
        directory with file name same as the url base name.

    Returns
    -------

    int
        Number of bytes downloaded.
    """
    res = requests.get(url)
    res.raise_for_status()
    if dest_path is None: # grab the url basename
        dest_path = url.split("/")[-1]
    with open(dest_path, 'wb') as fhand:
        return fhand.write(res.content)