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

@solara.component
def GithubAvatar(name: str, handle: str, img: str):
    with solara.v.Html(tag="a", attributes={"href": f"https://twitter.com/{handle}/", "target": "_blank"}):
        with solara.v.ListItem(class_="pa-0"):
            with solara.v.ListItemAvatar(color="grey darken-3"):
                solara.v.Img(
                    class_="elevation-6",
                    src=img,
                )
            with solara.v.ListItemContent():
                solara.v.ListItemTitle(children=["Done with love by " + name])

counter = solara.reactive(0)
@solara.component
def Page():
    solara.lab.theme.themes.light.primary = "#0000ff"
    solara.lab.theme.themes.dark.primary = "#0000ff"
    with solara.AppBar():
        solara.lab.ThemeToggle(enable_auto=False)
    textcolor = "#000000" if solara.lab.use_dark_effective()==False else "#ffffff"
    title = "Anywidget+Solara"
    with solara.Head():
        solara.Title(title)
    with solara.Column(style={"padding":"30px"}):
        solara.Markdown(f"#{title}", style={"color": textcolor})
        solara.Text("Click on the button or move the slider to activate a confetti animation.")
        CounterWidget.element(count=counter.value, on_count=counter.set)
        widgets.IntSlider.element(min=-180, max=180, value=counter.value, on_value=counter.set)
        solara.Markdown(f"## Counter value is {counter.value}", style={"color": textcolor})
        GithubAvatar(
            "Alonso Silva",
            "alonsosilva",
            "https://avatars.githubusercontent.com/u/30263736?v=4",
        )

Page()
