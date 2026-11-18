from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae600cac-0147-5c7d-86ac-664ac50c1789",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    display_name="Wooper",
    searchable_by=["Wooper", "Basic", "Wooper"],
    subtypes=["Basic"],
    collector_number=155,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=194,
    abilities=[
        Attack(
            title="Scoop Water",
            game_text="Shuffle up to 3 Basic Water Energy cards from your discard pile into your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)