import solara
import anywidget
import traitlets
import ipywidgets as widgets

class CounterWidget(anywidget.AnyWidget):
    _esm = """
        import confetti from "https://esm.sh/canvas-confetti@1.6.0"
        function render({ model, el }) {
          let count = () => model.get("value");
          let btn = document.createElement("button");
          btn.innerHTML = `count is ${count()}`;
          btn.classList.add("counter-btn");
          btn.addEventListener("click", () => {
            model.set("value", count() + 1);
            model.save_changes();
          });
          model.on("change:value", () => {
            btn.innerHTML = `count is ${count()}`;
            confetti({ angle: (45*(count()-1)) });
          });
          el.appendChild(btn);
        }
        export default { render };
    """
    _css = """
        .counter-btn {
            background:blue;
            padding:10px 50px;
        }
        .counter-btn:hover {
            background-color:green;
        }
    """
    value = traitlets.Int(0).tag(sync=True)

@solara.component
def Page():
    with solara.Column(style={"padding":"30px"}):
        solara.Markdown("#Anywidgets+Solara")
        counter = CounterWidget()
        counter.element()
Page()
