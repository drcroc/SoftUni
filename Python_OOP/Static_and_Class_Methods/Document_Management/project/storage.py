from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    #   CUSTOM FUNCTION FOR FINDING CATEGORY OBJECT  OBJECT FROM ID
    def __find_category(self, category_id):
        # for x in self.categories:
        #     if x.id == category_id:
        #         return x
        return [category for category in self.categories if category.id == category_id][0]
        # return [x for x in self.categories if x.id == category_id][0]

    #   CUSTOM FUNCTION FOR FINDING TOPIC OBJECT FROM ID
    def __find_topic(self, topic_id):
        # for x in self.topics:
        #     if x.id == topic_id:
        #         return x
        return [topic for topic in self.topics if topic.id == topic_id][0]
        # return [x for x in self.topics if x.id == topic_id][0]

    #   CUSTOM FUNCTION FOR FINDING DOCUMENT OBJECT FROM ID
    def __find_document(self, document_id):
        # for x in self.documents:
        #     if x.id == document_id:
        #         return x
        return [document for document in self.documents if document.id == document_id][0]
        # return [x for x in self.documents if x.id == document_id][0]

    #   FUNCTION FOR EDITING
    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_category(category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_topic(topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_document(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id: int):
        category = self.__find_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = self.__find_topic(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = self.__find_document(document_id)
        self.documents.remove(document)

    #
    def get_document(self, document_id: int):
        document = self.__find_document(document_id)
        return document[0]

    def __repr__(self):
        return '\n'.join([str(document) for document in self.documents])



