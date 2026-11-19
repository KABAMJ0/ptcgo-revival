from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect

card = PokemonCardDef(
    guid="eb915393-3ce5-54c4-9504-c7082a9c34a3",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lumineon.Name",
    display_name="Lumineon",
    searchable_by=["Lumineon", "Stage 1", "Lumineon"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name",
    family_id=456,
    abilities=[
        Attack(
            title="Return",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=draw_until_effect(6, optional=True),
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)