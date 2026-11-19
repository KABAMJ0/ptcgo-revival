from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import defender_is_ex
from ptcgo.game.card_effects.support_common import heal_targets


async def _shooting_star(ctx):
    boosted = defender_is_ex(ctx)
    await ctx.deal_damage(50 + (100 if boosted else 0))
    if boosted:
        await ctx.discard_energy_from(
            ctx.attacker, 99, prompt="Discard the Energy attached to Latias Star")

card = PokemonCardDef(
    guid="15bfc3c6-c319-5dc9-b721-9754fbd37387",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias ★",
    searchable_by=["Latias \u2605", "Basic", "Star", "Latias"],
    subtypes=["Basic", "Star"],
    collector_number=105,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=380,
    abilities=[
        Attack(
            title="Healing Light",
            game_text="Remove 1 damage counter from each of your Pok\u00e9mon (including Latias Star).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=heal_targets(10, scope="all_own"),
        ),
        Attack(
            title="Shooting Star",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, discard all Energy cards attached to Latias Star and this attack does 50 damage plus 100 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="+",
            effect=_shooting_star,
        ),
    ],
)