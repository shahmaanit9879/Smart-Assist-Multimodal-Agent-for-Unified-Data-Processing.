def test_text_agent():
    try:
        from src.text_agent import handle_text
        result = handle_text("Hello")
        assert "error" not in result
    except Exception:
        assert False, "Text agent test failed"


def test_image_agent():
    try:
        from src.image_agent import handle_image
        result = handle_image(None)
        assert "error" not in result
    except Exception:
        assert False, "Image agent test failed"


def test_audio_agent():
    try:
        from src.audio_agent import handle_audio
        result = handle_audio(None)
        assert "error" not in result
    except Exception:
        assert False, "Audio agent test failed"
