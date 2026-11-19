from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.attacks_common import condition_attack, damage_counters_on, damage_per

async def burning_aura(ctx):
    if ctx.source is None or not is_in_active_spot(ctx.source):
        return
    for target in (ctx.my_active(), ctx.opponent_active()):
        if target is not None:
            await ctx.deal_damage(10, target=target, apply_modifiers=False,
                                  as_counters=True)

card = PokemonCardDef(
    guid="0875485a-8b33-5c49-ac3b-8cf7497cbc74",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Typhlosion"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=157,
    abilities=[
        Ability(
            title="Burning Aura",
            game_text="As long as Typhlosion is your Active Pok\u00e9mon, put 1 damage counter on each Active Pok\u00e9mon (both yours and your opponent's) between turns.",
            effect=burning_aura,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title="Flickering Flames",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Rage",
            game_text="Does 50 damage plus 10 more damage for each damage counter on Typhlosion.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=50),
        ),
    ],
)