# Conversations

Methods:

- <code title="post /conversations">client.conversations.<a href="./src/agentlin/resources/conversations/conversations.py">create</a>(\*\*<a href="src/agentlin/types/conversation_create_params.py">params</a>) -> <a href="./src/agentlin/types/conversations/conversation_resource.py">ConversationResource</a></code>
- <code title="get /conversations/{conversation_id}">client.conversations.<a href="./src/agentlin/resources/conversations/conversations.py">retrieve</a>(conversation_id) -> <a href="./src/agentlin/types/conversations/conversation_resource.py">ConversationResource</a></code>
- <code title="post /conversations/{conversation_id}">client.conversations.<a href="./src/agentlin/resources/conversations/conversations.py">update</a>(conversation_id, \*\*<a href="src/agentlin/types/conversation_update_params.py">params</a>) -> <a href="./src/agentlin/types/conversations/conversation_resource.py">ConversationResource</a></code>
- <code title="delete /conversations/{conversation_id}">client.conversations.<a href="./src/agentlin/resources/conversations/conversations.py">delete</a>(conversation_id) -> object</code>

## Items

Types:

```python
from agentlin.types.conversations import (
    CodeInterpreterToolCall,
    ComputerScreenshotImage,
    ComputerToolCall,
    ComputerToolCallOutputResource,
    ComputerToolCallSafetyCheck,
    ConversationItem,
    ConversationItemList,
    ConversationResource,
    CustomToolCall,
    CustomToolCallOutput,
    EasyInputMessage,
    FileSearchToolCall,
    FunctionAndCustomToolCallOutput,
    FunctionCallItemStatus,
    FunctionToolCall,
    FunctionToolCallOutputResource,
    FunctionToolCallResource,
    ImageGenToolCall,
    Includable,
    InputAudio,
    InputContent,
    InputFileContent,
    InputImageContent,
    InputItem,
    InputMessage,
    InputTextContent,
    LocalShellToolCall,
    LocalShellToolCallOutput,
    McpApprovalRequest,
    McpApprovalResponseResource,
    McpListTools,
    McpToolCall,
    OutputMessage,
    OutputTextContent,
    ReasoningItem,
    ReasoningTextContent,
    RefusalContent,
    WebSearchToolCall,
)
```

Methods:

- <code title="post /conversations/{conversation_id}/items">client.conversations.items.<a href="./src/agentlin/resources/conversations/items.py">create</a>(conversation_id, \*\*<a href="src/agentlin/types/conversations/item_create_params.py">params</a>) -> <a href="./src/agentlin/types/conversations/conversation_item_list.py">ConversationItemList</a></code>
- <code title="get /conversations/{conversation_id}/items/{item_id}">client.conversations.items.<a href="./src/agentlin/resources/conversations/items.py">retrieve</a>(item_id, \*, conversation_id, \*\*<a href="src/agentlin/types/conversations/item_retrieve_params.py">params</a>) -> <a href="./src/agentlin/types/conversations/conversation_item.py">ConversationItem</a></code>
- <code title="get /conversations/{conversation_id}/items">client.conversations.items.<a href="./src/agentlin/resources/conversations/items.py">list</a>(conversation_id, \*\*<a href="src/agentlin/types/conversations/item_list_params.py">params</a>) -> <a href="./src/agentlin/types/conversations/conversation_item_list.py">ConversationItemList</a></code>
- <code title="delete /conversations/{conversation_id}/items/{item_id}">client.conversations.items.<a href="./src/agentlin/resources/conversations/items.py">delete</a>(item_id, \*, conversation_id) -> <a href="./src/agentlin/types/conversations/conversation_resource.py">ConversationResource</a></code>

# Responses

Types:

```python
from agentlin.types import (
    Response,
    ResponseProperties,
    ResponseTool,
    ResponseListInputItemsResponse,
)
```

Methods:

- <code title="post /responses">client.responses.<a href="./src/agentlin/resources/responses.py">create</a>(\*\*<a href="src/agentlin/types/response_create_params.py">params</a>) -> <a href="./src/agentlin/types/response.py">Response</a></code>
- <code title="get /responses/{response_id}">client.responses.<a href="./src/agentlin/resources/responses.py">retrieve</a>(response_id, \*\*<a href="src/agentlin/types/response_retrieve_params.py">params</a>) -> <a href="./src/agentlin/types/response.py">Response</a></code>
- <code title="delete /responses/{response_id}">client.responses.<a href="./src/agentlin/resources/responses.py">delete</a>(response_id) -> None</code>
- <code title="post /responses/{response_id}/cancel">client.responses.<a href="./src/agentlin/resources/responses.py">cancel</a>(response_id) -> <a href="./src/agentlin/types/response.py">Response</a></code>
- <code title="get /responses/{response_id}/input_items">client.responses.<a href="./src/agentlin/resources/responses.py">list_input_items</a>(response_id, \*\*<a href="src/agentlin/types/response_list_input_items_params.py">params</a>) -> <a href="./src/agentlin/types/response_list_input_items_response.py">ResponseListInputItemsResponse</a></code>

# Threads

Types:

```python
from agentlin.types import CreateThreadRequest, ThreadObject, ThreadDeleteResponse
```

Methods:

- <code title="post /threads">client.threads.<a href="./src/agentlin/resources/threads/threads.py">create</a>(\*\*<a href="src/agentlin/types/thread_create_params.py">params</a>) -> <a href="./src/agentlin/types/thread_object.py">ThreadObject</a></code>
- <code title="get /threads/{thread_id}">client.threads.<a href="./src/agentlin/resources/threads/threads.py">retrieve</a>(thread_id) -> <a href="./src/agentlin/types/thread_object.py">ThreadObject</a></code>
- <code title="post /threads/{thread_id}">client.threads.<a href="./src/agentlin/resources/threads/threads.py">update</a>(thread_id, \*\*<a href="src/agentlin/types/thread_update_params.py">params</a>) -> <a href="./src/agentlin/types/thread_object.py">ThreadObject</a></code>
- <code title="delete /threads/{thread_id}">client.threads.<a href="./src/agentlin/resources/threads/threads.py">delete</a>(thread_id) -> <a href="./src/agentlin/types/thread_delete_response.py">ThreadDeleteResponse</a></code>

## Runs

Methods:

- <code title="post /threads/{thread_id}/runs">client.threads.runs.<a href="./src/agentlin/resources/threads/runs/runs.py">create</a>(thread_id, \*\*<a href="src/agentlin/types/threads/run_create_params.py">params</a>) -> object</code>
- <code title="get /threads/{thread_id}/runs/{run_id}">client.threads.runs.<a href="./src/agentlin/resources/threads/runs/runs.py">retrieve</a>(run_id, \*, thread_id) -> object</code>
- <code title="post /threads/{thread_id}/runs/{run_id}">client.threads.runs.<a href="./src/agentlin/resources/threads/runs/runs.py">update</a>(run_id, \*, thread_id, \*\*<a href="src/agentlin/types/threads/run_update_params.py">params</a>) -> object</code>
- <code title="get /threads/{thread_id}/runs">client.threads.runs.<a href="./src/agentlin/resources/threads/runs/runs.py">list</a>(thread_id, \*\*<a href="src/agentlin/types/threads/run_list_params.py">params</a>) -> object</code>
- <code title="post /threads/{thread_id}/runs/{run_id}/cancel">client.threads.runs.<a href="./src/agentlin/resources/threads/runs/runs.py">cancel</a>(run_id, \*, thread_id) -> object</code>
- <code title="post /threads/runs">client.threads.runs.<a href="./src/agentlin/resources/threads/runs/runs.py">create_with_run</a>(\*\*<a href="src/agentlin/types/threads/run_create_with_run_params.py">params</a>) -> object</code>
- <code title="post /threads/{thread_id}/runs/{run_id}/submit_tool_outputs">client.threads.runs.<a href="./src/agentlin/resources/threads/runs/runs.py">submit_tool_outputs</a>(run_id, \*, thread_id, \*\*<a href="src/agentlin/types/threads/run_submit_tool_outputs_params.py">params</a>) -> object</code>

### Steps

Methods:

- <code title="get /threads/{thread_id}/runs/{run_id}/steps/{step_id}">client.threads.runs.steps.<a href="./src/agentlin/resources/threads/runs/steps.py">retrieve</a>(step_id, \*, thread_id, run_id, \*\*<a href="src/agentlin/types/threads/runs/step_retrieve_params.py">params</a>) -> object</code>
- <code title="get /threads/{thread_id}/runs/{run_id}/steps">client.threads.runs.steps.<a href="./src/agentlin/resources/threads/runs/steps.py">list</a>(run_id, \*, thread_id, \*\*<a href="src/agentlin/types/threads/runs/step_list_params.py">params</a>) -> object</code>

## Messages

Types:

```python
from agentlin.types.threads import (
    MessageContentImageFileObject,
    MessageContentImageURLObject,
    MessageObject,
    MessageListResponse,
    MessageDeleteResponse,
)
```

Methods:

- <code title="post /threads/{thread_id}/messages">client.threads.messages.<a href="./src/agentlin/resources/threads/messages.py">create</a>(thread_id, \*\*<a href="src/agentlin/types/threads/message_create_params.py">params</a>) -> <a href="./src/agentlin/types/threads/message_object.py">MessageObject</a></code>
- <code title="get /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/agentlin/resources/threads/messages.py">retrieve</a>(message_id, \*, thread_id) -> <a href="./src/agentlin/types/threads/message_object.py">MessageObject</a></code>
- <code title="post /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/agentlin/resources/threads/messages.py">update</a>(message_id, \*, thread_id, \*\*<a href="src/agentlin/types/threads/message_update_params.py">params</a>) -> <a href="./src/agentlin/types/threads/message_object.py">MessageObject</a></code>
- <code title="get /threads/{thread_id}/messages">client.threads.messages.<a href="./src/agentlin/resources/threads/messages.py">list</a>(thread_id, \*\*<a href="src/agentlin/types/threads/message_list_params.py">params</a>) -> <a href="./src/agentlin/types/threads/message_list_response.py">MessageListResponse</a></code>
- <code title="delete /threads/{thread_id}/messages/{message_id}">client.threads.messages.<a href="./src/agentlin/resources/threads/messages.py">delete</a>(message_id, \*, thread_id) -> <a href="./src/agentlin/types/threads/message_delete_response.py">MessageDeleteResponse</a></code>

# Chatkit

Types:

```python
from agentlin.types import ChatkitUploadFileResponse
```

Methods:

- <code title="post /chatkit/files">client.chatkit.<a href="./src/agentlin/resources/chatkit/chatkit.py">upload_file</a>(\*\*<a href="src/agentlin/types/chatkit_upload_file_params.py">params</a>) -> <a href="./src/agentlin/types/chatkit_upload_file_response.py">ChatkitUploadFileResponse</a></code>

## Sessions

Types:

```python
from agentlin.types.chatkit import ChatSession
```

Methods:

- <code title="post /chatkit/sessions">client.chatkit.sessions.<a href="./src/agentlin/resources/chatkit/sessions.py">create</a>(\*\*<a href="src/agentlin/types/chatkit/session_create_params.py">params</a>) -> <a href="./src/agentlin/types/chatkit/chat_session.py">ChatSession</a></code>
- <code title="post /chatkit/sessions/{session_id}/cancel">client.chatkit.sessions.<a href="./src/agentlin/resources/chatkit/sessions.py">cancel</a>(session_id) -> <a href="./src/agentlin/types/chatkit/chat_session.py">ChatSession</a></code>

## Threads

Types:

```python
from agentlin.types.chatkit import (
    TaskType,
    Thread,
    ThreadListResponse,
    ThreadDeleteResponse,
    ThreadListItemsResponse,
)
```

Methods:

- <code title="get /chatkit/threads/{thread_id}">client.chatkit.threads.<a href="./src/agentlin/resources/chatkit/threads.py">retrieve</a>(thread_id) -> <a href="./src/agentlin/types/chatkit/thread.py">Thread</a></code>
- <code title="get /chatkit/threads">client.chatkit.threads.<a href="./src/agentlin/resources/chatkit/threads.py">list</a>(\*\*<a href="src/agentlin/types/chatkit/thread_list_params.py">params</a>) -> <a href="./src/agentlin/types/chatkit/thread_list_response.py">ThreadListResponse</a></code>
- <code title="delete /chatkit/threads/{thread_id}">client.chatkit.threads.<a href="./src/agentlin/resources/chatkit/threads.py">delete</a>(thread_id) -> <a href="./src/agentlin/types/chatkit/thread_delete_response.py">ThreadDeleteResponse</a></code>
- <code title="get /chatkit/threads/{thread_id}/items">client.chatkit.threads.<a href="./src/agentlin/resources/chatkit/threads.py">list_items</a>(thread_id, \*\*<a href="src/agentlin/types/chatkit/thread_list_items_params.py">params</a>) -> <a href="./src/agentlin/types/chatkit/thread_list_items_response.py">ThreadListItemsResponse</a></code>
