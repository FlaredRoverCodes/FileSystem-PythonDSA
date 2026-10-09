from file_system_tree import FileSystemTree

# Sample implementation for testing
if __name__ == "__main__":
    fs_tree = FileSystemTree()
    fs_tree.insert("documents")
    fs_tree.insert("photos")
    fs_tree.insert("videos")
    fs_tree.insert("music")
    fs_tree.insert("downloads")
    print("Files and Directories:", fs_tree.list_all()) # Output: ['documents', 'downloads', 'music', 'photos', 'videos']
    print("Search 'music':", fs_tree.search("music")) # Output: <FileSystemNode object>
    print("Search 'archive':", fs_tree.search("archive")) # Output: None
    fs_tree.delete("photos")
    print("Files and Directories after deletion:", fs_tree.list_all()) # Output: ['documents', 'downloads', 'music', 'videos']