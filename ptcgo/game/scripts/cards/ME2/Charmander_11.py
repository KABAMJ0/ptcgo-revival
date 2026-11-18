from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2ddf9be4-2526-5c2e-8fbc-a548cea73342",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="ME2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Ability(
            title="Agile",
            game_text="If this Pok\u00e9mon has no Energy attached, it has no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)