from src.main import DocumentEditor
import pytest

class TestEditor:
    @pytest.mark.smoke
    def test_writing_operations(self):
        #GIVEN: inititalizing the DocumentEditor class
        document = DocumentEditor()

        #WHEN: writing a content
        document.write("This is the first line")

        #THEN: the content should be equal to the actual content
        assert document.content == "This is the first line"

    @pytest.mark.smoke
    def test_clearing_content(self):
        #GIVEN: inititalizing the DocumentEditor class
        document = DocumentEditor()

        #WHEN: writing a content and clearing the content
        document.write("This is the first line")
        document.clear()

        #THEN: the content should be equal to the actual content
        assert document.content == ""

    @pytest.mark.sanity
    def test_checking_last_content(self):
        #GIVEN: inititalizing the DocumentEditor class
        document = DocumentEditor()

        #WHEN: writing a contents and getching the last content
        document.write("This is the first line")
        document.write("This is the second line")
        document.write("This is the third line")
        print(document.history)

        #THEN: the content should be equal to the actual content
        assert document.get_last_content() == "This is the third line"

    @pytest.mark.sanity
    def test_checking_content_history(self):
        #GIVEN: inititalizing the DocumentEditor class
        document = DocumentEditor()

        #WHEN: writing a contents and getching the last content
        document.write("This is the first line")
        document.write("This is the second line")

        #THEN: the content should be equal to the actual content
        assert len(document.history) == 2

    @pytest.mark.sanity
    def test_check_if_content_is_empty_failure(self):
        #GIVEN: inititalizing the DocumentEditor class
        document = DocumentEditor()

        #WHEN: writing a contents and getching the last content
        document.write("This is the first line")
        document.write("This is the second line")
        document.clear()

        failure_message = (f"The actual last performed operation was: {document.document_action[-1]}, "
                            f" and the expected last content would be {document.document_action[-1]}")

        #  #THEN: the content should not be equal to the actual content
        # assert document.content == "This is second line", failure_message

        #THEN: the content should be equal to the actual content
        assert document.content == "", failure_message

    @pytest.mark.sanity
    def test_get_invalid_last_content(self):
        document = DocumentEditor()
        with pytest.raises(ValueError, match="no document history*"):
            document.get_last_content()
