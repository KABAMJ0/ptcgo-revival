from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import debuff_defender_attacks

from ptcgo.game.scripts.cards import printed_ability_type
from ptcgo.game.data_utils import def_for


def _has_printed(kind_name):
    def predicate(pokemon) -> bool:
        definition = def_for(pokemon.archetype_id)
        return any(printed_ability_type(definition, getattr(ability, "title", "") or "")
                   .strip().lower() == kind_name
                   for ability in (getattr(definition, "abilities", None) or []))
    return predicate


async def hit_one(kind_name):
    """30 to a chosen opposing Pokemon that prints the given ability kind."""
    return _has_printed(kind_name)


async def power_bolt(ctx):
    pool = [p for p in ctx.opponent_pokemon_in_play() if _has_printed("poké-power")(p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of their Pokemon with a Poke-Power")
    if target is not None:
        await ctx.deal_damage(30, target=target,
                               apply_modifiers=target is ctx.opponent_active())


async def body_bolt(ctx):
    pool = [p for p in ctx.opponent_pokemon_in_play() if _has_printed("poké-body")(p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of their Pokemon with a Poke-Body")
    if target is not None:
        await ctx.deal_damage(30, target=target,
                               apply_modifiers=target is ctx.opponent_active())


card = PokemonCardDef(
    guid="260b5405-c27e-5d15-8ab0-1b51ecb09489",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Plusle"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="POP3",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=311,
    abilities=[
        Attack(
            title="Cheer Up",
            game_text="Draw a card. If you have Minun in play, draw 2 cards instead.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Positive Ion",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(30)),
        ),
        Attack(
            title="Body Bolt",
            game_text="Choose 1 of your opponent's Pok\u00e9mon that has any Pok\u00e9-Bodies. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=body_bolt,
        ),
    ],
)