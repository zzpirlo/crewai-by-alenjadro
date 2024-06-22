from exa_py import Exa

exa = Exa(api_key)

result = exa.search_and_contents(
  "hottest AI startups",
  type="neural",
  use_autoprompt=True,
  num_results=10,
  text=True
)
