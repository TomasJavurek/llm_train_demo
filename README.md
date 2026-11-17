# Fine-tune Lab

A browser-based LLM fine-tuning simulation. Configure a dataset, a base model, LoRA and training settings, then watch generated metrics and try the two chat panels. No training or inference on the selected base model occurs. Files stay in the browser and are not parsed or uploaded; settings and metrics are illustrative.

## Run locally

The site is static and can be served with `python -m http.server 8000`. Alternatively, run the optional Flask server:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run
```

Open the local URL printed by the server.

## GitHub Pages

Push this repository to GitHub. In **Settings → Pages**, choose **Deploy from a branch**, select the desired branch and `/ (root)`, and save. GitHub Pages serves the static files; it does not run Flask. No build step is needed.

## Optional live chat

Open chat settings and enter your own OpenRouter API key. Both panels call `openrouter/free` directly from your browser; the key is held in page memory until reload and is not saved. The free router can select different models between requests and is subject to availability and rate limits. Prompts and conversation history are sent to OpenRouter and its providers, so do not send sensitive content. Dataset contents are never automatically sent. Without a key, both panels return simple scripted replies. Live replies are not fine-tuned and are unrelated to the selected simulated base model.
