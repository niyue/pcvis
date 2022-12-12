from pcvis.pcvis import main
import io


def test_vis_files():
    out = io.StringIO()
    main({"file": ["README.md", "LICENSE"]}, out)
    output = out.getvalue()
    assert "README.md" in output
    assert "LICENSE" in output
    assert "size=" in output
    assert "pages=" in output


def test_list_styles():
    out = io.StringIO()
    main({"list": True}, out)
    output = out.getvalue()
    assert "0" in output
    assert "▇▁▁" in output
    assert "23" in output
