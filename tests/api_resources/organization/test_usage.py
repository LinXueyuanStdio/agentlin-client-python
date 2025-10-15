# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from agentlin import Agentlin, AsyncAgentlin
from tests.utils import assert_matches_type
from agentlin.types import UsageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_audio_speeches(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_audio_speeches(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_audio_speeches_with_all_params(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_audio_speeches(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_audio_speeches(self, client: Agentlin) -> None:
        response = client.organization.usage.with_raw_response.retrieve_audio_speeches(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_audio_speeches(self, client: Agentlin) -> None:
        with client.organization.usage.with_streaming_response.retrieve_audio_speeches(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_audio_transcriptions(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_audio_transcriptions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_audio_transcriptions_with_all_params(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_audio_transcriptions(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_audio_transcriptions(self, client: Agentlin) -> None:
        response = client.organization.usage.with_raw_response.retrieve_audio_transcriptions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_audio_transcriptions(self, client: Agentlin) -> None:
        with client.organization.usage.with_streaming_response.retrieve_audio_transcriptions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_code_interpreter_sessions(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_code_interpreter_sessions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_code_interpreter_sessions_with_all_params(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_code_interpreter_sessions(
            start_time=0,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            page="page",
            project_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_code_interpreter_sessions(self, client: Agentlin) -> None:
        response = client.organization.usage.with_raw_response.retrieve_code_interpreter_sessions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_code_interpreter_sessions(self, client: Agentlin) -> None:
        with client.organization.usage.with_streaming_response.retrieve_code_interpreter_sessions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_completions(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_completions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_completions_with_all_params(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_completions(
            start_time=0,
            api_key_ids=["string"],
            batch=True,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_completions(self, client: Agentlin) -> None:
        response = client.organization.usage.with_raw_response.retrieve_completions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_completions(self, client: Agentlin) -> None:
        with client.organization.usage.with_streaming_response.retrieve_completions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_embeddings(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_embeddings(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_embeddings_with_all_params(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_embeddings(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_embeddings(self, client: Agentlin) -> None:
        response = client.organization.usage.with_raw_response.retrieve_embeddings(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_embeddings(self, client: Agentlin) -> None:
        with client.organization.usage.with_streaming_response.retrieve_embeddings(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_images(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_images(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_images_with_all_params(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_images(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            sizes=["256x256"],
            sources=["image.generation"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_images(self, client: Agentlin) -> None:
        response = client.organization.usage.with_raw_response.retrieve_images(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_images(self, client: Agentlin) -> None:
        with client.organization.usage.with_streaming_response.retrieve_images(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_moderations(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_moderations(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_moderations_with_all_params(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_moderations(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_moderations(self, client: Agentlin) -> None:
        response = client.organization.usage.with_raw_response.retrieve_moderations(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_moderations(self, client: Agentlin) -> None:
        with client.organization.usage.with_streaming_response.retrieve_moderations(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_vector_stores(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_vector_stores(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_vector_stores_with_all_params(self, client: Agentlin) -> None:
        usage = client.organization.usage.retrieve_vector_stores(
            start_time=0,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            page="page",
            project_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_vector_stores(self, client: Agentlin) -> None:
        response = client.organization.usage.with_raw_response.retrieve_vector_stores(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_vector_stores(self, client: Agentlin) -> None:
        with client.organization.usage.with_streaming_response.retrieve_vector_stores(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_audio_speeches(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_audio_speeches(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_audio_speeches_with_all_params(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_audio_speeches(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_audio_speeches(self, async_client: AsyncAgentlin) -> None:
        response = await async_client.organization.usage.with_raw_response.retrieve_audio_speeches(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_audio_speeches(self, async_client: AsyncAgentlin) -> None:
        async with async_client.organization.usage.with_streaming_response.retrieve_audio_speeches(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_audio_transcriptions(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_audio_transcriptions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_audio_transcriptions_with_all_params(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_audio_transcriptions(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_audio_transcriptions(self, async_client: AsyncAgentlin) -> None:
        response = await async_client.organization.usage.with_raw_response.retrieve_audio_transcriptions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_audio_transcriptions(self, async_client: AsyncAgentlin) -> None:
        async with async_client.organization.usage.with_streaming_response.retrieve_audio_transcriptions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_code_interpreter_sessions(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_code_interpreter_sessions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_code_interpreter_sessions_with_all_params(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_code_interpreter_sessions(
            start_time=0,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            page="page",
            project_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_code_interpreter_sessions(self, async_client: AsyncAgentlin) -> None:
        response = await async_client.organization.usage.with_raw_response.retrieve_code_interpreter_sessions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_code_interpreter_sessions(self, async_client: AsyncAgentlin) -> None:
        async with async_client.organization.usage.with_streaming_response.retrieve_code_interpreter_sessions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_completions(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_completions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_completions_with_all_params(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_completions(
            start_time=0,
            api_key_ids=["string"],
            batch=True,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_completions(self, async_client: AsyncAgentlin) -> None:
        response = await async_client.organization.usage.with_raw_response.retrieve_completions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_completions(self, async_client: AsyncAgentlin) -> None:
        async with async_client.organization.usage.with_streaming_response.retrieve_completions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_embeddings(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_embeddings(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_embeddings_with_all_params(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_embeddings(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_embeddings(self, async_client: AsyncAgentlin) -> None:
        response = await async_client.organization.usage.with_raw_response.retrieve_embeddings(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_embeddings(self, async_client: AsyncAgentlin) -> None:
        async with async_client.organization.usage.with_streaming_response.retrieve_embeddings(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_images(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_images(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_images_with_all_params(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_images(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            sizes=["256x256"],
            sources=["image.generation"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_images(self, async_client: AsyncAgentlin) -> None:
        response = await async_client.organization.usage.with_raw_response.retrieve_images(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_images(self, async_client: AsyncAgentlin) -> None:
        async with async_client.organization.usage.with_streaming_response.retrieve_images(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_moderations(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_moderations(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_moderations_with_all_params(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_moderations(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_moderations(self, async_client: AsyncAgentlin) -> None:
        response = await async_client.organization.usage.with_raw_response.retrieve_moderations(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_moderations(self, async_client: AsyncAgentlin) -> None:
        async with async_client.organization.usage.with_streaming_response.retrieve_moderations(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_vector_stores(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_vector_stores(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_vector_stores_with_all_params(self, async_client: AsyncAgentlin) -> None:
        usage = await async_client.organization.usage.retrieve_vector_stores(
            start_time=0,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            page="page",
            project_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_vector_stores(self, async_client: AsyncAgentlin) -> None:
        response = await async_client.organization.usage.with_raw_response.retrieve_vector_stores(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_vector_stores(self, async_client: AsyncAgentlin) -> None:
        async with async_client.organization.usage.with_streaming_response.retrieve_vector_stores(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
