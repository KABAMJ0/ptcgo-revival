from ptcgo.game.card_effects.attacks_common import no_weakness_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented


async def _devolution_punch(ctx):
    """Printed 60, then the Defending Pokemon devolves one stage and the
    highest evolution card goes to its owner's hand."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.devolve_pokemon(defender, steps=1, destination="hand")
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_weakness_next_turn

card = PokemonCardDef(
    guid="85885b73-1089-59bc-aa84-df1c0e8f3d7e",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1", "Golurk"],
    subtypes=["Stage 1"],
    collector_number=150,
    set_code="BW7",
    rarity=Rarities.RareSecret,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=623,
    abilities=[
        Attack(
            title="Devolution Punch",
            game_text="Devolve the Defending Pok\u00e9mon and put the highest Stage evolution card on it into your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_devolution_punch,
        ),
        Attack(
            title="Ghost Hammer",
            game_text="During your opponent's next turn, this Pok\u00e9mon has no Weakness.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=no_weakness_next_turn(),
        ),
    ],
)