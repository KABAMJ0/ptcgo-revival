from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _place_active_counters(ctx):
    await ctx.deal_damage()
    await ctx.place_damage_counters(7, [ctx.opponent_active()])
from ptcgo.game.data_utils import subtypes_for
from ptcgo.game.card_effects.passives_common import prevent_damage_when


def _is_ex_or_v(pokemon) -> bool:
    if pokemon is None:
        return False
    subtypes = [name.lower() for name in subtypes_for(pokemon.archetype_id)]
    return "ex" in subtypes or "v" in subtypes


card = PokemonCardDef(
    guid="f9c25ebe-fabc-591a-bffb-56e0c1bce199",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic", "Mimikyu"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=778,
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon ex and Pok\u00e9mon V.",
            passive=prevent_damage_when(lambda calc, carrier: calc.target is carrier and _is_ex_or_v(calc.attacker)),
        ),
        Attack(
            title="Ghost Eye",
            game_text="Put 7 damage counters on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=_place_active_counters,
        ),
    ],
)