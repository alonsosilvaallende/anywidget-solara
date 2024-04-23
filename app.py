import solara
import anywidget
import traitlets
import ipywidgets as widgets

class CounterWidget(anywidget.AnyWidget):
    _esm = """
        import confetti from "https://esm.sh/canvas-confetti@1.6.0"
        function render({ model, el }) {
          let count = () => model.get("count");
          let btn = document.createElement("button");
          btn.innerHTML = `count is ${count()}`;
          btn.classList.add("counter-btn");
          btn.addEventListener("click", () => {
            model.set("count", count() + 1);
            model.save_changes();
          });
          model.on("change:count", () => {
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
    count = traitlets.Int(0).tag(sync=True)

vae = solara.reactive(0)
@solara.component
def Page():
    with solara.Column(style={"padding":"30px"}):
        solara.Markdown("#Anywidget+Solara")
        counter = CounterWidget()
        counter.element()
Page()
