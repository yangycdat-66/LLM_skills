#!/usr/bin/env python3
"""Check OpenAI key authentication without displaying credentials."""
import argparse
import os
from pathlib import Path
import sys

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file', action='store_true', help='Check the local key file even when the environment overrides it')
    group.add_argument('--effective', action='store_true', help='Check the credential selected by the audio scripts')
    args = parser.parse_args()
    env_key = os.environ.get('OPENAI_API_KEY')
    source = 'environment' if args.effective and env_key else 'file'
    try:
        if source == 'environment':
            key = env_key
        else:
            path = Path.home() / '.config/openai/api-key'
            if not path.is_file():
                print('Key file is missing. Configure it locally first.', file=sys.stderr)
                return 1
            key = path.read_text(encoding='utf-8').strip()
        if not key:
            print('Selected key is empty. Configure it locally first.', file=sys.stderr)
            return 1
        try:
            import openai
        except ImportError:
            print('OpenAI Python SDK is not installed.', file=sys.stderr)
            return 1
        client = openai.OpenAI(api_key=key, timeout=20, max_retries=0)
        client.models.list()
        print(f'OpenAI accepted the {source} key for a model-list request. This does not verify audio-model access or billing.')
        if args.file and env_key:
            print('OPENAI_API_KEY is set and will override the file for audio requests.')
        return 0
    except PermissionError:
        print('Cannot read the key file: permission denied.', file=sys.stderr)
    except OSError:
        print('Cannot read the key file due to a local file error.', file=sys.stderr)
    except openai.AuthenticationError:
        print(f'OpenAI rejected the {source} key. Check it locally; do not share it in chat.', file=sys.stderr)
    except openai.APIConnectionError:
        print('Could not reach OpenAI. The key has not been validated.', file=sys.stderr)
    except openai.APIStatusError as e:
        print(f'OpenAI returned HTTP {e.status_code}; authentication and audio access were not confirmed.', file=sys.stderr)
    except Exception:
        print('Key check failed. Authentication was not confirmed.', file=sys.stderr)
    return 1

if __name__ == '__main__':
    sys.exit(main())
