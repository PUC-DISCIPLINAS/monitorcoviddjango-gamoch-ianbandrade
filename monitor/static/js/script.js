const toCountryEntry = obj => {
  const {countryName, ...data} = obj
  return [countryName, data]
}

const covidData = JSON.parse(document.getElementById("covidData").textContent)
const countries = Object.fromEntries(covidData.map(toCountryEntry))

const addRow = (table, key, value) => {
  const tableRow = document.createElement("tr")
  const tableKey = document.createElement("th")
  const tableValue = document.createElement("td")

  tableRow.append(tableKey, tableValue)
  table.appendChild(tableRow)

  tableKey.textContent = key
  tableValue.textContent = value
}

const country = document.querySelector("#country")
const dataList = document.querySelector("#countries")
const table = document.querySelector("#table")
let countryValue = Object.keys(countries)[0]

const renderTable = countryName => {
  const selectedCountry = countries[countryName]
  if (!selectedCountry) {
    country.value = countryValue
  } else {
    table.textContent = ""
    countryValue = countryName
    country.value = countryValue
    addRow(table, "country", countryName)
    Object.entries(selectedCountry).forEach(([key, value]) => {
      addRow(table, key, value.toLocaleString("en-US"))
    })
  }
}

renderTable(countryValue)
country.addEventListener("focus", event => event.target.value = "")
country.addEventListener("change", event => renderTable(event.target.value))

Object.keys(countries).forEach(country => {
  const option = document.createElement("option")
  dataList.appendChild(option)
  option.value = country
})

