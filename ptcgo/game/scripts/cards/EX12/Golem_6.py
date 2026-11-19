from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.attacks_common import damage_counters_on, snipe_attack
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import attach_from_discard

def _is_fighting_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def _mend(ctx):
    """Attach a Fighting Energy from the discard pile, then remove 2 damage
    counters from Golem."""
    attached = await attach_from_discard(_is_fighting_energy, count=1,
                                         target="self", minimum=0)(ctx)
    if attached and ctx.attacker is not None:
        await ctx.heal(20, ctx.attacker)


card = PokemonCardDef(
    guid="a94eeb92-a4e3-5e36-9b4d-d23a480ed15d",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golem.Name",
    display_name="Golem",
    searchable_by=["Golem", "Stage 2", "Golem"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Mend",
            game_text="Search your discard pile for a Fighting Energy card and attach it to Golem. If you do, remove 2 damage counters from Golem.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_mend,
        ),
        Attack(
            title="Enraged Linear Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage for each damage counter on Golem to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(lambda c: 10 * damage_counters_on("self")(c), pool="any"),
        ),
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
    ],
)