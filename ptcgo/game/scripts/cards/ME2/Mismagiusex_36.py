from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect

card = PokemonCardDef(
    guid="ff3166c0-bd6e-5559-a9a6-33e05c2bf5bf",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagiusex.Name",
    display_name="Mismagius ex",
    searchable_by=["Mismagius ex", "Stage 1", "ex", "Mismagiusex"],
    subtypes=["Stage 1", "ex"],
    collector_number=36,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Ability(
            title="Swirling Prose",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, whenever your opponent's Active Pok\u00e9mon moves to the Bench during their turn, their new Active Pok\u00e9mon is now Confused.",
            effect=unimplemented,
        ),
        Attack(
            title="Hexa-Magic",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=150,
            effect=draw_until_effect(6, optional=True),
        ),
    ],
)