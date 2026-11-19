from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, named_in_play

async def dragon_dance(ctx):
    from ptcgo.game.card_effects.passives_common import apply_own_next_turn_boost
    await ctx.deal_damage()
    await apply_own_next_turn_boost(ctx, 30)

card = PokemonCardDef(
    guid="cb865e38-afdc-51fa-a3c3-c6bed04ed207",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    family_id=384,
    abilities=[
        Attack(
            title="Dragon Dance",
            game_text="During your next turn, if any of your current Active Pok\u00e9mon does damage to any Defending Pok\u00e9mon, the attack does 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            effect=dragon_dance,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)