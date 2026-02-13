#!/usr/bin/env python3
"""Test suite for bogosort functionality."""

import os
from unittest.mock import Mock, patch

import pytest

from bogosort import bogo_llm


class TestSortWithLLM:
    """Test cases for the bogo_llm function."""

    @patch("bogosort.OpenAI")
    def test_basic_sort_integers(self, mock_openai_class: Mock) -> None:
        """Test sorting a list of integers."""
        # Setup mock
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="[1, 2, 3, 5, 8]"))]
        mock_client.chat.completions.create.return_value = mock_response  # pyright: ignore[reportAny]

        result = bogo_llm([5, 2, 8, 1, 3])

        assert "[1, 2, 3, 5, 8]" in result
        assert "The sorted list is" in result

    @patch("bogosort.OpenAI")
    def test_sort_floats(self, mock_openai_class: Mock) -> None:
        """Test sorting a list of floats."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="[1.5, 2.5, 3.14, 5.7]"))]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([3.14, 1.5, 5.7, 2.5])

        assert "[1.5, 2.5, 3.14, 5.7]" in result

    @patch("bogosort.OpenAI")
    def test_sort_negative_numbers(self, mock_openai_class: Mock) -> None:
        """Test sorting negative numbers."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="[-10, -5, -3, 0, 2, 5]"))]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([-5, 2, -10, 0, 5, -3])

        assert "[-10, -5, -3, 0, 2, 5]" in result

    @patch("bogosort.OpenAI")
    def test_sort_mixed_types(self, mock_openai_class: Mock) -> None:
        """Test sorting mix of integers and floats."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [
            Mock(message=Mock(content="[-2.5, -1, 0, 1.5, 2, 3.14]"))
        ]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([1.5, -1, 3.14, -2.5, 0, 2])

        assert "[-2.5, -1, 0, 1.5, 2, 3.14]" in result

    @patch("bogosort.OpenAI")
    def test_single_number(self, mock_openai_class: Mock) -> None:
        """Test sorting a single number."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="[42]"))]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([42])

        assert "[42]" in result

    @patch("bogosort.OpenAI")
    def test_empty_list(self, mock_openai_class: Mock) -> None:
        """Test sorting an empty list."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="[]"))]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([])

        assert "[]" in result

    @patch("bogosort.OpenAI")
    def test_sort_duplicates(self, mock_openai_class: Mock) -> None:
        """Test sorting with duplicate numbers."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="[1, 2, 2, 2, 3, 3, 5]"))]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([3, 1, 2, 3, 2, 5, 2])

        assert "[1, 2, 2, 2, 3, 3, 5]" in result

    @patch("bogosort.OpenAI")
    def test_large_numbers(self, mock_openai_class: Mock) -> None:
        """Test sorting very large numbers."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [
            Mock(message=Mock(content="[1000000, 999999999, 1000000000]"))
        ]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([999999999, 1000000000, 1000000])

        assert "[1000000, 999999999, 1000000000]" in result

    @patch("bogosort.OpenAI")
    def test_decimal_precision(self, mock_openai_class: Mock) -> None:
        """Test sorting numbers with high decimal precision."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="[0.001, 0.01, 0.1, 1.0]"))]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([0.1, 0.01, 1.0, 0.001])

        assert "[0.001, 0.01, 0.1, 1.0]" in result

    @patch("bogosort.OpenAI")
    def test_response_with_extra_text(self, mock_openai_class: Mock) -> None:
        """Test handling response with extra text before/after brackets."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [
            Mock(message=Mock(content="Here is the sorted list: [1, 2, 3] Thank you!"))
        ]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([3, 1, 2])

        assert "[1, 2, 3]" in result

    @patch("bogosort.OpenAI")
    def test_empty_response(self, mock_openai_class: Mock) -> None:
        """Test handling empty response from LLM."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content=None))]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([1, 2, 3])

        assert "I honestly have no idea! Get Bogo'd!" in result

    @patch("bogosort.OpenAI")
    def test_response_without_brackets(self, mock_openai_class: Mock) -> None:
        """Test handling response without bracket notation."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="1, 2, 3"))]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([3, 1, 2])

        # Should wrap in brackets
        assert "[1, 2, 3]" in result

    @patch("bogosort.OpenAI")
    def test_custom_model_and_url(self, mock_openai_class: Mock) -> None:
        """Test using custom model name and API URL."""
        from bogosort import DEFAULT_API_KEY

        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="[1, 2, 3]"))]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm(
            [3, 1, 2], model_name="custom-model", api_url="http://custom-url:8080/v1"
        )

        # Verify OpenAI client was called with correct parameters
        mock_openai_class.assert_called_once_with(
            base_url="http://custom-url:8080/v1", api_key=DEFAULT_API_KEY
        )

        # Verify the chat completion was called with custom model
        call_kwargs = mock_client.chat.completions.create.call_args[1]
        assert call_kwargs["model"] == "custom-model"


class TestEnvironmentVariables:
    """Test cases for environment variable handling."""

    @patch.dict(
        os.environ, {"MODEL_NAME": "env-model", "API_URL": "http://env-url:1234/v1"}
    )
    @patch("bogosort.OpenAI")
    def test_env_vars_used_as_defaults(self, mock_openai_class: Mock) -> None:
        """Test that environment variables are loaded and used as defaults."""
        # Reload module to pick up new env vars
        import importlib
        import bogosort

        importlib.reload(bogosort)

        assert bogosort.DEFAULT_MODEL == "env-model"
        assert bogosort.DEFAULT_API_URL == "http://env-url:1234/v1"


class TestIntegrationScenarios:
    """Integration-style test scenarios."""

    @patch("bogosort.OpenAI")
    def test_already_sorted_list(self, mock_openai_class: Mock) -> None:
        """Test sorting a list that's already sorted."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="[1, 2, 3, 4, 5]"))]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([1, 2, 3, 4, 5])

        assert "[1, 2, 3, 4, 5]" in result

    @patch("bogosort.OpenAI")
    def test_reverse_sorted_list(self, mock_openai_class: Mock) -> None:
        """Test sorting a reverse-sorted list."""
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="[1, 2, 3, 4, 5]"))]
        mock_client.chat.completions.create.return_value = mock_response

        result = bogo_llm([5, 4, 3, 2, 1])

        assert "[1, 2, 3, 4, 5]" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
