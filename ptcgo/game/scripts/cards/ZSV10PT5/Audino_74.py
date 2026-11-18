from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dc67f127-1d63-544e-b47e-11317700ef47",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino", "Basic", "Audino"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Attack(
            title="Return",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)