from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.card_effects.passives_common import on_ko_from_attack


async def _innards_out(ctx):
    attacker = getattr(ctx, "ko_attacker", None) or ctx.attacker
    if attacker is not None:
        await ctx.deal_damage(60, target=attacker, apply_modifiers=False,
                              as_counters=True)

card = PokemonCardDef(
    guid="58d01e93-4c99-57a6-981c-7b40618d2cbe",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyukumuku.Name",
    display_name="Pyukumuku",
    searchable_by=["Pyukumuku", "Basic", "Pyukumuku"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=771,
    abilities=[
        Ability(
            title="Innards Out",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is Knocked Out by damage from an opponent's attack, put 6 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=on_ko_from_attack(_innards_out),
        ),
        Attack(
            title="Continuous Tumble",
            game_text="Flip a coin until you get tails. This attack does 30 damage for each heads.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(per_heads=30, until_tails=True),
        ),
    ],
)