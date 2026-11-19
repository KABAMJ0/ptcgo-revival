from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities

from ptcgo.game.card_effects.attacks_common import damage_per, lock_defender_attacks

from ptcgo.game.card_effects.pokemon import is_pokemon_ex


def _off_type_count(ctx):
    """Darkness and Metal Pokemon you have in play, counted once per Pokemon."""
    total = 0
    for pokemon in ctx.my_pokemon_in_play():
        types = set(pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
        if PokemonTypes.DARKNESS.value in types or PokemonTypes.METAL.value in types:
            total += 1
    return total


async def _delta_fang(ctx):
    """Printed damage; if the defender is Pokemon-ex it cannot attack next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and is_pokemon_ex(defender):
        lock_defender_attacks(ctx, defender)

card = PokemonCardDef(
    guid="53b1e488-1e79-58ec-acae-d0e8820299f5",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name",
    display_name="Mightyena δ",
    searchable_by=["Mightyena \u03b4", "Stage 1", "Mightyena"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    family_id=261,
    abilities=[
        Attack(
            title="Delta Fang",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, that Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_delta_fang,
        ),
        Attack(
            title="Gang Up",
            game_text="Does 10 damage times the number of Darkness Pok\u00e9mon and Metal Pok\u00e9mon you have in play.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(_off_type_count, 10),
        ),
    ],
)