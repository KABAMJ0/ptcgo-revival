from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import shield_from_defender_next_turn


async def snivel(ctx):
    """The Defending Pokemon's attacks do 20 less to Togepi next turn."""
    await shield_from_defender_next_turn(reduce=20)(ctx)


async def mini_metronome(ctx):
    """On heads, copy one of the Defending Pokemon's attacks; its Energy cost is
    waived but any other requirement still applies."""
    heads = await ctx.flip_coins(1, "Mini-Metronome")
    if not heads or not heads[0]:
        return
    defender = ctx.defender
    if defender is None:
        return
    candidates = [(defender, attack) for attack in ctx.attacks_of(defender)]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    source, chosen = picked
    await ctx.use_attack(chosen, source=source)

card = PokemonCardDef(
    guid="f4633f7b-246f-5a21-9508-24393e008d71",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    display_name="Togepi",
    searchable_by=["Togepi", "Basic", "Togepi"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=175,
    abilities=[
        Attack(
            title="Snivel",
            game_text="If the Defending Pok\u00e9mon attacks Togepi during your opponent's next turn, any damage done to Togepi is reduced by 20 (before applying Weakness and Resistance). (Benching either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snivel,
        ),
        Attack(
            title="Mini-Metronome",
            game_text="Flip a coin. If heads, choose 1 of the Defending Pok\u00e9mon's attacks. Mini-Metronome copies that attack except for its Energy cost. (You must still do anything else in order to use that attack.) (No matter what type the Defending Pok\u00e9mon is, Togepi's type is still Colorless.) Togepi performs that attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=mini_metronome,
        ),
    ],
)