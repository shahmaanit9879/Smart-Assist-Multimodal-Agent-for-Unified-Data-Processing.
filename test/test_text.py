def test_text_basic():
    from src.text_agent import handle_text
    res = handle_text("Hello")
    assert res["ok"] is True
    assert "Processed Text" in res["result"]
