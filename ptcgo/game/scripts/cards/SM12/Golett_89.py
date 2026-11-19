from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect

card = PokemonCardDef(
    guid="9331d7ee-4f8c-539d-9de8-f92b3efd68b2",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    display_name="Golett",
    searchable_by=["Golett", "Basic", "Golett"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=622,
    abilities=[
        Attack(
            title="Return",
            game_text="You may draw cards until you have 5 cards in your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=draw_until_effect(5, optional=True),
        ),
    ],
)