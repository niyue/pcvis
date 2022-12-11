from pcvis.pcvis import main
import io

def test_main():
    out = io.StringIO()
    main({"file": ["README.md", "LICENSE"]}, out)
    output = out.getvalue()
    assert "README.md" in output
    assert "LICENSE" in output
    assert "size=" in output
    assert "pages=" in output