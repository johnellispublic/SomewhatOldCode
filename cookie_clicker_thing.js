function toggleRate()
{
  for (let i = 0; i < document.getElementsByClassName('product').length; i++)
  {
    var item = document.getElementsByClassName('product')[i]
    var content = item.children[2]

    if (content.children[1].childElementCount > 0) {var name = content.children[1].children[0].innerHTML}
    else {var name = content.children[1].innerHTML}
    if (name == "Antim. condenser") {name = "Antimatter condenser"}
    console.log(name)
    var price = Game.Objects[name].price
    var rate = Game.Objects[name].storedCps * Game.fps

    if (Game.displayingRate) {item.children[2].children[3].innerHTML = Beautify(price)}
    else {item.children[2].children[3].innerHTML = Beautify(price/rate,3) + "/s"}
  }
  Game.displayingRate = !Game.displayingRate


}

(function()
{
  Game.displayingRate = false
  if (! "toggleRate" in document.getElementById('storeBulk').innerHTML) { document.getElementById('storeBulk').innerHTML += '<div id="toggleRate" class="storePreButton storeBulkAmount" onclick="toggleRate()">Rate</div>' }
}
)()
