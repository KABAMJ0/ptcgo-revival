from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive

class CounterEchoPassive(Passive):
    """Reflects the damage this Pokémon takes onto the attacker as counters."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target is not carrier:
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.deal_damage(calc.amount, target=attacker,
                                  apply_modifiers=False, as_counters=True)
        return None


async def comeuppance(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, CounterEchoPassive())


card = PokemonCardDef(
    guid="a71807ad-629f-5e1b-aa33-da6b79c3f668",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mabosstiff.Name",
    display_name="Mabosstiff",
    searchable_by=["Mabosstiff", "Stage 1", "Mabosstiff"],
    subtypes=["Stage 1"],
    collector_number=143,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    family_id=942,
    abilities=[
        Attack(
            title="Comeuppance",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack\u00a0(even if it is Knocked Out), put damage counters on the Attacking Pok\u00e9mon equal to the damage done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=comeuppance,
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)