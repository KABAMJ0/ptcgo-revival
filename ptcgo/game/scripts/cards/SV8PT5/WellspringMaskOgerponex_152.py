from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="ca795607-a274-5df9-bdc0-8776cc0718ae",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WellspringMaskOgerponex.Name",
    display_name="Wellspring Mask Ogerpon ex",
    searchable_by=["Wellspring Mask Ogerpon ex", "Basic", "Tera", "ex", "WellspringMaskOgerponex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=152,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=1017,
    abilities=[
        Attack(
            title="Sob",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Torrential Pump",
            game_text="You may shuffle 3 Energy attached to this Pok\u00e9mon into your deck. If you do, this attack also does 120 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)