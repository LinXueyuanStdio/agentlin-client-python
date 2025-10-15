# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .message_content_image_url_object import MessageContentImageURLObject
from .message_content_image_file_object import MessageContentImageFileObject

__all__ = [
    "MessageObject",
    "Attachment",
    "Content",
    "ContentText",
    "ContentTextText",
    "ContentTextTextAnnotation",
    "ContentTextTextAnnotationFileCitation",
    "ContentTextTextAnnotationFileCitationFileCitation",
    "ContentTextTextAnnotationFilePath",
    "ContentTextTextAnnotationFilePathFilePath",
    "ContentRefusal",
    "IncompleteDetails",
]


class Attachment(BaseModel):
    file_id: Optional[str] = None
    """The ID of the file to attach to the message."""

    tools: Optional[List[object]] = None
    """The tools to add this file to."""


class ContentTextTextAnnotationFileCitationFileCitation(BaseModel):
    file_id: str
    """The ID of the specific File the citation is from."""


class ContentTextTextAnnotationFileCitation(BaseModel):
    end_index: int

    file_citation: ContentTextTextAnnotationFileCitationFileCitation

    start_index: int

    text: str
    """The text in the message content that needs to be replaced."""

    type: Literal["file_citation"]
    """Always `file_citation`."""


class ContentTextTextAnnotationFilePathFilePath(BaseModel):
    file_id: str
    """The ID of the file that was generated."""


class ContentTextTextAnnotationFilePath(BaseModel):
    end_index: int

    file_path: ContentTextTextAnnotationFilePathFilePath

    start_index: int

    text: str
    """The text in the message content that needs to be replaced."""

    type: Literal["file_path"]
    """Always `file_path`."""


ContentTextTextAnnotation: TypeAlias = Annotated[
    Union[ContentTextTextAnnotationFileCitation, ContentTextTextAnnotationFilePath], PropertyInfo(discriminator="type")
]


class ContentTextText(BaseModel):
    annotations: List[ContentTextTextAnnotation]

    value: str
    """The data that makes up the text."""


class ContentText(BaseModel):
    text: ContentTextText

    type: Literal["text"]
    """Always `text`."""


class ContentRefusal(BaseModel):
    refusal: str

    type: Literal["refusal"]
    """Always `refusal`."""


Content: TypeAlias = Annotated[
    Union[MessageContentImageFileObject, MessageContentImageURLObject, ContentText, ContentRefusal],
    PropertyInfo(discriminator="type"),
]


class IncompleteDetails(BaseModel):
    reason: Literal["content_filter", "max_tokens", "run_cancelled", "run_expired", "run_failed"]
    """The reason the message is incomplete."""


class MessageObject(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints."""

    assistant_id: Optional[str] = None
    """
    If applicable, the ID of the
    [assistant](https://platform.openai.com/docs/api-reference/assistants) that
    authored this message.
    """

    attachments: Optional[List[Attachment]] = None
    """A list of files attached to the message, and the tools they were added to."""

    completed_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the message was completed."""

    content: List[Content]
    """The content of the message in array of text and/or images."""

    created_at: int
    """The Unix timestamp (in seconds) for when the message was created."""

    incomplete_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the message was marked as incomplete."""

    incomplete_details: Optional[IncompleteDetails] = None
    """On an incomplete message, details about why the message is incomplete."""

    metadata: object

    object: Literal["thread.message"]
    """The object type, which is always `thread.message`."""

    role: Literal["user", "assistant"]
    """The entity that produced the message. One of `user` or `assistant`."""

    run_id: Optional[str] = None
    """
    The ID of the [run](https://platform.openai.com/docs/api-reference/runs)
    associated with the creation of this message. Value is `null` when messages are
    created manually using the create message or create thread endpoints.
    """

    status: Literal["in_progress", "incomplete", "completed"]
    """
    The status of the message, which can be either `in_progress`, `incomplete`, or
    `completed`.
    """

    thread_id: str
    """
    The [thread](https://platform.openai.com/docs/api-reference/threads) ID that
    this message belongs to.
    """
