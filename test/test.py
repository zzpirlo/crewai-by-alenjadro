from exa_py import Exa

exa = Exa(api_key="8392e6ad-a2be-4044-a9c2-26d502ab6ef8")

result = exa.search_and_contents(
  "hottest AI startups",
  type="neural",
  use_autoprompt=True,
  num_results=10,
  text=True
)