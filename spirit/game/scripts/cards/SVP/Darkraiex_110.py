from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e193a762-9bd1-59a0-b780-39b00b4935bb",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkraiex.Name",
    display_name="Darkrai ex",
    searchable_by=["Darkrai ex", "Basic", "ex", "Darkraiex"],
    subtypes=["Basic", "ex"],
    collector_number=110,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=491,
    abilities=[
        Attack(
            title="Wind of Darkness",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Night Impact",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)