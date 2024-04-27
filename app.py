import solara
import anywidget
import traitlets
import ipywidgets as widgets

class CounterWidget(anywidget.AnyWidget):
    _esm = """
    import confetti from "https://esm.sh/canvas-confetti@1.6.0"
    function render({ model, el }) {
      let getCount = () => model.get("count");
      let button = document.createElement("button");
      button.classList.add("counter-button");
      button.innerHTML = `count is ${getCount()}`;
      button.addEventListener("click", () => {
        model.set("count", getCount() + 1);
        model.save_changes();
      });
      model.on("change:count", () => {
        button.innerHTML = `count is ${getCount()}`;
        confetti({ angle: getCount() });
      });
      el.appendChild(button);
    }
    export default { render };
    """
    _css="""
    .counter-button { background:blue; padding:10px 50px;}
    .counter-button:hover { background-color:green; }
    """
    count = traitlets.Int(0).tag(sync=True)

counter = solara.reactive(0)
@solara.component
def Page():
    with solara.Column(style={"padding":"30px"}):
        solara.Markdown("#Anywidget+Solara")
        CounterWidget.element(count=counter.value, on_count=counter.set)
        widgets.IntSlider.element(min=-180, max=180, value=counter.value, on_value=counter.set)
        solara.Markdown(f"## Counter value is {counter.value}")
Page()
