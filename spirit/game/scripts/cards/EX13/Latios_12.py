from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="db666211-173a-584d-9a8c-571122ee7412",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios δ",
    searchable_by=["Latios \u03b4", "Basic", "Latios"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    family_id=381,
    abilities=[
        Ability(
            title="Dual Aura",
            game_text="As long as you have Latias or Latias ex in play, each player's Evolved Pok\u00e9mon (excluding Pok\u00e9mon-ex) can't use any Pok\u00e9-Bodies.",
            effect=unimplemented,
        ),
        Attack(
            title="Dive",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Aqua Blast",
            game_text="Discard a Water Energy attached to Latios.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)