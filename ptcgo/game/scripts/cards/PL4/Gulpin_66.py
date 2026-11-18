from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d878e194-95dc-55fd-a597-414c05a3f55d",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name",
    display_name="Gulpin",
    searchable_by=["Gulpin", "Basic", "Gulpin"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="PL4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=316,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Drool",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)