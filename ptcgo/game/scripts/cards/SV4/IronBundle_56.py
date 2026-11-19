from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_defender_attacks
from ptcgo.game.session.effects import is_evolution_pokemon


async def _hammer_pressure(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and is_evolution_pokemon(defender):
        lock_defender_attacks(ctx, defender)


card = PokemonCardDef(
    guid="4842f7a3-9e1b-51c7-8574-30d370db9f2b",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBundle.Name",
    display_name="Iron Bundle",
    searchable_by=["Iron Bundle", "Basic", "Future", "IronBundle"],
    subtypes=["Basic", "Future"],
    collector_number=56,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=991,
    abilities=[
        Ability(
            title="Hyper Blower",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, you may switch out your opponent's Active Pok\u00e9mon to the Bench. (Your opponent chooses the new Active Pok\u00e9mon.) If you do, discard this Pok\u00e9mon and all attached cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Refrigerated Stream",
            game_text="If the Defending Pok\u00e9mon is an Evolution Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=_hammer_pressure,
        ),
    ],
)