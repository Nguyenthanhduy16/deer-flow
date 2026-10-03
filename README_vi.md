# 🦌 DeerFlow - 2.0

[English](./README.md) | [中文](./README_zh.md) | [日本語](./README_ja.md) | [Français](./README_fr.md) | [Русский](./README_ru.md) | Tiếng Việt

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](./backend/pyproject.toml)
[![Node.js](https://img.shields.io/badge/Node.js-22%2B-339933?logo=node.js&logoColor=white)](./Makefile)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

<a href="https://trendshift.io/repositories/14699" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14699" alt="bytedance%2Fdeer-flow | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
> Ngày 28/02/2026, DeerFlow đã giành vị trí 🏆 #1 trên GitHub Trending ngay sau khi phát hành phiên bản 2. Cảm ơn cộng đồng tuyệt vời của chúng tôi rất nhiều — chính các bạn đã làm nên điều này! 💪🔥

DeerFlow (**D**eep **E**xploration and **E**fficient **R**esearch **Flow**) là một **super agent harness** mã nguồn mở, điều phối **sub-agent**, **bộ nhớ (memory)** và **sandbox** để làm được gần như mọi thứ — nhờ vào hệ thống **skill có thể mở rộng**.

https://github.com/user-attachments/assets/a8bcadc4-e040-4cf2-8fda-dd768b999c18

> [!NOTE]
> **DeerFlow 2.0 được viết lại hoàn toàn từ đầu.** Nó không dùng chung dòng code nào với v1. Nếu bạn đang tìm framework Deep Research nguyên bản, nó vẫn được duy trì trên [nhánh `1.x`](https://github.com/bytedance/deer-flow/tree/main-1.x) — vẫn rất hoan nghênh đóng góp tại đó. Việc phát triển chính đã chuyển sang 2.0.

## Trang chủ chính thức

Tìm hiểu thêm và xem các **demo thực tế** trên [**trang chủ chính thức**](https://deerflow.tech) của chúng tôi.
Các case study trên trang chủ mở ra dưới dạng showcase chỉ-đọc nằm trong danh sách cho phép, không yêu cầu đăng nhập.

## Dự án anh em

<img width="446" height="280" alt="image" align="middle" src="https://github.com/user-attachments/assets/077edef4-d560-41af-bb0d-d0a5f14fcc20" />

- [**LLM Space**](https://github.com/deer-flow/llm-space) - Vũ khí bí mật đằng sau DeerFlow — một công cụ desktop duy nhất để dựng nguyên mẫu ý tưởng agent, soi từng bước của harness, phát lại các lần thất bại và đo hiệu năng.

## Coding Plan từ ByteDance Volcengine

- Chúng tôi đặc biệt khuyến nghị dùng Doubao-Seed-2.0-Code, DeepSeek v3.2 và Kimi 2.5 để chạy DeerFlow
- [Tìm hiểu thêm](https://www.byteplus.com/en/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)
- [中国大陆地区的开发者请点击这里](https://www.volcengine.com/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)

## InfoQuest

Trình đọc (reader), tìm kiếm web và tìm kiếm ảnh của InfoQuest dùng timeout 30 giây cho
thời gian không hoạt động khi kết nối/đọc HTTP. Các thiết lập `timeout` và `navigation_timeout`
của crawl vẫn là những tùy chọn riêng ở phía server; chúng không điều khiển timeout HTTP cục bộ.

DeerFlow vừa tích hợp bộ công cụ tìm kiếm và thu thập dữ liệu thông minh do BytePlus tự phát triển -- [InfoQuest (hỗ trợ trải nghiệm trực tuyến miễn phí)](https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest)

<a href="https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest" target="_blank">
  <img
    src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/hubseh7bsbps/20251208-160108.png"   alt="InfoQuest_banner"
  />
</a>

---

## Mục lục

- [🦌 DeerFlow - 2.0](#-deerflow---20)
  - [Trang chủ chính thức](#trang-chủ-chính-thức)
  - [Coding Plan từ ByteDance Volcengine](#coding-plan-từ-bytedance-volcengine)
  - [InfoQuest](#infoquest)
  - [Mục lục](#mục-lục)
  - [Thiết lập agent bằng một câu lệnh](#thiết-lập-agent-bằng-một-câu-lệnh)
  - [Bắt đầu nhanh](#bắt-đầu-nhanh)
    - [Cấu hình](#cấu-hình)
    - [Chạy ứng dụng](#chạy-ứng-dụng)
      - [Định cỡ triển khai](#định-cỡ-triển-khai)
      - [Cách 1: Docker (Khuyến nghị)](#cách-1-docker-khuyến-nghị)
      - [Nâng cấp một bản checkout sẵn có](#nâng-cấp-một-bản-checkout-sẵn-có)
      - [Cách 2: Phát triển cục bộ](#cách-2-phát-triển-cục-bộ)
    - [Nâng cao](#nâng-cao)
      - [Chế độ Sandbox](#chế-độ-sandbox)
      - [MCP Server](#mcp-server)
      - [Kênh IM](#kênh-im)
      - [LangSmith Tracing](#langsmith-tracing)
      - [Langfuse Tracing](#langfuse-tracing)
      - [Monocle Tracing](#monocle-tracing)
      - [Dùng nhiều nhà cung cấp](#dùng-nhiều-nhà-cung-cấp)
      - [Personal Access Token](#personal-access-token)
  - [Từ Deep Research đến Super Agent Harness](#từ-deep-research-đến-super-agent-harness)
  - [Tính năng cốt lõi](#tính-năng-cốt-lõi)
    - [Skill \& Tool](#skill--tool)
      - [Tích hợp Claude Code](#tích-hợp-claude-code)
    - [Session Goal (Mục tiêu phiên)](#session-goal-mục-tiêu-phiên)
    - [Nén ngữ cảnh thủ công](#nén-ngữ-cảnh-thủ-công)
    - [Sub-Agent](#sub-agent)
    - [Sandbox \& Hệ thống tệp](#sandbox--hệ-thống-tệp)
    - [Context Engineering](#context-engineering)
    - [Bộ nhớ dài hạn](#bộ-nhớ-dài-hạn)
  - [Model khuyến nghị](#model-khuyến-nghị)
  - [Python Client nhúng](#python-client-nhúng)
  - [Project](#project)
  - [Tác vụ theo lịch](#tác-vụ-theo-lịch)
  - [Terminal Workbench (TUI)](#terminal-workbench-tui)
  - [Tài liệu](#tài-liệu)
  - [⚠️ Lưu ý bảo mật](#️-lưu-ý-bảo-mật)
    - [Triển khai sai cách có thể tạo ra rủi ro bảo mật](#triển-khai-sai-cách-có-thể-tạo-ra-rủi-ro-bảo-mật)
    - [Khuyến nghị bảo mật](#khuyến-nghị-bảo-mật)
  - [Đóng góp](#đóng-góp)
  - [Giấy phép](#giấy-phép)
  - [Lời cảm ơn](#lời-cảm-ơn)
    - [Những người đóng góp chính](#những-người-đóng-góp-chính)
  - [Star History](#star-history)

## Thiết lập agent bằng một câu lệnh

Nếu bạn dùng Claude Code, Codex, Cursor, Windsurf hay một coding agent khác, bạn có thể giao cho nó toàn bộ hướng dẫn cài đặt chỉ bằng một câu:

```text
Help me clone DeerFlow if needed, then bootstrap it for local development by following https://raw.githubusercontent.com/bytedance/deer-flow/main/Install.md
```

Câu nhắc đó dành cho coding agent. Nó bảo agent clone repo nếu cần, ưu tiên Docker khi có sẵn, và dừng lại ở đúng câu lệnh tiếp theo kèm theo mọi phần cấu hình còn thiếu mà người dùng cần cung cấp.

## Bắt đầu nhanh

### Cấu hình

Tùy chọn [`request_admission`](backend/docs/CONFIGURATION.md#model-request-admission) theo từng model
giúp điều tiết nhịp gửi yêu cầu để không vượt giới hạn số request mỗi phút của nhà cung cấp.
Mặc định nó bị tắt; xem hướng dẫn được liên kết để bật.

1. **Clone repository DeerFlow**

   ```bash
   git clone https://github.com/bytedance/deer-flow.git
   cd deer-flow
   ```

2. **Chạy trình hướng dẫn cài đặt**

   Từ thư mục gốc của dự án (`deer-flow/`), chạy:

   ```bash
   make setup
   ```

   Lệnh này khởi động một wizard tương tác, dẫn bạn qua việc chọn nhà cung cấp LLM, tìm kiếm web (tùy chọn), cùng các tùy chọn thực thi/an toàn như chế độ sandbox, quyền truy cập bash và các tool ghi tệp. Nó tạo ra một `config.yaml` tối giản và ghi các khóa của bạn vào `.env`. Mất khoảng 2 phút.

   Wizard cũng cho phép bạn cấu hình một nhà cung cấp tìm kiếm web tùy chọn, hoặc tạm bỏ qua.

   Khi tải nội dung web, Jina, Browserless và InfoQuest sẽ phân giải các liên kết tương đối và nguồn ảnh dựa trên URL trang được yêu cầu (hoặc một base URL HTML dùng được), nên Markdown trả về chứa địa chỉ đích đầy đủ. Việc phân giải liên kết vẫn giữ nguyên mã HTML xung quanh, kể cả định dạng của những trang bị lỗi cú pháp.

   Bạn có thể chạy `make doctor` bất cứ lúc nào để kiểm tra thiết lập và nhận gợi ý khắc phục cụ thể.
   Nếu bạn định mở một GitHub issue về sự cố cài đặt cục bộ hoặc sự cố lúc chạy, hãy chạy
   `make support-bundle`. Lệnh này in ra các bước tiếp theo dành cho người báo lỗi, ghi ra một tệp
   `*-issue-summary.md` để dán vào issue, một tệp `*-issue-draft.md`
   dành cho việc tạo issue có AI hỗ trợ, và một tệp zip bằng chứng tùy chọn nằm trong
   `.deer-flow/support-bundles/`. Nếu một trợ lý AI tạo issue, hãy bắt đầu từ
   bản nháp và thay thế mọi placeholder REQUIRED thay vì bịa ra những
   thông tin còn thiếu. Chỉ đính kèm tệp zip nếu maintainer yêu cầu, hoặc nếu chỉ riêng
   bản tóm tắt là chưa đủ. Maintainer và các công cụ phân loại bằng AI có thể bắt đầu từ
   `triage.json`; gói hỗ trợ chỉ chứa thông tin chẩn đoán đã che dữ liệu nhạy cảm và danh sách tệp,
   không chứa `.env`, nội dung hội thoại thô hay nội dung tệp của người dùng.

   > **Cấu hình nâng cao / thủ công**: Nếu bạn muốn sửa trực tiếp `config.yaml`, hãy chạy `make config` để sao chép template đầy đủ. Cơ chế tự phát hiện phụ thuộc tùy chọn chấp nhận các tệp cấu hình UTF-8 có hoặc không có byte-order mark (BOM). Xem `config.example.yaml` để có tài liệu tham chiếu đầy đủ, bao gồm các nhà cung cấp chạy qua CLI (Codex CLI, Claude Code OAuth), OpenRouter, Responses API, các giới hạn runtime cho subagent như `subagents.max_total_per_run`, và nhiều thứ khác.

   Phần giá (pricing) tùy chọn theo từng model phải dùng chung một loại tiền tệ cho mọi model có giá.
   DeerFlow sẽ tắt phần ước tính chi phí trong Console khi các loại tiền tệ bị trộn lẫn, thay vì
   hiển thị một con số tổng không hợp lệ.

   Quản trị viên cũng có thể mở **Settings → Models** để thêm, sửa, kiểm tra và
   bật/tắt các model Chat Completions tương thích OpenAI dùng chung mà không cần sửa
   `config.yaml`. Hãy nhập một tên duy nhất, base URL, model ID và API key (tùy chọn);
   sau khi lưu, danh sách model chat sẽ được làm mới. Việc kiểm tra kết nối gửi một yêu cầu
   tool-call dạng streaming ngắn và có thể phát sinh chi phí với nhà cung cấp. Nó không lưu bản nháp và không
   xác minh khả năng hỗ trợ ảnh; hãy thiết lập hỗ trợ ảnh và giới hạn token dựa theo tài liệu của nhà cung cấp.
   Các model DeepSeek chính thức tại `https://api.deepseek.com` hoặc
   `https://api.deepseek.com/v1` (cổng HTTPS mặc định) sẽ tự động dùng adapter
   DeepSeek của DeerFlow, giữ lại nội dung suy luận (reasoning) xuyên suốt các lần gọi tool và tôn trọng
   giới hạn token đầu ra. Chat dùng chế độ thinking đã chọn; bài kiểm tra kết nối
   tạm thời tắt thinking vì DeepSeek từ chối việc ép chọn tool
   trong chế độ thinking. Bài kiểm tra chỉ xác minh kết nối tool dạng streaming, không kiểm tra mọi
   luồng làm việc của agent hay hành vi của chế độ thinking. Các profile DeepSeek đã lưu từ trước cũng được
   hưởng adapter này mà không cần nhập lại thông tin đăng nhập. Các thiết lập riêng cho DeepSeek dùng với
   proxy bên thứ ba, các adapter native khác và các thiết lập reasoning nâng cao
   vẫn được cấu hình qua YAML.

   Các bài kiểm thử hồi quy cho DeepSeek chạy offline cùng bộ test backend thông thường. Để kiểm tra
   nhà cung cấp thật một cách tường minh, hãy đặt `DEEPSEEK_TEST_API_KEY` trong môi trường của bạn
   rồi chạy từ thư mục `backend/`:

   ```bash
   DEER_FLOW_RUN_LIVE_TESTS=1 uv run --no-sync pytest tests/test_managed_deepseek_live.py -q
   ```

   Các bài test tự chọn này gửi những yêu cầu ngắn đến DeepSeek và có thể phát sinh chi phí;
   chúng dùng trạng thái tạm thời, không bao giờ lưu thông tin đăng nhập vào catalog triển khai,
   và bị bỏ qua trong CI. `DEEPSEEK_TEST_MODEL` cho phép chọn một model ID DeepSeek
   khác (mặc định: `deepseek-flash`). Cùng bộ test đó có thể chạy trên các revision
   chưa sửa và đã sửa; kết quả kỳ vọng luôn là thành công.

   Các model khai báo trong YAML vẫn ở chế độ chỉ-đọc trong trang này và được ưu tiên khi trùng tên.
   Các model được quản lý (managed) sẽ được nối vào sau các model YAML; các chỉnh sửa áp dụng cho snapshot cấu hình
   mới, còn những lượt chạy đang diễn ra vẫn giữ snapshot hiện có. Việc tắt một model
   sẽ loại nó khỏi việc chọn/phân giải trong tương lai, vì vậy hãy cập nhật mọi định nghĩa custom-agent hoặc
   tác vụ theo lịch có tham chiếu trực tiếp đến nó trước khi tắt.
   Model được quản lý là tài nguyên dùng chung của toàn bộ deployment, không phải profile API-key cá nhân, và
   vẫn tuân theo chính sách phân quyền model hiện hành.

   Catalog được mã hóa cùng khóa mã hóa cục bộ được sinh ra sẽ nằm trong
   `$DEER_FLOW_HOME/managed-models/` (mặc định `.deer-flow/managed-models/`). Hãy giữ lại
   và sao lưu **toàn bộ thư mục**, hạn chế quyền truy cập hệ thống tệp, và chia sẻ nó
   cho các worker/replica Gateway cần dùng chung catalog đó. Khóa cục bộ
   được bảo vệ bằng quyền của hệ thống tệp; việc mã hóa không bảo vệ trước
   người có thể đọc được cả hai tệp. Mất khóa đồng nghĩa với việc phải khôi phục từ bản sao lưu.
   Nếu không giải mã được catalog thì thao tác đọc và ghi sẽ thất bại, thay vì ghi đè lên nó.
   Kho lưu trữ này độc lập với backend SQL và hoạt động được với các mount YAML chỉ-đọc.

   Khi có nhiều model được cấu hình, hãy mở một trong hai bộ chọn model và dùng
   biểu tượng ngôi sao bên cạnh một model để đánh dấu yêu thích. Model yêu thích sẽ xuất hiện đầu tiên trong cả
   bộ chọn của chat chính lẫn Side Chat mà không làm thay đổi model đang chọn hay model mặc định
   của từng cuộc chat. Chúng được lưu cho người dùng đã đăng nhập trên trình duyệt hiện tại,
   nên không đồng bộ sang trình duyệt hay thiết bị khác và không cần thiết lập lúc khởi động.
   Bộ chọn yêu thích dạng gọn cố tình lược bỏ ô tìm kiếm và chỉ bổ sung thứ tự ưu tiên
   cho danh sách model hai dòng.

   <details>
   <summary>Ví dụ cấu hình model thủ công</summary>

   ```yaml
   models:
     - name: gpt-4o
       display_name: GPT-4o
       use: langchain_openai:ChatOpenAI
       model: gpt-4o
       api_key: $OPENAI_API_KEY

     - name: openrouter-gemini-2.5-flash
       display_name: Gemini 2.5 Flash (OpenRouter)
       use: langchain_openai:ChatOpenAI
       model: google/gemini-2.5-flash-preview
       api_key: $OPENROUTER_API_KEY
       base_url: https://openrouter.ai/api/v1

     - name: gpt-5-responses
       display_name: GPT-5 (Responses API)
       use: langchain_openai:ChatOpenAI
       model: gpt-5
       api_key: $OPENAI_API_KEY
       use_responses_api: true
       output_version: responses/v1

     - name: qwen3-32b-vllm
       display_name: Qwen3 32B (vLLM)
       use: deerflow.models.vllm_provider:VllmChatModel
       model: Qwen/Qwen3-32B
       api_key: $VLLM_API_KEY
       base_url: http://localhost:8000/v1
       supports_thinking: true
       when_thinking_enabled:
         extra_body:
           chat_template_kwargs:
             enable_thinking: true
   ```

   OpenRouter và các gateway tương thích OpenAI tương tự nên được cấu hình với `langchain_openai:ChatOpenAI` kèm `base_url`. Nếu bạn muốn dùng một tên biến môi trường riêng của nhà cung cấp, hãy trỏ `api_key` tới biến đó một cách tường minh (ví dụ `api_key: $OPENROUTER_API_KEY`).

   Để định tuyến các model OpenAI qua `/v1/responses`, vẫn dùng `langchain_openai:ChatOpenAI` và đặt `use_responses_api: true` cùng `output_version: responses/v1`.

   Trình hướng dẫn cài đặt có sẵn một profile Z.AI GLM-5.3-Flash. Vì model đó bắt buộc phải bật thinking và chỉ chấp nhận các mức effort giới hạn của riêng nó, profile tương thích sẽ giữ thinking luôn bật cho mọi lệnh gọi foreground lẫn background và tạm thời ẩn bộ chọn effort tổng quát của DeerFlow. Xem `config.example.yaml` để biết cấu hình thủ công tương đương.

   Với vLLM 0.19.0, hãy dùng `deerflow.models.vllm_provider:VllmChatModel`. Với các model reasoning kiểu Qwen, DeerFlow bật/tắt reasoning thông qua `extra_body.chat_template_kwargs.enable_thinking` và giữ lại trường `reasoning` phi tiêu chuẩn của vLLM xuyên suốt các hội thoại tool-call nhiều lượt. Các cấu hình `thinking` cũ được chuẩn hóa tự động để tương thích ngược. Nếu endpoint báo cáo một snapshot usage tích lũy trên mỗi chunk streaming, hãy đặt `cumulative_stream_usage: true` để DeerFlow chuyển các snapshot đó thành delta cho từng chunk; tùy chọn này mặc định tắt và giữ nguyên usage khi không có completion id ổn định. Các model reasoning cũng có thể yêu cầu server được khởi động với `--reasoning-parser ...`. Nếu bản triển khai vLLM cục bộ của bạn chấp nhận bất kỳ API key không rỗng nào, bạn vẫn có thể đặt `VLLM_API_KEY` bằng một giá trị placeholder.

   Ví dụ về các nhà cung cấp chạy qua CLI:

   ```yaml
   models:
     - name: gpt-5.4
       display_name: GPT-5.4 (Codex CLI)
       use: deerflow.models.openai_codex_provider:CodexChatModel
       model: gpt-5.4
       supports_thinking: true
       supports_reasoning_effort: true

     - name: claude-sonnet-4.6
       display_name: Claude Sonnet 4.6 (Claude Code OAuth)
       use: deerflow.models.claude_provider:ClaudeChatModel
       model: claude-sonnet-4-6
       max_tokens: 4096
       supports_thinking: true
   ```

   - Codex CLI đọc `~/.codex/auth.json`
   - Claude Code chấp nhận `CLAUDE_CODE_OAUTH_TOKEN`, `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_CREDENTIALS_PATH`, hoặc `~/.claude/.credentials.json`
   - Các mục ACP agent tách biệt với các nhà cung cấp model — nếu bạn cấu hình `acp_agents.codex`, hãy trỏ nó tới một adapter ACP cho Codex, chẳng hạn `npx -y @zed-industries/codex-acp`
   - MiniMax Code nói trực tiếp giao thức ACP. Hãy cài đặt và xác thực nó, rồi thêm nó như một ACP agent:

   ```bash
   npm install --global @minimax-ai/code
   mcode login
   ```

   ```yaml
   acp_agents:
     mcode:
       command: mcode
       args: ["acp"]
       description: MiniMax Code for implementation, refactoring, debugging, and repository tasks
       auto_approve_permissions: false
   ```

   `mcode` phải nằm trong `PATH` của tiến trình Gateway; việc cài nó chỉ trên máy chủ Docker không làm nó khả dụng bên trong container Gateway. DeerFlow gọi nó thông qua `invoke_acp_agent` trong một workspace ACP riêng cho từng thread và chuyển tiếp các MCP server đang bật. Hãy giữ `auto_approve_permissions: false` cho những tác vụ không đáng tin cậy; chỉ bật nó khi MCode buộc phải sửa tệp hoặc chạy lệnh và bạn tin tưởng tác vụ đó.
   - Trên macOS, hãy export thông tin xác thực Claude Code một cách tường minh nếu cần:

   ```bash
   eval "$(python3 scripts/export_claude_code_oauth.py --print-export)"
   ```

   API key cũng có thể được đặt thủ công trong `.env` (khuyến nghị) hoặc export trong shell của bạn:

   ```bash
   OPENAI_API_KEY=your-openai-api-key
   TAVILY_API_KEY=your-tavily-api-key
   ```

   </details>

### Chạy ứng dụng

#### Định cỡ triển khai

Dùng bảng dưới đây làm điểm khởi đầu thực tế khi chọn cách chạy DeerFlow:

| Mục tiêu triển khai | Điểm khởi đầu | Khuyến nghị | Ghi chú |
|---------|-----------|------------|-------|
| Đánh giá cục bộ / `make dev` | 4 vCPU, 8 GB RAM, 20 GB SSD trống | 8 vCPU, 16 GB RAM | Phù hợp cho một lập trình viên hoặc một phiên nhẹ dùng API model trên cloud. `2 vCPU / 4 GB` thường là không đủ. |
| Phát triển bằng Docker / `make docker-start` | 4 vCPU, 8 GB RAM, 25 GB SSD trống | 8 vCPU, 16 GB RAM | Việc build image, bind mount và các container sandbox cần nhiều dư địa hơn so với phát triển cục bộ thuần túy. |
| Server chạy dài hạn / `make up` | 8 vCPU, 16 GB RAM, 40 GB SSD trống | 16 vCPU, 32 GB RAM | Nên dùng cho môi trường dùng chung, các lượt chạy multi-agent, tạo báo cáo hoặc khối lượng công việc sandbox nặng hơn. |

- Những con số này chỉ tính riêng cho DeerFlow. Nếu bạn còn tự host một LLM cục bộ, hãy tính dung lượng cho dịch vụ đó riêng.
- Linux kết hợp Docker là mục tiêu triển khai được khuyến nghị cho một server chạy thường trực. macOS và Windows tốt nhất nên xem là môi trường phát triển hoặc đánh giá.
- Nếu mức sử dụng CPU hoặc bộ nhớ luôn chạm trần, trước hết hãy giảm số lượt chạy đồng thời, sau đó mới nâng lên bậc cấu hình tiếp theo.

#### Cách 1: Docker (Khuyến nghị)

Yêu cầu Docker Desktop / Docker Engine và **Docker Compose v2.24+**
(`docker compose version`). Các client Compose cũ hơn không phân tích được cú pháp
`env_file` tùy chọn trong `docker/docker-compose-dev.yaml`.

**Phát triển** (hot-reload, mount mã nguồn):

```bash
make docker-init    # Kéo image sandbox (chỉ một lần, hoặc khi image được cập nhật)
make docker-start   # Khởi động dịch vụ (tự phát hiện chế độ sandbox từ config.yaml)
make docker-logs    # Xem log
```

`make docker-start` chỉ khởi động `provisioner` khi `config.yaml` dùng chế độ provisioner (`sandbox.use: deerflow.community.aio_sandbox:AioSandboxProvider` kèm `provisioner_url`).

Quá trình build Docker mặc định dùng registry `uv` gốc. Nếu bạn cần mirror nhanh hơn trong mạng bị hạn chế, hãy export `UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple` và `NPM_REGISTRY=https://registry.npmmirror.com` trước khi chạy `make docker-init` hoặc `make docker-start`.

Lưu lượng điều khiển của AIO sandbox cục bộ luôn đi trực tiếp: địa chỉ loopback/nội bộ,
host cluster một nhãn (single-label) và các hostname nội bộ của Docker/Podman không kế thừa
`HTTP_PROXY` hay `HTTPS_PROXY`. Các FQDN sandbox bên ngoài và IP công khai vẫn
tuân theo thiết lập proxy trong biến môi trường.

Các tiến trình backend tự động nhận thay đổi của `config.yaml` ở lần đọc cấu hình kế tiếp, nên việc cập nhật metadata của model không đòi hỏi khởi động lại thủ công trong quá trình phát triển.

Các lượt chạy qua Gateway dùng `recursion_limit` ở cấp cao nhất trong `config.yaml` khi một
yêu cầu API không cung cấp giá trị riêng. Mặc định là `100`; giá trị hợp lệ theo từng yêu cầu
được ưu tiên, và `max_recursion_limit` (mặc định `1000`) là trần cho cả hai. Các thay đổi
có hiệu lực ở lượt chạy kế tiếp mà không cần khởi động lại Gateway. Thiết lập cấp cao nhất này
áp dụng cho các lượt chạy qua Gateway API; các lượt chạy qua kênh IM và qua `DeerFlowClient` nhúng
vẫn giữ giá trị mặc định và cách ghi đè theo từng lệnh gọi của riêng chúng.
Các thiết lập lưu trữ checkpoint `database.checkpoint_channel_mode` và
`database.checkpoint_delta.snapshot_frequency` (mặc định `10`) là ngoại lệ:
cả hai bị "đóng băng" khi tiến trình dựng agent lần đầu tiên (kể cả thông qua
`DeerFlowClient`) và cần khởi động lại tiến trình để thay đổi một cách an toàn.

Phần tùy chọn `database.checkpoint_cache` (chỉ dùng với chế độ kênh delta)
cache lại lịch sử checkpoint đã được dựng: `type` nhận giá trị `memory` (mặc định) hoặc
`redis`, và `max_entries: 0` sẽ tắt cache. Backend `redis` chỉ dành cho
Gateway/async; luồng TUI/nhúng đồng bộ chỉ hỗ trợ `memory`. Cache
thuần túy phục vụ hiệu năng — kết quả vẫn y hệt khi tắt nó — nên nó
không bao giờ bị đóng băng, và các worker dùng chung một cơ sở dữ liệu checkpoint có thể chạy
các thiết lập cache khác nhau một cách an toàn.

> [!TIP]
> Trên Linux, nếu các lệnh dựa trên Docker báo lỗi `permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock`, hãy thêm người dùng của bạn vào nhóm `docker` rồi đăng nhập lại trước khi thử lại. Xem [CONTRIBUTING.md](CONTRIBUTING.md#linux-docker-daemon-permission-denied) để có cách khắc phục đầy đủ.

**Production** (build image cục bộ, mount cấu hình và dữ liệu runtime):

```bash
make up     # Build image và khởi động toàn bộ dịch vụ production
make down   # Dừng và xóa container
```

Truy cập: http://localhost:2026

`make up` chờ endpoint `/health` của Gateway trước khi báo thành công.
Nếu Gateway không trở nên khỏe mạnh trong khoảng thời gian khởi động cho phép, quá trình triển khai
sẽ kết thúc với mã lỗi khác 0 và in ra trạng thái container cùng log Gateway gần đây. Image
production khởi chạy từ môi trường đã được build sẵn và không bao giờ phân giải
hay cài đặt phụ thuộc Python lúc container khởi động.

Với các bản triển khai thường trực, hãy cấu hình `database.backend` là `sqlite` hoặc
`postgres`. Backend đã chọn được dùng chung bởi LangGraph checkpointer,
LangGraph Store và dữ liệu ứng dụng của DeerFlow. Phần `checkpointer` đã lỗi thời,
nếu có mặt, sẽ ghi đè lên hai thành phần đầu để giữ tương thích ngược.

Quá trình khởi động Gateway tự động sửa lược đồ run-change bị thiếu, vốn ảnh hưởng đến
một số cơ sở dữ liệu hiện có (#5516). Việc sửa chữa này giữ nguyên lịch sử chạy và các vị trí
thay đổi hiện có; hạ cấp bản sửa về phiên bản tiền nhiệm cũng vẫn giữ lại lược đồ
và các vị trí mà phiên bản đó cần.

Với nhu cầu lưu trữ sự kiện nhẹ trong một tiến trình duy nhất, `run_events.backend: jsonl`
giữ nguyên vẹn nội dung tin nhắn Unicode, bao gồm cả ký tự phân tách dòng và đoạn.
Các bản ghi JSONL hợp lệ hiện có vẫn đọc được mà không cần ghi lại tệp.

Endpoint nginx hợp nhất mặc định là same-origin và không phát ra header CORS cho trình duyệt. Nếu bạn chạy một client trình duyệt khác origin hoặc qua port-forward, hãy đặt `GATEWAY_CORS_ORIGINS` thành danh sách origin chính xác, phân tách bằng dấu phẩy, chẳng hạn `http://localhost:3000`; khi đó Gateway sẽ áp dụng danh sách CORS cho phép và các kiểm tra origin CSRF tương ứng.

Khi bật phân quyền chi tiết (fine-grained authorization), các kết nối Live Browser yêu cầu quyền `threads:write` cũng như quyền sở hữu thread, ngay cả khi chỉ xem khung hình: chính kết nối đó có thể điều khiển trình duyệt. Việc kiểm tra quyền diễn ra lúc kết nối. Hãy khởi động lại Gateway sau khi nâng cấp để ngắt các phiên đã được chấp nhận bởi mã nguồn cũ.

Đăng nhập trên trình duyệt dùng cookie phiên `HttpOnly`. Trang đăng nhập có tùy chọn "keep me signed in" giúp kéo dài phiên trình duyệt khi yêu cầu là HTTPS (bao gồm cả `X-Forwarded-Proto: https` đáng tin cậy) hoặc HTTP trên localhost. Ngoại lệ localhost dựa trên header `Host` của yêu cầu trực tiếp và bỏ qua các header host được chuyển tiếp. Các bản triển khai HTTP công khai, bao gồm nhiều URL sandbox tạm thời, mặc định quay về dùng cookie phiên. DeerFlow không bao giờ lưu mật khẩu trong bộ nhớ trình duyệt; giao diện chỉ có thể ghi nhớ địa chỉ email.

DeerFlow vẫn dùng các header `Forwarded` / `X-Forwarded-*` để khôi phục scheme và origin mà trình duyệt nhìn thấy khi chạy sau proxy. nginx đi kèm sẽ đặt `X-Forwarded-Proto`, nhưng giữ lại giá trị HTTPS từ upstream và không ghi đè mọi header chuyển tiếp. Hãy cấu hình proxy tin cậy ở vòng ngoài để thay thế hoặc loại bỏ các header chuyển tiếp do client cung cấp trước khi lưu lượng đến DeerFlow.

> [!IMPORTANT]
> Gateway vẫn sở hữu các tác vụ chạy đang hoạt động ngay trong tiến trình của nó, nên production mặc định chỉ dùng một worker Gateway (`GATEWAY_WORKERS=1`). Các bản triển khai nhiều worker đòi hỏi Postgres, cầu nối stream Redis (`stream_bridge.type: redis`), `run_ownership.heartbeat_enabled: true` và `run_events.backend: db`; các kho sự kiện memory/JSONL cục bộ trong tiến trình không thể đảm bảo biên nhận giao hàng dạng singleton xuyên suốt các worker. Cầu nối này chia sẻ việc phân phối SSE và khả năng phát lại `Last-Event-ID` có giới hạn giữa các worker. Khi một con trỏ kết nối lại hợp lệ đã bị cắt bỏ, hoặc khi một subscriber đã thiết lập trạng thái chờ stream rỗng bị tụt lại trước lần nhận đầu tiên, Memory và Redis sẽ phát ra một sự kiện SSE `gap` mà máy đọc được, thay vì âm thầm trả về một bản phát lại không đầy đủ; Web UI sẽ tải lại trạng thái thread/sự kiện bền vững rồi tiếp tục từ phần đuôi được giữ lại. Cơ chế đối soát lease đánh dấu các lượt chạy thuộc worker đã chết là lỗi, lưu lại biên nhận giao hàng của chúng, phát ra dấu hiệu kết thúc stream, lên lịch dọn dẹp phần stream được giữ lại, và cập nhật trạng thái thread bị ảnh hưởng. SSE, `/wait` và các bên tiêu thụ stream nội bộ dùng `stream_bridge.heartbeat_interval_seconds` (mặc định `15`) để kiểm tra "còn sống" khi nhàn rỗi; thay đổi giá trị này đòi hỏi khởi động lại Gateway. Các ID kết nối lại Redis sai định dạng sẽ chuyển sang bám đuôi sự kiện mới theo thời gian thực thay vì phát lại bộ đệm được giữ lại, và TTL cuộn của bộ đệm giữ lại (`stream_ttl_seconds`) vẫn là lưới an toàn cho việc dọn dẹp chứ không phải timeout của lượt chạy. Trạng thái kênh IM và các dịch vụ cục bộ khác trong tiến trình vẫn cần cơ chế phối hợp nhiều worker của riêng chúng.
>
> Trong các bản triển khai JSONL đơn tiến trình, việc hủy một thao tác ghi đã được chấp nhận vào kho sự kiện sẽ chờ cho phần I/O tệp chạy nền, thao tác rollback và việc ghi sổ hoàn tất trước khi nhả khóa ghi của thread. Điều này ngăn một thao tác ghi cũ đã bị hủy tái tạo lại các bản ghi đã xóa hoặc quay ngược một thao tác ghi thành công sau đó. Vì vậy việc hủy có thể phải chờ kho lưu trữ chậm; nó không dừng một thao tác hệ thống tệp đang diễn ra. Những bên gọi vẫn đang chờ giành khóa có thể hủy mà không cần bắt đầu thao tác ghi. Một lô trải trên nhiều thread sẽ xử lý xong nhóm thread hiện tại trước khi lan truyền việc hủy; các nhóm thread tiếp theo sẽ không khởi động.
>
> Sau khi một lượt chạy phát ra dấu hiệu kết thúc stream, `RunRecord` cục bộ trong tiến trình của nó vẫn khả dụng trong khoảng thời gian ân hạn năm phút như hiện tại trước khi bị dọn; lịch sử chạy bền vững vẫn truy cập được qua `RunStore`, còn cầu nối stream giữ phần đuôi giao hàng của nó theo lịch dọn dẹp riêng.
>
> Yêu cầu hủy một lượt chạy có thể rơi vào bất kỳ worker Gateway nào. Một worker không sở hữu lượt chạy giờ đây sẽ lưu lại yêu cầu ngắt hoặc rollback cho worker chủ sở hữu đang hoạt động; worker đó phát hiện yêu cầu trong lúc gia hạn lease và thực hiện luồng hủy thông thường; chỉ riêng việc định tuyến của load balancer không còn gây ra lỗi 409. Hành động được chấp nhận đầu tiên sẽ thắng ngay cả khi một lần thử lại rơi đúng vào worker chủ sở hữu, và việc hủy được chấp nhận cạnh tranh một cách nguyên tử với việc hoàn tất của chủ sở hữu. Các chủ sở hữu đã chết vẫn đi theo cơ chế tiếp quản lease và khôi phục lượt chạy mồ côi. Do đó độ trễ hủy bị giới hạn bởi khoảng heartbeat của lease.

> Việc hủy một lần dò khôi phục model (recovery probe), kể cả khi nó đang xếp hàng hoặc chờ thử lại, sẽ cho phép lệnh gọi kế tiếp kiểm tra xem nhà cung cấp đã hồi phục chưa. Việc hủy không bị tính là một lần hỏng của nhà cung cấp và cũng không giải phóng lần dò khôi phục đang hoạt động của một lệnh gọi khác.
>
> Khi bật lease heartbeat, một lỗi gia hạn RunStore thoáng qua chỉ được thử lại cho đến khi lease được xác nhận lần cuối hết hạn; khi đó worker lỗi thời sẽ hủy việc thực thi cục bộ và chặn việc hoàn tất checkpoint, completion hook, biên nhận giao hàng và trạng thái thread. Một tác dụng phụ của tool từ xa đang diễn ra có thể vẫn nằm ngoài phạm vi hủy cục bộ.
>
> Quá trình đối soát dùng một yêu cầu tiếp quản nguyên tử, kiểm tra lại lease sau khi chọn ứng viên, nên việc gia hạn thành công của chủ sở hữu sẽ thắng cơ chế khôi phục lượt chạy mồ côi và chỉ một bộ đối soát có thể báo cáo một lượt chạy đã được khôi phục. Khi nhiều worker Gateway dùng chung backend sandbox Docker/AIO hoặc E2B, hãy cấu hình thêm `sandbox.ownership.type: redis`; E2B dùng các lease này trong lúc khởi động nền và đối soát định kỳ để việc dọn dẹp bản trùng/mồ côi không thể chấm dứt sandbox đang sống của một worker khác.

Xem [CONTRIBUTING.md](CONTRIBUTING.md) để có hướng dẫn phát triển với Docker chi tiết.

#### Nâng cấp một bản checkout sẵn có

Hãy giữ lại `config.yaml`, `.env` và `extensions_config.json`. Dừng các dịch vụ bạn
đang dùng, chạy `git pull --ff-only`, rồi khởi động lại đúng chế độ đó. Đừng chạy lại
`make config` hay `make docker-init` cho một lần nâng cấp mã nguồn thông thường. Nếu phiên bản
mới yêu cầu thay đổi cấu hình, hãy chạy `make config-upgrade` trước khi khởi động lại.
Xem [Operations and Troubleshooting](frontend/src/content/en/application/operations-and-troubleshooting.mdx#upgrading-an-existing-checkout)
để biết lệnh cụ thể cho từng chế độ.

#### Cách 2: Phát triển cục bộ

Nếu bạn thích chạy các dịch vụ ngay trên máy:

Điều kiện tiên quyết: hoàn thành các bước "Cấu hình" ở trên trước (`make setup`). `make dev` cần một `config.yaml` hợp lệ ở thư mục gốc dự án. Hãy đặt `DEER_FLOW_PROJECT_ROOT` để chỉ định thư mục gốc đó một cách tường minh, hoặc `DEER_FLOW_CONFIG_PATH` để trỏ tới một tệp cấu hình cụ thể. Trạng thái runtime mặc định nằm ở `.deer-flow` dưới thư mục gốc dự án và có thể chuyển đi bằng `DEER_FLOW_HOME`; skill mặc định nằm ở `skills/` dưới thư mục gốc dự án và có thể chuyển đi bằng `DEER_FLOW_SKILLS_PATH`. Hãy chạy `make doctor` để kiểm tra thiết lập trước khi bắt đầu.
Trên Windows, hãy chạy luồng phát triển cục bộ từ Git Bash. Shell `cmd.exe` và PowerShell gốc không được hỗ trợ cho các script dịch vụ viết bằng bash, và WSL cũng không được đảm bảo vì một số script dựa vào các tiện ích của Git for Windows như `cygpath`.

Các lệnh `make` ở thư mục gốc được ghi trong tài liệu sẽ gọi các tệp `.sh` của repo
thông qua Bash một cách tường minh. Nhờ vậy chúng vẫn hoạt động khi chạy từ bản lưu trữ mã nguồn hoặc
hệ thống tệp không giữ được bit thực thi POSIX. Khi gọi trực tiếp một script từ
một bản checkout như vậy, hãy dùng `bash ./scripts/<name>.sh ...`.

1. **Kiểm tra điều kiện tiên quyết**:
   ```bash
   make check  # Kiểm tra Node.js 22+, pnpm, uv, nginx
   ```

   Các điểm vào cục bộ `make check`, `make install`, `make dev` và `make start` dùng trực tiếp tệp thực thi `pnpm` khi có sẵn, nếu không thì quay về `corepack pnpm`. Với Python Windows native, bộ chạy dùng chung sẽ kiểm tra `pnpm.cmd` trước khi tra cứu `pnpm` tổng quát — vốn đi theo `PATH`/`PATHEXT` và có thể chọn một tệp `.exe` hoặc `.bat` nằm trong cùng thư mục PATH hoặc một thư mục PATH đứng trước. Phương án dự phòng Corepack cũng tương tự: kiểm tra `corepack.cmd` trước `corepack`. Python trên POSIX vẫn ưu tiên tên tổng quát trước, kể cả khi chạy dưới MSYS/Cygwin. Bộ chạy và phần chẩn đoán phân giải đường dẫn repo theo dạng tuyệt đối, nên các kiểm tra này hoạt động bất kể thư mục hiện tại của bên gọi. Corepack chạy từ `frontend/`, nên nó tôn trọng phiên bản `packageManager` được ghim trong `frontend/package.json`; không cần bật shim pnpm toàn cục.

2. **Cài đặt phụ thuộc**:
   ```bash
   make install  # Cài phụ thuộc backend + frontend + pre-commit hook
   ```

   Việc thiết lập hook gọi pre-commit thông qua uv, nên thư mục tool của uv không cần nằm trong `PATH`.

3. **(Tùy chọn) Kéo sẵn image sandbox**:
   ```bash
   # Khuyến nghị nếu dùng sandbox dựa trên Docker/Container
   make setup-sandbox
   ```
   Lệnh này đọc image sandbox đã cấu hình từ `config.yaml` dạng UTF-8, có hoặc không có BOM ở đầu, dùng kiểu xuống dòng LF hay CRLF đều được.
   Trên macOS, một lần pull thành công bằng Apple Container là đủ để hoàn thành bước này ngay cả khi chưa cài Docker. Nếu có Docker, image của nó cũng sẽ được kéo về.

4. **Khởi động dịch vụ**:
   ```bash
   make dev
   ```

5. **Truy cập**: http://localhost:2026

6. **(Tùy chọn) Nạp dữ liệu bộ nhớ mẫu để xem thử cục bộ**: mở `Settings > Memory`, bấm **Import memory**, rồi chọn `backend/docs/memory-settings-sample.json`. Trình duyệt sẽ nhập dữ liệu vào bộ nhớ của người dùng đang đăng nhập.

   Để thay thế bộ nhớ cho mọi người dùng đã đăng ký trong một môi trường kiểm thử dùng-một-lần:

   ```bash
   cd backend
   uv run python ../scripts/load_memory_sample.py --all-users
   ```

   Chế độ hàng loạt hỗ trợ sổ đăng ký người dùng SQLite/PostgreSQL, tạo bản sao lưu có dấu thời gian trong `.deer-flow/memory-sample-backups/`, và từ chối chế độ không bền vững `database.backend: memory`. Xem [backend/docs/MEMORY_SETTINGS_REVIEW.md](backend/docs/MEMORY_SETTINGS_REVIEW.md) để biết quy trình xem xét đầy đủ.

Các dịch vụ cục bộ luôn dùng cổng nội bộ của chúng (`8001`, `3000` và `2026`).
Biến `PORT` trong `.env` ở thư mục gốc chỉ cấu hình cổng ingress Docker được công bố;
nó không làm thay đổi cổng Next.js mà `make dev` sử dụng.

#### Các chế độ khởi động

DeerFlow chạy runtime của agent ngay bên trong Gateway API. Chế độ phát triển bật hot-reload; chế độ production dùng frontend đã build sẵn.

| | **Cục bộ, tiền cảnh** | **Cục bộ, daemon** | **Docker Dev** | **Docker Prod** |
|---|---|---|---|---|
| **Dev** | `./scripts/serve.sh --dev`<br/>`make dev` | `./scripts/serve.sh --dev --daemon`<br/>`make dev-daemon` | `./scripts/docker.sh start`<br/>`make docker-start` | — |
| **Prod** | `./scripts/serve.sh --prod`<br/>`make start` | `./scripts/serve.sh --prod --daemon`<br/>`make start-daemon` | — | `./scripts/deploy.sh`<br/>`make up` |

| Hành động | Cục bộ | Docker Dev | Docker Prod |
|---|---|---|---|
| **Dừng** | `./scripts/serve.sh --stop`<br/>`make stop` | `./scripts/docker.sh stop`<br/>`make docker-stop` | `./scripts/deploy.sh down`<br/>`make down` |
| **Khởi động lại** | `./scripts/serve.sh --restart [flags]` | `./scripts/docker.sh restart` | — |

`make start` và `make start-daemon` build lại frontend bằng `next build` ở
mỗi lần chạy. Để tái sử dụng bản build lần trước, hãy truyền `SKIP_FRONTEND_BUILD=1` (hoặc thêm
`--skip-frontend-build` khi gọi trực tiếp `./scripts/serve.sh --prod`). Đây là
tùy chọn phải tự bật: nó dừng ngay lập tức nếu `frontend/.next` chưa có bản build hoàn chỉnh.

Gateway sở hữu `/api/langgraph/*` và dịch các đường dẫn công khai tương thích LangGraph đó thành các router `/api/*` gốc của nó phía sau nginx.

Để có một bản demo chỉ-đọc không cần Gateway, hãy chạy `make build-static` từ `frontend/`,
rồi chạy `HOSTNAME=127.0.0.1 PORT=3000 node --env-file=.env .next/standalone/server.js`
từ cùng thư mục đó. Bản build bao gồm các tài nguyên demo công khai và xử lý
các thao tác đọc API demo được hỗ trợ ngay tại chỗ; không hỗ trợ ghi. Để hiển thị số sao GitHub
trên trang chủ, hãy đặt `GITHUB_OAUTH_TOKEN` trong `frontend/.env` trước khi khởi động Node.
Token chỉ nằm trên server; nếu thiếu thông tin đăng nhập hoặc GitHub gặp lỗi thì số sao sẽ bị ẩn.
Hãy khởi động lại Node sau khi đổi token; không cần build lại.

#### LangGraph Studio (Tùy chọn)

Cấu trúc mặc định của `make dev` dùng runtime nhúng trong Gateway của DeerFlow và
không cần đến LangGraph Studio. Để soi và kiểm thử graph lead-agent đã đăng ký
bằng development server độc lập, hãy chạy lệnh từ thư mục `backend/`
để CLI tìm thấy `langgraph.json`:

```bash
cd backend
uv run langgraph dev --allow-blocking
```

Lệnh này in ra URL của API cục bộ và của giao diện Studio. Server chạy trong bộ nhớ này
chỉ dành cho phát triển và kiểm thử. Cờ `--allow-blocking` cho phép thiết lập cấu hình đồng bộ và
graph-factory của DeerFlow trong các yêu cầu Studio cục bộ; không được xem nó
là một thiết lập cho server production. Việc xác thực Studio cục bộ
được xử lý tự động, nên kết nối không cần header tùy chỉnh. Hãy dùng
các chế độ khởi động production được ghi trong tài liệu của DeerFlow hoặc một bản triển khai
LangSmith được hỗ trợ cho khối lượng công việc production. Quyền sở hữu và nguồn gốc assistant ở
chế độ độc lập này thuộc về server: Studio có thể khám phá các graph đã đăng ký và
những assistant do chính nó tạo, và việc chọn phiên bản assistant thông thường vẫn dùng được.
Trước khi runtime cục bộ đã khóa nạp kho phát triển bền vững của nó, DeerFlow
sửa chữa các bản ghi assistant cũ và lịch sử phiên bản để metadata client trong quá khứ
không thể khôi phục đặc quyền phía server hoặc bị quá trình dọn dẹp lúc khởi động của runtime loại bỏ.
Hãy giữ các phụ thuộc backend được đồng bộ bằng `uv sync`; đường đi
tương thích này đòi hỏi đúng các phiên bản runtime LangGraph đã khai báo và sẽ ghi
cảnh báo nếu hợp đồng của kho bền vững không còn khớp với kỳ vọng của nó.
Lệnh được ghi trong tài liệu dùng bộ nạp custom-app dựa trên tệp của LangGraph, vốn cũng
được bao phủ trực tiếp bởi các bài kiểm thử hồi quy của DeerFlow.

Các lượt chạy độc lập dùng `if_not_exists="create"` sẽ giữ lại cấu hình và metadata của lượt chạy
trên thread mới được tạo, bao gồm cả các tag tìm kiếm được; metadata của lượt chạy được
ưu tiên khi trùng khóa. Quyền sở hữu thread và incarnation MCP vẫn thuộc về
server, và các lượt chạy sau đó không thay thế metadata lúc tạo của thread.

Với các luồng làm việc gọi `backend/langgraph.json` thông qua LangGraph Studio hoặc
một LangGraph Server trực tiếp, DeerFlow sử dụng danh tính đã xác thực
do runtime đó công bố và dùng nó cho cấu hình/SOUL của custom-agent,
skill người dùng và chính sách skill, tệp tải lên, dữ liệu thread, cùng các thao tác đọc/ghi bộ nhớ.
Nhờ vậy các lượt chạy đã xác thực không rơi vào bucket hệ thống tệp `default` dùng chung, và
danh tính do server sở hữu được ưu tiên hơn các giá trị `user_id` thông thường do client cung cấp.
Các danh tính bên ngoài như địa chỉ email được ánh xạ thành user ID ổn định,
an toàn cho tên thư mục và khó va chạm, trước khi truy cập kho lưu trữ của DeerFlow.
Cấu trúc dịch vụ mặc định của DeerFlow vẫn là runtime nhúng trong Gateway được mô tả ở trên.

Các lượt chạy qua Gateway tự động bắt buộc việc giao kết quả theo cơ chế native cho các artifact được tạo hoặc sửa trong `/mnt/user-data/outputs`: `present_files` phải trình bày ít nhất một kết quả đầu ra do lượt chạy hiện tại sinh ra, và biên nhận `run.delivery` cuối cùng phải được ghi lại một cách bền vững. Các đường dẫn artifact ảo được phân giải trong cùng phạm vi người dùng đã xác thực và thread đã sinh ra kết quả đó, trước khi ranh giới thư mục đầu ra được kiểm tra. Những lượt chạy không sinh ra artifact đầu ra vẫn giữ hành vi hội thoại thông thường.

Các sự kiện tùy chỉnh dựng sẵn của DeerFlow khả dụng qua cả hai giao diện streaming của LangGraph: các client native có thể tiếp tục đăng ký `stream_mode="custom"`, trong khi các tích hợp dựa trên callback có thể tiêu thụ đúng payload đó dưới dạng bản ghi `on_custom_event` từ `astream_events(version="v2")`. Tên sự kiện callback khớp với trường `type` của payload.

#### Triển khai production bằng Docker

`deploy.sh` hỗ trợ tách riêng việc build và khởi động:

```bash
# Một bước (build + khởi động)
deploy.sh

# Hai bước (build một lần, khởi động sau)
deploy.sh build              # build toàn bộ image
deploy.sh start              # khởi động các image đã build sẵn

# Dừng
deploy.sh down
```

### Nâng cao
#### Chế độ Sandbox

DeerFlow hỗ trợ nhiều chế độ thực thi sandbox:
- **Thực thi cục bộ** (chạy mã sandbox trực tiếp trên máy chủ)
- **Thực thi bằng Docker** (chạy mã sandbox trong các container Docker cách ly)
- **Thực thi bằng Docker với Kubernetes** (chạy mã sandbox trong các pod Kubernetes thông qua dịch vụ provisioner)

Các tham chiếu sandbox trong trạng thái hội thoại thuộc quyền sở hữu của server. Các API bên ngoài
cho lượt chạy và trạng thái thread sẽ từ chối giá trị `sandbox` do bên gọi cung cấp; khi khôi phục
một checkpoint, runtime sẽ phân giải tham chiếu đó theo người dùng đã xác thực
và thread trước khi một tool có thể tái sử dụng nó. Thiếu runtime thread ID sẽ gây ra
lỗi ngay cả khi sandbox được tham chiếu đang nằm trong cache.

Khi bật Bash trên máy chủ cho chế độ Thực thi cục bộ, DeerFlow bắt đầu việc nhận diện hệ điều hành bằng `uname -s`, rồi dùng `sw_vers` trên Darwin. Trên Linux, nó chỉ đọc các tệp hệ thống của máy chủ như `/etc/os-release` khi chính sách sandbox đang áp dụng cho phép. Các kiểm tra đường dẫn hệ thống tệp của máy chủ vẫn được áp dụng; sau khi một đường dẫn bị chặn, agent sẽ được hướng dẫn dùng một lệnh dò chỉ-dùng-lệnh được phép hoặc một đường dẫn ảo thay vì lặp lại lệnh đã bị từ chối.

Với môi trường phát triển Docker, việc khởi động dịch vụ tuân theo chế độ sandbox trong `config.yaml`. Ở chế độ Local/Docker, `provisioner` sẽ không được khởi động.

Xem [Hướng dẫn cấu hình Sandbox](backend/docs/CONFIGURATION.md#sandbox) để cấu hình chế độ bạn muốn.

Việc liệt kê thư mục từ xa sẽ báo cáo các lỗi duyệt cây thư mục (ví dụ, thư mục
không đọc được) dưới dạng kết quả không đầy đủ, ngay cả khi không có mục nào được trả về. Một đường dẫn
khởi đầu không tồn tại được báo riêng là "Directory not found."

#### MCP Server

Trong giao diện chat, hãy bật **Token Usage → Debug** để soi các lệnh gọi tool thường/MCP.
Mỗi bảng **Tool details** ban đầu ở trạng thái thu gọn và hiển thị tên tool, call ID,
đầu vào, cùng kết quả nhận được hoặc lỗi tường minh. Các bản xem trước lớn sẽ bị cắt bớt;
những trường có tên vượt quá ngân sách xem trước còn lại sẽ bị bỏ đi chứ không bị đổi tên.
Bản xem trước có cấu trúc vẫn giữ cú pháp JSON hoàn chỉnh, gồm cả chuỗi đã escape và dấu đóng.
Bản xem trước mảng dừng lại khi ngân sách văn bản không đủ hiển thị thêm một phần tử; các giá trị dấu ba chấm nguyên gốc được giữ nguyên.
Nhiều dấu hiệu được sinh ra liên tiếp ở cuối một mảng sẽ dùng chung một dấu ba chấm để biểu thị phần đuôi bị lược; các dấu hiệu đứng trước những giá trị sau đó vẫn giữ nguyên vị trí.
Kết quả dạng văn bản giữ nguyên cách biểu diễn gốc, bao gồm cả các ID số rất lớn và các khóa JSON trùng lặp, mà không phân tích lại. Văn bản vượt quá giới hạn sẽ được hiển thị dưới dạng phần đầu kèm thông báo đã cắt bớt; các đối tượng và mảng có cấu trúc được định dạng riêng.
Thao tác sao chép chỉ chép phần xem trước đang hiển thị. Đây là một khung nhìn ở phía frontend trên dữ liệu
mà trình duyệt đã nhận được, không có thêm một lớp che giấu thông tin bí mật.

DeerFlow hỗ trợ các MCP server và skill có thể cấu hình để mở rộng khả năng của nó.
Với các MCP server HTTP/SSE, các luồng OAuth token được hỗ trợ (`client_credentials`, `refresh_token`).
Với các MCP server stdio, có thể cấu hình timeout riêng cho từng lệnh gọi tool bằng `tool_call_timeout`; các lệnh gọi tác vụ nền bền vững cũng tôn trọng thiết lập này đối với server HTTP/SSE.
Với các lệnh gọi tác vụ nền HTTP/SSE, `session_init_timeout` giới hạn riêng phần thiết lập kết nối (bao gồm cả sự kiện endpoint SSE) cùng với quá trình khởi tạo MCP; nó ngừng áp dụng khi lệnh gọi tool bắt đầu. Các lỗi quá hạn khởi tạo sẽ nêu rõ tên server và giới hạn thời gian đã cấu hình.
Các subagent `task` thông thường giữ lại thread incarnation đã được ghi nhận của lượt chạy cha khi gọi MCP, kể cả với các thread cũ, nên việc ủy quyền vẫn giữ nguyên phạm vi vòng đời.
Tên tool MCP mặc định được gắn tiền tố `<server_name>_` để tránh trùng tên giữa các server. Nếu một server đã tự đặt namespace cho tool của mình, hãy đặt `tool_name_prefix: false` cho server đó trong `extensions_config.json` để giữ nguyên tên gốc. Chỉ tắt tiền tố khi các tên kết quả vẫn là duy nhất trên toàn bộ các server đang bật.
Với người dùng đã đăng nhập, công tắc thông báo, model mặc định, chế độ hội thoại và mức reasoning effort sẽ được lưu vào tài khoản và khôi phục trên trình duyệt khác hoặc sau khi xóa dữ liệu trình duyệt. Quyền thông báo của trình duyệt vẫn phải được cấp trên từng thiết bị. Các thay đổi sẽ thử lại sau khi gặp lỗi mạng; những thay đổi chưa gửi vẫn tồn tại qua một lần tải lại trong cùng tab. Các chỉnh sửa đồng thời trên những trường khác nhau đều được giữ lại; với cùng một trường, lần ghi cuối cùng lên server sẽ thắng. Các tùy chọn trình duyệt hiện có chưa gắn phạm vi sẽ không được tải lên tự động vì chúng không có chủ sở hữu tài khoản; hãy chọn lại các thiết lập đó một lần sau khi nâng cấp. Các bản demo tĩnh và môi trường phát triển tắt xác thực vẫn giữ thiết lập cục bộ trên trình duyệt. Việc ghi đè model theo từng thread và các tùy chọn hiển thị khác vẫn được lưu cục bộ.

Capability Center nhóm các plugin theo: cộng tác văn phòng, tài liệu và tri thức, tìm kiếm và nghiên cứu, kinh doanh và dữ liệu, phát triển và vận hành. Danh mục này bao gồm các tài liệu thiết lập tham khảo bên cạnh các cấu hình MCP hiện có và Lark. Việc một tích hợp được khuyến nghị hay được hỗ trợ sẵn không có nghĩa là kết nối đã được cài đặt hay đã được xác minh; bộ lọc Installed chỉ hiển thị các mục MCP đã cấu hình và Lark đã cài.

Về manifest của plugin, việc đăng ký adapter và cách chọn năng lực cho Agent, xem
[Hợp đồng tích hợp Capability Center](docs/capability-center.md).

Thông báo nhóm DingTalk và WeCom cùng HubSpot CRM là các plugin đi kèm có thể cấu hình.
Quản trị viên cung cấp thông tin đăng nhập của robot hoặc một token private app của HubSpot;
sau đó Agent có thể gửi các thông báo nhóm được yêu cầu, liệt kê công ty, hoặc tạo
liên hệ. Việc lưu cấu hình không thực hiện bất kỳ thao tác ghi ra bên ngoài nào. Các plugin này tái sử dụng
vòng đời MCP hiện có và không cần một dịch vụ plugin riêng. Xem
hợp đồng tích hợp ở trên để biết các trường bắt buộc, phạm vi quyền và ranh giới tính năng.

Biểu tượng thương hiệu của plugin được đóng gói sẵn cục bộ. Khi thêm hoặc sửa một plugin MCP, quản trị viên có thể tải lên ảnh PNG, JPG hoặc WebP (tối đa 2 MB), xem trước, hoặc khôi phục biểu tượng mặc định. Thay đổi chỉ có hiệu lực sau khi bấm Save; biểu tượng tùy chỉnh được giữ lại xuyên suốt các trình duyệt dưới dạng PNG 128px đã chuẩn hóa trong metadata `presentation.icon` chỉ-dùng-để-hiển-thị của mục server. Chúng không được gửi tới transport MCP.

Capability Center > Plugins thêm, thay thế và xóa từng MCP server một thông qua các thao tác ghi có mục tiêu, giữ nguyên những thay đổi đồng thời trên các mục anh em; thao tác xóa dùng một yêu cầu không có body, định danh bằng URL. Một lệnh stdio không hợp lệ ở một server không còn chặn việc bật/tắt một server khác, trong khi việc bật chính server không hợp lệ đó vẫn được bảo vệ bởi danh sách lệnh cho phép và hiển thị thông báo kiểm tra từ backend trong giao diện.
Các cập nhật có mục tiêu chấp nhận cả trường `type` của DeerFlow lẫn trường `transport` theo đặc tả MCP cho các server SSE/HTTP.
Các cập nhật MCP và skill lúc chạy sẽ thay thế `extensions_config.json` một cách nguyên tử, nên một thao tác ghi bị gián đoạn không thể để lại cấu hình dùng chung bị cắt cụt hoặc ghi dở dang.
Các gợi ý định tuyến MCP cũng có thể ưu tiên một tool MCP cụ thể cho những yêu cầu phù hợp mà không cấm các tool khác. Khi `tool_search` hoãn việc nạp schema MCP, metadata định tuyến phù hợp có thể tự động đưa tối đa `tool_search.auto_promote_top_k` schema đang hoãn lên trước lệnh gọi model.

Người dùng OpenViking có thể đăng ký endpoint Streamable HTTP chính thức tại `/mcp`
bằng một USER API key gắn với chủ sở hữu. Tool `forget` native được phơi ra để
đảm bảo tương đương về năng lực; việc xóa là không thể hoàn tác, nên chỉ nên gọi nó sau khi
người dùng xác nhận rõ ràng. DeerFlow không tự bắt buộc việc xác nhận đó. Đường đi qua tool MCP
do model chủ động chọn này có thể chạy song song với backend bộ nhớ OpenViking tự động riêng biệt;
nó không thay thế việc tự động ghi nhận và gợi nhớ theo lượt. Xem
[cấu hình tool MCP của OpenViking](backend/docs/MCP_SERVER.md#openviking-mcp-tools).

Gateway có thể biến các tool `submit` / `status` / `cancel` thông thường của một MCP server thành các tác vụ nền bền vững. Agent chỉ nhìn thấy tool submit đã cấu hình và một task ID cục bộ của DeerFlow; các ID từ xa được lưu lại trước khi lệnh gọi submit trả về, trong khi status và cancel vẫn là chuyện nội bộ của runtime. Việc poll dùng lease xuyên worker, backoff thử lại theo cấp số nhân, các phiên MCP có phạm vi, kho lưu kết quả có giới hạn và khả năng khôi phục sau khởi động lại. Một `isError` từ tool status được giữ lại như một thông tin chẩn đoán có giới hạn và sẽ được thử lại; server báo hiệu một kết cục vĩnh viễn của tác vụ từ xa thông qua một kết quả có cấu trúc thông thường với `status: "failed"`. Các gợi ý về nhịp poll từ xa là số dương hữu hạn, tối đa 24 giờ; JSON tham chiếu artifact giới hạn ở 64 KiB; và định danh tác vụ/server được kiểm tra theo giới hạn cột SQL bền vững trước khi lưu. Các cập nhật cần đầu vào từ người dùng và các cập nhật kết thúc sẽ đánh thức cuộc chat hiện tại thông qua các lượt chạy Agent idempotent, trong khi `list_background_tasks` và `cancel_background_task` cho phép Agent quản lý tác vụ mà không cần hỏi người dùng các handle từ xa. Các tác vụ của thread hiện tại có thể truy cập qua `GET /api/threads/{thread_id}/mcp-tasks`, endpoint chi tiết của nó, và `POST /api/threads/{thread_id}/mcp-tasks/{task_id}/cancel`; khi runtime tác vụ thực sự khởi động, Web UI sẽ phơi ra đúng khung nhìn cục bộ an toàn đó ngay trên header của cuộc chat, kèm làm mới trạng thái theo thời gian thực, khả năng hủy, và các chi tiết theo yêu cầu về kết quả, artifact, yêu cầu đầu vào, lỗi trạng thái và việc thử hủy lại. Các bản triển khai mặc định tắt tính năng này hoặc dùng backend memory sẽ ẩn giao diện đó và không poll các endpoint tác vụ. Một lần hủy từ xa thất bại vẫn nằm trong hàng đợi kèm backoff, và lỗi có giới hạn mới nhất cùng số lần thử của nó vẫn hiển thị trong thẻ tác vụ khi mở rộng. Hãy bật `mcp_tasks` trong `config.yaml`, cấu hình `task_toolsets` với đúng tên tool thô trong `extensions_config.json`, và dùng backend cơ sở dữ liệu SQL (`sqlite` hoặc `postgres`). Mọi thay đổi về kết nối, xác thực, interceptor, timeout hoặc ràng buộc của một server có bật tác vụ đều đòi hỏi khởi động lại Gateway, để việc khám phá tool của Agent và các lệnh gọi nền không dùng những phiên bản cấu hình khác nhau. Hiện tại `input_required` chỉ mang tính thông báo: DeerFlow có thể hiển thị yêu cầu nhưng chưa thể gửi câu trả lời của người dùng ngược về tác vụ từ xa.

Việc khởi chạy thông báo và các lần giao kết quả từ lượt chạy Agent bị thất bại sẽ dùng backoff theo cấp số nhân có giới hạn, kèm số lần thử hiển thị rõ, và dừng lại sau năm lần thất bại. Khi một lần giải phóng thông thường có giới hạn vượt quá hạn chót xả hàng đợi, dịch vụ sẽ giữ lại quyền sở hữu cho đến khi mọi thứ ổn định. Một đích đến bị từ chối vĩnh viễn, chẳng hạn một cuộc chat đã bị xóa, sẽ được đưa vào dead letter ngay lập tức thay vì thử lại mãi mãi hay bị tạo lại. Các endpoint hủy trả về sau khi đã ghi lại yêu cầu một cách bền vững; dịch vụ nền chịu trách nhiệm cho lệnh gọi MCP từ xa có thể chậm cùng lịch thử lại của nó.

Các lượt chạy thông báo giữ chỉ thị giao hàng đáng tin cậy của chúng tách biệt khỏi payload sự kiện từ xa không đáng tin đã được đóng khung. Chính runtime tác vụ được khởi động cùng tiến trình — chứ không phải một lần đọc cấu hình nóng — quyết định các tool quản lý tác vụ có được phơi ra hay không, nên việc thay đổi `mcp_tasks` đòi hỏi khởi động lại Gateway. Khi chính sách `allowed-tools` của một skill đang có hiệu lực, `list_background_tasks` và `cancel_background_task` phải được khai báo tường minh như các tool nghiệp vụ khác.
Xem [Hướng dẫn MCP Server](backend/docs/MCP_SERVER.md) để có chỉ dẫn chi tiết.

Bảo mật: chỉ truyền thông tin đăng nhập MCP theo từng yêu cầu thông qua `config.context.secrets`;
tuyệt đối không được đặt thông tin đăng nhập vào bất kỳ bề mặt metadata nào của lượt chạy
(`metadata.auth_token` hay `config.metadata.auth_token`). Xem [Di chuyển và dọn dẹp thông tin đăng nhập MCP](backend/docs/MCP_SERVER.md#migrating-legacy-mcp-credentials)
để biết luồng interceptor được hỗ trợ cùng việc xoay vòng khóa bắt buộc và dọn dẹp các bản sao
còn lưu lại khi di chuyển khỏi cách lưu thông tin đăng nhập trong metadata kiểu cũ.

#### Kênh IM

DeerFlow hỗ trợ nhận tác vụ từ các ứng dụng nhắn tin. Các kênh tự khởi động khi được cấu hình — không kênh nào yêu cầu IP công khai.

DeerFlow cũng có thể phơi ra các kết nối kênh IM thuộc sở hữu người dùng ngay trong giao diện workspace. Khi bật `channel_connections`, người dùng đã đăng nhập có thể liên kết Telegram, Slack, Discord, Feishu/Lark, DingTalk, WeChat, WeCom hoặc Buzz từ thanh bên / Settings > Channels. Tính năng này tái sử dụng các transport `channels.*` hướng ra ngoài sẵn có, nên không cần IP công khai hay URL callback của nhà cung cấp. Khi đó các tin nhắn IM đến sẽ chạy dưới tài khoản người dùng DeerFlow đã kết nối. Xem [IM Channel Connections](backend/docs/IM_CHANNEL_CONNECTIONS.md) để biết cách thiết lập và các lưu ý bảo mật.

| Kênh | Transport | Độ khó |
|---------|-----------|------------|
| Telegram | Bot API (long-polling) | Dễ |
| Slack | Socket Mode | Trung bình |
| Feishu / Lark | WebSocket | Trung bình |
| WeChat | Tencent iLink (long-polling) | Trung bình |
| WeCom | WebSocket | Trung bình |
| DingTalk | Stream Push (WebSocket) | Trung bình |
| Buzz | Nostr relay (WebSocket, NIP-42) | Trung bình |

**Cấu hình trong `config.yaml`:**

```yaml
channels:
  # Base URL của Gateway API tương thích LangGraph (mặc định: http://localhost:8001/api)
  langgraph_url: http://localhost:8001/api
  # URL của Gateway API (mặc định: http://localhost:8001)
  gateway_url: http://localhost:8001

  # Số tin nhắn đến tối đa đang xếp hàng hoặc được nhà cung cấp giữ chỗ (mặc định: 1000)
  inbound_queue_maxsize: 1000
  # Số lượng worker xử lý tin nhắn đến chạy dài hạn, cố định (mặc định: 5)
  max_concurrency: 5
  # Số giây xả hết công việc đã nhận trước khi hủy các handler đang chạy (mặc định: 3)
  shutdown_grace_period_seconds: 3

  # Tùy chọn: thiết lập phiên mặc định toàn cục cho mọi kênh di động
  session:
    assistant_id: lead_agent  # hoặc tên một custom agent; custom agent được định tuyến qua lead_agent + agent_name
    config:
      recursion_limit: 100
    context:
      thinking_enabled: true
      is_plan_mode: false
      subagent_enabled: false

  feishu:
    enabled: true
    app_id: $FEISHU_APP_ID
    app_secret: $FEISHU_APP_SECRET
    # domain: https://open.feishu.cn       # Trung Quốc (mặc định)
    # domain: https://open.larksuite.com   # Quốc tế

  wecom:
    enabled: true
    bot_id: $WECOM_BOT_ID
    bot_secret: $WECOM_BOT_SECRET
    # Tùy chọn: các hậu tố host bổ sung mà media tải về từ tin nhắn đến có thể đi qua,
    # ngoài họ tên miền qq.com có sẵn và host media COS chính thức của WeCom
    # (ww-aibot-img-1258476243.<region>.myqcloud.com); hãy thêm vào đây nếu
    # WeCom chuyển sang một tài khoản COS mới hoặc media đi qua proxy
    allowed_media_hosts: []

  slack:
    enabled: true
    bot_token: $SLACK_BOT_TOKEN     # xoxb-...
    app_token: $SLACK_APP_TOKEN     # xapp-... (Socket Mode)
    allowed_users: []               # rỗng = cho phép tất cả

  telegram:
    enabled: true
    bot_token: $TELEGRAM_BOT_TOKEN
    # Tùy chọn: hiển thị phản hồi Markdown cuối cùng dưới dạng Telegram Rich Message.
    rich_messages: false
    allowed_users: []               # rỗng = cho phép tất cả

  wechat:
    enabled: false
    bot_token: $WECHAT_BOT_TOKEN
    ilink_bot_id: $WECHAT_ILINK_BOT_ID
    qrcode_login_enabled: true      # tùy chọn: cho phép khởi tạo lần đầu bằng QR khi chưa có bot_token
    allowed_users: []               # rỗng = cho phép tất cả
    polling_timeout: 35             # các giá trị thời gian phải là số giây dương và hữu hạn
    polling_retry_delay: 5
    qrcode_poll_interval: 2
    qrcode_poll_timeout: 180
    state_dir: ./.deer-flow/wechat/state
    max_inbound_image_bytes: 20971520
    max_outbound_image_bytes: 20971520
    max_inbound_file_bytes: 52428800
    max_outbound_file_bytes: 52428800
    # Media đến được tải theo kiểu stream với các giới hạn ở trên và chỉ được phép
    # đến từ các hậu tố host này (cộng thêm *.qq.com và host của cdn_base_url theo mặc định)
    allowed_media_hosts: []

    # Tùy chọn: thiết lập phiên theo từng kênh / từng người dùng
    session:
      assistant_id: mobile-agent  # tên custom agent cũng được hỗ trợ ở đây
      context:
        thinking_enabled: false
      users:
        "123456789":
          assistant_id: vip-agent
          config:
            recursion_limit: 150
          context:
            thinking_enabled: true
            subagent_enabled: true

  dingtalk:
    enabled: true
    client_id: $DINGTALK_CLIENT_ID             # Client ID của ứng dụng DingTalk của bạn
    client_secret: $DINGTALK_CLIENT_SECRET     # Client Secret của ứng dụng DingTalk của bạn
    allowed_users: []                          # rỗng = cho phép tất cả
    card_template_id: ""                       # Tùy chọn: ID template AI Card cho hiệu ứng gõ chữ dạng streaming
```

Ghi chú:
- `assistant_id: lead_agent` gọi trực tiếp assistant LangGraph mặc định.
- Nếu `assistant_id` được đặt thành tên một custom agent, DeerFlow vẫn định tuyến qua `lead_agent` và đưa giá trị đó vào làm `agent_name`, nhờ đó SOUL/cấu hình của custom agent có hiệu lực cho các kênh IM.
- Các worker của kênh IM gọi API tương thích LangGraph của Gateway ở bên trong và tự động đính kèm cơ chế xác thực nội bộ cục bộ trong tiến trình cùng cặp cookie/header CSRF cần thiết để tạo thread và lượt chạy.
- Công việc đến bị giới hạn ở `inbound_queue_maxsize` tin nhắn đang chờ cộng với `max_concurrency` worker đang hoạt động. Khi hết sức chứa, các nhà cung cấp dạng socket/polling sẽ bỏ tin nhắn mới trước khi gửi thông báo xác nhận "đang xử lý" của DeerFlow và phát ra một cảnh báo có giới hạn tần suất. Buzz giữ nguyên con trỏ phát lại của nó và kết nối lại để relay phát lại; webhook GitHub trả về `503`, đánh dấu lần giao là thất bại để gửi lại thủ công/qua API. Khi tắt dịch vụ, việc nhận việc mới bị đóng ngay lập tức, các transport của kênh vẫn hoạt động trong lúc những tin nhắn đã nhận được xả hết trong tối đa `shutdown_grace_period_seconds`, rồi các handler đang chạy bị hủy và được chờ hoàn tất trước khi đóng tài nguyên của nhà cung cấp; timeout ở vòng ngoài của Gateway có thể hủy một quá trình tắt chưa hoàn tất mà không tách rời các tài nguyên đó.
- Feishu/Lark giờ đây xếp hàng các tin nhắn nối tiếp nhanh theo từng `thread_id` DeerFlow đã ánh xạ thay vì lập tức hiển thị phản hồi "đang bận" chung chung, và các phản hồi trong topic giữ một thẻ riêng cho mỗi tin nhắn kèm bản xem trước gọn của tin nhắn nguồn, xuyên suốt các trạng thái xếp hàng/đang chạy/kết thúc.

Hãy đặt các API key tương ứng trong tệp `.env` của bạn:

```bash
# Telegram
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ

# Slack
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...

# Feishu / Lark
FEISHU_APP_ID=cli_xxxx
FEISHU_APP_SECRET=your_app_secret

# WeChat iLink
WECHAT_BOT_TOKEN=your_ilink_bot_token
WECHAT_ILINK_BOT_ID=your_ilink_bot_id

# WeCom
WECOM_BOT_ID=your_bot_id
WECOM_BOT_SECRET=your_bot_secret

# DingTalk
DINGTALK_CLIENT_ID=your_client_id
DINGTALK_CLIENT_SECRET=your_client_secret
```

**Thiết lập Telegram**

1. Chat với [@BotFather](https://t.me/BotFather), gửi `/newbot`, rồi sao chép HTTP API token.
2. Đặt `TELEGRAM_BOT_TOKEN` trong `.env` và bật kênh này trong `config.yaml`.
3. Bot nhận được văn bản, ảnh và tài liệu đến (có hoặc không có chú thích). Việc tải xuống qua Bot API được host giới hạn ở 20 MB cho mỗi tệp đính kèm.

**Thiết lập Slack**

1. Tạo một Slack App tại [api.slack.com/apps](https://api.slack.com/apps) → Create New App → From scratch.
2. Trong **OAuth & Permissions**, thêm các Bot Token Scope: `app_mentions:read`, `chat:write`, `im:history`, `im:read`, `im:write`, `files:write`.
3. Bật **Socket Mode** → tạo một App-Level Token (`xapp-…`) với scope `connections:write`.
4. Trong **Event Subscriptions**, đăng ký các sự kiện bot: `app_mention`, `message.im`.
5. Đặt `SLACK_BOT_TOKEN` và `SLACK_APP_TOKEN` trong `.env` và bật kênh này trong `config.yaml`.

**Thiết lập Feishu / Lark**

1. Tạo một ứng dụng trên [Feishu Open Platform](https://open.feishu.cn/) → bật năng lực **Bot**.
2. Thêm các quyền: `im:message`, `im:message.p2p_msg:readonly`, `im:resource`.
3. Trong **Events**, đăng ký `im.message.receive_v1` và chọn chế độ **Long Connection**.
4. Sao chép App ID và App Secret. Đặt `FEISHU_APP_ID` và `FEISHU_APP_SECRET` trong `.env` và bật kênh này trong `config.yaml`.
5. Bot hỗ trợ tin nhắn văn bản, ảnh và tệp đến. Việc tải tệp đính kèm đến được giới hạn ở 20 MB cho mỗi tệp.

**Thiết lập WeChat**

1. Bật kênh `wechat` trong `config.yaml`.
2. Hoặc đặt `WECHAT_BOT_TOKEN` trong `.env`, hoặc đặt `qrcode_login_enabled: true` để khởi tạo lần đầu bằng mã QR.
3. Khi không có `bot_token` và đã bật khởi tạo bằng QR, hãy theo dõi log backend để lấy nội dung QR do iLink trả về rồi hoàn tất luồng liên kết.
4. Sau khi luồng QR thành công, DeerFlow lưu token thu được vào `state_dir` để dùng cho các lần khởi động lại sau.
5. Với các bản triển khai Docker Compose, hãy đặt `state_dir` trên một volume bền vững để con trỏ `get_updates_buf` và trạng thái xác thực đã lưu không bị mất khi khởi động lại.

**Thiết lập WeCom**

1. Tạo một bot trên nền tảng WeCom AI Bot và lấy `bot_id` cùng `bot_secret`.
2. Bật `channels.wecom` trong `config.yaml` và điền `bot_id` / `bot_secret`.
3. Đặt `WECOM_BOT_ID` và `WECOM_BOT_SECRET` trong `.env`.
4. Hãy đảm bảo các phụ thuộc backend có `wecom-aibot-python-sdk`. Kênh này dùng kết nối WebSocket dài hạn và không cần URL callback công khai.
5. Bản tích hợp hiện tại hỗ trợ tin nhắn văn bản, ảnh và tệp đến. Ảnh/tệp cuối cùng do agent tạo ra cũng được gửi ngược lại cuộc hội thoại WeCom.

**Thiết lập DingTalk**

1. Tạo một ứng dụng DingTalk trong [DingTalk Developer Console](https://open.dingtalk.com/) và bật năng lực **Robot**.
2. Đặt chế độ nhận tin nhắn thành **Stream Mode** trong trang cấu hình robot.
3. Sao chép `Client ID` và `Client Secret`, đặt `DINGTALK_CLIENT_ID` và `DINGTALK_CLIENT_SECRET` trong `.env`, rồi bật kênh này trong `config.yaml`.
4. *(Tùy chọn)* Để bật phản hồi AI Card dạng streaming (hiệu ứng gõ chữ), hãy tạo một template **AI Card** trên [DingTalk Card Platform](https://open.dingtalk.com/document/dingstart/typewriter-effect-streaming-ai-card), rồi đặt `card_template_id` trong `config.yaml` thành ID của template đó. Bạn cũng cần xin cấp quyền `Card.Streaming.Write` và `Card.Instance.Write`.


Khi DeerFlow chạy trong Docker Compose, các kênh IM thực thi bên trong container `gateway`. Trong trường hợp đó, đừng trỏ `channels.langgraph_url` hay `channels.gateway_url` tới `localhost`; hãy dùng tên dịch vụ của container như `http://gateway:8001/api` và `http://gateway:8001`, hoặc đặt `DEER_FLOW_CHANNELS_LANGGRAPH_URL` và `DEER_FLOW_CHANNELS_GATEWAY_URL`.

**Các lệnh**

Khi một kênh đã được kết nối, bạn có thể tương tác với DeerFlow ngay trong cuộc chat:

| Lệnh | Mô tả |
|---------|-------------|
| `/new` | Bắt đầu một cuộc hội thoại mới |
| `/status` | Hiển thị thông tin thread hiện tại |
| `/models` | Liệt kê các model khả dụng |
| `/memory` | Xem bộ nhớ |
| `/agent list` | Liệt kê các Custom Agent của bạn |
| `/agent use <name>` | Bắt đầu một cuộc hội thoại mới với một Custom Agent |
| `/help` | Hiển thị trợ giúp |

> Những tin nhắn không có tiền tố lệnh được xem là chat thông thường — DeerFlow sẽ tạo một thread và trả lời theo kiểu hội thoại.

Việc chọn agent có phạm vi theo cuộc hội thoại: `/agent use <name>` bắt đầu một cuộc hội thoại mới và ghim Custom Agent đó vào metadata của thread. Các cuộc hội thoại đang có không bao giờ đổi agent giữa chừng, lựa chọn này vẫn tồn tại sau khi khởi động lại Gateway, và việc mở thread được tạo từ IM trong Web UI sẽ tiếp tục với đúng Custom Agent đó.
Dùng `/agent use lead_agent` để quay về agent mặc định trong một cuộc hội thoại mới.

#### Tương quan trace của request

Mọi phản hồi HTTP của Gateway đều mang header `X-Trace-Id`. ID này được kế thừa
từ `X-Trace-Id` ở request đến khi bên gọi có gửi, và được sinh ra trong trường hợp ngược lại, nên
một proxy hoặc một dịch vụ upstream có thể ghim một ID duy nhất xuyên suốt các dịch vụ. Nó không cần
cấu hình gì và không thể tắt.

Chính ID đó vẫn được gắn với những phần việc sống lâu hơn phản hồi HTTP: tác vụ chạy
đã tách rời, mọi subagent mà nó ủy quyền, và các thread cập nhật bộ nhớ chạy nền.
Nó được ghi lại dưới dạng `deerflow_trace_id` trên bản ghi lượt chạy (nhìn thấy được qua API runs),
trong metadata checkpoint của thread, và trong các trace của Langfuse. Các tác vụ theo lịch, các lượt chạy
thông báo tác vụ MCP và tin nhắn kênh IM khởi đầu bên ngoài HTTP nên tự sinh
ID riêng cho từng lần xảy ra.

Các bản ghi log chỉ mang ID đó khi bật logging nâng cao:

```yaml
logging:
  enhance:
    enabled: true   # in trace_id vào các bản ghi log
    format: text    # hoặc json
```

Mặc định tắt vì bật nó sẽ làm thay đổi định dạng log. `logging` là
thiết lập cần khởi động lại, nên hãy sửa `config.yaml` rồi khởi động lại Gateway. Thiết lập này
chỉ ảnh hưởng đến đầu ra log — ID, header phản hồi và metadata của lượt chạy đều không bị ảnh hưởng.

`deerflow_trace_id` là một ID tương quan của DeerFlow: nó không phải run id, và cũng không phải
trace id native của nhà cung cấp. Nó cũng không phải khóa tra cứu — không có gì phân giải được một
thread hay một lượt chạy từ nó; hãy dùng nó để đối chiếu các dòng log. Một `deerflow_trace_id` được gửi
trong `metadata` hoặc `config.context` của một yêu cầu chạy sẽ bị bỏ qua và ghi đè, nên
header phản hồi, log và lượt chạy đã lưu không bao giờ mâu thuẫn nhau. Để ghim một
ID tương quan, hãy gửi header `X-Trace-Id`.

Lịch sử chạy của Gateway cũng ghi lại một biên nhận `run.delivery` cuối cùng cho mỗi lượt chạy,
kể cả những lượt chạy không sinh đầu ra và những lượt được khôi phục sau sự cố. Biên nhận được lưu trước
trạng thái kết thúc bền vững của lượt chạy trong quá trình thực thi bình thường. Việc khôi phục lượt chạy mồ côi
trước tiên giành lấy một lease đã hết hạn một cách nguyên tử, rồi điền bù biên nhận theo kiểu idempotent,
nên một lần quét khôi phục lỗi thời không thể ghi đè lên dữ liệu giao hàng chi tiết của một lượt chạy đang sống.
Việc lưu biên nhận vẫn ở mức "cố gắng hết sức" khi kho sự kiện gặp sự cố. Những lượt chạy
không qua được bước tiền kiểm checkpoint (hoặc bị hủy trong lúc chờ quá trình hoàn tất trước đó)
vẫn giữ hành vi hiện tại đối với dữ liệu hoàn tất: chúng nhận được biên nhận
không-giao-gì nhưng không ghi đè các trường hoàn tất của RunStore bằng một snapshot rỗng.

Khi `tool_progress.enabled` là true, cùng lịch sử sự kiện của lượt chạy đó cũng ghi lại
các thay đổi pha của bộ bảo vệ chất lượng kết quả. Nó ghi lại các quyết định phát hiện vòng lặp và
việc đưa các tool MCP bị hoãn lên trước, cho cả lead agent lẫn các subagent `task` thông thường.
Các sự kiện đưa-lên-trước nêu tên những tool bị hoãn vừa được kích hoạt và cho biết chúng được chọn bởi
metadata định tuyến hay bởi `tool_search`, mà không sao chép truy vấn tìm kiếm, từ khóa định tuyến,
schema, đối số, kết quả hay hash catalog vào chính sự kiện đó.

#### LangSmith Tracing

DeerFlow có sẵn tích hợp [LangSmith](https://smith.langchain.com) để phục vụ khả năng quan sát. Khi được bật, mọi lệnh gọi LLM, lượt chạy agent và lần thực thi tool đều được trace và hiển thị trong bảng điều khiển LangSmith.

Thêm các dòng sau vào tệp `.env` của bạn:

```bash
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=lsv2_pt_xxxxxxxxxxxxxxxx
LANGSMITH_PROJECT=xxx
```

#### Langfuse Tracing

DeerFlow cũng hỗ trợ khả năng quan sát bằng [Langfuse](https://langfuse.com) cho các lượt chạy tương thích LangChain.

Thêm các dòng sau vào tệp `.env` của bạn:

```bash
LANGFUSE_TRACING=true
LANGFUSE_PUBLIC_KEY=pk-lf-xxxxxxxxxxxxxxxx
LANGFUSE_SECRET_KEY=sk-lf-xxxxxxxxxxxxxxxx
LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

Nếu bạn dùng một instance Langfuse tự host, hãy đặt `LANGFUSE_BASE_URL` thành URL triển khai của bạn.

**Các trường tương quan trace.** Mỗi lượt chạy agent đều được chú thích bằng các thuộc tính trace dành riêng của Langfuse để trang Sessions và Users tự động hiển thị dữ liệu:

- `session_id` = `thread_id` của LangGraph — gom mọi trace của cùng một cuộc hội thoại
- `user_id` = người dùng hiệu dụng từ `get_effective_user_id()` (quay về `default` ở chế độ không xác thực)
- `trace_name` = assistant id (mặc định là `lead-agent`)
- `tags` = `[env:<DEER_FLOW_ENV>, model:<model_name>]` (bị bỏ qua khi không được đặt)
- `metadata.deerflow_trace_id` = ID tương quan request của DeerFlow, khớp với `X-Trace-Id` khi bật tính năng tương quan trace của request

Chúng được đưa vào `RunnableConfig.metadata` tại gốc lệnh gọi graph cho cả đường đi qua gateway (`runtime/runs/worker.py::run_agent`) lẫn đường đi nhúng (`client.py::DeerFlowClient.stream`), nên bất kỳ callback tương thích LangChain nào cũng đọc được. Hãy đặt `DEER_FLOW_ENV` (hoặc `ENVIRONMENT`) để gắn tag trace theo môi trường triển khai.

#### Monocle Tracing

DeerFlow cũng hỗ trợ [Monocle](https://github.com/monocle2ai/monocle), một tracer dựa trên OpenTelemetry dành cho ứng dụng agentic. Nó ghi lại mỗi lượt chạy từ đầu đến cuối: các lệnh gọi LLM, các bước của agent, cùng các lần gọi tool và MCP, kèm đầu vào, đầu ra, thời gian và số token.

Thêm các dòng sau vào tệp `.env` của bạn:

```bash
MONOCLE_TRACING=true
MONOCLE_EXPORTERS=file          # file, console, okahu, s3, blob, gcs (mặc định: file)
OKAHU_API_KEY=okh_xxxxxxxx      # chỉ bắt buộc với exporter `okahu`
```

Mỗi lượt chạy ghi ra một tệp trace trong `.monocle/`; hãy mở nó bằng [tiện ích mở rộng Monocle cho VS Code](https://marketplace.visualstudio.com/items?itemName=OkahuAI.monocle-apptrace) để xem dòng thời gian của các span và số token. Kết nối tới [Okahu](https://www.okahu.ai), một nền tảng quan sát agent, để phân tích trace qua nhiều lượt chạy và chạy các bài đánh giá dựa trên trace và dạng agentic (thông qua exporter `okahu`).

Trace ghi lại nguyên văn đầu vào và đầu ra của các span — prompt, đối số tool và phản hồi của model — cùng với mức dùng token và thời gian. Exporter `file` giữ chúng trên đĩa cục bộ và không bao giờ xoay vòng hay dọn dẹp, nên hãy định kỳ dọn bớt `.monocle/`; các exporter từ xa (`okahu`, `s3`, `blob`, `gcs`) gửi chính dữ liệu đó ra ngoài máy, nên chỉ bật những đích đến mà bạn tin tưởng. Monocle được khởi tạo một lần lúc Gateway khởi động: lỗi cấu hình (exporter không xác định, thiếu `OKAHU_API_KEY`) sẽ được ghi log ở đó và tracing vẫn tắt cho đến khi Gateway khởi động lại.

#### Dùng nhiều nhà cung cấp

LangSmith và Langfuse gắn vào dưới dạng callback của LangChain, nên bạn có thể bật cả hai và DeerFlow sẽ báo cáo mỗi lượt chạy tới cả hai. Nếu một nhà cung cấp đã bật bị thiếu thông tin đăng nhập bắt buộc hoặc khởi tạo thất bại, DeerFlow sẽ dừng ngay và nêu đích danh nhà cung cấp đó. Monocle dùng một OpenTelemetry provider toàn cục thay vì callback; Langfuse cũng dùng chung provider đó, nên cả ba có thể chạy cùng nhau. Vì cả hai span processor nằm trên cùng một provider dùng chung, các exporter của Monocle cũng nhìn thấy span của Langfuse khi cả hai cùng được bật.

Với các bản triển khai Docker, tracing mặc định bị tắt. Hãy đặt `LANGSMITH_TRACING=true` và `LANGSMITH_API_KEY` trong `.env` để bật.

#### Hành động trên stream của lượt chạy đang có

Việc tham gia SSE vào một lượt chạy đang có chỉ mang tính quan sát với `GET`: truyền
`action=interrupt|rollback` sẽ trả về `405`. Việc hủy trên tuyến stream này chỉ
dùng `POST` và yêu cầu quyền `runs:cancel`. Tương ứng, hợp đồng OpenAPI
chỉ phơi ra `action` và `wait` trên `POST`; thao tác `GET` chỉ phơi ra
các tham số đường dẫn của nó.

#### Personal Access Token

Các client phi tương tác (pipeline CI, script, tích hợp server-to-server)
có thể gọi Gateway API bằng một **personal access token (PAT)** thay vì
phiên trình duyệt. Hãy tạo một token khi đang đăng nhập qua `POST /api/v1/auth/pats` —
giá trị `dfp_...` thô chỉ hiển thị đúng một lần; chỉ bản tóm tắt SHA-256 của nó được lưu —
rồi gửi nó dưới dạng thông tin đăng nhập Bearer:

```http
POST /api/threads/search
Authorization: Bearer dfp_...
Content-Type: application/json

{}
```

Mỗi token chạy với danh tính của người dùng sở hữu nó (việc lọc theo chủ sở hữu và
bộ nhớ theo từng người dùng vẫn hoạt động), mang theo một tập scope chỉ có thể thu hẹp quyền
của người dùng đó, và chỉ được phép đi vào các tuyến thuộc vòng đời thread/lượt chạy — mọi
tuyến khác đều trả về `403` cho bên gọi bằng PAT, và PAT không bao giờ mang
năng lực quản trị. Token có thể được liệt kê và thu hồi bất cứ lúc nào; việc thu hồi có hiệu lực
ngay lập tức. PAT yêu cầu một backend cơ sở dữ liệu (SQLite/PostgreSQL). Tài liệu
đầy đủ: [API Reference — Personal Access Tokens](backend/docs/API.md#personal-access-tokens).

## Từ Deep Research đến Super Agent Harness

DeerFlow khởi đầu là một framework Deep Research — và cộng đồng đã đẩy nó đi xa hơn rất nhiều. Kể từ khi ra mắt, các lập trình viên đã dùng nó vượt xa phạm vi nghiên cứu: xây dựng data pipeline, tạo slide thuyết trình, dựng dashboard, tự động hóa quy trình nội dung. Những điều chúng tôi chưa từng lường trước.

Điều đó cho chúng tôi một bài học quan trọng: DeerFlow không chỉ là một công cụ nghiên cứu. Nó là một **harness** — một runtime cung cấp cho agent hạ tầng để thực sự hoàn thành công việc.

Vì vậy chúng tôi đã xây dựng lại nó từ đầu.

DeerFlow 2.0 không còn là một framework mà bạn phải tự ráp nối. Nó là một super agent harness — đầy đủ pin sẵn, hoàn toàn mở rộng được. Được xây trên LangGraph và LangChain, nó đi kèm mọi thứ một agent cần ngay từ đầu: một hệ thống tệp, bộ nhớ, skill, khả năng thực thi có nhận biết sandbox, cùng khả năng lập kế hoạch và sinh ra sub-agent cho những tác vụ phức tạp, nhiều bước.

Dùng nó nguyên trạng. Hoặc tháo tung ra và biến nó thành của riêng bạn.

## Tính năng cốt lõi

### Skill & Tool

Mở **Capability Center** từ thanh bên của workspace để quản lý **Plugins**
(các MCP server và tích hợp Lark/Feishu) và **Skills**. Cả hai danh mục đều hỗ trợ
tìm kiếm; thẻ skill hiển thị mô tả ngắn gọn, còn mô tả đầy đủ nằm trong khung xem chi tiết.
Skill dựng sẵn và skill do người dùng tạo/nhập được liệt kê riêng. Tab
Community hỗ trợ nhập các gói `.skill` vào My skills.
Các tùy chọn chung vẫn nằm trong Settings.

Skill chính là thứ khiến DeerFlow có thể làm *gần như mọi thứ*.

Một Agent Skill chuẩn là một mô-đun năng lực có cấu trúc — một tệp Markdown định nghĩa một quy trình làm việc, các thực hành tốt nhất, và các tham chiếu tới tài nguyên hỗ trợ. DeerFlow đi kèm các skill dựng sẵn cho nghiên cứu, tạo báo cáo, tạo slide, trang web, tạo ảnh và video, cùng nhiều thứ khác. Nhưng sức mạnh thực sự nằm ở khả năng mở rộng: thêm skill của riêng bạn, thay thế skill dựng sẵn, hoặc kết hợp chúng thành các quy trình phức hợp.

Skill được nạp dần dần — chỉ khi tác vụ cần đến, chứ không phải nạp tất cả cùng lúc. Nhờ vậy cửa sổ ngữ cảnh luôn gọn nhẹ và DeerFlow hoạt động tốt ngay cả với những model nhạy cảm về token.

Khi bật cơ chế khám phá skill theo kiểu hoãn lại, `describe_skill` xếp hạng các skill đã cài dựa trên mức độ bao phủ các từ khóa ý định đã chuẩn hóa Unicode và có giới hạn, trên cả tên lẫn mô tả. Nhờ đó những yêu cầu tự nhiên gồm nhiều từ vẫn tìm được skill phù hợp mà không cần đúng một cụm từ chính xác, trong khi cách tra cứu chính xác `select:` và `+prefix` yêu-cầu-đúng-tên vẫn dùng được. Các lượt tìm kiếm có xếp hạng dùng tối đa 256 ký tự và trả về tối đa năm kết quả; danh sách `select:` chính xác không bị cắt bớt và trả về mọi mục khớp trong catalog.

Một thư mục skill là một ranh giới gói: khi DeerFlow đã tìm thấy `SKILL.md` của nó, các tệp `SKILL.md` lồng bên trong gói đó (ví dụ các fixture dùng để đánh giá) vẫn chỉ là dữ liệu hỗ trợ và không được đăng ký thành skill lúc chạy. Các thư mục namespace không có `SKILL.md` riêng vẫn có thể dùng để nhóm các skill lồng bên trong.

Markdown của skill và các tài nguyên văn bản đi kèm dùng UTF-8. CLI skill-creator và các tiện ích rà soát đọc và ghi văn bản một cách tường minh dưới dạng UTF-8, nên các skill đã bản địa hóa hoạt động nhất quán trên mọi hệ điều hành.

Người dùng có thể kích hoạt tường minh một skill đang bật cho đúng một lượt bằng cách bắt đầu yêu cầu với `/tên-skill`, ví dụ `/data-analysis analyze uploads/foo.csv`. DeerFlow sẽ nạp `SKILL.md` của skill đó làm ngữ cảnh ẩn cho lượt hiện tại, trong khi prompt nền vẫn chỉ giới hạn ở metadata của skill. Việc kích hoạt bằng dấu gạch chéo vẫn tôn trọng các skill bị tắt, danh sách trắng skill của custom agent, và các lệnh kênh sẵn có như `/new` và `/help`.

Sau khi một câu trả lời đã nạp skill, thanh công cụ của nó có mục **Skills used**. Hãy rê chuột hoặc bấm vào biểu tượng để xem các skill và nguồn của chúng; rê chuột lên tên một skill sẽ gạch chân nó. Chọn một skill để xem `SKILL.md` của nó trong bảng bên có thể thay đổi kích thước (dạng ngăn kéo trên di động). Khung nhìn này dùng các snapshot được ghi lại trong những lần nạp thành công bằng tool đọc đã cấu hình hoặc bằng kích hoạt gạch chéo tường minh, nên việc chỉnh sửa hay gỡ bỏ skill sau này không làm thay đổi lịch sử của nó. Các lần nạp lặp lại chỉ xuất hiện một lần cho mỗi lượt chạy, theo thứ tự nạp lần đầu. Các lần đọc theo khoảng và các snapshot có giới hạn được ghi nhãn là một phần; những cuộc hội thoại cũ không có bằng chứng được ghi lại sẽ không hiển thị menu này. Thao tác sao chép trả về đúng phần Markdown đã ghi lại, bao gồm cả YAML frontmatter. Các liên kết và ảnh tương đối trong gói vẫn là tham chiếu đọc được chứ không điều hướng bạn rời khỏi cuộc hội thoại. Những lần nạp skill thực hiện qua công cụ khác, chẳng hạn lệnh shell, sẽ không được suy đoán từ nội dung câu trả lời.

Chính sách `allowed-tools` của một skill đang bật chỉ có hiệu lực sau khi skill đó được kích hoạt tường minh bằng dấu gạch chéo hoặc được ghi nhận vào ngữ cảnh skill đang hoạt động của agent sau một lần nạp bằng `read_file`. Việc chỉ bật, quảng bá, hay liệt kê một skill trong danh sách `skills` cho phép của một custom agent hoặc subagent không làm thu hẹp bộ tool thông thường của agent đó; subagent dùng chung chính sách khám phá dần và kích hoạt giống như lead agent. Trong một lượt chạy được kích hoạt bằng gạch chéo, chính sách của skill tường minh đó là tối thượng: việc đọc một `SKILL.md` khác có thể cung cấp chỉ dẫn nhưng không thể mở rộng bộ tool của skill gạch chéo. Khi không có kích hoạt gạch chéo, chính sách của những skill thực sự được nạp vào ngữ cảnh đang hoạt động vẫn giữ ngữ nghĩa hợp (union). Khi đã có hiệu lực, chính sách lọc cả schema tool mà model nhìn thấy lẫn việc thực thi tool. Các tool khám phá của framework (`tool_search` và `describe_skill`) vẫn khả dụng để một tool bị hoãn được phép hoặc một skill đã cài vẫn có thể được tìm thấy, nhưng việc khám phá và đưa lên trước không bao giờ cấp quyền thực thi một tool nghiệp vụ không có trong `allowed-tools`. `task` không được miễn trừ như tool framework; một skill có chính sách hạn chế phải liệt kê nó tường minh thì mới ủy quyền được cho subagent. Các quyết định chính sách theo từng bước là ngữ cảnh runtime nội bộ và bị loại khỏi các bản sao ngữ cảnh có thể quan sát hoặc được lưu lại. Lỗi registry và một tập đang hoạt động không còn skill hợp lệ nào sẽ "hỏng theo hướng an toàn", quay về các tool an toàn của framework; các đường dẫn lỗi thời riêng lẻ chỉ bị bỏ qua khi vẫn còn một skill đang hoạt động hợp lệ khác. Đây là cơ chế khoanh vùng hành vi ở mức "cố gắng hết sức", không phải một ranh giới bảo mật cứng: việc nạp chỉ dẫn skill thông qua một tool khác sẽ không được ghi nhận, và các mục skill đang hoạt động có thể bị đẩy ra khỏi ngữ cảnh có giới hạn.

Khi bạn cài các gói `.skill` thông qua Gateway, DeerFlow chấp nhận `allowed-tools` dạng chuẩn phân tách bằng khoảng trắng, metadata frontmatter tùy chọn, và trường `argument-hint` tương thích Claude, thay vì từ chối những skill bên ngoài vốn hợp lệ. Danh sách YAML vẫn được hỗ trợ cho `allowed-tools` và giữ nguyên chính xác tên lúc chạy. Các cách viết khả chuyển chính xác như `WebFetch`, `WebSearch`, `Glob`, `Grep` và `Read` được ánh xạ sang các tool `web_fetch`, `web_search`, `glob`, `grep` và `read_file` của DeerFlow; các tên vô hướng viết thường hoặc không xác định vẫn được giữ nguyên để các tool tùy chỉnh và MCP giữ đúng cách viết lúc chạy. Các mục nằm trong ngoặc như `Bash(tvly *)` được xem là một mục nguyên văn duy nhất, gồm cả khoảng trắng, văn bản trong dấu nháy và dấu ngoặc đã escape, nhưng chúng không có hiệu lực vì DeerFlow không xem xét đối số của tool; hãy khai báo `bash` chỉ khi skill được phép dùng toàn bộ tool Bash.

Việc tắt một skill cũng loại nó khỏi khung nhìn hệ thống tệp của sandbox, nên các lệnh shell và các tool tệp có cấu trúc đều tuân theo cùng một trạng thái bật/tắt. Sandbox Local, Docker/AIO, provisioner hostPath và các sandbox E2B mới tạo đều lấy `/mnt/skills` từ các phép chiếu chỉ-gồm-skill-đang-bật, và các phép chiếu này cập nhật khi skill công khai, tùy chỉnh, kiểu cũ hoặc skill tích hợp được quản lý bị bật/tắt, sửa, tạo, xóa hay cài đặt. Các lệnh gọi `read_file` có cấu trúc (bao gồm cả đọc theo khoảng dòng và kiểm tra đọc-trước-khi-ghi) dùng ánh xạ mount của nhà cung cấp sandbox, nên danh tính người dùng được ghi nhận lúc lấy sandbox vẫn là nguồn chân lý. Các gói tích hợp được quản lý vẫn dùng chung, trong khi mức hiển thị của chúng trên hệ thống tệp được chiếu theo trạng thái bật/tắt của từng người dùng. Các Gateway nhiều worker sẽ đọc lại trạng thái bật/tắt trên đĩa trong lúc dựng lại phép chiếu cho người dùng, nên một thao tác bật/tắt do một worker xử lý sẽ được worker khác tôn trọng ở lần lấy sandbox kế tiếp. Các sandbox E2B đang tồn tại giữ nguyên snapshot lúc tạo cho đến khi chúng được tạo lại. Các skill dùng provisioner dựa trên PVC hiện vẫn giữ snapshot/bố cục PVC đã cấu hình; việc hiện thực hóa PVC động được theo dõi riêng.

Với `LocalSandboxProvider`, đây là một ranh giới đường-đi-tool được quản lý, chứ không phải cách ly hệ thống tệp của máy chủ. Các chính sách skill tường minh theo từng Agent chỉ được chấp nhận khi bash trên máy chủ bị tắt (mặc định), vì một tiến trình con trên máy chủ có thể truy cập trực tiếp các đường dẫn thật mà không đi qua ánh xạ đường-dẫn-ảo của nhà cung cấp. Hãy dùng Docker/AIO, provisioner Kubernetes, hoặc E2B khi ranh giới hệ thống tệp phải được thực thi nghiêm ngặt song song với quyền truy cập shell.

Các tích hợp được quản lý cài đặt những gói skill chỉ-đọc dùng chung mà không trộn lẫn
vào skill tùy chỉnh. Tích hợp Lark/Feishu CLI nằm ở
`Capability Center → Plugins → Lark / Feishu`; quản trị viên cài đặt hoặc
nâng cấp gói `lark-*` chính thức một lần tại
`{DEER_FLOW_HOME}/integrations/skills/lark-cli`, và mọi người dùng đều nhìn thấy
đúng gói đó với trạng thái bật/tắt độc lập. Cấu hình ứng dụng và
dữ liệu OAuth của mỗi người dùng được cách ly tại
`{DEER_FLOW_HOME}/users/{user_id}/integrations/lark-cli/{config,data}`. Các
thư mục chứa bí mật này bị giới hạn quyền ở `0700`, các tệp thông tin đăng nhập thông thường ở
`0600`, và các symlink bị từ chối.

Sau khi cài đặt, người dùng có thể bấm **Connect Lark** để mở một liên kết
ủy quyền trên trình duyệt; không cần ủy quyền qua terminal. Cùng giao diện đó có thể
yêu cầu thêm các miền quyền như Calendar, Docs hay Drive, hoặc một
scope OAuth cụ thể do `lark-cli` báo cáo. Một lần làm mới trạng thái "rẻ tiền" chỉ
kiểm tra cây thông tin đăng nhập cục bộ, nên giao diện sẽ báo **Credentials configured
(not live-verified)** cho đến khi một lần hoàn tất tường minh trên trình duyệt thực hiện xác minh token trực tiếp.
Khi đó hành động sẽ chuyển thành **Reconnect Lark** để người dùng có thể thay thế
hoặc mở rộng ủy quyền. Nếu một agent gặp tình trạng thiếu ủy quyền Lark trong lúc
hội thoại, phần hướng dẫn `lark-shared` được quản lý sẽ chỉ người dùng quay lại
đúng phần cấu hình plugin đó với `/workspace/capabilities?tab=plugins&plugin=lark`.

Khi đã cấu hình xong, **Change Lark app** cho phép người dùng trỏ tài khoản DeerFlow của họ sang
một ứng dụng Lark/Feishu khác mà không cần cài lại — bằng cách dán App ID / App Secret
của một ứng dụng sẵn có, hoặc đăng ký lại một ứng dụng trên trình duyệt. Việc chuyển đổi
áp dụng theo từng người dùng (không bao giờ đụng đến thông tin đăng nhập của người khác), kiểm tra thông tin
đăng nhập mới bằng lần dò tenant-token trực tiếp của CLI chính thức trước khi thay thế
ứng dụng đang dùng, rồi thu hồi/xóa các token OAuth của ứng dụng cũ. Một thay đổi
thông tin đăng nhập bị từ chối sẽ không ghi đè lên một luồng thiết lập hay ủy quyền đang diễn ra.
Dữ liệu OAuth cũ được xóa trước khi CLI lưu ứng dụng thay thế,
để bí mật keychain dựa trên tệp mới vẫn khả dụng trong lúc kết nối lại.
Sau đó DeerFlow lập tức mở trang ủy quyền trên trình duyệt cho ứng dụng vừa liên kết,
để việc chuyển đổi kết thúc bằng một kết nối dùng được.

Việc cài gói skill Lark sẽ phân giải bản phát hành `larksuite/cli` chính thức mới nhất
từ GitHub và tải các skill của phiên bản đó ngay lúc cài, nên
Gateway cần truy cập Internet hướng ra ngoài cho bước này (nó sẽ quay về một phiên bản
được ghim làm "đáy" nếu việc tra cứu bản phát hành thất bại). Trang cài đặt hiển thị
phiên bản đã cài và, khi có thể, phiên bản mới nhất được công bố, để quản trị viên
có thể cài lại nhằm nâng cấp. Các bản triển khai không kết nối Internet có thể chuẩn bị sẵn gói lưu trữ
rồi trỏ `DEER_FLOW_LARK_CLI_SKILLS_ARCHIVE` tới tệp cục bộ đó. Tính toàn vẹn
không phụ thuộc vào một hash byte cố định của gói lưu trữ (GitHub không đảm bảo các byte của gói
mã nguồn là ổn định); thay vào đó, việc tải xuống bị giới hạn ở đúng host GitHub
chính thức, mọi thành phần trong gói đều phải vượt qua các rào an toàn về cấu trúc, và một hash nội dung
của cây skill thực sự được cài (bao gồm cả phần hướng dẫn dùng chung mà DeerFlow chèn vào)
được ghi lại để các thay đổi nội dung có thể kiểm toán qua nhiều lần cài lại.

Khi `sandbox.use` chọn nhà cung cấp AIO, cùng lần cài đặt đó cũng tải về
các gói phát hành CLI chính thức cho Linux amd64 và arm64, xác minh
checksum SHA-256 đã công bố của chúng, trích xuất an toàn một tệp thực thi cho mỗi kiến trúc,
rồi mount runtime thu được ở chế độ chỉ-đọc tại `/mnt/integrations/lark-cli/runtime`. Một
launcher tự chọn kiến trúc nằm trong mount đó giúp `lark-cli` có mặt trong `PATH` của sandbox.
Các bản triển khai AIO không kết nối Internet có thể chuẩn bị sẵn một cây runtime không chứa symlink
gồm `bin/lark-cli` cùng cả hai tệp `linux-{amd64,arm64}/lark-cli`, rồi
đặt `DEER_FLOW_LARK_CLI_SANDBOX_RUNTIME_DIR` trỏ tới thư mục đó.

> **Ranh giới tin cậy của sandbox:** trình duyệt không bao giờ nhận được app secret của Lark, nhưng
> các cuộc hội thoại với agent chạy `lark-cli` bên trong sandbox, nên các thư mục
> thông tin đăng nhập theo từng người dùng được mount vào đó: `config` (chứa `appSecret`
> dài hạn) được mount **chỉ-đọc**, thư mục con `config/locks` vốn rỗng của nó
> được mount đè ở chế độ ghi được để phục vụ các tệp phối hợp của `lark-cli`, và
> `data` (các token OAuth có thể làm mới) thì ghi được. Các mount config và data chứa
> thông tin đăng nhập vẫn *đọc được* bởi bất kỳ tiến trình nào agent chạy ở đó, nên mã
> được kích hoạt qua prompt injection trong một kết quả tool có thể đọc được chúng. Hãy xem
> sandbox là nằm bên trong ranh giới tin cậy của thông tin đăng nhập Lark cho đến khi bản cập nhật
> tiếp theo về sidecar môi giới thông tin đăng nhập loại bỏ các mount này khỏi việc thực thi sandbox.

Với các bản triển khai từ xa/Kubernetes (backend provisioner), runtime
`lark-cli` trong sandbox có thể được cung cấp bởi một init container tùy chọn, container này
sao chép các tệp nhị phân vào một `emptyDir` dùng chung — không cần tải từ GitHub lúc cài và
không cần mount runtime kiểu hostPath/PVC. Hãy publish image nằm ở
[`docker/lark-cli-init`](docker/lark-cli-init/README.md) và đặt
`LARK_CLI_INIT_IMAGE` trên provisioner; nếu không đặt thì tính năng vẫn tắt (hành vi cũ).
Trạng thái tích hợp Lark (`GET /api/integrations/lark/status`) báo cáo
`sandbox_runtime_mode` và `sandbox_runtime_ready` để giao diện Settings cho biết
`lark-cli` có thực sự hiện diện trong sandbox lúc chat hay không, thay vì một trạng thái
màu xanh che giấu một lỗi `command not found` xuất hiện sau đó.

Nếu một người vận hành đáng tin quản lý thư mục skill đã cấu hình thông qua một mount bên ngoài như MinIO, NFS hay CSI, quản trị viên có thể gọi `POST /api/skills/reload` sau khi thay đổi tệp. Lệnh này vô hiệu hóa cache prompt của skill cho tiến trình Gateway hiện tại và chờ tối đa đến hết thời gian làm mới có giới hạn, để các lượt chạy sau đó quét lại các tệp mới nhất; các tác vụ đang chạy không bị ảnh hưởng. Một lỗi hệ thống tệp ở tầng loader sẽ trả về lỗi server chung chung và giữ lại cache tiến trình được nạp thành công lần cuối, thay vì công bố một catalog rỗng. Mỗi worker Uvicorn và mỗi Pod Kubernetes đều phải được nhắm tới riêng. Việc ghi trực tiếp vào mount sẽ bỏ qua bước kiểm tra, SkillScan và lịch sử mà các API cài đặt/chỉnh sửa của DeerFlow áp dụng, nên chỉ những hệ thống do người vận hành kiểm soát mới nên có quyền ghi.

Việc cài skill và các chỉnh sửa skill do agent thực hiện đều đi qua **SkillScan**, một bộ quét an toàn xác định (deterministic) chạy native trước bộ quét skill dựa trên LLM. Giai đoạn 1 chạy offline mà không cần phụ thuộc Semgrep/OpenGrep, chặn các phát hiện `CRITICAL` có độ tin cậy cao như khóa riêng tư hay việc thực thi shell, và chuyển các phát hiện mức cảnh báo cho bộ quét LLM xem xét theo ngữ cảnh. Các tệp mã nguồn (bất kỳ tệp nào nằm dưới `scripts/`, có phần mở rộng script như `.py`, `.sh`, `.js`, hoặc tệp không có phần mở rộng nhưng bắt đầu bằng `#!`) mà không phải là văn bản UTF-8 không chứa byte NUL sẽ sinh ra một cảnh báo và vẫn được phân tích qua một lần giải mã có hao hụt, để một byte lạc lõng không thể giúp chúng né các kiểm tra `CRITICAL`. Adapter kiểm duyệt chuẩn hóa cả phản hồi model dạng văn bản thuần lẫn các khối văn bản của Responses API trong LangChain trước khi phân tích quyết định JSON bắt buộc. Các kiểm tra rò rỉ dữ liệu qua instance client trong Python đi theo một chuỗi bằng chứng tối thiểu trong cùng phạm vi: một tên đơn giản được gán bởi một constructor client đã biết, các bí danh tên-sang-tên tùy chọn, và một lần dùng phương thức hướng ra ngoài hoặc context manager thực sự được constructor đó hỗ trợ. Gốc của constructor phải là các lệnh import chứng minh được; những tên trông có vẻ chính tắc nhưng trơ trọi sẽ không được suy diễn thành module. Các phạm vi lồng nhau không kế thừa handle của client và chỉ kế thừa các bí danh import của constructor vốn không bao giờ bị gán lại trong phạm vi bao ngoài. Các comprehension, câu lệnh chứa toán tử walrus, chú thích kiểu, đích gán phức tạp, các thao tác không được hỗ trợ và các luồng rẽ nhánh mơ hồ đều không tạo ra phát hiện nào từ tín hiệu này; những cấu trúc bị bỏ qua sẽ vô hiệu hóa một cách thận trọng mọi tên chúng có thể gán, để trạng thái client lỗi thời không thể tạo ra phát hiện sai. Việc phân tích "cố gắng hết sức" này chạm tới ngân sách công việc xác định hoặc giới hạn đệ quy cũng không làm mất đi những phát hiện đã thu thập được cho tệp đó. Hãy đặt `skill_scan.enabled: false` trong `config.yaml` để chỉ tắt các bộ phân tích xác định; việc trích xuất gói lưu trữ an toàn và bộ quét LLM vẫn chạy.

DeerFlow cũng đi kèm **skill-reviewer**, một skill công khai dùng để rà soát chất lượng skill ở chế độ chỉ-đọc. Nó dùng tool dựng sẵn `review_skill_package` để kiểm tra các skill đã cài, các gói cục bộ, các tệp lưu trữ, hoặc nội dung `SKILL.md` được dán vào, mà không kích hoạt skill mục tiêu, không gắn các bí mật của nó, không chạy script của nó và không cài nó. Tool trả về một payload JSON gọn, đã trung hòa các thẻ, vào ngữ cảnh của model, đồng thời giữ payload rà soát thô đầy đủ trong artifact của tool cho những bên tiêu thụ tự động. Lõi rà soát xác định tái sử dụng khả năng phân tích của DeerFlow cùng các dữ kiện từ SkillScan, phát ra các hợp đồng JSON có đánh phiên bản trong `contracts/skill_review/`, và có thể chạy từ CLI của backend:

```bash
cd backend
uv run python -m deerflow.skills.review.cli ../skills/public/data-analysis --format text --fail-on error --fail-on-incomplete
```

Các miễn trừ CI cho skill công khai là những ngoại lệ chính xác, có hạn dùng, nằm trong `.github/skill-review-waivers.v1.json`. Vì chỉ manifest nền đáng tin cậy mới có thể ẩn một phát hiện, một pull request thay đổi tệp có thể được ủy quyền trước một cách an toàn bằng cách trước tiên merge một thay đổi chỉ-sửa-manifest, trong đó liệt kê SHA-256 của toàn bộ tệp tương lai đã được rà soát trong `preapproved_file_sha256s`; sau đó thay đổi tệp mới được đưa vào ở một pull request sau.

Tool cũng theo cùng triết lý đó. DeerFlow đi kèm một bộ tool cốt lõi — tìm kiếm web, tải nội dung web, chụp trang web đã render, các thao tác tệp, thực thi bash — và hỗ trợ tool tùy chỉnh qua các MCP server và hàm Python. Các nhà cung cấp tìm kiếm đi kèm là DDG, Brave, Tavily và SearXNG đều chấp nhận một `time_range` tùy chọn với giá trị `day`, `week`, `month` hoặc `year`; nếu bỏ qua thì hành vi tìm kiếm hiện tại được giữ nguyên. Với các lần tìm kiếm theo độ mới trên DDG, DeerFlow loại trừ những backend DDGS bỏ qua giới hạn thời gian. Thay thế bất cứ thứ gì. Thêm bất cứ thứ gì.

Với tìm kiếm DDG, `max_results` trong `config.yaml` có thể là một số nguyên dương hoặc một tham chiếu biến môi trường như `max_results: $DDG_MAX_RESULTS` với `DDG_MAX_RESULTS=5`. Giá trị đã cấu hình được ưu tiên hơn đối số `max_results` trong lệnh gọi tool. Các giá trị không hợp lệ (ví dụ `abc`, chuỗi rỗng, hay `3.5`), giá trị 0 và số âm sẽ sinh ra cảnh báo và quay về mặc định 5 kết quả.

Các MCP server stdio có thể đặt `cwd` trong `extensions_config.json` khi điểm vào
hoặc tệp dữ liệu của chúng phụ thuộc vào một thư mục làm việc cụ thể. Thiết lập này áp dụng cho
cả việc khám phá lẫn các lệnh gọi tool; xem [cấu hình MCP](backend/docs/MCP_SERVER.md#stdio-working-directory).
Nếu bỏ qua, để `null` hoặc để rỗng thì các thư mục làm việc mặc định được giữ nguyên.

`web_search` của Tavily cũng chấp nhận các danh sách tùy chọn `include_domains` và `exclude_domains`
trong mục tool của nó trong `config.yaml` để kiểm soát nguồn tìm kiếm. Nếu
`include_domains` không rỗng, Tavily sẽ dùng chế độ `filter` để giới hạn kết quả trong các tên miền đó.
Đây là các thiết lập ở mức triển khai; model vẫn chỉ cung cấp `query` và `time_range` tùy chọn.
Nếu bỏ qua bộ lọc thì yêu cầu SDK hiện tại được giữ nguyên; một danh sách rỗng
tường minh sẽ được chuyển tiếp và không áp đặt hạn chế nào thuộc loại đó. Xem
[ví dụ cấu hình tool](backend/docs/CONFIGURATION.md#tools).

Khi dùng Tavily cho `web_fetch`, các trang được trích xuất mà không có tiêu đề sẽ dùng URL của chúng
làm tiêu đề; nội dung của chúng vẫn khả dụng với agent.
Tiêu đề của các bước tool trong chat chấp nhận các dòng trống ở đầu và tối đa ba khoảng trắng đứng trước
tiêu đề H1 đầu tiên của trang. Mã nguồn được thụt lề, kể cả khi trộn khoảng trắng và tab, không
được dùng làm tiêu đề; khi đó bước tool sẽ quay về dùng URL.
Tính năng tìm kiếm và tải nội dung của Tavily đều đọc `api_key` từ mục tool riêng của chúng trong
`config.yaml`, và quay về dùng `TAVILY_API_KEY` khi không có. Phần tải nội dung không
tái sử dụng khóa của mục tìm kiếm, nên phần tìm kiếm có thể dùng một nhà cung cấp khác. Nếu trước đây
bạn chỉ cấu hình một khóa Tavily dùng chung trong `web_search`, hãy đặt nó cả trong
`web_fetch` hoặc dùng `TAVILY_API_KEY` cho cả hai.

### Truy hồi tri thức riêng tư (RAGFlow)

Các câu trả lời có thể trích dẫn bằng chứng truy hồi từ RAGFlow kèm các trích dẫn tri thức bấm được.
Bấm vào một trích dẫn, hoặc vào một mục trong danh sách nguồn tri thức của câu trả lời, để xem
đoạn trích gốc đã truy hồi, tên dataset và tài liệu, cùng số trang khi
RAGFlow cung cấp. Đây là các snapshot tại thời điểm truy hồi được giữ lại cùng
cuộc hội thoại, bao gồm cả những nguồn do các subagent `task` thông thường chuyển tiếp; chúng
vẫn xem lại được sau khi tải lại cuộc hội thoại. Một đoạn trích không phải là bản sao
trực tiếp của tài liệu đầy đủ: các thay đổi trong RAGFlow không làm thay đổi bằng chứng trong quá khứ.
Các bản ghi nguồn bị thiếu sẽ được hiển thị là không khả dụng thay vì bị biến thành những liên kết
phỏng đoán. Các snapshot nguồn không thêm một trang quản lý tri thức nào và cũng không phơi ra
API key của RAGFlow. Các bản xuất theo lô bền vững và các tệp Markdown độc lập không
mang theo những bản ghi nguồn tương tác này của cuộc hội thoại.
Các liên kết tiêu đề tài liệu thông thường trong mục Sources mở ra đúng bằng chứng như
các trích dẫn nội dòng. Khi có giới hạn ngân sách đầu ra của tool, chỉ những mục bằng chứng
đầy đủ vừa với ngân sách mới trích dẫn được; những nguồn bị lược bỏ sẽ được báo cáo thay vì
giữ lại một bản ghi nguồn cho một đoạn trích bị cắt cụt.

DeerFlow có thể tùy chọn kết nối tới một bản triển khai RAGFlow theo phạm vi tenant. Tool Agent
`knowledge_search` phân giải phạm vi dataset đã cấu hình, nhóm các dataset theo model embedding,
rồi truy hồi các nhóm đó song song, nên việc trộn nhiều model embedding không gây lỗi phía nhà cung cấp.
ID dataset và API key không bao giờ bị phơi ra cho model. Tool tùy chọn `list_knowledge_bases`
chỉ trả về tên.

Chat chính và chat với custom agent có thể tùy chọn hiển thị một bộ chọn **Knowledge**
chỉ-có-biểu-tượng, cục bộ theo trang, nằm cạnh nút điều khiển chế độ. Phần tô sáng thường trực của nó
cho biết truy hồi tri thức đang bật; trạng thái trung tính nghĩa là truy hồi đang tắt.
Hãy đặt `knowledge_base.scope_selection_enabled: true` trong `config.yaml`
khi dùng nhà cung cấp RAGFlow `knowledge_search` dựng sẵn để cho phép chọn toàn bộ
dataset được phép, một số dataset/tệp nhất định, hoặc không truy hồi gì cho một lượt.
Cùng một cờ cấu hình điều khiển cả hai loại chat; khi tắt, không khung soạn thảo nào
hiển thị bộ chọn hay gửi đi một phạm vi. Lựa chọn sẽ quay về mặc định đã lưu của custom agent (hoặc toàn bộ khi chưa gắn)
khi trang được làm mới hoặc khi mở một cuộc hội thoại khác; mỗi tin nhắn người dùng đã gửi đều giữ
một snapshot phạm vi bất biến để phát lại và lưu lịch sử. Gateway kiểm tra
mọi snapshot, giao nó với danh sách dataset được phép của người vận hành, lan truyền
phạm vi chỉ-dùng-để-thực-thi tới các subagent native và bền vững, rồi loại nó khỏi
đầu vào của model và các trace bên ngoài. Các điều khiển runtime nội bộ và thông tin đăng nhập
do client cung cấp cũng bị loại khỏi ngữ cảnh chạy trước khi thực thi hoặc
lưu checkpoint. Các lần thử lại idempotent chấp nhận cả snapshot chính tắc lẫn
đầu vào chạy thô kiểu cũ, giữ được tính tương thích khi thử lại xuyên suốt các bản nâng cấp.
Custom agent có thể lưu một lựa chọn **Default knowledge** từ **Agents → Agent
settings**, bao gồm cả bộ lọc tệp tùy chọn hoặc tắt truy hồi. Chọn toàn bộ kho tri thức
sẽ xóa ràng buộc đó. Cùng trường `knowledge_scope` cũng có trên các API tạo/cập nhật agent
và trong cấu hình đã lưu của agent; nếu không truyền thì cập nhật sẽ giữ nguyên nó, còn `null` sẽ xóa nó.
Đây là một giá trị mặc định, không phải ranh giới phân quyền: một lựa chọn tường minh theo từng tin nhắn
sẽ ghi đè nó, và danh sách cho phép của người vận hành vẫn được áp dụng lúc truy hồi. Các lượt chạy qua Gateway
không có phạm vi theo tin nhắn (kể cả lượt theo lịch và lượt từ kênh IM) sẽ dùng và chụp lại giá trị mặc định đã lưu,
ngay cả khi bộ chọn trên khung soạn thảo bị ẩn. Việc tạo lại/tiếp tục giữ nguyên phạm vi của lượt gốc,
kể cả các lượt cũ không có phạm vi, chứ không lấy theo những thay đổi cấu hình sau này.
Các lựa chọn không xác định hoặc không khả dụng không bao giờ làm mở rộng phạm vi truy hồi.
Các lần thử lại idempotent giữ nguyên lượt chạy và phạm vi gốc khi một giá trị mặc định được thêm,
thay đổi hoặc xóa, kể cả với những lượt chạy không có phạm vi được chấp nhận trước khi có tính năng này.
Giá trị mặc định này áp dụng cho các lượt chat với custom agent do Gateway host; các tích hợp
harness/client trực tiếp vẫn tự cung cấp phạm vi thực thi của riêng chúng.

Khối `knowledge_base` là trung lập với nhà cung cấp và chỉ điều khiển việc
năng lực tri thức cùng bộ chọn có được bật hay không. Kết nối RAGFlow, danh sách dataset
được phép, và các tham số truy hồi (`base_url`, `api_key`, `datasets`,
`page_size`, các ngưỡng, và giới hạn đầu ra) phải được cấu hình trong
mục `tools[].name: knowledge_search`; chúng không bao giờ được đọc từ
`knowledge_base`.
Các yêu cầu chat với custom agent mang tên agent đã chọn ở cả `assistant_id`
lẫn `context.agent_name`, nên việc chấp nhận phạm vi của Gateway và việc nạp agent lúc chạy
dùng chung một danh tính. Các yêu cầu chat chính dùng `lead_agent`; cả hai danh tính
chỉ được chấp nhận khi cấu hình dùng chung có bật nhà cung cấp RAGFlow.
Khi trả lời một câu hỏi làm rõ đang chờ, một snapshot bộ chọn hiện tại được gửi
tường minh sẽ thắng; các client bỏ qua nó sẽ kế thừa phạm vi đã được chấp nhận của lượt trước.
Việc sửa-và-tạo-lại cũng theo cùng quy tắc dự phòng đó, và danh mục tệp
chỉ được nạp sau khi một dataset chuyển từ "toàn bộ tệp" sang "các tệp đã chọn".
Bản phát hành này không bổ sung một mục Knowledge độc lập vào thanh bên
workspace hay một trang quản lý tri thức trong DeerFlow; hãy tạo, tải lên, phân tích và
xóa dataset cùng tài liệu trực tiếp trong RAGFlow.

Mỗi tin nhắn vẫn có thể chọn tối đa 1000 tài liệu. Khi chọn hơn 100 tài liệu từ cùng một dataset, DeerFlow sẽ kiểm tra chúng theo lô tối đa 100 tài liệu trong khi vẫn giữ nguyên toàn bộ lựa chọn. Nếu bất kỳ lô nào chứa một tài liệu không truy cập được hoặc không tìm kiếm được, việc truy hồi sẽ bị từ chối.

Các bản triển khai nâng cao có thể bật cơ chế phân quyền cắm-thêm-được bằng `authorization.enabled` trong `config.yaml`. Một `AuthorizationProvider` đã cấu hình sẽ lọc bỏ các tool bị từ chối trước khi chúng đến được model hay catalog tool bị hoãn, rồi chính provider đó được kiểm tra lại trước mỗi lần thực thi tool nghiệp vụ thông qua lớp middleware guardrail sẵn có. Quyền truy cập các tuyến `threads:*` và `runs:*` của Gateway cũng được suy ra từ chính provider đó, trong khi các kiểm tra quyền sở hữu hiện có và các cổng quản lý chỉ-dành-cho-admin vẫn giữ nguyên hiệu lực. Mọi tuyến HTTP khởi động hoặc cho phép một lượt chạy Agent trong tương lai đều yêu cầu `runs:create`: bao gồm các endpoint không trạng thái `POST /api/runs/stream` và `POST /api/runs/wait`, cùng các thao tác tạo, cập nhật, tiếp tục và kích hoạt thủ công cho tác vụ theo lịch. Các thao tác ghi với tác vụ theo lịch vẫn giữ yêu cầu `threads:write` hiện có, còn các tuyến không trạng thái sẽ kiểm tra quyền sở hữu riêng khi thread ID tùy chọn được truyền trong body của yêu cầu. Một `tool_search` được sinh ra chỉ có thể bỏ qua lần kiểm tra tool thứ hai khi nó đứng trước catalog bị hoãn vốn đã được lọc của bản build hiện tại. Quyền truy cập model cũng theo cùng provider đó: danh sách `models` của Gateway được lọc theo từng chủ thể, `model:use` được áp dụng cho các yêu cầu xem chi tiết model và lại được áp dụng khi runtime phân giải model của agent, và một model mặc định bị từ chối sẽ quay về ứng viên còn lại đầu tiên cũng vượt qua được `model:use`. Nhà cung cấp RBAC dựng sẵn hỗ trợ các chính sách cho phép/từ chối `tools`, `routes`, `models`, `skills` và `sandbox` theo từng vai trò, đồng thời kiểm tra rằng `default_role` trỏ tới một vai trò đã cấu hình; phân quyền mặc định bị tắt. Xem `config.example.yaml` và [RFC về phân quyền](docs/plans/2026-07-10-pluggable-authorization-rfc.md).

Các gợi ý câu hỏi tiếp theo cũng kiểm tra `model:use` trước khi gọi model đã chọn, kể cả model mặc định khi không có tên nào được truyền. Một model bị từ chối sẽ trả về HTTP 403 mà không gọi LLM; các lỗi của nhà cung cấp phân quyền tuân theo chính sách `fail_closed` đã cấu hình.

Với các agent có khả năng xử lý hình ảnh, `view_image` và lần đọc ảnh vào ngữ cảnh model sau đó cũng yêu cầu `sandbox:execute`. Việc chỉ cho phép tên tool không đồng nghĩa với việc cấp quyền truy cập tệp ảnh; một vai trò bị từ chối quyền thực thi sandbox không thể đọc lại metadata ảnh đã ghi trước đó sau khi quyền của nó thay đổi.

Các bản triển khai nâng cao cũng có thể mở rộng chính runtime của agent bằng cách khai báo các lớp `AgentMiddleware` trong `extensions.middlewares` ở `config.yaml` hoặc `extensions_config.json`. Mỗi mục là một chuỗi `module.path:ClassName` (constructor không tham số) hoặc một đối tượng `{class, kwargs}` với `kwargs` được truyền vào constructor. Giá trị trong `kwargs` phải là kiểu JSON (object, array, string, number, boolean hoặc null); ngày tháng và dấu thời gian trong YAML được ép về chuỗi ISO để khớp với JSON. DeerFlow nạp cùng danh sách đã cấu hình đó vào pipeline của lead agent và subagent, sau các middleware runtime dựng sẵn và các bộ bảo vệ vòng lặp/token của chúng, nhưng trước phần đuôi xử lý phản hồi cuối/an toàn/làm rõ, nhờ đó các bản fork dành cho doanh nghiệp có thể thêm guardrail theo lĩnh vực, cơ chế quản trị lệnh gọi tool, hoặc hook quan sát mà không phải vá các bộ dựng middleware có sẵn. Gói bị thiếu, lớp không hợp lệ, module lỗi và lỗi constructor đều sẽ báo lỗi rõ ràng lúc tạo agent. Hãy xem `config.yaml` và `extensions_config.json` là những tệp đáng tin do người vận hành kiểm soát: đường dẫn middleware chính là việc thực thi mã, giống như các khai báo tool tùy chỉnh, model, sandbox, guardrail, MCP server và MCP interceptor. Các endpoint bật/tắt skill/MCP của Gateway giữ nguyên trường này nhưng không phơi ra đường ghi qua API cho `extensions.middlewares`. Hiện chưa hỗ trợ danh sách middleware riêng cho chỉ-lead hoặc chỉ-subagent.

Với các tích hợp runtime được đóng gói và có thể cấu hình, hãy dùng trình quản lý extension của DeerFlow.
Nó chấp nhận một yêu cầu gói Python, một URL Git HTTPS công khai, hoặc một thư mục cục bộ; cài
gói đó vào nhóm phụ thuộc `extensions` riêng của backend, cập nhật
`backend/uv.lock`, và thêm một mục đã bật vào danh sách `plugins:` ở cấp cao nhất (chỉ đọc lúc khởi động)
trong `config.yaml`:

```bash
# PyPI — ghim một phiên bản để triển khai có thể tái lập
make extension-install SOURCE="deerflow-extension-acme==1.2.3"

# Git HTTPS công khai — ghim một commit bất biến
make extension-install \
  SOURCE="git+https://github.com/acme/deerflow-extension-acme.git@0123456789abcdef0123456789abcdef01234567"

# Gói cục bộ — đường dẫn tuyệt đối giúp tránh thư mục làm việc tương đối với backend của Make
make extension-install SOURCE="$PWD/examples/deerflow-extension-example"

make extension-list
make extension-upgrade SOURCE="$PWD/examples/deerflow-extension-example"
make extension-disable NAME=acme
make extension-enable NAME=acme
make extension-remove NAME=acme
```

Việc cài đặt diễn ra ở chế độ tương tác vì quá trình cài gói có thể chạy các build hook của Python,
và extension được nạp sau đó sẽ chạy với đặc quyền của Gateway. Với một nguồn đã được rà soát,
các quy trình tự động có thể xác nhận ranh giới đó một cách tường minh bằng
`cd backend && uv run --frozen --no-group extensions deerflow extensions install <source> --yes`.
Trình quản lý yêu cầu uv 0.8.0 trở lên; các image Docker đi kèm ghim uv 0.11.1.
Các lệnh trực tiếp khác là `deerflow extensions upgrade SOURCE`, `list`, `enable NAME`, `disable NAME` và `remove NAME`;
`NAME` có thể là tên extension, tên distribution Python, hoặc giá trị `module:install`. Đừng
đặt thông tin đăng nhập vào URL nguồn — một URL mang userinfo nhúng hoặc một tham số truy vấn
trông giống thông tin đăng nhập sẽ bị từ chối trước khi uv chạy. Các nguồn Git từ xa phải dùng HTTPS công khai;
các URL Git kiểu SSH bị từ chối vì builder Docker mặc định không chuyển tiếp thông tin đăng nhập SSH
của máy chủ. Việc cài từ một URL loopback vẫn được phép cho công cụ cục bộ nhưng sẽ có cảnh báo, vì
`127.0.0.1` được ghi vào tệp lock lại là một máy khác khi ở bên trong builder Docker.

Một gói được quản lý khai báo đúng một entry point chuẩn theo PEP 621:

```toml
[project.entry-points."deerflow.extensions"]
acme = "acme_deerflow_extension:install"
```

Hàm đó dùng hợp đồng `deerflow-extension-api` độc lập và có thể đăng ký nhiều
loại đóng góp: middleware cách ly tại các vị trí ngữ nghĩa của model hoặc tool ở lead/subagent,
các hook vòng đời tác vụ cho lead và subagent, các observer cho những lệnh gọi model thuộc về DeerFlow mà
không được bọc bởi hook model-call của middleware (goal, memory, title và summarization),
các dịch vụ sống suốt vòng đời Gateway, và các router HTTP FastAPI được nạp sớm. Gói hợp đồng không có
phụ thuộc framework nào; các extension phải tự khai báo FastAPI, LangChain, LangGraph hay các
thư viện khác mà chúng import.

Các đóng góp full-stack còn có thể cung cấp thêm trang trên trình duyệt, hành động trong hội thoại,
các thao tác backend đã xác thực và các tool cho model thông qua
[plugin API](docs/full-stack-plugins.md). Ví dụ độc lập
[bookmarks](examples/deerflow-extension-bookmarks/README.md) minh họa
một gói có dữ liệu người dùng bền vững, trang riêng trên thanh bên và một tool tìm kiếm chỉ-đọc.
Việc mở lại một bookmark sẽ phân giải agent hiện tại của cuộc hội thoại thông qua host, nên
các cuộc hội thoại với custom agent vẫn giữ đúng điểm vào chat ban đầu, kể cả với bookmark cũ.
Việc cài đặt và kích hoạt vẫn do bản triển khai kiểm soát; Capability Center hiển thị thông tin
và trạng thái của plugin. Mã chạy trên trình duyệt được xem là mã cùng-origin đáng tin cậy.
API trình duyệt và cơ chế truyền `BrowserModule.code` nội dòng đang ở giai đoạn thử nghiệm.
Hướng dẫn về plugin mô tả một lộ trình bổ sung tiến tới manifest và tài nguyên tĩnh được đóng gói.

DeerFlow chỉ cấp phát một kho extension theo phạm vi tác vụ cho middleware, vòng đời, hoặc
việc quan sát model hệ thống. Các dịch vụ nhận phụ thuộc runtime theo phạm vi ứng dụng sau khi lớp
lưu trữ của Gateway đã sẵn sàng, và dừng theo thứ tự ngược lại sau khi các lượt chạy đang hoạt động xả hết.
`ExtensionRuntimeDeps.run_evidence_reader` (tùy chọn) là một giao diện chỉ-đọc ổn định dành cho các dịch vụ
kiểm toán, đánh giá, đồng bộ và quan sát: nó khám phá các lượt chạy đã thay đổi bằng một
con trỏ mờ có thể tiếp tục, phân trang các sự kiện đã lưu của một lượt chạy đã biết bằng `after_seq`, và đọc
trạng thái chính thức của lượt chạy một cách tách biệt khỏi bằng chứng sự kiện. Một kho lượt chạy dựa trên
cơ sở dữ liệu giữ cho con trỏ khám phá vẫn hợp lệ qua các lần khởi động lại Gateway; kho lượt chạy trong
bộ nhớ chỉ đảm bảo cùng thứ tự đó trong vòng đời của tiến trình hiện tại. Metadata sự kiện được che
thông tin bí mật ở ranh giới này, nhưng nội dung sự kiện được trả về nguyên vẹn. Cả hai payload đều là
snapshot tách rời, nên việc sửa các giá trị lồng bên trong không thể làm thay đổi bằng chứng mà host đã lưu.
Gateway phiên bản production cung cấp một reader theo phạm vi ứng dụng, xuyên người dùng, cho các
extension đáng tin của người vận hành; một host nhúng có thể gắn đúng adapter đó cho một người dùng.
Các trang kết quả "lượt chạy đã thay đổi" chứa các bản ghi mới tạo và các thay đổi trên những dòng được giữ lại,
chứ không chứa "bia mộ" xóa; các bên tiêu thụ cần đối soát việc xóa phải poll trạng thái cho những lượt chạy
đã biết và xem việc không có kết quả là đã bị xóa. Extension vẫn chạy với đặc quyền của Gateway và
vẫn giữ `session_factory` kiểu cũ, nên reader này là một ranh giới về tính ổn định của API và
giảm-đặc-quyền-do-vô-ý, chứ không phải một sandbox cho các gói Python không đáng tin. Các router HTTP của
extension được gắn sau toàn bộ tuyến của host; những tuyến chắc chắn che khuất tuyến khác và những tuyến
đi vào các đường dẫn được miễn xác thực hoặc miễn CSRF của host sẽ bị từ chối kèm thông tin chẩn đoán
chỉ rõ nguồn gốc, trong khi các router không liên quan vẫn được nạp bình thường. Vì các đường dẫn công khai của
host là một danh sách tiền tố dành riêng mà extension không thể chen vào, **mọi endpoint do extension đóng góp
đều yêu cầu một phiên đã xác thực** — hiện chưa có cách nào để một extension phơi ra một tuyến
không xác thực, nên các webhook từ nhà cung cấp bên ngoài và các endpoint trạng thái công khai nằm ngoài
phạm vi của bản phát hành này. Trong khuôn khổ đó, một extension phân biệt người dùng thường với
quản trị viên thông qua `deerflow_extension_api.auth`: `resolve_principal(request)` trả về
bên gọi, còn `require_admin(request)` ném `PermissionError` với mọi người khác và "hỏng theo hướng an toàn"
khi không xác định được danh tính. Extension nhận được một phép chiếu — user id, cờ admin,
cờ internal, các vai trò — chứ không bao giờ nhận ngữ cảnh xác thực của host. Các hook khởi động/tắt của router,
lifespan tùy chỉnh, Mount và tuyến WebSocket đều không được chấp nhận; các tài nguyên có vòng đời nên nằm trong
`ExtensionService`, và các đóng góp WebSocket cần một lớp bọc xác thực/Origin do host sở hữu trong tương lai.
Các callback vòng đời và model hệ thống dùng vòng lặp thông báo chính tắc của Gateway,
bao gồm cả các subagent chạy trên vòng lặp riêng biệt.

Các tuyến extension hướng tới người dùng có thể gọi
`deerflow_extension_api.require_run_evidence_reader(request)` (extension API 0.2.2+).
Gateway yêu cầu quyền `runs:read` đã xác thực và cố định phạm vi của reader
về đúng người dùng đó, kể cả với quản trị viên và các bên gọi nội bộ. Các ID do bên gọi cung cấp không thể
thay đổi phạm vi này. Các lượt chạy không nhìn thấy được và các lượt chạy không tồn tại trả về cùng một kết quả; con trỏ
"lượt chạy đã thay đổi" không thể tái sử dụng trực tiếp giữa các người dùng khác nhau. Hàm tùy chọn `resolve_run_evidence_reader(request)`
trả về `None` khi host không hỗ trợ năng lực này; còn hàm bắt buộc thì ném `NotImplementedError`.
Việc bị từ chối quyền sẽ ném `PermissionError`. Các tuyến nên ánh xạ
các ngoại lệ này lần lượt thành HTTP 503 và 403; lỗi của bộ phân giải không bao giờ quay về
dùng reader của dịch vụ toàn cục.

Thứ tự plugin là xác định, cấu hình riêng của từng plugin được truyền vào `install()`, và
`required: true` khiến việc nạp thất bại làm dừng quá trình khởi động; ngược lại, lỗi sẽ được báo cáo và
bỏ qua. `enabled: false` bỏ qua cả việc phân giải lẫn import. Trình quản lý giữ nguyên phần `config`
riêng tư của extension khi bật/tắt nó, và ghi các metadata `name`, `package`, `use`, `enabled` và
`required` cho những lần cài do nó quản lý. Các lần cài được ghi là `required: false` để một extension
bị hỏng sau này được báo cáo thay vì chặn Gateway khởi động; hãy truyền
`extensions install <source> --required` khi bạn muốn sự vắng mặt của gói đó làm dừng quá trình khởi động.
Plugin chỉ được nạp một lần khi ứng dụng Gateway được dựng lên,
nên việc cài, bật, tắt, gỡ và sửa `plugins:` thủ công đều đòi hỏi khởi động lại Gateway.
Vì việc này import mã Python, `plugins:` cố tình không khả dụng
thông qua `extensions_config.json` (vốn ghi được qua API).

Các lệnh quản lý khởi tạo môi trường checkout mà không kèm nhóm extension thông qua
`uv run --frozen --no-group extensions`. Chế độ frozen cho phép `disable` và `remove` khởi chạy ngay cả
khi nguồn từ xa hoặc snapshot được quản lý của một extension đã cài trở nên không khả dụng,
trong khi một bản checkout mới vẫn có thể tạo môi trường không-extension từ tệp lock hiện có.
Bản thân trình quản lý sở hữu giao dịch phụ thuộc đã khóa diễn ra sau đó.
Các thao tác ghi cho một bản checkout được tuần tự hóa thông qua một khóa tiến trình. Bề mặt ban đầu của
trình quản lý là tạo/gỡ chứ không phải nâng cấp tại chỗ: để đổi một nguồn đã cài, hãy lưu lại
phần `plugins[].config` riêng tư của nó, gỡ nó đi, cài lại bản ghim mới, rồi khôi phục cấu hình đó.

Các lần cài từ thư mục cục bộ được sao chép vào
`backend/extensions/sources/<normalized-distribution>/`; chính snapshot có thể triển khai này,
chứ không phải thư mục gốc, được ghi vào tệp lock. Metadata Git, môi trường ảo,
cache bytecode, symbolic link và các tệp có khả năng chứa thông tin đăng nhập đều không được chấp nhận
làm nội dung snapshot. Dù vậy vẫn hãy rà soát thứ bạn cài: việc lọc bỏ các tệp vô tình không
tạo ra sandbox cho một extension, cho build backend của nó, hay cho mã chạy lúc runtime của nó.

`make dev`/`make start` cục bộ, môi trường phát triển Docker và image Gateway production đều
dùng chung `backend/pyproject.toml` và `backend/uv.lock`. Các bộ khởi chạy cục bộ và Docker-dev
thực hiện một lần sync theo tệp lock trước khi khởi động; image production thực hiện lần sync đó
trong lúc build và đưa các snapshot cục bộ được quản lý vào build context. Sau đó các lệnh runtime
của Gateway dùng môi trường đã được tạo sẵn mà không phân giải hay cài đặt gói nào.
Các lần sync trước khi khởi động ở môi trường cục bộ và Docker-dev có thể tải về những artifact đã khóa còn thiếu. Một
bản triển khai production thì chỉ tải chúng trong lúc cài đặt tường minh hoặc lúc build image;
việc khởi động container Gateway production kết quả không bao giờ phân giải hay cài
extension từ mạng. Một tệp wheel cục bộ hoặc URL Git dạng `file://` sẽ bị từ chối vì
nó sẽ không tồn tại trong build context của Docker; thay vào đó hãy truyền một thư mục nguồn để tạo một
snapshot được quản lý. Vì cấu hình môi trường (chẳng hạn một wheelhouse `UV_FIND_LINKS`)
vẫn có thể phân giải một tên gói thông thường thành một wheel cục bộ, trình quản lý sẽ kiểm toán mọi tệp lock mới
trước khi bật extension: bất kỳ tham chiếu cục bộ nào mà bản build image mặc định không tái lập được
sẽ khiến toàn bộ lần cài hoặc gỡ bị quay ngược.
Hãy build lại bằng `make up` sau khi thay đổi tập extension được quản lý. Xem
`config.example.yaml` và
[extension tham khảo](examples/deerflow-extension-example/) để có một ví dụ đầy đủ.

Các gợi ý câu hỏi tiếp theo do Gateway sinh ra giờ đây chuẩn hóa cả đầu ra model dạng chuỗi thuần lẫn nội dung phong phú dạng khối/danh sách trước khi phân tích phản hồi mảng JSON, nên các lớp bọc nội dung riêng của từng nhà cung cấp không âm thầm làm mất gợi ý.

Khung soạn thảo của Web UI có thể trau chuốt bản nháp trước khi gửi. Việc viết lại chạy như một yêu cầu LLM ngắn qua Gateway, dùng cấu hình model `input_polish`, giữ nguyên các tiền tố skill dạng gạch chéo như `/data-analysis`, và chỉ thay thế bản nháp cục bộ sau khi người dùng bấm nút trau chuốt; nó không tạo một lượt chạy trên thread và không lưu tin nhắn nào.

Khi agent hỏi để làm rõ, Web UI hiển thị thẻ phản hồi có cấu trúc nhưng vẫn giữ khung soạn thảo thông thường khả dụng. Người dùng có thể điền thẻ đó hoặc gửi một tin nhắn chat tự do để bỏ qua nó; tin nhắn đó sẽ đóng câu hỏi làm rõ đang chờ gần nhất và trở thành đầu vào tiếp theo của agent. Phần văn bản trả lời đi kèm vẫn nằm ngoài bảng các bước thực thi, và việc trả lời yêu cầu vẫn giữ lại những đoạn văn bản đã hoàn tất trước đó trong cuộc hội thoại trong khi agent tiếp tục làm việc.

Các bản nháp chưa gửi trong khung soạn thảo của Web UI vẫn tồn tại qua các lần tải lại trang và khi chuyển giữa các cuộc hội thoại trong cùng một tab trình duyệt. Bản nháp được cách ly theo người dùng, agent và cuộc hội thoại, bao gồm cả skill gạch chéo đã chọn nếu có, và bị xóa khi một lần gửi được chấp nhận. Tệp đính kèm và ngữ cảnh hội thoại được trích dẫn cố tình không được lưu lại.

Khung soạn thảo của Web UI cũng hỗ trợ đọc chính tả bằng giọng nói trên trình duyệt khi trình duyệt cung cấp Web Speech API. Nút micro chỉ chuyển lời nói thành văn bản trong bản nháp cục bộ; DeerFlow chỉ nhận được phần văn bản đã chuyển đổi, còn việc xử lý âm thanh được giao cho dịch vụ nhận dạng giọng nói của trình duyệt hoặc hệ điều hành theo chính sách của môi trường đó. Người dùng có thể xem lại hoặc chỉnh sửa văn bản trước khi gửi.

Web UI hiển thị một dòng tuyên bố miễn trừ đã được bản địa hóa về nội dung do AI tạo ra, nằm dưới khung soạn thảo trong cả cuộc hội thoại tiêu chuẩn lẫn với custom agent, nhắc người dùng kiểm chứng những thông tin quan trọng.

Các lượt chạy đầu tiên bị gián đoạn vẫn lưu lại một tiêu đề hội thoại dự phòng, nên việc dừng một phản hồi đang stream không khiến thread bị bỏ lại ở trạng thái "Untitled" sau khi làm mới.

Các phản hồi Markdown dạng streaming chỉ tạo hiệu ứng động cho những từ vừa đến; phần văn bản đã hiển thị sẽ không bị làm mờ rồi phát lại khi chunk kế tiếp nối dài cùng khối đó.

Trong Web UI, các lượt trả lời đã hoàn tất của assistant có thể được tách nhánh thành một cuộc hội thoại chính mới. Tiêu đề nhánh được kế thừa tự động sẽ dùng hậu tố số trung lập về ngôn ngữ còn trống kế tiếp (`Title (2)`, rồi `Title (3)` cho một nhánh anh em khác hoặc một nhánh của cuộc hội thoại đã đánh số), nên các tiêu đề anh em được sinh ra vẫn phân biệt được mà không cần lưu một nhãn phụ thuộc ngôn ngữ; các tiêu đề anh em tường minh hoặc đã đổi tên mà trùng khớp cũng giữ chỗ hậu tố đang hiển thị của chúng dù không mang metadata chuỗi số được sinh ra. Một tiêu đề đặt tường minh qua API sẽ được giữ nguyên. Việc đổi tên một nhánh sẽ xóa chuỗi số được sinh ra của nó, nên nhánh tự động kế tiếp của nó bắt đầu từ tiêu đề mới với `(2)`. Mục Recent chats cũng nhóm các nhánh đã nạp ngay bên dưới nhánh cha đã nạp, kèm các đường nối cây mờ nhạt. Các nhánh cha bị thiếu, quan hệ dòng dõi sai định dạng hoặc vòng lặp, và những nhánh có trạng thái ghim khác nhau sẽ vẫn hiển thị ở cấp cao nhất thay vì bị ẩn đi hay bị chuyển qua ranh giới ghim. Thread mới bắt đầu từ checkpoint của lượt đó và giữ lại checkpoint phát lại đứng trước, nên phản hồi trong nhánh có thể được tạo lại ngay lập tức. Phản hồi mới nhất cũng có thể được tạo lại sau một lần gián đoạn, ngay cả khi phần văn bản stream dở dang của nó chưa bao giờ đến được một checkpoint. Việc tạo lại phản hồi mới nhất vẫn giữ tiêu đề hiện tại của thread, kể cả tiêu đề bạn tự đổi tên sau phản hồi gốc. Các lịch sử cũ hoặc được nhập vào mà không có liên kết checkpoint cha sẽ dùng phương án dự phòng theo thứ tự thời gian có giới hạn; nếu không tồn tại checkpoint phát lại nào trước đó, việc tách nhánh vẫn thành công với hình dạng một-checkpoint kiểu cũ, còn việc tạo lại sẽ không khả dụng cho phản hồi được kế thừa đó. Các nhánh một-checkpoint hiện có được giữ nguyên thay vì thử một thao tác sao chép checkpoint không an toàn. Vì các tệp trong workspace không được checkpoint, nhánh mới chỉ nhận được một bản sao "cố gắng hết sức" của workspace hiện tại khi bạn tách nhánh từ lượt mới nhất; tách nhánh từ một lượt cũ hơn chỉ giữ lại lịch sử tin nhắn được khôi phục, nên nhánh đó không bao giờ kế thừa những tệp được tạo ở phần sau của cuộc hội thoại.

Web UI báo cáo thời gian hoàn thành tác vụ một lần cho mỗi lượt chạy. Đây là tổng thời gian thực tế — bao gồm cả thời gian model suy luận, gọi tool và chờ đợi — chứ không phải thời lượng theo từng bước hay chỉ riêng thời gian model suy nghĩ. Nội dung suy luận vẫn xem được qua phần hiển thị riêng của nó.

Trong lúc một phản hồi đang stream, những tin nhắn chỉ chứa nội dung suy luận vẫn nằm trong bảng xử lý, bao gồm cả các khối thinking của Anthropic. Khi nội dung trả lời xuất hiện cùng phần suy luận, nó sẽ hiện ra trong một bong bóng của assistant.

Các thẻ `<think>` nguyên văn nằm trong khối mã có rào, mã thụt lề hoặc mã nội dòng vẫn là một phần của câu trả lời và của phần văn bản được sao chép, thay vì bị chuyển vào phần hiển thị suy luận. Điều này bao gồm cả những khối mã có rào mở ra trên dòng của một mục danh sách: phần suy luận thật sự nằm sau đoạn mã vẫn được tách ra. Các đoạn mã nội dòng chưa đóng vẫn được giữ nguyên trong lúc stream bên trong một đoạn văn, nhưng kết thúc ở một dòng trống hoặc ở một tiêu đề, danh sách, đường phân cách hay khối mã có rào chen vào. Các đoạn văn nối tiếp được thụt lề không tạo ra một khối mã.

Trong Web UI, lượt người dùng đã hoàn tất gần nhất cũng có thể được sửa và chạy lại từ thanh công cụ của tin nhắn. DeerFlow khôi phục checkpoint của cuộc hội thoại ngay trước tin nhắn người dùng đó, gửi phần văn bản đã sửa như một tin nhắn người dùng mới, rồi ẩn lượt bị thay thế khi việc phát lại đang diễn ra hoặc đã thành công. Đây chỉ là việc phát lại trạng thái hội thoại: các tệp, các bản cập nhật bộ nhớ và các tác dụng phụ của tool bên ngoài sẽ không được hoàn tác.

Các liên kết chat trong Web UI mã hóa phần trăm (percent-encode) các định danh thread tùy chỉnh trước khi đặt chúng vào các đoạn đường dẫn, nên các ký tự URL dành riêng như `#` và `?` không làm thay đổi cuộc hội thoại được mở.

```
# Đường dẫn bên trong container sandbox
/mnt/skills/public
├── research/SKILL.md
├── report-generation/SKILL.md
├── slide-creation/SKILL.md
├── web-page/SKILL.md
└── image-generation/SKILL.md

/mnt/skills/custom
└── your-custom-skill/SKILL.md      ← của bạn

/mnt/skills/integrations
└── lark-cli/lark-doc/SKILL.md      ← được quản lý, chỉ-đọc
```

Skill `image-generation` dựng sẵn hỗ trợ các Images API của Gemini, MiniMax và
các API tương thích OpenAI. Hãy chọn loại cuối bằng
`IMAGE_GENERATION_PROVIDER=openai`, rồi cấu hình
`IMAGE_GENERATION_API_KEY`, `IMAGE_GENERATION_BASE_URL` và
`IMAGE_GENERATION_MODEL`. Với sandbox dạng container, hãy phơi các biến này
qua `sandbox.environment`; các lệnh trong sandbox cố tình không kế thừa
API key từ tiến trình Gateway.

#### Xuất skill tùy chỉnh

Quản trị viên có thể xuất các skill tùy chỉnh của chính mình từ **Capability Center → Skills → My skills → View details → Export**. Hãy xem lại danh sách tệp và các yêu cầu môi trường đã khai báo, rồi chọn **Download .skill**. Gói lưu trữ chứa skill đang được lưu hiện tại, bao gồm cả tệp hỗ trợ và thư mục rỗng; skill đang tắt cũng xuất được. Nếu skill thay đổi sau khi xem trước, hãy làm mới danh sách tệp trước khi tải xuống. Hãy nhập gói đó vào một instance DeerFlow khác bằng **Install .skill**; các xung đột trùng tên và các kiểm tra bảo mật cài đặt thông thường vẫn được áp dụng.

Các thiết lập tài khoản, cuộc hội thoại và lịch sử nằm ngoài thư mục skill đều bị loại trừ. Các tệp bên trong thư mục được giữ nguyên không đổi, kể cả bất kỳ thông tin đăng nhập nào mà tác giả đã đặt ở đó; các cảnh báo dựa trên tên tệp chỉ mang tính gợi ý. Hãy cấu hình phụ thuộc và thông tin đăng nhập ở nơi đến. Các thư mục/tệp dạng liên kết, hard link, tệp nhị phân thực thi không được hỗ trợ, các tệp `SKILL.md` lồng nhau và các đường dẫn không khả chuyển đều không xuất được. Việc xuất hỗ trợ các máy chủ có API hệ thống tệp dạng không-đi-theo-liên-kết theo descriptor (Linux/macOS); các máy chủ không hỗ trợ sẽ báo lỗi rõ ràng. Giới hạn: 4096 mục ZIP, 64 MiB cho mỗi tệp, 100 MiB tổng nội dung/gói lưu trữ và 1 MiB cho frontmatter. Các alias YAML và những khai báo quá phức tạp không được hỗ trợ. Ngữ nghĩa thực thi thông thường của script được giữ nguyên khi nhập trên POSIX, nhưng không khôi phục các quyền đặc biệt. Xem [hợp đồng API xuất skill](backend/docs/API.md#export-a-custom-skill).

#### Tích hợp Claude Code

Skill `claude-to-deerflow` cho phép bạn tương tác với một instance DeerFlow đang chạy ngay từ [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Gửi tác vụ nghiên cứu, kiểm tra trạng thái, quản lý thread — tất cả mà không cần rời khỏi terminal.

**Cài skill**:

```bash
npx skills add https://github.com/bytedance/deer-flow --skill claude-to-deerflow
```

Sau đó hãy đảm bảo DeerFlow đang chạy (mặc định tại `http://localhost:2026`) và dùng lệnh `/claude-to-deerflow` trong Claude Code.

**Những gì bạn có thể làm**:
- Gửi tin nhắn tới DeerFlow và nhận phản hồi dạng streaming
- Chọn chế độ thực thi: flash (nhanh), standard, pro (lập kế hoạch), ultra (sub-agent)
- Kiểm tra tình trạng DeerFlow, liệt kê model/skill/agent
- Quản lý thread và lịch sử hội thoại
- Tải tệp lên để phân tích

**Biến môi trường** (tùy chọn, dành cho endpoint tùy chỉnh):

```bash
DEERFLOW_URL=http://localhost:2026            # Base URL của proxy hợp nhất
DEERFLOW_GATEWAY_URL=http://localhost:2026    # Gateway API
DEERFLOW_LANGGRAPH_URL=http://localhost:2026/api/langgraph  # LangGraph API
```

Xem [`skills/public/claude-to-deerflow/SKILL.md`](skills/public/claude-to-deerflow/SKILL.md) để có tài liệu API đầy đủ.

### Lưu trữ cuộc chat

Việc xóa một cuộc chat từ thanh bên cần xác nhận có hiển thị tiêu đề của nó. Xóa sẽ loại bỏ cuộc hội thoại cùng các tệp của nó và không thể hoàn tác.

Hãy dùng **Archive chat** trong menu thanh bên của một cuộc chat gần đây để ẩn đi phần việc đã xong mà vẫn giữ lại tin nhắn, tệp và liên kết gốc. Thông báo thành công có kèm nút **Undo**. Mở **Chats → Archived** để tìm các cuộc hội thoại đã lưu trữ và khôi phục từng cái; một cuộc hội thoại đã lưu trữ khi mở ra cũng có nút khôi phục ở phần header. Ô tìm kiếm lọc theo tiêu đề của các cuộc hội thoại đã nạp, kèm nút **Load more** cho những mục cũ hơn.

Việc lưu trữ và khôi phục giữ nguyên thời điểm hoạt động và trạng thái ghim của cuộc chat. Lưu trữ không làm dừng một tác vụ đang chạy hay tạm dừng các lịch của nó, và hoạt động mới cũng không tự động khôi phục nó. Hãy dùng hành động Delete sẵn có khi bạn thực sự muốn xóa một cuộc hội thoại cùng các tệp của nó.

### Session Goal (Mục tiêu phiên)

Dùng `/goal <điều kiện hoàn thành>` để gắn một điều kiện hoàn thành đang hoạt động vào thread hiện tại. Mục tiêu là trạng thái theo phạm vi thread, không phải một lần kích hoạt skill, nên nó vẫn có hiệu lực qua nhiều lượt cho đến khi DeerFlow xác định là đã đạt được hoặc bạn xóa nó đi.

Các lệnh được hỗ trợ:

```text
/goal finish the implementation and make all tests pass
/goal              # hiển thị mục tiêu đang hoạt động
/goal clear        # xóa mục tiêu
```

Sau mỗi lượt chạy qua Gateway, DeerFlow đánh giá cuộc hội thoại đang hiển thị so với mục tiêu đang hoạt động bằng một model đánh giá không dùng thinking. Bộ đánh giá phải trả về một loại rào cản có kiểu (`missing_evidence`, `needs_user_input`, `run_failed`, `external_wait`, hoặc `goal_not_met_yet`) kèm bằng chứng nhìn thấy được. DeerFlow chỉ chèn một lượt tiếp diễn ẩn khi lượt assistant mới nhất đã được checkpoint bền vững, rào cản là `goal_not_met_yet`, thread không thay đổi trong lúc đánh giá, và bộ ngắt "không tiến triển" chưa kích hoạt. Mức trần an toàn mặc định là 8 lượt tiếp diễn ẩn, và các lần đánh giá không-tiến-triển giống hệt nhau lặp lại sẽ dừng sau 2 lần. `/goal clear` và bất kỳ đầu vào mới nào do người dùng viết đều thắng các lượt tiếp diễn đang xếp hàng. Khi mục tiêu đã đạt, DeerFlow tự động xóa nó và công bố trạng thái thread đã cập nhật.

Web UI hiển thị mục tiêu đang hoạt động ngay phía trên khung soạn thảo. Cùng lệnh đó cũng dùng được từ TUI và các kênh IM được hỗ trợ. Trong Web UI và các kênh IM được hỗ trợ, việc đặt `/goal <điều kiện hoàn thành>` cũng khởi động một lượt chạy với điều kiện đó làm tác vụ; các lệnh xem trạng thái và xóa thì chỉ quản lý trạng thái mục tiêu. Việc đặt hoặc xóa mục tiêu sẽ bị từ chối khi thread đó đang có một lượt chạy dở dang, kể cả lượt chạy thuộc về một worker Gateway khác, để checkpoint của mục tiêu không tách khỏi dòng dõi checkpoint của lượt chạy đang hoạt động.

Khi vai trò của bạn không có `runs:create`, Web UI sẽ từ chối một tác vụ mới hoặc `/goal <điều kiện hoàn thành>` trước khi chuẩn bị thread hay lưu mục tiêu, và giữ lại bản nháp của bạn để thử lại. Việc xem trạng thái mục tiêu, xóa mục tiêu và `/compact` vẫn do quyền trên chính endpoint của chúng quyết định.

### Nén ngữ cảnh thủ công

Việc nén tự động và thủ công đều loại các tin nhắn nhắc việc (todo reminder) cũ ra khỏi cả
đầu vào tóm tắt lẫn ngữ cảnh được giữ lại. Danh sách todo hiện tại vẫn nằm trong trạng thái thread.
Ở chế độ lập kế hoạch, nếu lệnh gọi `write_todos` gốc không còn nhìn thấy được,
DeerFlow sẽ thêm một lời nhắc dùng trạng thái tác vụ mới nhất trước lệnh gọi model kế tiếp.
Việc nén bị bỏ qua hoặc thất bại sẽ giữ nguyên các tin nhắn hiện có.

Tùy chọn `pii_redaction.enabled` sẽ che các định danh được phát hiện trong tin nhắn người dùng,
kết quả tool từ xa, đầu vào nén, các bản tóm tắt được chèn lại, và đầu vào tạo tiêu đề bằng LLM đã cấu hình.
Mặc định nó tắt. Các placeholder tóm tắt hiện có giữ chỗ các chỉ số
để giá trị mới không tái sử dụng chúng sau khi nén. Không có ánh xạ PII nào
được lưu lại, nên các giá trị lặp lại không thể bị liên kết ngược về nguồn đã nén; việc đánh số
có thể thay đổi khi lịch sử hoặc các placeholder tóm tắt biến mất. Văn bản thread thô và
các tiêu đề dự phòng cục bộ vẫn khả dụng để hiển thị; việc trích xuất bộ nhớ nằm ngoài
phạm vi của tính năng này.

Web UI giữ nguyên thứ tự tin nhắn đã lưu khi gộp lịch sử với các cập nhật trực tiếp. Các bước streaming quanh một kết quả đã lưu bên trong lịch sử đã nạp vẫn nằm cạnh nhau, kể cả những bước đến sau kết quả đó. Các bước được ghi lại trong lúc nén cũng vẫn hiển thị trước kết quả đã lưu của chúng khi lịch sử chưa được làm mới và giao diện chưa kịp render chúng.

Việc nén giữ lại yêu cầu hiện tại của người dùng và tóm tắt các hoạt động assistant/tool cũ hơn. Khi việc cứu lấy yêu cầu đó để lại một cửa sổ tóm tắt chỉ gồm assistant/tool, cơ chế cắt bớt đầu vào sẽ ưu tiên phần nội dung mới nhất của nó. Với các lịch sử hỗn hợp mà điểm neo là tin nhắn người dùng nằm ngoài ngân sách cắt bớt, việc nén vẫn giữ phương án dự phòng "tin nhắn cuối cùng" sẵn có. `summarization.trim_tokens_to_summarize` (mặc định 4000) điều khiển việc cắt bớt đầu vào tóm tắt thô; việc escape và định dạng prompt sẽ phát sinh thêm chi phí vượt ngoài ngân sách đó. Đặt tùy chọn này thành `null` sẽ tắt việc cắt bớt đầu vào cho model tóm tắt; chỉ chọn phương án đó khi model có thể tiếp nhận toàn bộ lịch sử đang được nén.

Dùng `/compact` trong khung soạn thảo của Web UI để tóm tắt phần ngữ cảnh cũ của thread hiện tại. DeerFlow vẫn giữ toàn bộ cuộc chat hiển thị, nhưng các lệnh gọi model về sau sẽ dùng bản tóm tắt đã nén cộng với các tin nhắn gần đây. Lệnh này bị bỏ qua khi chưa có đủ lịch sử để nén, và bị chặn khi thread đang có một lượt chạy dở dang, kể cả khi lượt chạy đó thuộc về một worker Gateway khác. Nếu một lượt giữ chỗ ở môi trường nhiều worker mất lease, DeerFlow sẽ hủy bộ ghi checkpoint trước khi lượt chạy thay thế tiếp tục, rồi trả về một lỗi xung đột có thể thử lại sau khi dọn dẹp. Việc sửa tiêu đề thread cũng được tuần tự hóa qua cùng ranh giới ghi trạng thái đó, và sẽ báo xung đột mà không đóng hộp thoại đổi tên khi có một lượt chạy đang hoạt động.

Header của cuộc chat cũng hiển thị một thước đo cửa sổ ngữ cảnh khi model đang chọn có `context_window` được cấu hình là số dương. Nó ước lượng số token tin nhắn của checkpoint mới nhất đã được dựng, và giữ hiển thị tỷ lệ phần trăm trước đó của cùng thread trong lúc dữ liệu được nạp lại, độc lập với thiết lập hiển thị mức dùng token tích lũy.

### Sub-Agent

Các lệnh gọi `task` thông thường chấp nhận `context_mode="isolated"` (mặc định) hoặc
`context_mode="snapshot"`. Các tác vụ isolated nhận prompt được ủy quyền như trước.
Các tác vụ snapshot còn nhận thêm phần hội thoại được giữ lại của agent cha và
bản tóm tắt nén, được ghi lại tại thời điểm điều phối như bối cảnh lịch sử. Điều này giúp ích cho
những lần bàn giao phụ thuộc vào các yêu cầu trước đó hoặc các hướng tiếp cận đã thất bại, đổi lại là
tốn thêm token đầu vào. Văn bản được giữ lại, các mô tả/kết quả lệnh gọi tool, và
các khối media đầu vào có thể tuần tự hóa sang JSON đều được mang theo. Các khối media dạng nhị phân
hoặc không tuần tự hóa được sẽ trở thành một thông báo lược bỏ tường minh; phần hội thoại
xung quanh vẫn khả dụng. Prompt hệ thống của agent cha, các tin nhắn framework ẩn
(chẳng hạn bộ nhớ được chèn vào và lời nhắc todo), các khối suy luận, metadata thực thi tool,
và các lệnh gọi tool đang chờ đều bị loại trừ. Các mô tả lệnh gọi tool
cần có một kết quả khớp được giữ lại, bao gồm cả những lệnh gọi song song với tác vụ hiện tại.
Các phản hồi làm rõ ẩn hợp lệ của người dùng vẫn là một phần của cuộc hội thoại. Agent con
giữ vai trò, model, tool và các hạn chế skill của riêng nó. Các bản ghi tool của agent cha
không thể thỏa mãn các kiểm tra thực thi của agent con. Lịch sử của agent cha và agent con tiến triển
độc lập sau đó; hành vi dùng chung sandbox/hệ thống tệp không thay đổi.
Chế độ snapshot không khôi phục những tin nhắn đã bị nén và cũng không hứa hẹn việc tái sử dụng
prompt cache. Các mục `batch_task` bền vững vẫn cần prompt tự chứa đầy đủ.

Để có một so sánh thủ công, mang tính tổng hợp giữa các lần bàn giao đầy đủ và snapshot, xem
[đánh giá context snapshot](backend/scripts/benchmark/context_snapshot/README.md).

Custom Agent hỗ trợ một tên hiển thị Unicode tùy chọn, bao gồm cả tiếng Trung và
emoji. Hãy mở **Agent settings → Display name** của một agent để đặt nó (tối đa 100
code point Unicode), hoặc để trống để hiển thị định danh sẵn có. Các ký tự điều khiển
và ký tự điều khiển định dạng hai chiều sẽ bị từ chối; văn bản đa ngôn ngữ thông thường
và emoji đều được hỗ trợ. Các tên chỉ gồm ký tự vô hình và các ký tự định dạng vô hình
như khoảng trắng độ rộng bằng không sẽ bị từ chối. Các tên hiển thị không hợp lệ trong
kho lưu trữ cũ hoặc bị sửa tay sẽ quay về dùng định danh của agent khi đọc;
một cảnh báo sẽ chỉ rõ agent bị ảnh hưởng.
Việc khởi tạo lại vẫn giữ các tên hiển thị hợp lệ. Trang thư viện,
header của cuộc chat và trang chào mừng đều dùng nhãn này; URL và các lệnh gọi API vẫn tiếp tục dùng
trường `name` tiếng Anh ổn định. Bên gọi API có thể truyền `display_name` trong các yêu cầu tạo
hoặc cập nhật agent; nếu bỏ qua khi cập nhật thì giá trị được giữ nguyên, còn `null` sẽ xóa nó.
Cùng trường tùy chọn đó cũng được hỗ trợ trong `config.yaml` của agent.

Sub-agent là một cách tối ưu, không phải phản ứng mặc định cho một yêu cầu phức tạp.

Sau khi nút Stop ngắt một tác vụ được ủy quyền trước khi nó trả về phản hồi, lượt người dùng
kế tiếp sẽ đánh dấu tác vụ trước đó là đã hủy trong ngữ cảnh bền vững của agent để nó
có thể thử lại. Các phản hồi đã có được giữ nguyên. Những phản hồi cũ không có metadata trạng thái
có thể vẫn hiển thị là đang tiến hành; kết cục của chúng không được suy đoán từ nội dung văn bản.

Lead agent có thể sinh ra sub-agent ngay khi cần — mỗi sub-agent có ngữ cảnh, tool và điều kiện kết thúc riêng theo phạm vi của nó — khi việc ủy quyền mang lại lợi ích ròng rõ ràng nhờ độ trễ song song thực sự, năng lực chuyên biệt, hoặc sự cách ly ngữ cảnh. Nó giữ các phạm vi phụ thuộc lẫn nhau và các tác dụng phụ chồng lấn ra khỏi việc điều phối song song; một chuỗi tuần tự có giới hạn vẫn có thể chạy trong một sub-agent khi lợi ích về chuyên môn hoặc cách ly ngữ cảnh rõ ràng thắng thế. Lead agent dùng ít sub-agent hữu ích nhất có thể và đánh giá lại các lô sau, thay vì tỏa ra nhiều nhánh chỉ vì tác vụ lớn hay có nhiều bước. Sub-agent báo cáo lại kết quả có cấu trúc, và lead agent kiểm chứng rồi tổng hợp chúng thành một đầu ra mạch lạc. Các biên nhận tool xác định bao phủ cả tin nhắn tool trực tiếp lẫn các kết quả `Command` làm thay đổi trạng thái, chẳng hạn phản hồi `task` được ủy quyền; khi sổ biên nhận chạm ngân sách ngữ cảnh, nó giữ lại các hành động mới nhất cùng ID biên nhận gốc của chúng. Người vận hành có thể tắt lớp truy xuất nguồn gốc này bằng `verification.receipts_enabled: false`. Các skill đã cấu hình của sub-agent được phân giải từ cùng catalog theo phạm vi người dùng như lead agent, nên các skill tùy chỉnh thuộc sở hữu người dùng vẫn khả dụng mà không phơi ra phiên bản của người dùng khác. Các tin nhắn AI và tool nội bộ của chúng chỉ nằm trong phạm vi graph được ủy quyền chứ không đi vào luồng chat của agent cha. Lịch sử thread được nạp lại cũng tuân theo đúng ranh giới đó: các phản hồi AI của sub-agent được ghi lại qua callback vẫn xem được trong phần chẩn đoán sự kiện của lượt chạy nhưng bị loại khỏi bản ghi hội thoại của agent cha, trong khi kết quả `task` của agent cha vẫn gắn với thẻ tác vụ con của nó. Các sub-agent chạy dài sẽ nén phần lịch sử cũ khi bật tính năng tóm tắt và chèn lại bản tóm tắt dưới dạng ngữ cảnh bền vững ẩn có bảo vệ trước khi tiếp tục, nên các hoạt động assistant/tool gần đây vẫn bám sát tác vụ. Các chỉ dẫn hệ thống của chúng, bao gồm vai trò và hợp đồng báo cáo, vẫn tồn tại qua việc nén; nếu chỉ còn những chỉ dẫn đó và yêu cầu hiện tại để tóm tắt thì việc nén sẽ bị bỏ qua. Các lỗi yêu cầu của nhà cung cấp/model được báo cáo là tác vụ sub-agent thất bại chứ không phải kết quả thành công, để lead agent và Web UI phản ứng đúng. Các lượt chạy cha đồng thời cũng nhận được ID thực thi sub-agent độc lập ở phía server, nên một nhà cung cấp tái sử dụng ID lệnh gọi tool không thể khiến một lượt chạy poll, hủy hay dọn dẹp tác vụ nền của lượt chạy khác. Các thẻ sub-agent khi thu gọn sẽ hiển thị model đang dùng và, khi nhà cung cấp trả về metadata usage, một tổng token tích lũy được cập nhật sau mỗi lệnh gọi LLM hoàn tất của sub-agent và vẫn còn sau khi tải lại. Khi bật theo dõi mức dùng token, mức dùng của sub-agent đã hoàn tất được quy về bước điều phối tương ứng dựa trên metadata tin nhắn tool cuối cùng của lượt chạy đó, chứ không dựa trên một cache ID nhà cung cấp toàn cục của tiến trình.

Với các tiêu chí chấp nhận tệp, một tệp thường rỗng trong workspace dùng chung vẫn có thể thỏa mãn `file:<path> exists` và `file_written:<path>`, kể cả trên các sandbox từ xa. Nó không thỏa mãn `file:<path> non-empty`, với một kết quả "tệp rỗng" xác định.

Các tin nhắn cuối cùng không có nội dung của sub-agent sẽ báo `No response generated` thay vì văn bản `None` nguyên văn. Một phương án dự phòng cho lỗi nhà cung cấp mà không có nội dung sẽ báo chi tiết lỗi có cấu trúc của nó khi có.

Một `task` thông thường cũng nhận được một snapshot phòng vệ về các tệp đã tải lên hiện tại của lượt chạy điều phối. Nhờ vậy các sub-agent đủ điều kiện có thể dùng `list_uploaded_files` để tìm các tệp từ lượt trước mà không trả về các tệp đính kèm của cùng lượt như thể là dữ liệu lịch sử. Các worker `batch_task` bị trễ hoặc được khôi phục sẽ để tool này ở trạng thái tắt vì chúng không có ranh giới tải lên cục bộ theo lượt hợp lệ.

Các worker `batch_task` bền vững dùng một snapshot plugin thuộc sở hữu ứng dụng để lắp ráp và thực thi tool. Các tác vụ được khôi phục sẽ nhận snapshot plugin của worker mới sau khi Gateway khởi động lại; các đối tượng plugin không bao giờ được lưu trong bản ghi tác vụ bền vững.

Việc ủy quyền `task` thông thường và việc thực thi `batch_task` bền vững tường minh dùng chung sức chứa tiến trình `subagent_runtime` được xác định lúc khởi động. Chế độ batch giữ các tập mục độc lập lớn trong SQL với các giới hạn riêng về tổng số, số đang sống và số đang chạy, kèm khả năng khôi phục sau khởi động lại, kết quả có giới hạn, và một bảng trong Web UI theo phạm vi thread. Bảng này phân trang qua các bản xem trước có giới hạn theo yêu cầu; toàn bộ văn bản kết quả đã lưu chỉ truy cập được qua bản xuất JSONL theo phạm vi chủ sở hữu, còn ngữ cảnh thực thi và phân quyền nội bộ thì không bao giờ đi vào các phản hồi hướng tới chủ sở hữu. Nếu worker batch sau này bị dừng hoặc tắt, các thread có batch đã lưu vẫn giữ khả năng xem từng mục ở chế độ chỉ-đọc và xuất JSONL; các nút điều khiển thực thi vẫn bị tắt cho đến khi worker chạy lại. Xem `config.example.yaml` và [hợp đồng hiện thực](docs/plans/2026-08-24-subagent-batch-capacity-implementation.md) để biết các giới hạn và ngữ nghĩa khôi phục.

Các tích hợp `create_deerflow_agent(...)` trực tiếp có thể tự sở hữu ranh giới đó một cách tường minh thay vì dựa vào quá trình khởi động của Gateway. Hãy dựng một `SubagentRuntime` duy nhất và dùng chung nó cho mọi graph trong ứng dụng đó; khi ấy `max_running`, tổng số theo từng lượt chạy thông thường, tool `task` đã gắn, và các tool batch bền vững tùy chọn của nó sẽ dùng chung snapshot và bộ điều khiển thực thi thuộc sở hữu bên gọi. Một runtime có kèm repository batch sẽ sở hữu một worker và phải được khởi động trước khi dựng graph, đồng thời phải được dừng khi ứng dụng tắt:

```python
from deerflow.agents import RuntimeFeatures, create_deerflow_agent
from deerflow.subagents import SubagentRuntime

runtime = SubagentRuntime.from_app_config(app_config, batch_repository=batch_repository)
async with runtime:
    graph = create_deerflow_agent(
        model,
        features=RuntimeFeatures(subagent=True),
        subagent_runtime=runtime,
    )
    # Phục vụ hoặc gọi graph trong khi worker bền vững đang chạy.
```

`SubagentRuntime.stop()` chờ dịch vụ batch thuộc sở hữu của nó hoàn tất trước khi lan truyền lệnh hủy của bên gọi, kể cả khi hủy nhiều lần. Lần xả này không có timeout; các thao tác repository và việc dọn dẹp tiến trình con bắt buộc phải kết thúc. Nếu việc tắt dịch vụ cũng thất bại hoặc bị hủy, lệnh hủy đầu tiên của bên gọi vẫn được giữ lại, với lỗi của dịch vụ là nguyên nhân.

Factory này vẫn không nạp YAML và không tạo hạ tầng SQL: bên gọi phải cung cấp snapshot cấu hình, repository và vòng đời. Vì nó chấp nhận một `system_prompt` thuộc sở hữu bên gọi, các tích hợp trực tiếp cũng tự chịu trách nhiệm về mọi câu chữ mà model nhìn thấy liên quan đến các giới hạn đó; middleware mặc định vẫn áp đặt các giới hạn runtime bất kể thế nào. Factory không gắn các tuyến HTTP theo phạm vi chủ sở hữu của Gateway hay Web UI, nên các ứng dụng trực tiếp phải tự phơi ra API/giao diện kết quả của mình nếu cần những bề mặt đó. Nếu chỉ cần ủy quyền thông thường, `SubagentRuntime(...)` không cần khởi động bất đồng bộ.

Quản trị viên có thể thêm, sửa, tắt và xóa các định nghĩa worker dùng lại được từ **Settings → Subagents**. Các định nghĩa dựng sẵn và định nghĩa từ `config.yaml` vẫn hiển thị ở đó dưới dạng mục chỉ-đọc. Lead Agent mặc định có thể dùng mọi sub-agent runtime đang bật; mỗi Custom Agent được tạo từ trang này thì có thể cho phép tất cả, không cho phép cái nào, hoặc chọn một tập nhất định. Lựa chọn đó được áp dụng cả trong danh bạ mà model nhìn thấy lẫn bởi tool `task` phía server. Trong phiên bản này, các định nghĩa được quản lý áp dụng cho toàn bộ deployment và tuân theo `agent_storage.backend`: tệp nguyên tử cho bản triển khai cục bộ, hoặc cơ sở dữ liệu ứng dụng dùng chung cho nhiều instance.

Ví dụ, việc nghiên cứu chỉ-đọc độc lập có thể chạy đồng thời khi lượng thời gian tiết kiệm được lớn hơn chi phí khám phá và tổng hợp bị trùng lặp, trong khi một lần refactor repository với các tệp dùng chung và phản hồi kiểm thử tuần tự thì vẫn nên để lead agent làm. Khi `max_concurrent_subagents` bằng `1`, phần hướng dẫn định tuyến song song và nhiều lô sẽ bị tắt; việc ủy quyền chỉ còn khả dụng khi có lợi ích thực chất về chuyên môn hoặc cách ly ngữ cảnh.

### Sandbox & Hệ thống tệp

`E2BSandboxProvider` dùng `wait` làm chính sách xử lý quá tải mặc định. Nó chờ trong
`acquire_timeout`, rồi làm lượt agent đó thất bại. DeerFlow không tự động thử lại lượt đó.
Client có thể dùng lỗi có cấu trúc để lên lịch thử lại.

Hãy dùng `burst` cùng `burst_limit` để cho phép một số VM bổ sung có giới hạn. Các chính sách `wait` và
`reject` chỉ dùng `replicas`. Chính sách `reject` có thể loại bỏ một VM còn ấm
trước khi trả về lỗi.

Với cơ chế sở hữu trong bộ nhớ, `replicas` giới hạn cho một tiến trình Gateway. Với cơ chế sở hữu
qua Redis, E2B chia sẻ một Hash sức chứa giữa các worker dùng chung
`sandbox.ownership.key_prefix`; khi đó `replicas` (cộng với phần burst đã cấu hình) là một giới hạn cứng
cho toàn deployment. Hãy dùng một tiền tố duy nhất và cùng một giới hạn hiệu dụng cho mỗi deployment.
Để thay đổi giới hạn, hãy dừng các Gateway của nó, xóa Hash sức chứa,
rồi khởi động lại; các worker không khớp sẽ "hỏng theo hướng an toàn".

Hash này đếm các VM từ xa và các lần tạo đang dở, sửa chữa các lần tạo bị gián đoạn
từ metadata của E2B, bảo vệ có thời hạn ân hạn với các thiếu sót trong kiểm kê lỗi thời, và chặn các lần
tạo mới khi Redis hoặc kiểm kê ban đầu không khả dụng. Hãy chạy Redis với chế độ lưu bền, bộ nhớ không bị đẩy ra (non-evicting) và có HA.

Cơ chế đối soát của E2B gia hạn các VM đang hoạt động với một timeout dương bao phủ được
nhịp đối soát đã cấu hình, ngay cả khi `idle_timeout` bằng 0 hoặc ngắn hơn nhịp đó.
Các VM còn ấm vẫn giữ hành vi idle-timeout đã cấu hình. Các mục "ấm" cục bộ đã hết hạn
không trực tiếp giải phóng sức chứa dùng chung: kiểm kê từ xa phải xác nhận
chúng đã biến mất qua thời gian ân hạn sẵn có trước đã.
Việc gia hạn cho VM đang hoạt động hoàn tất trước khi thao tác giải phóng đặt timeout ấm, nên một lượt
bảo trì chạy đồng thời không thể kéo dài tuổi thọ của một VM đang nhàn rỗi. Việc dọn các mục ấm cũng
giữ lại quyền sở hữu mà một yêu cầu mới giành được trong lúc quét dọn.
Các heartbeat sở hữu vẫn độc lập với các yêu cầu timeout chậm của E2B, ngăn
sự chậm trễ ở control plane làm hết hạn lease của các sandbox đang hoạt động.

E2B chụp snapshot `skills.container_path` khi nhà cung cấp khởi động và đưa
thư mục gốc chính tắc vào danh tính thread, hạt giống của warm pool và metadata từ xa.
Một VM được tạo cho một thư mục gốc khác sẽ không bao giờ được nhận nuôi; cơ chế đối soát sẽ thu hồi nó sau
thời gian ân hạn đã cấu hình khi không còn worker nào đang sống sở hữu nó. Hãy khởi động lại Gateway sau khi
thay đổi thư mục gốc.

Việc giành sandbox E2B dùng một executor có giới hạn. Các lần giành đang chờ không dùng
executor asyncio mặc định.

Mỗi lượt tải lên cho một mount E2B chấp nhận tối đa 512 MiB và 2.000 tệp. Lượt tải này
cũng có một hạn chót hợp tác 120 giây. Các phép chiếu skill và các mount đã cấu hình
dùng chung các giới hạn này. Nhà cung cấp kiểm tra hạn chót trước mỗi mount
và trong lúc tiền kiểm thư mục. Hạn chót dừng các lần tải tệp mới sau khi nó hết hạn.
Nó không ngắt các lệnh gọi hệ thống tệp hay SDK E2B đang diễn ra.

Một VM E2B giữ chỗ của nó cho đến khi E2B xác nhận đã hủy. Quy tắc này áp dụng cho
cả thao tác tạo lẫn thu hồi. Cơ chế khám phá có thể tìm thấy một VM từ một Gateway khác.
Khi tắt, một client khám phá không sở hữu VM sẽ được đóng lại mà không hủy VM đó.
Thao tác giải phóng ngừng đếm một lần chuyển trạng thái khi VM đi vào warm pool.
Các tình huống tranh chấp lúc tắt sẽ thử lại việc dọn dẹp từ xa sau một lần kill thất bại thoáng qua.
Thao tác reset hủy cả các VM E2B đang hoạt động lẫn đang ấm được theo dõi. Instance nhà cung cấp cũ
không thể nhận thêm lần giành nào nữa.

DeerFlow không chỉ *nói* về việc làm mọi thứ. Nó có máy tính của riêng mình.

Mỗi tác vụ có môi trường thực thi riêng với khung nhìn hệ thống tệp đầy đủ — skill, workspace, uploads, outputs. Agent đọc, ghi và sửa tệp. Nó có thể xem ảnh và, khi được cấu hình an toàn, thực thi lệnh shell.

Tool `grep` dựng sẵn tìm kiếm trong một tệp văn bản duy nhất hoặc trong tất cả các tệp văn bản khớp nằm dưới một thư mục, nên agent có thể tìm ngay trong một tài liệu đã tải lên mà không cần trước tiên mở rộng yêu cầu ra toàn bộ thư mục uploads.

Lệnh `ls` từ xa loại bỏ các thư mục con bị bỏ qua trước khi áp dụng giới hạn liệt kê 500 mục, nên các cây phụ thuộc và cây build không chiếm chỗ của các tệp cần nhìn thấy. Việc liệt kê tường minh một thư mục bị bỏ qua vẫn hiển thị nội dung của nó; các giới hạn về độ sâu và đầu ra thông thường vẫn có hiệu lực.

Việc liệt kê thư mục trên AIO sẽ loại bỏ các phiên shell đã biến mất để yêu cầu kế tiếp có thể phục hồi.
Sau một lần rớt kết nối, việc liệt kê thư mục và các lệnh shell thường trực sẽ báo một kết cục
không xác định mà không phát lại thao tác; các lệnh gọi sau đó dùng một phiên mới.

Phần dàn ý (outline) của các tệp Markdown đã tải lên nhận diện cú pháp tiêu đề ATX, dọn các dấu đóng bằng một lần quét hậu tố tuyến tính, và bỏ qua các ví dụ mã trong khối có rào, nên các dấu thăng và chú thích trong mã không
chiếm chỗ của các mục tài liệu thật trong phần xem trước tiêu đề của agent.
Các tệp Markdown UTF-8 có hoặc không có byte-order mark (BOM) đều cho ra cùng
dàn ý và bản xem trước dự phòng, với số dòng gốc được giữ nguyên.
Tiêu đề trong dàn ý giới hạn ở 200 ký tự và bản xem trước dự phòng giới hạn ở 2.000
ký tự cho mỗi tệp, kèm các dấu hiệu cắt bớt. Toàn bộ tệp đã tải lên vẫn khả dụng
cho các lần đọc có mục tiêu.

Các byte ảnh được nạp cho một lệnh gọi model thị giác chỉ tồn tại tạm thời: DeerFlow xóa tin nhắn base64 ẩn sau khi model đã tiêu thụ nó, để các checkpoint sau không liên tục nhân bản payload đó.

Sau mỗi lượt chạy, DeerFlow ghi lại một bản tóm tắt thay đổi workspace cho các thư mục `workspace` và `outputs` thuộc lượt chạy đó. Web UI hiển thị một huy hiệu "files changed" gọn trên lượt trả lời của assistant; mở nó ra sẽ thấy các tệp được tạo, sửa và xóa kèm diff văn bản khi an toàn để hiển thị. Thư mục uploads bị loại trừ vì đó là đầu vào của người dùng chứ không phải thay đổi do agent tạo ra, và các tệp tạm/gỡ lỗi của MCP stdio nằm trong namespace `.mcp/` thuộc DeerFlow cũng bị loại trừ vì chúng là trạng thái nội bộ của tiến trình (giống như `.git/` và `node_modules/`, bất kỳ thư mục nào tên `.mcp` đều bị loại trừ ở mọi độ sâu). Các tệp lớn, tệp nhị phân hoặc trông có vẻ nhạy cảm chỉ được hiển thị dưới dạng metadata.

Các tệp được trình bày qua `present_files` vẫn là một phần trạng thái artifact của thread, và Web UI khôi phục bảng artifact cùng tài liệu đang chọn sau khi làm mới trang. Khi một phản hồi đã hoàn tất trình bày thành công từ 2 đến 50 tệp, thẻ tệp cuối cùng của nó còn cung cấp một lựa chọn tải xuống dạng ZIP. Thành phần của gói lưu trữ được lấy từ biên nhận giao hàng cuối cùng chứ không từ các đường dẫn do trình duyệt cung cấp, và tệp ZIP chứa các phiên bản tệp hiện tại, vốn có thể đã thay đổi kể từ lúc phản hồi. Artifact chính thức đang được chọn sẽ được làm mới một lần khi lượt chạy kết thúc, để các chỉnh sửa hiển thị ra mà không cần tải lại thủ công. Các artifact văn bản UTF-8 hiện có nằm dưới `/mnt/user-data/outputs` cũng có thể được sửa và lưu tường minh ngay trong bảng đó trên Unix và Windows khi thread đang rảnh; việc lưu dùng cơ chế phiên bản nội dung để tránh ghi đè lên các thay đổi của agent.

Các artifact CSV và TSV mở ra dưới dạng bảng trong bảng artifact và trong một cửa sổ riêng. Bản xem trước giữ nguyên giá trị văn bản (kể cả số 0 ở đầu), hỗ trợ một hàng tiêu đề tùy chọn, và phân trang tối đa 200 hàng và 50 cột từ mẫu ban đầu. Các ô dài hoặc nhiều dòng có thể mở ra và sao chép đầy đủ. Hãy chuyển sang chế độ xem mã nguồn để kiểm tra hoặc sửa tệp; việc tải xuống và các cửa sổ riêng dùng phiên bản đã lưu.

Các artifact văn bản được truyền theo kiểu stream với hỗ trợ HTTP byte-range. Ban đầu Web UI
nạp tối đa 1 MiB, hiển thị kích thước bản xem trước khi tệp lớn hơn, và chờ
một hành động **Load full file** tường minh trước khi tải phần còn lại hoặc gắn
trình soạn thảo mã đầy đủ. Các artifact HTML, XHTML và SVG có khả năng thực thi vẫn bị buộc
phải tải xuống tại ranh giới Gateway.

Bản xem trước và việc tải xuống artifact giữ nguyên các chuỗi phần trăm nguyên văn trong tên tệp:
`report%20final.md` và `report final.md` vẫn là hai tệp khác nhau. Các liên kết Markdown
vẫn chấp nhận đường dẫn đã mã hóa URL.

Phần hướng dẫn cho `write_file` phản ánh giới hạn token đầu ra của model đang dùng, bao gồm cả các giá trị ghi đè của custom agent và chế độ thinking. Với những tài liệu dài hơn, agent được hướng dẫn viết theo từng phần với `append=True`; các model không có giới hạn xác định sẽ không nhận được gợi ý ngân sách bằng số.

Với `AioSandboxProvider`, việc thực thi shell diễn ra bên trong các container cách ly. Với `LocalSandboxProvider`, các tool tệp vẫn ánh xạ tới các thư mục riêng theo thread trên máy chủ, nhưng `bash` trên máy chủ mặc định bị tắt vì đó không phải một ranh giới cách ly an toàn. Chỉ bật lại bash trên máy chủ cho những quy trình cục bộ hoàn toàn đáng tin cậy. Các lệnh bash trên máy chủ có timeout theo thời gian thực, và các tiến trình chạy dài nên được khởi động ở chế độ nền với đầu ra chuyển hướng vào một tệp log trong workspace. Trên Windows, các ngoại lệ chuyển đổi đối số của Git Bash/MSYS chỉ giới hạn ở những tiền tố đường dẫn ảo an toàn không phải thư mục gốc, nên các bộ khởi chạy CLI native của máy chủ vẫn giữ được khả năng tương thích MSYS thông thường. Khi sandbox cục bộ quay về dùng PowerShell, nó thu đầu ra dưới dạng UTF-8 để văn bản CJK không phụ thuộc vào locale của máy chủ Gateway.

Các sandbox Docker AIO mặc định giữ hành vi cho phép lưu lượng đi ra tự do như trước
để đảm bảo tương thích. Người vận hành có thể đặt `sandbox.network.mode` thành `isolated` hoặc
`allowlist`; chế độ allowlist hỗ trợ các tên miền do người vận hành định nghĩa cùng một
thẻ Human Input tương tác để phê duyệt HTTP(S) tạm thời hoặc trong suốt vòng đời sandbox.
Các địa chỉ nội bộ, loopback, link-local, multicast và địa chỉ metadata của cloud vẫn
không thể phê duyệt. Các hostname bị từ chối sẽ bị chặn trước khi phân giải DNS.
Các lượt chạy ở chế độ tương tác `scheduled`, `webhook` hay `autonomous` sẽ tự động từ chối
mà không mở thẻ phê duyệt. Những lượt chạy không có người giám sát này chỉ tiếp tục với các giả định tối thiểu
cho công việc rủi ro thấp và có thể đảo ngược; công việc rủi ro cao hoặc không thể đảo ngược mà thiếu
ủy quyền đầy đủ sẽ trả về một kết quả `BLOCKED` có cấu trúc, nêu rõ
quyết định còn thiếu, ngay cả khi model cố gắng hỏi để làm rõ.
Sidecar đáng tin cậy dùng một cầu nối lưu lượng ra riêng cho từng sandbox thay vì
cầu mặc định dùng chung của Docker, và từ chối các tên trường HTTP mơ hồ trước khi
chuyển tiếp. Xem
[Cấu hình Sandbox](backend/docs/CONFIGURATION.md#sandbox-network-policy)
để biết các yêu cầu runtime và mô hình chính sách đầy đủ.

`AioSandboxProvider` thường tự phát hiện các mount dữ liệu thread từ backend của nó: các container
cục bộ dùng những thư mục gateway đã được mount, trong khi các sandbox từ xa/qua provisioner
nhận tệp tải lên thông qua đồng bộ hóa tường minh. Với những bản triển khai
mà cả hai phía chắc chắn dùng chung các thư mục user-data theo thread, bạn có thể
đặt `sandbox.thread_data_mounts: true` để bỏ qua bước giành sandbox và đồng bộ cho từng lần tải lên.
Hãy để trống trường này để hệ thống tự phát hiện; đặt sai có thể khiến các tệp đã tải lên
không khả dụng bên trong sandbox.

Đây chính là khác biệt giữa một chatbot có quyền dùng tool và một agent có môi trường thực thi thực sự.

```
# Đường dẫn bên trong container sandbox
/mnt/user-data/
├── uploads/          ← tệp của bạn
├── workspace/        ← thư mục làm việc của agent
└── outputs/          ← sản phẩm bàn giao cuối cùng
```

### Điều khiển trình duyệt bằng agent

Cơ chế tự phát hiện phụ thuộc của trình duyệt chấp nhận `name`, `group` và `use` theo bất kỳ
thứ tự nào trong một mục tool, với danh sách YAML có thụt lề hoặc không thụt lề.

Đọc một trang không giống với việc *sử dụng* nó. Bên cạnh các tool chỉ-đọc `web_fetch` và `web_capture`, DeerFlow còn có một nhóm tool trình duyệt dạng agentic (tùy chọn), duy trì một phiên trình duyệt sống theo từng cuộc hội thoại để agent có thể thực sự thao tác trên trang — điều hướng, đọc các phần tử tương tác, bấm, gõ, gửi biểu mẫu và đi theo các luồng nhiều bước trên những trang nặng JavaScript.

Mỗi hành động trả về một snapshot mới của các phần tử tương tác trên trang, mỗi phần tử được định danh bằng một số `[ref]` ổn định, nên agent hành động dựa trên thứ nó vừa quan sát thay vì đoán selector. Các URL đi ra mặc định được sàng lọc chống SSRF. Tính năng này chạy trên Playwright và được đóng gói như một gói bổ sung tùy chọn để bản cài cốt lõi vẫn gọn nhẹ:

```bash
cd backend
uv sync --extra browser
uv run playwright install chromium
```

Sau đó hãy bỏ chú thích các mục tool `group: browser` trong `config.yaml` (`browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`, `browser_get_text`, `browser_back`, `browser_screenshot`, `browser_close`). Quá trình khởi động `make dev` / Docker sẽ phát hiện tool `browser_navigate` đang bật và giữ lại gói bổ sung `browser` khi đồng bộ phụ thuộc. Gateway sẽ không khởi động được nếu tính năng điều khiển trình duyệt đã được cấu hình nhưng thiếu Playwright, và `/api/features` sẽ ẩn giao diện Browser trừ khi backend thực sự phục vụ được nó. Hãy giữ `headless: true` và `allow_private_addresses: false` cho mọi trường hợp ngoại trừ việc gỡ lỗi cục bộ, đáng tin cậy. Việc gắn vào một Chrome sẵn có bằng `cdp_url` không thể áp dụng cơ chế bảo vệ SSRF cho tài nguyên con/chuyển hướng của DeerFlow, nên nó sẽ "hỏng theo hướng an toàn" trừ khi `allow_unguarded_cdp: true` xác nhận tường minh rủi ro đó; chỉ dùng nó với một trình duyệt cục bộ đáng tin cậy. Các phiên trình duyệt là cục bộ trong tiến trình; hãy giữ `GATEWAY_WORKERS=1` khi nhóm tool này được bật, vì cơ chế điều phối worker thông thường của uvicorn không đảm bảo ái lực theo thread.

Các cuộc chat với Custom Agent sẵn có, không phải dạng mock, cũng phơi ra các nút điều khiển Browser Live khi tính năng điều khiển trình duyệt khả dụng và agent hoặc để `tool_groups` không giới hạn, hoặc có bao gồm nhóm `browser`. Một danh sách cho phép nhóm tool tường minh mà không có `browser` sẽ giữ các nút điều khiển đó ở trạng thái ẩn.

Client Browser Live trong workspace thương lượng để dùng khung WebSocket JPEG dạng nhị phân,
chỉ giữ lại khung mới nhất đang chờ cho mỗi lần làm mới màn hình, và thu hồi
các object URL bị thay thế. Các thông điệp điều khiển của Gateway vẫn là JSON, và các client không
yêu cầu năng lực nhị phân vẫn dùng giao thức khung JSON/base64 kiểu cũ.

### Context Engineering

**Ngữ cảnh sub-agent được cách ly**: Mỗi sub-agent chạy trong ngữ cảnh cách ly của riêng nó. Điều này nghĩa là sub-agent sẽ không nhìn thấy ngữ cảnh của agent chính hay của các sub-agent khác. Đây là điều quan trọng để đảm bảo sub-agent có thể tập trung vào đúng tác vụ trước mắt và không bị phân tâm bởi ngữ cảnh của agent chính hay các sub-agent khác.

**Tóm tắt**: Trong một phiên, DeerFlow quản lý ngữ cảnh một cách quyết liệt — tóm tắt các tác vụ con đã hoàn thành, đẩy các kết quả trung gian ra hệ thống tệp, nén lại những gì không còn liên quan trực tiếp. Nhờ vậy nó giữ được sự sắc bén xuyên suốt những tác vụ dài, nhiều bước mà không làm nổ cửa sổ ngữ cảnh.

**Khôi phục nghiêm ngặt cho lệnh gọi tool**: Khi một nhà cung cấp hoặc middleware làm gián đoạn vòng lặp gọi tool, DeerFlow giờ đây sẽ loại bỏ metadata lệnh gọi tool thô ở cấp nhà cung cấp trên các tin nhắn assistant bị dừng ép buộc, và chèn các kết quả tool giữ chỗ cho những lệnh gọi lơ lửng trước lần gọi model kế tiếp. Điều này ngăn các model reasoning tương thích OpenAI vốn kiểm tra nghiêm ngặt chuỗi `tool_call_id` bị lỗi vì lịch sử sai định dạng.

**Kết thúc lượt chạy tool có thể nhìn thấy**: Với các lượt tương tác, DeerFlow sẽ thử lại một lần khi phản hồi cuối cùng sau tool bị rỗng, rồi hiển thị một lỗi rõ ràng thay vì báo cáo một lượt chạy thành công một cách âm thầm.

### Đọc một cuộc hội thoại được tham chiếu

Bên gọi Gateway API có thể tự chọn bật `read_conversation` và gửi kèm một danh sách
`conversation_references` cùng lượt chạy. Khi đó lead agent có thể đọc từng trang có giới hạn
của phần văn bản đang hiển thị hiện tại trong những cuộc hội thoại mà họ sở hữu. Quyền đọc
hết hiệu lực cùng lượt chạy, và văn bản trong các tin nhắn cũ không cấp quyền truy cập. Phần văn bản mà
agent đã đọc vẫn nằm lại trong cuộc hội thoại đích sau khi quyền truy cập hết hạn hoặc nguồn bị xóa.
Một tin nhắn quá dài so với một lần đọc sẽ mang theo phần tiếp nối, để agent có thể đọc nốt phần còn lại;
nó chỉ hỏi xin phần còn thiếu nếu lần đọc đó không khả dụng.
Các client SDK không thể thêm trường ở cấp cao nhất của yêu cầu có thể gửi cùng danh sách đó dưới dạng
`context.conversation_references`, và `GET /api/features` cho biết tool này có được bật hay không.
Khi được bật, khung soạn thảo trên web hiển thị nút "Reference a conversation" bên cạnh nút đính kèm:
hãy chọn tối đa ba cuộc hội thoại gần đây của bạn, và chúng chỉ được đính kèm vào tin nhắn kế tiếp,
hiển thị dưới dạng các chip trong khung soạn thảo và trong bản ghi hội thoại. Không có việc tìm kiếm lịch sử tự động nào. Xem
[cấu hình](backend/docs/CONFIGURATION.md#reading-referenced-conversations)
và [hợp đồng yêu cầu](backend/docs/API.md#referencing-a-previous-conversation).

### Bộ nhớ dài hạn

[Bài benchmark cách ly phạm vi của DeerMem](backend/scripts/benchmark/deermem_scope_isolation/README.md) (tự chọn bật)
kiểm tra tính an toàn ngữ nghĩa trên các fact và bản tóm tắt, cùng việc định tuyến fact giữa các người dùng
và agent. Các lần trích xuất thất bại là lỗi thực thi có thể thử lại, không phải là "đạt" về mặt an toàn.

Với DeerMem, `memory.backend_config.storage_class: markdown` cho phép đọc bản tóm tắt theo kiểu
khoan dung trong khi vẫn ghi bằng JSON và giữ giao diện hiện có. Một tệp `memory.json` được sửa tay
có thể chứa đối tượng JSON của nó bên trong một khối có rào `memory-json`;
các dấu backtick nhúng và các ghi chú có rào phía sau đều được hỗ trợ. Phần văn bản tóm tắt không phân tích được
sẽ được chuyển sang `memory.json.corrupt-<timestamp>` để khôi phục trước khi dựng lại.
`storage_path` phải trỏ tới thư mục gốc chứa dữ liệu, chứ không phải một tệp JSON đã tồn tại.

Quá trình tắt Gateway sẽ xả hết các cập nhật bộ nhớ trước khi đóng backend, ngay cả khi
việc tắt bị hủy. Lỗi khi nạp lại cấu hình được ghi log mà không làm dừng quá trình
dọn dẹp runtime. Với Kubernetes, hãy dự trù `terminationGracePeriodSeconds` đủ cho mọi hook lúc tắt,
việc phân giải cấu hình/backend, `memory.shutdown_flush_timeout_seconds`, và việc
đóng backend, cộng thêm một biên an toàn. Timeout xả không giới hạn `close()`:
các backend tùy chỉnh phải đảm bảo việc đóng diễn ra nhanh hoặc có giới hạn bên trong, nếu không quá trình tắt có thể phải chờ
cho đến khi tiến trình bị buộc dừng.

Hầu hết agent quên sạch mọi thứ ngay khi cuộc hội thoại kết thúc. DeerFlow thì nhớ.

DeerMem có thể tùy chọn loại bỏ các fact trích xuất gần-trùng-lặp bằng
`memory.backend_config.fact_dedup_enabled: true` và
`fact_dedup_similarity_threshold` (mặc định `0.7`, khoảng `0.5`–`1.0`).
Đây là một heuristic cục bộ, xác định, dựa trên từ/bigram CJK, chỉ so sánh các fact trong
cùng một người dùng, agent và danh mục; nó không phải là cơ chế phát hiện tương đương ngữ nghĩa.
Nó giữ nguyên ID, nội dung và thời điểm tạo hiện có, nâng độ tin cậy lên mức
tối đa, và chỉ làm mới nguồn khi độ tin cậy tăng lên. Các thay thế do sửa lỗi tường minh
và các fact được đề xuất xóa sẽ được bảo vệ khỏi việc gộp gần-trùng-lặp. Một lần gộp
không được tính là sự xác nhận của người dùng. Cơ chế này mặc định tắt và
không ảnh hưởng tới các cập nhật fact có mục tiêu.

DeerFlow cũng có một backend bộ nhớ tùy chọn tên `openviking`. Nó dùng
gói chính thức `langchain-openviking` để ghi lại các lượt đã hoàn tất vào các OpenViking Session
ổn định và gợi nhớ bộ nhớ để chèn vào prompt, trong khi DeerMem vẫn là mặc định.
Bản tích hợp ban đầu hỗ trợ một người dùng DeerFlow với
một USER API key OpenViking gắn với thông tin đăng nhập ở chế độ `memory.mode: middleware` và
không kế thừa các header HTTP tùy ý từ `ovcli.conf`.
Xem [backend bộ nhớ OpenViking](docs/OPENVIKING.md) để biết cấu hình,
hành vi và các giới hạn hiện tại của nó.

Xuyên suốt các phiên, DeerFlow xây dựng một bộ nhớ bền vững về hồ sơ, sở thích và tri thức tích lũy của bạn. Bạn càng dùng nhiều, nó càng hiểu bạn — phong cách viết của bạn, ngăn xếp công nghệ của bạn, những quy trình bạn lặp đi lặp lại. Bộ nhớ được lưu cục bộ và vẫn nằm dưới sự kiểm soát của bạn.

DeerMem vẫn là backend cục bộ mặc định. Một backend `mem0` tự chọn bật cũng
khả dụng cho mem0 Platform API dạng dịch vụ hoặc các server tự host tương thích API.
`base_url` mang token của nó mặc định phải dùng HTTPS; HTTP thuần
đòi hỏi phải tự chọn bật tường minh cho môi trường phát triển cục bộ. Xem
[hướng dẫn backend mem0](backend/packages/harness/deerflow/agents/memory/backends/mem0/README.md).

Một backend `honcho` tự chọn bật cũng khả dụng cho Honcho tự host hoặc dạng dịch vụ (API v3).
Nó xây dựng bộ nhớ mô hình người dùng — các sở thích dài hạn và một biểu diễn làm việc
xuyên phiên — ở phía server của Honcho, nên backend không thực hiện lệnh gọi LLM nào ở cục bộ.
Mỗi người dùng có một workspace cách ly được suy ra từ `user_id`; nếu thiếu user id thì
hệ thống "hỏng theo hướng an toàn" thay vì quay về một workspace dùng chung.
Việc CRUD fact và chỉnh sửa fact trong trang Settings không khả dụng với backend này. Xem
[hướng dẫn backend Honcho](backend/packages/harness/deerflow/agents/memory/backends/honcho/README.md).

Các cập nhật bộ nhớ giờ đây bỏ qua các mục fact trùng lặp ngay lúc áp dụng, nên những sở thích và ngữ cảnh lặp lại không tích tụ vô tận qua các phiên.
Các tệp bộ nhớ kiểu cũ được chuẩn hóa khi đọc hoặc khi nhập, bao gồm cả metadata fact có thể khôi phục, nên dữ liệu cục bộ cũ vẫn dùng được khi lược đồ tiến hóa. Việc chuẩn hóa ở frontend và backend dùng độ tin cậy `0.5` khi giá trị bị thiếu hoặc không hợp lệ, đặt nguồn trống thành `unknown`, và cắt bỏ khoảng trắng thừa trong nội dung fact.

Ở chế độ `middleware` mặc định của DeerMem, việc trích xuất tự động giờ đây phân loại mọi fact được đề xuất theo phạm vi, độ bền và thẩm quyền trước khi một cổng ghi xác định chấp nhận nó. Chỉ những fact bền vững, mang tính mô tả ở cấp người dùng mới được lưu; các ràng buộc thuộc về thread hiện tại hoặc dự án và các quyền hành động một lần vẫn nằm trong trạng thái hội thoại. Các bản tóm tắt toàn cục cho người dùng đòi hỏi cả phạm vi người dùng lẫn thẩm quyền mô tả, việc xóa do mâu thuẫn bị khống chế theo phạm vi, và một thao tác xóa phụ thuộc vào bản thay thế chỉ được áp dụng khi bản thay thế đó thực sự vượt qua được khâu kiểm tra và lưu trữ. Các nhãn phân loại này chỉ là metadata của quá trình trích xuất, không phát sinh lệnh gọi LLM bổ sung, và không được ghi vào các tệp fact. Các tool CRUD tường minh trong `memory.mode: tool` vẫn là một đường đi riêng, do model điều khiển. Những bản triển khai ghi đè các prompt DeerMem đi kèm thông qua `memory.backend_config.prompts_dir` phải bổ sung các trường phân loại mới vào template tùy chỉnh của mình (các định dạng fact/summary/removal của `memory_update` và lược đồ consolidated-fact của `consolidation`): cổng ghi "hỏng theo hướng an toàn", nên một template chưa được cập nhật sẽ chặn mọi thao tác ghi fact, summary và removal do trích xuất tạo ra, và điều này chỉ lộ ra qua chỉ số `rejected_by_scope_gate` cùng cảnh báo về tỷ lệ từ chối cao.

Khi một phạm vi fact chạm `max_facts`, DeerMem mặc định vẫn dùng thứ tự loại bỏ chỉ-dựa-trên-độ-tin-cậy như trước đây. Người vận hành có thể tự chọn bật `memory.backend_config.fact_eviction_policy: hybrid-v1`, vốn kết hợp độ tin cậy có giới hạn (65%), độ mới của xác nhận tường minh (25%) và độ "nóng" truy cập do truy vấn tạo ra (10%). Metadata tín hiệu của chế độ lai chỉ được thu thập khi hybrid-v1 hoặc chế độ shadow được bật. Xác nhận tường minh được trả về dưới dạng `factsToReinforce` bởi lệnh gọi LLM cập nhật bộ nhớ sẵn có, và chỉ được chấp nhận khi việc xử lý tin nhắn theo kiểu xác định cũng phát hiện một tín hiệu củng cố từ người dùng; nó cũng đặt lại đồng hồ rà soát độ cũ của fact. Cổng xác định này hoạt động ở cấp lô: nó chỉ khẳng định rằng một tin nhắn của con người nằm trong sáu tin nhắn đã lọc gần nhất của lô trích xuất hiện tại khớp với một mẫu củng cố. ID trong `factsToReinforce` do LLM chọn sẽ cung cấp liên kết tới fact; DeerMem không tự xác minh độc lập sự tương ứng giữa tín hiệu và fact. Việc trích xuất lặp lại hay chèn tự động không bao giờ được tính là xác nhận một fact. Các prompt `memory_update` tùy chỉnh nên bổ sung mảng tùy chọn `factsToReinforce` để tham gia vào cơ chế độ-mới-của-xác-nhận. Độ nóng truy cập được lưu trong một sidecar suy giảm riêng biệt và chỉ tăng khi `memory_search` thực sự trả về fact đó, nên việc đọc không ghi lại phần Markdown chính tắc hay `updatedAt` của nó. Chế độ lai cũng dành riêng một số tối thiểu có giới hạn các suất cho fact sửa lỗi (10% của mức trần, tối đa 10; các suất không dùng sẽ quay lại cạnh tranh bình thường). Việc xóa do hết sức chứa vẫn là xóa vật lý, nhưng một bản kiểm toán chỉ-gồm-metadata có giới hạn sẽ ghi lại ID fact, danh mục, điểm chính sách và lý do mà không sao chép nội dung fact. `fact_eviction_shadow_enabled: true` đánh giá hybrid-v1 song song với chính sách mặc định mà không làm thay đổi việc giữ lại thực tế. Tính năng này không thêm lệnh gọi LLM nào và có thể hoàn tác bằng cách chọn lại `confidence`.

Bộ nhớ lưu trên tệp giờ đây tách bạch ngữ cảnh người dùng toàn cục khỏi các fact của agent. Mỗi người dùng có một `memory.json` chỉ chứa các bản tóm tắt `user` và `history` độc lập với dự án; mọi fact là một tệp Markdown chính tắc nằm dưới `agents/{agent_name}/facts/`. Các lệnh gọi middleware của lead agent, API, Settings, import/export và client nhúng hiện có mà bỏ qua `agent_name` sẽ được phân giải bên trong DeerMem về bucket dành riêng `__default__`. Bucket đó nằm ngoài ngữ pháp tên hợp lệ của custom agent, nên một custom agent thật tên `lead-agent` sẽ có kho fact riêng, và việc xóa một custom agent không thể xóa một thư mục chỉ-chứa-bộ-nhớ mà không có `config.yaml`. Các định danh agent công khai không phân biệt hoa thường và được chuẩn hóa về chữ thường. Các bên đọc qua runtime/API vẫn nhận được một mảng `facts` tương thích cho agent đang chọn/mặc định, nên frontend không đọc fact của agent từ `memory.json`; metadata `source` có cấu trúc trong Markdown được chiếu về trường chuỗi kiểu cũ tại ranh giới MemoryManager. Một thao tác Clear All không giới hạn phạm vi trước tiên sẽ di chuyển các fact từ những tệp JSON theo từng agent kiểu cũ chưa được đọc mà không tiếp nhận các bản tóm tắt sắp bị xóa của chúng, rồi xóa các bản tóm tắt dùng chung và fact khỏi mọi bucket agent trong khi vẫn giữ các tệp cấu hình agent, nên một lần đọc sau đó không thể làm sống lại những fact cũ đã bị bỏ qua; một thao tác xóa giới hạn tường minh theo agent thì chỉ xóa fact của agent đó. Ở lần đọc bình thường đầu tiên, các fact cũ nhúng trong tệp JSON của người dùng sẽ tự động được chuyển sang `__default__`; các fact từng được ghi vào bucket `lead-agent` ngầm định trước đây cũng được chuyển đi khi thư mục đó không phải một custom agent thật. Việc di chuyển và các thao tác ghi thông thường chỉ thông báo cho adapter truy hồi đã cấu hình sau khi các khóa lưu trữ bền vững đã được nhả. DeerMem mặc định dùng một adapter SQLite FTS5/BM25 có nhận biết phạm vi, chỉ lưu dữ liệu chỉ mục dẫn xuất có thể dựng lại trong `.retrieval/`, và dựng lại nó ở chế độ nền trong lúc Gateway khởi động hoặc theo kiểu lười ở lần tìm kiếm theo phạm vi đầu tiên. Một chỉ mục dẫn xuất bị hỏng sẽ được tạo lại tự động. Đặt `memory.backend_config.retrieval_adapter` thành chuỗi rỗng để tắt nó và dùng phương án dự phòng so khớp chuỗi con cục bộ. Việc tách từ tiếng Trung là tùy chọn; hãy cài gói bổ sung `memory-zh` của backend (`uv sync --extra memory-zh`) để có tìm kiếm cụm con với sự hỗ trợ của jieba. Cơ chế ghi có nhật ký, một khóa dùng chung theo người dùng, và các revision bộ nhớ người dùng theo kiểu lạc quan giúp ngăn việc mất cập nhật một cách âm thầm.

Hãy đặt `memory.backend_config.retrieval_relevance_enabled: true` để tự chọn bật cơ chế xếp hạng theo độ liên quan/độ tin cậy mang tính xác định cùng việc chèn có nhận biết truy vấn. Tùy chọn này **bỏ qua `retrieval_adapter` khi tìm kiếm**, bao gồm cả FTS5/BM25 mặc định lẫn các adapter tùy chỉnh; việc lập chỉ mục vẫn giữ nguyên cấu hình. `retrieval_relevance_weight` điều khiển tỷ lệ pha trộn và `retrieval_diversity_weight` bật cơ chế phạt các mục gần-trùng-lặp (mặc định 0). Việc chấm điểm dùng tối đa 4096 ký tự đầu tiên và 128 token cho mỗi truy vấn/fact. Việc tìm kiếm chỉ đa dạng hóa đến mức `top_k`; việc chèn thì đa dạng hóa các fact được đảm bảo và fact thông thường một cách độc lập cho đến khi chạm ngân sách token của chúng. Hãy để tính năng này tắt nếu muốn giữ hành vi truy hồi và chèn như hiện tại.

Độ liên quan từ vựng đo mức độ bao phủ có trọng số IDF của các từ khóa truy vấn khác biệt, nên
các lần khớp một phần lặp lại không thể ngang bằng một lần khớp trọn vẹn chỉ nhờ làm bão hòa
điểm số. Việc khớp tiền tố đòi hỏi một token trọn vẹn phải là tiền tố của token kia, chứ không chỉ
là bốn ký tự chung. Với các tệp tải lên, việc chèn có nhận biết truy vấn dùng
yêu cầu gốc được giữ lại của người dùng thay vì các mô tả tệp được thêm vào đầu; những tin nhắn
chỉ-có-đính-kèm vẫn dùng cơ chế chèn không-truy-vấn. Các backend bộ nhớ tùy chỉnh cũ có thể giữ nguyên
chữ ký `get_context` hiện có của chúng: việc chèn prompt và lớp bọc bất đồng bộ được kế thừa chỉ truyền `query`
khi hàm đó hỗ trợ từ khóa này và gợi ý không phải `None`.
Việc tìm kiếm và chèn tự động dùng cùng trọng số IDF cho cùng
phạm vi ứng viên theo người dùng/agent. Việc tìm kiếm có lọc theo danh mục và các ngân sách token
riêng cho phần được-đảm-bảo/phần-thông-thường của cơ chế chèn vẫn có thể cho ra những lựa chọn cuối cùng khác nhau.

Việc chèn bộ nhớ tuân theo chế độ hoạt động đã cấu hình. Ở chế độ `middleware`, DeerMem chèn các bản tóm tắt toàn cục của người dùng và các fact của agent đang chọn. Các cuộc hội thoại khởi tạo custom agent cũng dùng bucket fact của chính agent đó, nên các chi tiết thiết lập không rò rỉ sang bộ nhớ của agent mặc định. Ở chế độ `tool`, khối `<memory>` tự động chỉ chứa các bản tóm tắt `user` và `history` toàn cục; các fact của agent được truy hồi tường minh qua `memory_search`, tránh việc trùng lặp giữa ngữ cảnh fact tự động và ngữ cảnh do tool trả về. Đặt `memory.injection_enabled: false` vẫn tắt toàn bộ khối này ở cả hai chế độ.

Một Custom Agent riêng lẻ có thể từ chối dùng bộ nhớ mà không cần thay đổi thiết lập toàn cục. Hãy thêm `memory_enabled: false` vào `users/{user_id}/agents/{name}/config.yaml` của agent đó. Agent vẫn nhận được lời nhắc về ngày hiện tại, nhưng DeerFlow sẽ không chèn bộ nhớ đã gợi nhớ, không xếp hàng các cập nhật bộ nhớ thụ động hay do tóm tắt tạo ra (bao gồm cả `/compact` thủ công), không phơi ra các tool bộ nhớ, và không thêm chỉ dẫn về tool bộ nhớ cho agent đó. Nếu một agent đang có bị tắt tính năng này, khối bộ nhớ đã chèn trước đó của nó sẽ bị loại khỏi trạng thái checkpoint trước lệnh gọi model kế tiếp, trong khi lời nhắc ngày tháng và cuộc hội thoại vẫn được giữ. Bỏ qua trường này (hoặc đặt nó thành `true`) sẽ giữ nguyên hành vi `memory` toàn cục hiện có.

Các thao tác kho lưu trữ trên một fact đơn lẻ thực sự mang tính tăng dần: một thao tác upsert/delete chỉ đọc, ghi nhật ký, ghi và lập chỉ mục lại đúng các tệp fact được nhắm tới, và trả về một delta không đầy đủ một cách tường minh thay vì một tài liệu đầy đủ giả tạo phụ thuộc vào cache. Các tập thay đổi bản tóm tắt sẽ gộp các khóa con `user`/`history` được cung cấp lên trên các phần đã lưu, nên một cập nhật một phần không thể xóa mất những phần anh em bị bỏ qua; các lần nhập đầy đủ sẽ chuẩn hóa cả hai phần về lược đồ tương thích hoàn chỉnh trước khi áp dụng giá trị thay thế. Các lần nhập từ chối những danh sách fact sai định dạng hoặc nội dung trống/không phải văn bản với HTTP 400 trước khi thay đổi bộ nhớ đã lưu; metadata kiểu cũ có thể khôi phục vẫn được gán giá trị mặc định. Một danh sách fact rỗng tường minh vẫn được xem là một thao tác xóa có chủ đích. Các phương thức tương thích của Manager/API chỉ dựng ra một tài liệu đầy đủ mới khi hợp đồng phản hồi công khai của chúng đòi hỏi. Các thao tác điểm ở cấp fact dùng revision kỳ vọng riêng cho bộ nhớ người dùng và cho fact, và có thể rebase tường minh khi mọi điều kiện tiên quyết của các fact được nhắm tới vẫn còn đúng. Các thao tác dẫn xuất từ snapshot như xóa theo phạm vi, tạo có giới hạn, hợp nhất và cắt tỉa sẽ không bao giờ phát lại các tập xóa/cắt tỉa lỗi thời: một xung đột manifest sẽ nạp lại toàn bộ tài liệu và tính lại thao tác, với số lần thử lại có giới hạn. Đường dẫn fact dùng hai ký tự hexa đầu tiên của `SHA-256(fact_id)` để các ID `fact_*` được sinh ra phân bố đều trên các shard. Token cache kết hợp mtime cấp nano giây của tệp JSON dùng chung, kích thước và revision đã lưu; điều này ngăn những lần ghi có cùng kích thước với mtime độ phân giải thô trả về dữ liệu cũ mà không cần quét các tệp fact. Việc sửa Markdown trực tiếp từ bên ngoài đòi hỏi một lần nạp lại tường minh. Các xung đột và hỏng hóc đặc thù của kho lưu trữ được chuyển dịch tại ranh giới MemoryManager; Gateway trả về xung đột dưới dạng HTTP 409 và một lỗi hỏng dữ liệu ổn định, không chứa thông tin nhạy cảm, dưới dạng HTTP 500. Hàm `save()` cho toàn bộ tài liệu vẫn là một API tương thích và sẽ tính diff trước khi ghi; một trường `facts` sai định dạng hoặc bị thiếu không còn có thể âm thầm xóa các tệp Markdown của một agent. Việc di chuyển dữ liệu cũ sẽ giữ lại các phần `user`/`history` không rỗng trước khi xóa `memory.json` của một agent; các bản tóm tắt mâu thuẫn sẽ khiến tệp cũ được giữ lại và báo lỗi rõ ràng thay vì tự chọn bên thắng.

Các fact cũ trong `memory.json` sẽ tự động được chuyển vào bucket Markdown dành riêng `__default__` ở lần đọc bộ nhớ bình thường đầu tiên của người dùng. Những người vận hành muốn kiểm toán hoặc hoàn tất việc di chuyển trước khi phục vụ lưu lượng có thể chạy CLI idempotent tùy chọn từ thư mục `backend/`:

```bash
PYTHONPATH=. python scripts/migrate_memory_markdown.py --all-users --dry-run
PYTHONPATH=. python scripts/migrate_memory_markdown.py --all-users
# Có thể chỉ định tường minh một thư mục gốc DeerMem tùy chỉnh hoặc một danh tính gốc không an toàn cho tên thư mục:
PYTHONPATH=. python scripts/migrate_memory_markdown.py --storage-path /path/to/deerflow-home --user-id 'test@example.com'
```

Việc di chuyển kho lưu trữ từ v1 sang v2 là một chiều đối với một ứng dụng đang chạy: mã trước PR này không đọc được các fact dạng Markdown. Trước khi nâng cấp một bản triển khai thường trực, hãy dừng DeerFlow và tạo một snapshot hệ thống tệp hoặc sao lưu đầy đủ thư mục gốc lưu trữ bộ nhớ đã cấu hình. Quá trình di chuyển cũng lưu bền mỗi nguồn JSON bị thay đổi ngay cạnh đường dẫn gốc dưới tên `{manifest_filename}.v1.bak` trước khi ghi dữ liệu v2; nếu đã tồn tại một bản sao lưu không khớp hoặc việc ghi bản sao lưu thất bại thì quá trình di chuyển sẽ dừng lại mà không sửa nguồn v1. Bản sao lưu cục bộ này giữ lại dữ liệu trước khi di chuyển nhưng không thay thế được một snapshot đầy đủ và không chứa các fact được tạo sau khi nâng cấp.

`--user-id` có thể lặp lại nhiều lần. `--all-users` sẽ khám phá các bucket an-toàn-cho-tên-thư-mục hiện có nằm dưới thư mục gốc lưu trữ đã chọn; các bản tích hợp độc lập từng truyền ID thô chứa những ký tự như `@` nên dùng giá trị gốc kèm `--user-id`. Việc di chuyển thất bại của một người dùng sẽ được báo cáo mà không che khuất phần còn lại của bản kiểm toán, và lệnh sẽ kết thúc với mã khác 0 khi có bất kỳ người dùng nào thất bại. Đường đi tự động ở lần đọc đầu tiên vẫn được bật, nên việc chạy CLI này là không bắt buộc để khởi động.

## Model khuyến nghị

DeerFlow không phụ thuộc vào model cụ thể — nó hoạt động với mọi LLM triển khai API tương thích OpenAI. Tuy vậy, nó chạy tốt nhất với các model hỗ trợ:

- **Cửa sổ ngữ cảnh dài** (100k+ token) cho nghiên cứu sâu và các tác vụ nhiều bước
- **Khả năng suy luận** cho việc lập kế hoạch thích ứng và phân rã bài toán phức tạp
- **Đầu vào đa phương thức** để hiểu ảnh và hiểu video
- **Khả năng dùng tool tốt** cho việc gọi hàm đáng tin cậy và đầu ra có cấu trúc

## Python Client nhúng

Với `DeerFlowClient(agent_name="researcher")`, lựa chọn `mcp_plugins` của agent được đặt tên
sẽ áp dụng cho cả lead agent lẫn các lần ủy quyền `task` / `batch_task` của nó:
`null` kế thừa toàn bộ plugin MCP đang bật, `[]` không chọn plugin nào, và các
ID cài đặt sẽ chỉ chọn đúng những plugin đó. Hãy gọi `client.reset_agent()` sau khi
sửa cấu hình agent đã lưu để làm mới lựa chọn.

`DeerFlowClient.stream()` bao gồm `summary_text` trong mỗi sự kiện `values`. Đây là bản tóm tắt ngữ cảnh đã nén hiện tại, hoặc `None` khi không có. Các bên tiêu thụ có thể ghi nhận thay đổi mà không cần đọc phần bên trong của checkpoint; các snapshot lặp lại có thể mang cùng một bản tóm tắt, và một snapshot ban đầu có thể đã chứa sẵn một bản tóm tắt từ lượt trước.

DeerFlow có thể được dùng như một thư viện Python nhúng mà không cần chạy đầy đủ các dịch vụ HTTP. `DeerFlowClient` cung cấp quyền truy cập trực tiếp ngay trong tiến trình tới mọi năng lực của agent và Gateway, trả về đúng những lược đồ phản hồi như HTTP Gateway API. HTTP Gateway cũng phơi ra `DELETE /api/threads/{thread_id}` để xóa dữ liệu thread cục bộ do DeerFlow quản lý sau khi chính thread LangGraph đã bị xóa:

Thread ID có thể do bên gọi cung cấp và không nhất thiết phải là UUID. Các ID tường minh
phải gồm 1–64 chữ cái ASCII, chữ số, dấu gạch ngang hoặc gạch dưới
(`^[A-Za-z0-9_-]{1,64}$`). DeerFlow chỉ sinh ra một UUID khi `thread_id` bị
bỏ qua hoặc là `None`; một chuỗi rỗng được cung cấp tường minh là không hợp lệ.
Các thread định địa chỉ được qua route đã tạo dưới những quy tắc lỏng lẻo hơn trước đây vẫn
đọc được và xóa được, nhưng không thể khởi động lượt chạy mới hoặc tạo trạng thái hệ thống tệp
hay sandbox mới. Việc xóa kiểu cũ sẽ bỏ qua bước dọn đường dẫn cục bộ khi ID không
an toàn theo hợp đồng chính tắc. Với các thread cũ hợp chuẩn mà cuộc hội thoại chỉ tồn tại
trong các checkpoint LangGraph, DeerFlow sẽ gieo một luồng sự kiện chạy rỗng
từ checkpoint trước lượt chạy mới đầu tiên, để
`/messages/page` giữ được cả lượt cũ lẫn lượt mới.

```python
from deerflow.client import DeerFlowClient

client = DeerFlowClient()

# Chat
response = client.chat("Analyze this paper for me", thread_id="my-thread")

# Streaming (giao thức SSE của LangGraph: values, messages-tuple, end)
for event in client.stream("hello"):
    if event.type == "messages-tuple" and event.data.get("type") == "ai":
        print(event.data["content"])
    elif event.type == "messages-tuple" and event.data.get("type") == "tool" and "artifact" in event.data:
        # Các artifact tool có cấu trúc (ví dụ, các thẻ ask_clarification)
        # được giữ lại khi ToolMessage có cung cấp.
        print(event.data["artifact"])

# Cấu hình & quản lý — trả về các dict khớp với Gateway
models = client.list_models()        # {"models": [...]}
skills = client.list_skills()        # {"skills": [...]}
client.update_skill("web-search", enabled=True)
client.upload_files("thread-1", ["./report.pdf"])  # {"success": True, "files": [...]}
client.set_goal("thread-1", "finish the implementation and make all tests pass")
client.get_goal("thread-1")       # {"goal": {...}} hoặc {"goal": None}
client.clear_goal("thread-1")
```

HTTP Gateway chấp nhận các chế độ stream `values`, `messages-tuple`, `updates`, `debug`, `tasks`, `checkpoints` và `custom`. Các chế độ không được hỗ trợ như `messages` và `events`, các tùy chọn chạy khác mặc định không được hỗ trợ như webhook, thực thi trì hoãn hay `multitask_strategy="enqueue"`, cùng các tùy chọn SDK không khai báo như việc ghi đè độ bền checkpoint, đều trả về `422` trước khi thực thi thay vì bị âm thầm bỏ qua hoặc hạ cấp.

Mọi phương thức trả về dict đều được kiểm tra đối chiếu với các model phản hồi Pydantic của Gateway trong CI (`TestGatewayConformance`), đảm bảo client nhúng luôn đồng bộ với lược đồ của HTTP API. Xem `backend/packages/harness/deerflow/client.py` để có tài liệu API đầy đủ.

## Project

Project nhóm các cuộc hội thoại liên quan lại dưới một tên chung, một bộ chỉ dẫn chung và một
kệ tài liệu chung.

Một cuộc hội thoại gia nhập một project lúc được tạo (khi đã chọn một project) hoặc
về sau thông qua menu di chuyển. Các lượt chạy không bao giờ thay đổi việc thuộc về project nào:
việc gửi một tin nhắn không thể gán hay gán lại một cuộc hội thoại. Chuyển một cuộc hội thoại ra khỏi một project
sẽ giữ nó ở trạng thái chưa gán cho đến khi được chuyển đi lần nữa một cách tường minh.

Việc chuyển một cuộc hội thoại sẽ làm mới phần thông tin project trên header của nó cũng như các
danh sách project, kể cả khi một yêu cầu metadata cũ hơn vẫn đang dở dang.

Project đòi hỏi các bảng và cột cơ sở dữ liệu hiện hành. Một cơ sở dữ liệu được đóng dấu
`0019_thread_incarnations` từ đợt triển khai cũ dựa trên 0018 sẽ bị từ chối lúc
khởi động nếu thiếu lược đồ project. Hãy làm theo
[quy trình khôi phục cơ sở dữ liệu offline](docs/database-forward-revision-recovery.md)
trước khi chạy bản build này với cơ sở dữ liệu đó.

### Chỉ dẫn của project

Mỗi project lưu một bộ chỉ dẫn tự do — bối cảnh, quy ước và các ràng buộc
áp dụng cho mọi cuộc hội thoại trong project — có thể sửa trên tab Instructions của
trang project kèm bộ đếm byte trực tiếp. Khi một lượt chạy bắt đầu trên một thread thành viên,
Gateway sẽ ghim trạng thái hiện tại của project một lần và render bộ chỉ dẫn
thành một khối `<project>` có giới hạn, theo phạm vi yêu cầu, chỉ cho lượt chạy đó:
khối này không bao giờ đi vào prompt hệ thống hay lịch sử được lưu, và mọi
lượt chạy mới đều thấy bộ chỉ dẫn đã lưu mới nhất. Chỉ dẫn bị giới hạn ở
`projects.instructions_max_bytes` byte UTF-8 (mặc định 8192, khoảng 256–262144);
các ký tự nhiều byte được tính theo độ dài byte UTF-8 của chúng. Chỉ dẫn quá dài
sẽ bị từ chối với mã `422` lúc ghi và không bao giờ bị âm thầm cắt bớt.

### Kệ tài liệu

Mỗi project có một kệ tài liệu dành cho các tệp mà cả project dùng chung, được quản lý
từ mục Documents của trang project:

- **Upload** một tệp (bằng nút hoặc kéo-thả, mỗi yêu cầu một tệp). Giới hạn kích thước của kệ
  dùng lại `uploads.max_file_size` (mặc định 50 MiB); việc tải lên lại nội dung giống hệt
  sẽ trả về mục đã có thay vì tạo bản trùng.
- **List** các mục kèm tên, kích thước, thời điểm sửa đổi và nguồn gốc (tải lên hay
  được lưu từ một cuộc hội thoại), cùng khả năng xem trước hoặc tải xuống bất kỳ mục nào.
- **Save to project** từ một tệp trong thread: trình duyệt tệp hội thoại ở chế độ chỉ-đọc
  nằm dưới kệ sẽ liệt kê các tệp uploads và outputs của những thread thành viên, mỗi tệp
  đều có hành động Save to project.
- **Attach to thread**: sao chép một tệp trên kệ vào thư mục uploads của một thread thông qua
  pipeline nạp tệp thông thường, để cuộc hội thoại có thể làm việc trực tiếp với nó.

Các lượt chạy trên thread thành viên cũng nhận được một chỉ mục `<documents>` có giới hạn, được render cho từng
lượt chạy từ snapshot đã ghim (bị khống chế bởi `projects.shelf_index_max_entries` và
`projects.shelf_index_max_bytes`), và agent có thể phân trang kệ tài liệu cũng như đọc
tài liệu bằng các tool `list_project_documents` và `read_project_document`.

### Ngữ nghĩa đọc khi đã lưu trữ

Việc lưu trữ một project sẽ đóng băng các thao tác ghi nhưng vẫn cho phép đọc. Các thread trong một project
đã lưu trữ vẫn chạy được và vẫn nhận được bộ chỉ dẫn cùng chỉ mục kệ của project,
và kệ vẫn đọc được đầy đủ: việc liệt kê, xem trước/tải xuống, trình duyệt
tệp hội thoại, và thao tác gắn-vào-thread đều tiếp tục hoạt động. Việc tải lên,
lưu-vào-project, và chuyển từng tệp trên kệ vào thùng rác đòi hỏi project phải đang hoạt động,
và một tài liệu trong thùng rác không thể được khôi phục vào một project đã lưu trữ.
Việc xóa một project đã lưu trữ vẫn được phép và sẽ chuyển toàn bộ kệ của nó vào
thùng rác.

### Thùng rác

Việc xóa một tài liệu trên kệ sẽ chuyển nó vào thùng rác thay vì xóa hẳn: mục đó
giữ nguyên nội dung và một snapshot về project gốc của nó trong
`projects.trash_retention_days` (mặc định 30) trước khi lượt quét dọn theo thời hạn lưu giữ có thể
xóa hẳn nó. Trang `/workspace/trash` — truy cập được từ mục Documents của trang project
và từ header Projects trên thanh bên — liệt kê các tài liệu trong thùng rác kèm project gốc và
thời gian lưu giữ còn lại, với các hành động Restore và Delete permanently cho từng mục,
cộng thêm hành động Empty trash để xóa vĩnh viễn mọi tài liệu trong thùng rác —
ngay lập tức, chứ không phải sau khoảng thời gian lưu giữ; khoảng thời gian đó chỉ giới hạn việc một mục
có thể nằm đó bao lâu trước khi lượt quét dọn thu hồi nó. Thao tác Restore trả tài liệu về
project gốc của nó, hoặc về một project bạn chọn khi project gốc không còn hoặc đã lưu trữ;
nếu nơi đến đã có một tệp đang hoạt động giống hệt, các mục sẽ được gộp lại.
Việc xóa một project sẽ chuyển toàn bộ kệ của nó vào thùng rác trong cùng một bước.

## Tác vụ theo lịch

DeerFlow giờ đã có một bản MVP tác vụ theo lịch hạng nhất ngay trong workspace.

Việc sửa tiêu đề hoặc prompt của một tác vụ chạy-một-lần vẫn giữ nguyên thời điểm thực thi gốc, bao gồm cả phần giây và lần xảy ra đã chọn trong đợt lùi giờ do quy ước giờ mùa hè. Việc thay đổi ngày, giờ hoặc múi giờ sẽ tính lại thời điểm thực thi. Việc chuyển sang tác vụ khác trong lúc đang sửa sẽ nạp tiêu đề, prompt và lịch của chính tác vụ được chọn.

Các năng lực hiện có của MVP:

- Quản lý tác vụ tại `/workspace/scheduled-tasks`
- Biểu mẫu cho tác vụ chạy-một-lần từ chối các thời điểm địa phương bị bỏ qua do chuyển đổi giờ mùa hè; hãy chọn một thời điểm khác trước khi tạo hoặc lưu tác vụ.
- Chọn việc mỗi tác vụ theo lịch dùng lại một thread cùng lịch sử hội thoại của nó, hay tạo một thread mới cho mỗi lần chạy
- Ghim mỗi tác vụ vào `lead_agent` (mặc định) hoặc một custom agent mà chủ sở hữu đã có; các tên không xác định sẽ bị từ chối
- Nhân bản một tác vụ sẵn có vào biểu mẫu tạo mới dưới dạng bản nháp sửa được, mà không sao chép lịch sử chạy của nó
- Hỗ trợ các lịch `once`, `cron` và `interval`
- Việc sửa hoặc nhân bản một tác vụ dạng interval vẫn giữ nhịp đã lưu cho đến khi khoảng thời gian được thay đổi tường minh, bao gồm cả các khoảng dưới một phút mà cấu hình scheduler của người vận hành cho phép
- Chạy các lần thực thi theo lịch ở chế độ nền như các lượt chạy DeerFlow phi tương tác (`ask_clarification` không được phơi ra ở đó)
- Lưu một lần thực thi đến hạn ở trạng thái `queued` khi thread được dùng lại hoặc ngân sách thực thi toàn cục đang bận, rồi khởi chạy nó khi có sức chứa; các lần xảy ra đang xếp hàng vẫn tồn tại qua các lần khởi động lại Gateway và sẽ thất bại sau `scheduler.queue_timeout_seconds`
- Đóng băng định nghĩa của một tác vụ khi một lần xảy ra đang ở trạng thái `queued`, `launching` hoặc `running`, để một lần xảy ra bền vững không thể âm thầm nhận một prompt, thread hay lịch khác; việc chuyển một tác vụ sang trạng thái tạm dừng hoặc xóa nó sẽ hủy một lần xảy ra đang chờ, trong khi các phần việc `launching`/`running` phải hoàn tất trước khi các thao tác đó được thử lại, và một lần kích hoạt thủ công tường minh vẫn có thể chờ rồi chạy mà không làm khôi phục một lịch đang tạm dừng
- Tạm dừng, tiếp tục, kích hoạt, xem lịch sử và xóa tác vụ
- Tìm kiếm theo tiêu đề hoặc prompt của tác vụ, kết hợp với bộ lọc trạng thái/loại và phạm vi thread hiện tại.
- Thực thi công việc theo lịch thông qua vòng đời chạy thông thường của DeerFlow
- Duyệt lịch sử thực thi theo trang 50 mục; các trang cũ hơn sẽ tạm dừng việc tự làm mới, kèm một cách quay lại các lượt chạy mới nhất một cách tường minh. Các con số chỉ xuất hiện sau một lần đọc thành công; trạng thái đang tải và các lần đọc thất bại không bị báo là không có lượt chạy nào.

**Lọc lịch sử thực thi qua API**

Để xem các lần thất bại mà không phải tải về mọi lần xảy ra thành công, các client đã xác thực có quyền `threads:read` có thể gọi `GET /api/scheduled-tasks/{task_id}/runs?status=failed&limit=50&offset=0` cho một tác vụ mà họ sở hữu. Tham số tùy chọn `status` nhận các giá trị `queued`, `launching`, `running`, `success`, `failed`, `skipped` hoặc `interrupted`; đây là trạng thái của lần xảy ra, nên các trạng thái của tác vụ như `completed` là không hợp lệ (422).

Việc lọc diễn ra trước khi phân trang. `limit` (1–200, mặc định 50) và `offset` (không âm, mặc định 0) áp dụng cho các bản ghi khớp, sắp xếp theo thời điểm tạo rồi tới ID, cả hai đều giảm dần. Bỏ qua `status` sẽ giữ nguyên phản hồi dạng mảng lịch sử hỗn hợp hiện có; không có kết quả nào khớp thì trả về `[]`. API này không làm thay đổi việc thực thi tác vụ, và giao diện lịch sử trong workspace vẫn không có bộ lọc.

Các giới hạn hiện tại của MVP:

- Chưa có tool `schedule_task` tạo từ trong cuộc hội thoại
- Chưa có các job thông báo chỉ-gồm-văn-bản
- Chưa có đích gửi qua kênh IM hay GitHub

Hãy bật cơ chế poll chạy nền bằng `config.yaml -> scheduler.enabled`. Việc kích hoạt thủ công dùng chung tài nguyên tác vụ theo lịch và đường thực thi đó.

Các lượt chạy theo lịch dùng `scheduler.recursion_limit` trong `config.yaml` (mặc định `1000`, khớp với ngân sách tương tác của giao diện web). Các giá trị trên `max_recursion_limit` sẽ bị khống chế. Trường này được đọc lúc điều phối, nên lượt chạy theo lịch kế tiếp sẽ nhận giá trị mới mà không cần khởi động lại Gateway.

Bộ lập lịch chạy nền mặc định chỉ chạy một instance. Với một bản triển khai nhiều pod, hãy đặt `scheduler.multi_instance: true` và dùng Postgres dùng chung, `run_ownership.heartbeat_enabled: true`, và `run_events.backend: db`; khi đó quá trình khởi động và khôi phục định kỳ sẽ giữ lại các lượt chạy của những worker còn sống, trả các yêu cầu khởi chạy đã hết hạn về hàng đợi một cách nguyên tử, chỉ tiếp quản những lease chạy đã hết hạn, và rào chặn các thao tác ghi khởi chạy lỗi thời. `max_concurrent_runs` là một mức trần toàn cục dùng chung giữa các Pod cho các lần xảy ra ở trạng thái `launching`/`running`; các dòng `queued` đang chờ không chiếm mức trần này. Nếu không có các thiết lập đó, hãy chỉ bật scheduler trên đúng một pod Gateway. Các trường scheduler này chỉ đọc lúc khởi động; hãy khởi động lại toàn bộ Pod Gateway cùng lúc khi thay đổi chúng.

### Xem trước các lần xảy ra của cron qua API

Các client đã xác thực có quyền `threads:read` có thể gọi `POST /api/scheduled-tasks/preview-cron` trước khi tạo một tác vụ:

```json
{"cron":"0 9 * * 1-5","timezone":"Asia/Shanghai","count":3,"start_at":"2026-09-12T00:00:00Z"}
```

Phản hồi chứa `cron` và `timezone` đã chuẩn hóa, `start_at` hiệu dụng theo UTC, cùng `occurrences` với `run_at` theo UTC và `local_time` có kèm độ lệch múi giờ. Trong ví dụ này, lần xảy ra đầu tiên là `2026-09-14T01:00:00Z` / `2026-09-14T09:00:00+08:00`.

`count` là một số nguyên từ 1 đến 10 (mặc định 5). `start_at` phải bao gồm múi giờ; bỏ qua nó để lấy thời gian server một lần. Các biểu thức cron dùng cú pháp năm trường của scheduler (tối đa 256 ký tự); tên múi giờ tối đa 128 ký tự. Đầu vào không hợp lệ hoặc các lịch không có đủ số lần xảy ra trong tương lai như yêu cầu sẽ trả về 422. Việc xem trước dùng chung hành vi DST của scheduler, không tạo ra tác vụ, thread hay lượt chạy nào, và không giữ chỗ thực thi. Đây là một năng lực ở mức API; biểu mẫu trong workspace chưa hiển thị các lần xảy ra này.

### Lưu ý khi nâng cấp

- Thứ tự các lần xảy ra chỉ áp dụng cho những dòng được chấp nhận bởi các instance Gateway đã nâng cấp — vốn chỉ chiếu các lần xảy ra đã được đánh số thứ tự lên tác vụ cha và hoãn việc khôi phục khi vẫn còn một lần xảy ra đang sống, bất kể instance nào đã chấp nhận nó; một tác vụ có lịch sử hoàn toàn chưa được đánh số thứ tự sẽ giữ cách sắp xếp theo dấu thời gian như trước cho tới lần chấp nhận có đánh số đầu tiên của nó. Trong một đợt nâng cấp cuốn chiếu, các dòng được chấp nhận bởi những instance chưa nâng cấp sẽ do chính các instance đó chiếu, y như trước khi nâng cấp, và các đảm bảo về thứ tự sẽ có hiệu lực khi mọi bên ghi Gateway đều chạy phiên bản đã nâng cấp. Lịch sử hiện có không được điền bù; việc nâng cấp không tái dựng lại thứ tự quá khứ hay sửa các con số thống kê trong lịch sử.
- Trước khi nâng cấp một bản triển khai có `GATEWAY_WORKERS > 1` và `scheduler.enabled: true`, hãy hoặc giữ scheduler chỉ trên đúng một worker Gateway, hoặc cấu hình `scheduler.multi_instance: true` cùng Postgres dùng chung, `run_ownership.heartbeat_enabled: true` và `run_events.backend: db`. Gateway sau khi nâng cấp sẽ từ chối tổ hợp không an toàn ngay lúc khởi động thay vì khởi động một cách âm thầm.
- Ở chế độ nhiều instance, `scheduler.max_concurrent_runs` là mức trần thực thi cho toàn cụm, không phải cho từng Pod. Nó bao gồm các lần xảy ra theo lịch ở trạng thái `launching` và `running`, nên sức chứa không nhân lên theo số bản sao; các dòng đang chờ bền vững thì nằm ngoài mức trần này.
- `scheduler.multi_instance` và các thiết lập liên quan về scheduler, quyền sở hữu và sự kiện chạy đều chỉ đọc lúc khởi động. Hãy áp dụng thay đổi bằng một lần khởi động lại đồng bộ toàn bộ Pod Gateway; chỉ sửa ConfigMap thôi thì không kích hoạt được cơ chế khôi phục nhiều instance.

## Terminal Workbench (TUI)

`deerflow` là một bàn làm việc chạy ngay trên terminal dành cho những người sống trong shell. Nó chạy ở chế độ **nhúng** thông qua `DeerFlowClient` — không cần Gateway, frontend, nginx hay Docker — trong khi vẫn tôn trọng cùng các thiết lập `config.yaml`, checkpointer, skill, bộ nhớ, MCP và sandbox như phần còn lại của DeerFlow.

Các lệnh gọi MCP stdio đồng bộ chạy song song sẽ dùng các phiên độc lập trên vòng lặp sự kiện
riêng của chúng. Chúng không hủy kết nối của nhau, nhưng chúng cũng không dùng chung
trạng thái phía server; việc dùng lại phiên đòi hỏi cùng một vòng lặp. Xem
[ghi chú về phiên MCP](backend/docs/MCP_SERVER.md) để biết chi tiết.
Các vòng lặp sự kiện được quản lý thủ công phải xả hết các bên sở hữu phiên đang chờ trước khi đóng;
đường đi `asyncio.run()` thông thường tự động làm việc này.

![DeerFlow TUI](docs/tui/tui-preview.svg)

```bash
uv pip install 'deerflow-harness[tui]'        # phụ thuộc 'textual' tùy chọn

deerflow                                      # khởi chạy giao diện terminal (cần TTY)
deerflow --tui-transparent                    # dùng màu nền mặc định của terminal
deerflow --continue                           # tiếp tục thread gần nhất
deerflow --resume THREAD                      # tiếp tục một thread theo id
deerflow --print "summarize this repo"        # trả lời một lần không giao diện, ra stdout
deerflow --json  "hello"                       # StreamEvents phân tách bằng dòng mới, không giao diện
deerflow --recursion-limit 250 --print "task" # ghi đè giới hạn vòng lặp agent ở chế độ không giao diện
```

Một bề mặt chat điều khiển bằng bàn phím với bản ghi hội thoại dạng streaming (câu trả lời render Markdown), các thẻ hoạt động tool gọn gàng, một bảng lệnh gạch chéo `/`, lệnh `/clear` chỉ ảnh hưởng hiển thị, quản lý mục tiêu bằng `/goal`, các bộ chọn `/model` và `/threads`, lịch sử nhập liệu, điều hướng bản ghi bằng PageUp/PageDown, và ngắt bằng `Esc` / `Ctrl+C`. Việc làm mới bản ghi vẫn giữ vị trí đọc của bạn sau khi bạn cuộn lên, và tự động bám theo đầu ra mới khi bạn quay lại cuối trang. `/clear` xóa các dòng khỏi phần hiển thị trên terminal hiện tại mà không xóa thread hay cuộc hội thoại đã lưu của nó; `/new` và `/clear` sẽ yêu cầu bạn chờ khi có một lượt chạy đang hoạt động, thay vì đặt lại trạng thái hiển thị đang dở dang. Các phiên mở trong TUI cũng xuất hiện trong thanh bên của Web UI — nó ghi vào kho thread dùng chung dưới người dùng mặc định cục bộ, nên terminal và web luôn đồng bộ **mà không cần chạy Gateway**.

Xem [backend/docs/TUI.md](backend/docs/TUI.md) để có hướng dẫn đầy đủ.

## Tài liệu

- [Hướng dẫn đóng góp](CONTRIBUTING.md) - Thiết lập môi trường phát triển và quy trình làm việc
- [Hướng dẫn cấu hình](backend/docs/CONFIGURATION.md) - Hướng dẫn cài đặt và cấu hình
- [Tổng quan kiến trúc](backend/CLAUDE.md) - Chi tiết kiến trúc kỹ thuật
- [Kiến trúc backend](backend/README.md) - Kiến trúc backend và tài liệu API

## ⚠️ Lưu ý bảo mật

### Triển khai sai cách có thể tạo ra rủi ro bảo mật

DeerFlow có những năng lực đặc quyền cao quan trọng, bao gồm **thực thi lệnh hệ thống, thao tác trên tài nguyên và gọi logic nghiệp vụ**, và theo thiết kế mặc định nó được **triển khai trong một môi trường cục bộ đáng tin cậy (chỉ truy cập được qua giao diện loopback 127.0.0.1)**. Nếu bạn triển khai agent trong các môi trường không đáng tin cậy — chẳng hạn mạng LAN, server trên public cloud, hoặc các môi trường có nhiều điểm truy cập khác — mà không có biện pháp bảo mật nghiêm ngặt, điều đó có thể tạo ra rủi ro bảo mật, bao gồm:

- **Bị gọi trái phép, bất hợp pháp**: Chức năng của agent có thể bị bên thứ ba không được phép hoặc các công cụ quét độc hại trên Internet phát hiện, dẫn đến hàng loạt yêu cầu trái phép thực thi các thao tác rủi ro cao như lệnh hệ thống và đọc/ghi tệp, có thể gây ra hậu quả bảo mật nghiêm trọng.
- **Rủi ro tuân thủ và pháp lý**: Nếu agent bị gọi bất hợp pháp để tiến hành tấn công mạng, đánh cắp dữ liệu hoặc các hoạt động phi pháp khác, điều đó có thể dẫn đến trách nhiệm pháp lý và rủi ro về tuân thủ.

### Quyền admin của Gateway tương đương quyền thực thi mã

Một quản trị viên có thể đăng ký các MCP server dạng stdio, vốn chạy lệnh bên trong container
Gateway. API giới hạn chúng theo một danh sách cho phép (`npx`, `uvx` theo mặc định,
mở rộng qua `DEER_FLOW_MCP_STDIO_COMMAND_ALLOWLIST`) và từ chối những đối số cùng
biến môi trường có thể dẫn tới việc thực thi mã tùy ý. Đó là phòng thủ nhiều lớp,
không phải một ranh giới: các bộ khởi chạy này sinh ra chính là để tải về và chạy các gói từ xa,
nên hãy **xem quyền admin của Gateway là tương đương với quyền thực thi mã trên máy chủ** và cấp
nó một cách tương xứng.

### Vai trò của tin nhắn chat từ bên ngoài

Các yêu cầu chạy qua Gateway và các cập nhật trạng thái thread thủ công sẽ từ chối các tin nhắn
`system` / `developer` do client cung cấp với mã HTTP 400, bao gồm cả các dạng tin nhắn
được tuần tự hóa tương đương. Chat thông thường, tệp đính kèm và việc phát lại lịch sử assistant/tool
vẫn được hỗ trợ. Việc xác thực bằng phiên hay PAT không cấp
thẩm quyền đặt prompt hệ thống; các bên tạo lượt chạy nội bộ đáng tin cậy vẫn giữ khả năng đó.

Kiểm tra này ngăn việc chèn vai trò mới; nó không viết lại các checkpoint
đã có. Nếu một phiên bản cũ từng chấp nhận một tin nhắn hệ thống bị chèn vào, hãy dùng một
thread mới hoặc nhờ người vận hành rà soát và dọn dẹp trạng thái bị ảnh hưởng. Việc khởi động lại
dịch vụ không xóa được các chỉ dẫn đã được lưu, và việc khôi phục một checkpoint cũ
có thể làm chúng sống lại.

Để kiểm chứng cục bộ, hãy chạy `python backend/tests/poc_external_system_message_injection.py --help`.
Cùng bản PoC tự chọn đó hỗ trợ `--expect vulnerable` trên một revision cũ được cô lập
và `--expect blocked` sau khi đã sửa. Phần trợ giúp của nó bao gồm cách tạo PAT, cách chọn
thread ID, cách theo dõi trên trình duyệt, và sự khác biệt giữa việc dữ liệu được lưu lại và việc
model có tuân theo hay không. Hãy dùng một thread mới, dùng-một-lần cho mỗi lần chạy; bài test sẽ thêm tin nhắn vào đó.

Trên một bản checkout chưa sửa lỗi được cô lập, `--expect vulnerable` chỉ chứng minh là bị chấp nhận
khi yêu cầu trả về 200 và đúng tin nhắn bị chèn vẫn nằm trong
checkpoint với `type=system` qua một lượt tiếp theo bình thường. Một dấu hiệu trong câu trả lời trên web
phụ thuộc vào model và tự nó không phải bằng chứng cho thấy vai trò đã được nâng cấp.
Sau khi áp dụng bản sửa, hãy chạy đúng script đó với `--expect blocked`: nó đòi hỏi
đúng lỗi 400 từ chối vai trò, một checkpoint không thay đổi, một lượt tiếp theo thông thường thành công,
và sự vắng mặt của các ID tin nhắn bị từ chối. Các phản hồi 400 khác cùng các lỗi xác thực,
xung đột hay lỗi server đều là không kết luận được, chứ không phải là "đạt".

Bản PoC không tự dọn dẹp. Khi đã kiểm chứng xong, hãy xóa
cuộc chat dùng-một-lần bằng hành động xóa trên thanh bên của web và thu hồi
PAT ngắn hạn nếu bạn đã tạo. Việc khởi động lại dịch vụ không xóa được một chỉ dẫn
đã bị chèn và lưu lại.

### Mặc định khi triển khai

Bộ Docker chỉ công bố cổng vào của nó trên `127.0.0.1`, khớp với
mô hình môi-trường-cục-bộ-đáng-tin-cậy mô tả ở trên. Để truy cập nó từ một máy khác,
hãy đặt `BIND_HOST` trong `.env` (ví dụ `BIND_HOST=0.0.0.0`) — và chỉ sau khi
đã áp dụng các biện pháp bảo mật bên dưới.

**Hãy hoàn tất thiết lập lần đầu trước khi máy chủ có thể truy cập được từ bên ngoài.** Một
instance mới chưa có tài khoản nào, nên hãy tạo tài khoản quản trị qua `/setup`
ngay sau khi khởi động bất kỳ bản triển khai nào không chỉ giới hạn ở loopback.

### Khuyến nghị bảo mật

**Lưu ý: Chúng tôi đặc biệt khuyến nghị triển khai DeerFlow trong một môi trường mạng cục bộ đáng tin cậy.** Nếu bạn cần triển khai xuyên thiết bị hoặc xuyên mạng, bạn phải áp dụng các biện pháp bảo mật nghiêm ngặt, chẳng hạn:

- **Danh sách IP cho phép**: Dùng `iptables`, hoặc triển khai tường lửa / switch phần cứng có Access Control List (ACL), để **cấu hình các quy tắc danh sách IP cho phép** và chặn truy cập từ mọi địa chỉ IP khác.
- **Gateway xác thực**: Cấu hình một reverse proxy (ví dụ nginx) và **bật cơ chế tiền xác thực mạnh**, chặn mọi truy cập chưa xác thực.
- **Cách ly mạng**: Nếu có thể, hãy đặt agent và các thiết bị đáng tin cậy trong **cùng một VLAN riêng**, cách ly khỏi các thiết bị mạng khác.
- **Luôn cập nhật**: Hãy tiếp tục theo dõi các bản cập nhật về tính năng bảo mật của DeerFlow.

## Đóng góp

Chúng tôi hoan nghênh mọi đóng góp! Vui lòng xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết cách thiết lập môi trường phát triển, quy trình làm việc và các hướng dẫn.

Lệnh `make test` ở backend không bao gồm phần kiểm thử API bên ngoài thật và phần kiểm tra I/O chặn.
Hãy chạy `cd backend && make test-blocking-io` để có các kiểm tra I/O chặn nghiêm ngặt.
Maintainer có thể chạy bộ test `DeerFlowClient` thật bằng `cd backend && make test-live`.
Lệnh này cần một `config.yaml` hợp lệ ở thư mục gốc và thông tin đăng nhập API.
Nó có thể phát sinh chi phí API và tạo ra các sandbox, artifact hoặc tệp cục bộ.
Việc chạy pytest trực tiếp còn đòi hỏi thêm `DEER_FLOW_RUN_LIVE_TESTS=1`.

Phạm vi kiểm thử hồi quy bao gồm các bài test về việc nhận diện chế độ sandbox Docker và xử lý đường dẫn kubeconfig của provisioner trong `backend/tests/`.
Phần chẩn đoán I/O chặn của backend có thể chạy từ thư mục gốc của repo bằng
`make detect-blocking-io`: nó quét tĩnh mã nghiệp vụ của backend để tìm
các thao tác I/O chặn có thể chạy trên vòng lặp sự kiện của backend, in ra một bản tóm tắt ngắn gọn,
và ghi toàn bộ phát hiện dạng JSON vào `.deer-flow/blocking-io-findings.json`.
Tệp JSON bao gồm các bản ghi rà soát gọn với `priority`, `location`,
`blocking_call`, `event_loop_exposure`, `reason` và `code`.
Việc phục vụ artifact của Gateway giờ đây buộc các kiểu nội dung web có khả năng thực thi (`text/html` và các tài liệu XML như `.xml`, `.xhtml` và `.svg`) phải tải xuống dưới dạng tệp đính kèm thay vì render nội dòng, giảm rủi ro XSS cho các artifact được sinh ra.

Ngân sách tài nguyên theo từng route của frontend có thể kiểm tra bằng `cd frontend && pnpm
perf:check`. Lệnh này đo route `/login` từ một bản build production thông thường, rồi
thực hiện một bản build demo tĩnh production cho các route workspace dựa trên dữ liệu fixture.
Nó đo lượng JavaScript và CSS duy nhất mà các route tiêu biểu tham chiếu tới
và ghi kết quả chi tiết vào `.next/performance-results.json`.

## Giấy phép

Dự án này là mã nguồn mở và được phát hành theo [Giấy phép MIT](./LICENSE).

## Lời cảm ơn

DeerFlow được xây dựng trên nền tảng công sức tuyệt vời của cộng đồng mã nguồn mở. Chúng tôi vô cùng biết ơn tất cả các dự án và những người đóng góp mà nhờ nỗ lực của họ, DeerFlow mới có thể ra đời. Thực sự, chúng tôi đang đứng trên vai những người khổng lồ.

Chúng tôi xin gửi lời cảm ơn chân thành tới các dự án sau vì những đóng góp vô giá của họ:

- **[LangChain](https://github.com/langchain-ai/langchain)**: Framework xuất sắc của họ là nền tảng cho các tương tác và chuỗi xử lý LLM của chúng tôi, cho phép tích hợp và vận hành một cách mượt mà.
- **[LangGraph](https://github.com/langchain-ai/langgraph)**: Cách tiếp cận sáng tạo của họ trong việc điều phối nhiều agent đã đóng vai trò then chốt, giúp DeerFlow có được những quy trình làm việc tinh vi như hiện nay.

Những dự án này là minh chứng cho sức mạnh chuyển hóa của sự hợp tác trong mã nguồn mở, và chúng tôi tự hào được xây dựng trên nền tảng của họ.

### Những người đóng góp chính

Xin gửi lời cảm ơn tự đáy lòng tới các tác giả cốt lõi của `DeerFlow`, những người mà tầm nhìn, đam mê và sự tận tụy đã đưa dự án này vào cuộc sống:

- **[Daniel Walnut](https://github.com/hetaoBackend/)**
- **[Henry Li](https://github.com/magiccube/)**

Sự cam kết bền bỉ và chuyên môn của các bạn chính là động lực đứng sau thành công của DeerFlow. Chúng tôi vinh dự khi có các bạn dẫn dắt hành trình này.

## Star History

[![Star History Chart](https://star-history.dera.page/svg?repos=bytedance/deer-flow&type=Date)](https://star-history.dera.page/#bytedance/deer-flow&Date)
