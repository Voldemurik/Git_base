#!/usr/bin/env python3

import hashlib
import json
import sys


VARIANTS = [
    {
        "gitignore": [
            ".idea/",
            "*.log",
            "temp/",
        ],

        "env": {
            "OPENAI_API_KEY": "sk-demo-7f31c9a2",
            "CLAUDE_API_KEY": "sk-ant-demo-84d1",
            "AGENT_MODEL": "gpt-5",
            "AGENT_MAX_TURNS": "12",
            "MCP_SERVER_TOKEN": "mcp-demo-a91f",
        },

        "step4": {
            "source_file": "src/log_analyzer.py",
            "source_topic": (
                "небольшая программа для работы с логами. "
                "Программа должна запускаться без ошибки"
            ),
            "document_file": "docs/ai_agent.pptx",
            "document_topic": (
                "небольшая презентация об AI-агентах: "
                "LLM, OpenAI/Claude и MCP"
            ),
        },

        "step5": {
    "keywords": [
        "OpenAI",
        "Claude",
        "MCP",
    ],
},
    },

    {
        "gitignore": [
            ".vscode/",
            "*.tmp",
            "build/",
        ],

        "env": {
            "GEMINI_API_KEY": "gem-demo-f28c91",
            "CURSOR_AGENT_TOKEN": "cursor-demo-44ae",
            "DATABASE_URL": "postgresql://demo:demo@localhost/vibedb",
            "SUPABASE_KEY": "supabase-demo-b719",
            "DEBUG_MODE": "true",
        },

        "step4": {
            "source_file": "src/temp_cleaner.py",
            "source_topic": (
                "небольшая программа, связанная с временными файлами. "
                "Программа должна запускаться без ошибки"
            ),
            "document_file": "docs/vibe_app.pdf",
            "document_topic": (
                "небольшой документ о приложении, использующем "
                "Gemini, базу данных и Supabase"
            ),
        },

        "step5": {
    "keywords": [
        "Gemini",
        "Supabase",
        "database",
    ],
},
    },

    {
        "gitignore": [
            "dist/",
            "*.bak",
            "cache/",
        ],

        "env": {
            "OPENAI_API_KEY": "sk-demo-rag-821f",
            "QDRANT_API_KEY": "qdrant-demo-991c",
            "EMBEDDING_MODEL": "text-embedding-demo",
            "VECTOR_DB_URL": "http://localhost:6333",
            "RAG_CHUNK_SIZE": "512",
        },

        "step4": {
            "source_file": "src/cache_manager.py",
            "source_topic": (
                "небольшая программа для работы с кэшем. "
                "Программа должна запускаться без ошибки"
            ),
            "document_file": "docs/rag_system.pdf",
            "document_topic": (
                "небольшой документ о RAG: embeddings, "
                "vector database и поиске по данным"
            ),
        },

        "step5": {
    "keywords": [
        "RAG",
        "Qdrant",
        "embedding",
    ],
},
    },

    {
        "gitignore": [
            "logs/",
            "*.swp",
            ".DS_Store",
        ],

        "env": {
            "CLAUDE_API_KEY": "sk-ant-demo-agent-72a1",
            "GROQ_API_KEY": "gsk-demo-19ac",
            "PRIMARY_AGENT": "claude",
            "REVIEW_AGENT": "groq",
            "MAX_AGENT_LOOPS": "7",
        },

        "step4": {
            "source_file": "src/log_reader.py",
            "source_topic": (
                "небольшая программа для чтения или обработки логов. "
                "Программа должна запускаться без ошибки"
            ),
            "document_file": "docs/multi_agent.docx",
            "document_topic": (
                "небольшой документ о взаимодействии нескольких "
                "AI-агентов: primary agent и review agent"
            ),
        },

        "step5": {
    "keywords": [
        "Claude",
        "Groq",
        "agent",
    ],
},
    },

    {
        "gitignore": [
            "coverage/",
            "*.cache",
            "debug/",
        ],

        "env": {
            "MCP_SERVER_URL": "http://localhost:8765",
            "MCP_SERVER_TOKEN": "mcp-demo-33fa",
            "OPENAI_API_KEY": "sk-demo-mcp-98c2",
            "TOOL_TIMEOUT": "30",
            "AGENT_TEMPERATURE": "0.7",
        },

        "step4": {
            "source_file": "src/cache_inspector.py",
            "source_topic": (
                "небольшая программа, связанная с кэшем приложения. "
                "Программа должна запускаться без ошибки"
            ),
            "document_file": "docs/mcp_agent.pptx",
            "document_topic": (
                "небольшая презентация о MCP: сервере, "
                "инструментах и взаимодействии с LLM"
            ),
        },

        "step5": {
    "keywords": [
        "MCP",
        "OpenAI",
        "tool",
    ],
},
    },
]


def get_variant_number(username: str) -> int:
    digest = hashlib.sha256(
        username.encode("utf-8")
    ).hexdigest()

    number = int(digest[:8], 16)

    return number % len(VARIANTS)


def get_variant(username: str) -> dict:
    number = get_variant_number(username)

    return {
        "number": number,
        **VARIANTS[number],
    }


def main():
    if len(sys.argv) != 2:
        print(
            "Использование: "
            "python scripts/quest_variant.py <username>",
            file=sys.stderr,
        )
        sys.exit(1)

    username = sys.argv[1]

    result = get_variant(username)

    print(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()